#!/usr/bin/env python3
"""
ObservationCollection Consistency Checker
==========================================
Analyses JSON files for SOSA/SSN ObservationCollection consistency per
W3C SSN spec section 5.5.2.2:
  https://w3c.github.io/sdw-sosa-ssn/ssn/#SOSAObservationCollection

Rules (paraphrased from the spec):
  If a property from the set {hasFeatureOfInterest, hasUltimateFeatureOfInterest,
  madeBySensor, observedProperty, phenomenonTime, resultTime, usedProcedure}
  is declared on an ObservationCollection, then ALL member observations must
  either (a) NOT declare that property themselves (inheriting from the
  collection), or (b) declare the SAME value for that property.

Input targets (positional arguments):
  Omit entirely      → all *.json files in the current working directory
  One or more paths  → files, directories, or shell globs
                       Directories are searched for *.json (add --recursive
                       to descend into sub-directories).
                       Backup files (*.backup_*.json) are always excluded.

Edit strategies (--strategy):
  collection-wins   (default)
    For "conflict" violations: remove the member-level value so the member
    inherits the collection value.  The collection is authoritative.

  member-wins
    For "conflict" violations: update the collection-level value to reflect
    the members.
    - If all members agree on a single value, promote it to the collection
      and remove it from every member (clean inheritance).
    - For time aspects (phenomenonTime, resultTime), if members carry
      DIFFERENT values, the collection is set to an ISO 8601 interval dict
      spanning the full member time range:
          {"interval": ["<earliest>", "<latest>"]}
      Use --open-end to produce {"interval": ["<earliest>", ".."]} instead.
      Member values are preserved as-is (they are the detail; the collection
      provides the bounding envelope).
    - For non-time aspects where members disagree, the violation is flagged
      as unresolvable and manual intervention is required.

Modes (--mode):
  report            Print violations only (default)
  report-edit       Print violations, then prompt Y/n for each fix
  edit              Apply all fixes automatically without prompting
  restore           Restore a previously backed-up file
                    (requires exactly one file target)

Usage:
  python obs_collection_check.py [targets ...] [options]

Options:
  --dir DIR             Directory to search (repeatable; alternative to
                        positional directory args)
  --recursive           Descend into sub-directories when scanning dirs
  --mode {report,report-edit,edit,restore}
  --strategy {collection-wins,member-wins}
  --aspects ASPECTS     Comma-separated aspects to check (default: all)
                        Names: hasFeatureOfInterest, hasUltimateFeatureOfInterest,
                               madeBySensor, observedProperty, phenomenonTime,
                               resultTime, usedProcedure
                        Aliases: time  -> phenomenonTime,resultTime
                                 procedure, sensor, property, foi, all
  --backup-dir DIR      Directory for backup files (default: same as each input)
  --restore-from FILE   Path to a specific backup to restore
  --verbose             Show passing checks too
  --normalize-tz        Treat times differing only in Z/tz-suffix as equal.
                        E.g. 2022-05-22T00:00:00 == 2022-05-22T00:00:00Z
  --open-end            Under member-wins, produce open-ended time intervals:
                        {"interval": ["earliest", ".."]}
  --summary             Print a one-line-per-file summary table at the end
                        (automatically enabled when processing multiple files)

Examples:
  # All *.json files in the current directory
  python obs_collection_check.py

  # All files in a specific directory
  python obs_collection_check.py /path/to/surveys/
  python obs_collection_check.py --dir /path/to/surveys/

  # Recursive directory scan
  python obs_collection_check.py /path/to/surveys/ --recursive

  # Shell glob (quoted to prevent shell expansion; script expands it)
  python obs_collection_check.py "surveys/*.json"

  # Multiple explicit files
  python obs_collection_check.py a.json b.json c.json

  # Mix of files, directories, and globs
  python obs_collection_check.py parcels-angles.json "extra/*.json" --dir archive/

  # Edit all files in a directory with normalize-tz
  python obs_collection_check.py --dir surveys/ --mode edit --normalize-tz

  # Restore one specific file
  python obs_collection_check.py survey.json --mode restore
"""

import argparse
import copy
import glob as glob_module
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ALL_ASPECTS = [
    "hasFeatureOfInterest",
    "hasUltimateFeatureOfInterest",
    "madeBySensor",
    "observedProperty",
    "phenomenonTime",
    "resultTime",
    "usedProcedure",
]

TIME_ASPECTS = {"phenomenonTime", "resultTime"}

ASPECT_ALIASES = {
    "time": ["phenomenonTime", "resultTime"],
    "procedure": ["usedProcedure"],
    "sensor": ["madeBySensor"],
    "property": ["observedProperty"],
    "foi": ["hasFeatureOfInterest"],
    "all": ALL_ASPECTS,
}

OBS_COLLECTION_MARKERS = [
    "ObservationCollection",
    "sosa:ObservationCollection",
    "ssn:ObservationCollection",
]

COLLECTION_PROP_CONTAINERS = ["properties"]
MEMBER_KEYS = ["hasMember", "features", "members"]
MEMBER_PROP_CONTAINERS = ["properties"]

# ISO 8601 datetime: date + optional time + optional tz
_ISO_RE = re.compile(
    r'^(\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?)?)'
    r'(Z|[+-]\d{2}:?\d{2})?$'
)


# ---------------------------------------------------------------------------
# Time utilities
# ---------------------------------------------------------------------------

def _parse_iso(s: str) -> Optional[datetime]:
    """Parse ISO 8601 string -> aware datetime (assumed UTC if no tz)."""
    if not isinstance(s, str):
        return None
    m = _ISO_RE.match(s.strip())
    if not m:
        return None
    naive_str, tz_suffix = m.group(1), m.group(2)
    if 'T' not in naive_str and ' ' not in naive_str:
        naive_str += 'T00:00:00'
    try:
        dt = datetime.fromisoformat(naive_str)
    except ValueError:
        return None
    if not tz_suffix:
        return dt.replace(tzinfo=timezone.utc)
    if tz_suffix.upper() == 'Z':
        return dt.replace(tzinfo=timezone.utc)
    sign = 1 if tz_suffix[0] == '+' else -1
    tz_str = tz_suffix[1:].replace(':', '')
    hh, mm = int(tz_str[:2]), int(tz_str[2:])
    tz = timezone(timedelta(hours=sign * hh, minutes=sign * mm))
    return dt.replace(tzinfo=tz)


def _strip_tz(s: str) -> str:
    """Strip trailing Z or +hh:mm timezone marker."""
    return re.sub(r'(Z|[+-]\d{2}:?\d{2})$', '', s.strip())


def _canonical_z(s: str) -> str:
    """Return the string with a Z suffix, adding one if absent."""
    stripped = _strip_tz(s)
    return stripped + 'Z'


def extract_time_string(v: Any) -> Optional[str]:
    """Extract a time string from a plain ISO string or interval dict."""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        iv = v.get('interval')
        if isinstance(iv, list) and len(iv) >= 1:
            # Return first non-open endpoint
            for x in iv:
                if x and x != '..':
                    return x
    return None


def all_time_strings(v: Any) -> list[str]:
    """Return all time strings from a value (handles intervals)."""
    if isinstance(v, str):
        return [v]
    if isinstance(v, dict):
        iv = v.get('interval')
        if isinstance(iv, list):
            return [x for x in iv if x and x != '..']
    return []


def build_interval_value(time_strings: list[str], open_end: bool = False) -> dict:
    """
    Given a list of ISO time strings, return an interval dict spanning them.
    {"interval": ["earliest", "latest"]}  or {"interval": ["earliest", ".."]}
    Preserves Z-suffix on whichever representative string had it.
    """
    parsed = []
    for t in time_strings:
        dt = _parse_iso(t)
        if dt is not None:
            parsed.append((dt, t))
    if not parsed:
        end = '..' if open_end else (time_strings[-1] if time_strings else '..')
        return {"interval": [time_strings[0] if time_strings else '..', end]}
    parsed.sort(key=lambda x: x[0])
    earliest_str = parsed[0][1]
    latest_str = parsed[-1][1]
    # Prefer the Z-form for endpoints if available
    def prefer_z(candidate, all_strs):
        z_version = _canonical_z(candidate)
        # if any member already uses that string, prefer it
        if z_version in all_strs:
            return z_version
        return candidate
    earliest_str = prefer_z(earliest_str, time_strings)
    latest_str = prefer_z(latest_str, time_strings)
    end = '..' if open_end else latest_str
    return {"interval": [earliest_str, end]}


def times_semantically_equal(a: Any, b: Any, normalize_tz: bool) -> bool:
    """Check whether two time values are semantically equal."""
    if normalize_tz:
        def key(v):
            if isinstance(v, str):
                return _strip_tz(v)
            if isinstance(v, dict):
                iv = v.get('interval')
                if iv:
                    return json.dumps(
                        [_strip_tz(x) if isinstance(x, str) and x != '..' else x
                         for x in iv]
                    )
            return str(v)
        return key(a) == key(b)
    return values_equal(a, b)


def time_covered_by_collection(member_val: Any, col_val: Any,
                                normalize_tz: bool) -> bool:
    """
    Return True if col_val logically covers member_val.
    An interval covers a point if the point is within [start, end].
    A point covers a point if they are equal.
    """
    # Exact equality first
    if times_semantically_equal(member_val, col_val, normalize_tz):
        return True
    # If collection is an interval, check containment
    if isinstance(col_val, dict) and 'interval' in col_val:
        iv = col_val['interval']
        if isinstance(iv, list) and len(iv) == 2:
            start_str, end_str = iv[0], iv[1]
            m_strs = all_time_strings(member_val)
            for m_str in m_strs:
                m_dt = _parse_iso(m_str)
                if m_dt is None:
                    continue
                s_dt = _parse_iso(start_str) if start_str and start_str != '..' else None
                e_dt = _parse_iso(end_str) if end_str and end_str != '..' else None
                start_ok = (s_dt is None) or (m_dt >= s_dt)
                end_ok = (e_dt is None) or (m_dt <= e_dt)
                if start_ok and end_ok:
                    return True
    return False


# ---------------------------------------------------------------------------
# General value helpers
# ---------------------------------------------------------------------------

def values_equal(a: Any, b: Any) -> bool:
    if type(a) != type(b):
        return False
    if isinstance(a, (dict, list)):
        return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    return a == b


def _resolve(obj: dict, key: str) -> tuple[Any, bool]:
    for ck in COLLECTION_PROP_CONTAINERS:
        c = obj.get(ck)
        if isinstance(c, dict) and key in c:
            return c[key], True
    if key in obj:
        return obj[key], True
    return None, False


def _resolve_member(member: dict, key: str) -> tuple[Any, bool]:
    for ck in MEMBER_PROP_CONTAINERS:
        c = member.get(ck)
        if isinstance(c, dict) and key in c:
            return c[key], True
    if key in member:
        return member[key], True
    return None, False


def _set_col_value(col: dict, key: str, value: Any):
    """Set a property on a collection, preferring the 'properties' sub-dict."""
    for ck in COLLECTION_PROP_CONTAINERS:
        c = col.get(ck)
        if isinstance(c, dict):
            c[key] = value
            return
    if key in col:
        col[key] = value
        return
    col.setdefault('properties', {})[key] = value


def _delete_member_key(member: dict, key: str):
    for ck in MEMBER_PROP_CONTAINERS:
        c = member.get(ck)
        if isinstance(c, dict) and key in c:
            del c[key]
            return
    if key in member:
        del member[key]


# ---------------------------------------------------------------------------
# Collection discovery
# ---------------------------------------------------------------------------

def is_obs_collection(node: Any) -> bool:
    if not isinstance(node, dict):
        return False
    for type_key in ('featureType', '@type', 'type'):
        t = node.get(type_key, '')
        if isinstance(t, str) and any(m in t for m in OBS_COLLECTION_MARKERS):
            return True
        if isinstance(t, list) and any(
            any(m in x for m in OBS_COLLECTION_MARKERS) for x in t if isinstance(x, str)
        ):
            return True
    if 'hasMember' in node:
        return True
    return False


def find_collections(node: Any, path: str = 'root') -> list[tuple[str, dict]]:
    results = []
    if isinstance(node, dict):
        if is_obs_collection(node):
            results.append((path, node))
        for k, v in node.items():
            results.extend(find_collections(v, f'{path}.{k}'))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            results.extend(find_collections(item, f'{path}[{i}]'))
    return results


def get_members(collection: dict) -> list[tuple[str, dict]]:
    for mk in MEMBER_KEYS:
        members = collection.get(mk)
        if isinstance(members, list):
            return [(f'{mk}[{i}]', m) for i, m in enumerate(members)
                    if isinstance(m, dict)]
    return []


# ---------------------------------------------------------------------------
# Violation
# ---------------------------------------------------------------------------

class Violation:
    def __init__(
        self,
        collection_path: str,
        aspect: str,
        collection_value: Any,
        member_index: int,
        member_path: str,
        member_value: Any,
        rule: str,  # "conflict" | "missing_from_member"
    ):
        self.collection_path = collection_path
        self.aspect = aspect
        self.collection_value = collection_value
        self.member_index = member_index
        self.member_path = member_path
        self.member_value = member_value
        self.rule = rule

    def describe(self) -> str:
        lines = [
            f'  Collection : {self.collection_path}',
            f'  Aspect     : {self.aspect}',
            f'  Rule       : {self.rule}',
            f'  Member [{self.member_index}] : {self.member_path}',
        ]
        if self.rule == 'conflict':
            lines.append(f'  Collection value : {json.dumps(self.collection_value)}')
            lines.append(f'  Member value     : {json.dumps(self.member_value)}')
        return '\n'.join(lines)


def _group_violations(
    violations: list[Violation],
) -> dict[tuple[str, str], list[Violation]]:
    groups: dict[tuple[str, str], list[Violation]] = {}
    for v in violations:
        key = (v.collection_path, v.aspect)
        groups.setdefault(key, []).append(v)
    return groups


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyse_collection(
    collection_path: str,
    collection: dict,
    aspects: list[str],
    verbose: bool,
    normalize_tz: bool,
) -> list[Violation]:
    violations = []
    members = get_members(collection)
    if not members:
        if verbose:
            print(f'  [INFO] {collection_path} – no members found, skipping.')
        return violations

    for aspect in aspects:
        col_value, col_has = _resolve(collection, aspect)
        is_time = aspect in TIME_ASPECTS

        for idx, (member_rel_path, member) in enumerate(members):
            member_path = f'{collection_path}.{member_rel_path}'
            mem_value, mem_has = _resolve_member(member, aspect)

            if col_has and mem_has:
                if is_time:
                    # An interval on the collection covers a point value on a member
                    equal = time_covered_by_collection(mem_value, col_value, normalize_tz)
                else:
                    equal = values_equal(col_value, mem_value)

                if not equal:
                    violations.append(Violation(
                        collection_path, aspect, col_value,
                        idx, member_path, mem_value, 'conflict',
                    ))
                else:
                    if verbose:
                        if is_time and isinstance(col_value, dict) and 'interval' in col_value:
                            print(f'  [OK] {collection_path} | {aspect} | '
                                  f'member[{idx}] value covered by collection interval.')
                        else:
                            print(f'  [OK] {collection_path} | {aspect} | '
                                  f'member[{idx}] matches collection value.')
            elif col_has and not mem_has:
                if verbose:
                    print(f'  [OK] {collection_path} | {aspect} | '
                          f'member[{idx}] inherits from collection.')
            elif not col_has and not mem_has:
                if verbose:
                    print(f'  [INFO] {collection_path} | {aspect} | '
                          f'absent at both levels for member[{idx}].')
            else:
                if verbose:
                    print(f'  [OK] {collection_path} | {aspect} | '
                          f'member[{idx}] carries its own value (collection absent).')

    return violations


def analyse_file(
    data: Any,
    aspects: list[str],
    verbose: bool,
    normalize_tz: bool,
) -> tuple[list[tuple[str, dict]], list[Violation]]:
    collections = find_collections(data)
    all_violations: list[Violation] = []
    for path, col in collections:
        if verbose:
            print(f'\nChecking collection at: {path}')
        violations = analyse_collection(path, col, aspects, verbose, normalize_tz)
        all_violations.extend(violations)
    return collections, all_violations


# ---------------------------------------------------------------------------
# Fix logic
# ---------------------------------------------------------------------------

def _compute_member_wins_fix(
    aspect: str,
    col_value: Any,
    all_member_values: list[Any],
    normalize_tz: bool,
    open_end: bool,
) -> tuple[Optional[Any], str, bool]:
    """
    Determine the new collection value under member-wins strategy.
    Returns (new_col_value, description, can_fix).
    """
    is_time = aspect in TIME_ASPECTS

    if is_time:
        # Gather all distinct time strings (from members + current collection)
        all_time_strs: list[str] = []
        for mv in all_member_values:
            all_time_strs.extend(all_time_strings(mv))
        if col_value is not None:
            all_time_strs.extend(all_time_strings(col_value))

        if not all_time_strs:
            return None, f"No parseable time values found for '{aspect}'.", False

        # Check if all times are semantically equivalent (ignoring tz)
        normed = {_strip_tz(t) for t in all_time_strs}
        if len(normed) == 1:
            # All the same — pick canonical form (prefer Z)
            canonical = (
                next((t for t in all_time_strs if t.endswith('Z')), all_time_strs[0])
            )
            desc = (
                f"Set collection '{aspect}' = {json.dumps(canonical)} "
                f"(all members agree; will inherit from collection)"
            )
            return canonical, desc, True
        else:
            interval_val = build_interval_value(all_time_strs, open_end=open_end)
            desc = (
                f"Set collection '{aspect}' to interval "
                f"{json.dumps(interval_val)} spanning {len(normed)} distinct time(s); "
                f"member values retained"
            )
            return interval_val, desc, True
    else:
        # Non-time: members must unanimously agree
        normed_vals: dict[str, Any] = {}
        for mv in all_member_values:
            k = json.dumps(mv, sort_keys=True) if isinstance(mv, (dict, list)) else str(mv)
            normed_vals[k] = mv
        if len(normed_vals) == 1:
            new_val = list(normed_vals.values())[0]
            desc = (
                f"Set collection '{aspect}' = {json.dumps(new_val)} "
                f"(all members agree; will inherit from collection)"
            )
            return new_val, desc, True
        else:
            desc = (
                f"Cannot auto-fix '{aspect}': members have "
                f"{len(normed_vals)} distinct values: "
                f"{list(normed_vals.values())!r} — manual resolution required"
            )
            return None, desc, False


def apply_fixes(
    data: Any,
    violations: list[Violation],
    strategy: str,
    interactive: bool,
    normalize_tz: bool,
    open_end: bool = False,
) -> tuple[Any, list[str]]:
    modified = copy.deepcopy(data)
    fix_log = []

    collections_map: dict[str, tuple[dict, list[tuple[str, dict]]]] = {}
    for path, col in find_collections(modified):
        collections_map[path] = (col, get_members(col))

    groups = _group_violations(violations)

    for (col_path, aspect), group_violations in groups.items():
        if col_path not in collections_map:
            fix_log.append(f'[SKIP] Cannot locate collection {col_path} in data.')
            continue

        col_node, members = collections_map[col_path]
        col_value, _ = _resolve(col_node, aspect)
        is_time = aspect in TIME_ASPECTS

        # ── Collection-wins ───────────────────────────────────────────────
        if strategy == 'collection-wins':
            desc = (
                f"Remove '{aspect}' from {len(group_violations)} member(s); "
                f"inherit collection value {json.dumps(col_value)}"
            )

            if interactive:
                _print_group_header(col_path, aspect, group_violations)
                print(f'\nStrategy: collection-wins')
                print(f'Proposed fix: {desc}')
                ans = input('Apply? [Y/n/skip-all]: ').strip().lower()
                if ans == 'skip-all':
                    fix_log.append('[USER] Remaining fixes skipped.')
                    break
                if ans in ('n', 'no'):
                    fix_log.append(f'[SKIP] User skipped: {col_path} | {aspect}')
                    continue

            removed = 0
            for v in group_violations:
                if v.member_index < len(members):
                    _, member_node = members[v.member_index]
                    _delete_member_key(member_node, aspect)
                    removed += 1
            fix_log.append(
                f'[FIXED][collection-wins] {col_path} | {aspect}: '
                f'removed from {removed} member(s). '
                f'Collection value: {json.dumps(col_value)}'
            )

        # ── Member-wins ───────────────────────────────────────────────────
        elif strategy == 'member-wins':
            # Collect all member values (violating ones only; non-violating
            # members already agree, so also include their values for full span)
            all_member_vals = []
            for v in group_violations:
                all_member_vals.append(v.member_value)
            # Also include non-violating member values for complete time span
            for _, member_node in members:
                mv, mh = _resolve_member(member_node, aspect)
                if mh:
                    all_member_vals.append(mv)

            new_col_value, desc, can_fix = _compute_member_wins_fix(
                aspect, col_value, all_member_vals, normalize_tz, open_end
            )

            if not can_fix:
                fix_log.append(f'[CANNOT FIX][member-wins] {col_path} | {aspect}: {desc}')
                continue

            if interactive:
                _print_group_header(col_path, aspect, group_violations)
                print(f'\nStrategy: member-wins')
                print(f'Proposed fix: {desc}')
                ans = input('Apply? [Y/n/skip-all]: ').strip().lower()
                if ans == 'skip-all':
                    fix_log.append('[USER] Remaining fixes skipped.')
                    break
                if ans in ('n', 'no'):
                    fix_log.append(f'[SKIP] User skipped: {col_path} | {aspect}')
                    continue

            # Update collection
            _set_col_value(col_node, aspect, new_col_value)

            # If result is a single point value (not interval), remove from
            # all members so they cleanly inherit
            is_interval = isinstance(new_col_value, dict) and 'interval' in new_col_value
            if not is_interval:
                removed = 0
                for _, member_node in members:
                    mv, mh = _resolve_member(member_node, aspect)
                    if mh:
                        _delete_member_key(member_node, aspect)
                        removed += 1
                fix_log.append(
                    f'[FIXED][member-wins] {col_path} | {aspect}: '
                    f'collection → {json.dumps(new_col_value)}, '
                    f'removed from {removed} member(s) (now inherited).'
                )
            else:
                # Interval: members keep their fine-grained values; collection
                # provides the bounding envelope — no member removal needed
                fix_log.append(
                    f'[FIXED][member-wins] {col_path} | {aspect}: '
                    f'collection → {json.dumps(new_col_value)}; '
                    f'member values retained (covered by interval).'
                )

    return modified, fix_log


def _print_group_header(col_path, aspect, group_violations):
    print(f'\n{"─"*60}')
    print(f'VIOLATIONS ({len(group_violations)}) — {col_path} | {aspect}')
    col_val = group_violations[0].collection_value
    print(f'  Collection: {json.dumps(col_val)}')
    member_val_map: dict[str, list[int]] = {}
    for v in group_violations:
        k = json.dumps(v.member_value)
        member_val_map.setdefault(k, []).append(v.member_index)
    for val_str, idxs in member_val_map.items():
        idxs_repr = (
            str(idxs) if len(idxs) <= 8
            else f'[{idxs[0]}..{idxs[-1]}] ({len(idxs)} members)'
        )
        print(f'  Member value {val_str}: members {idxs_repr}')


# ---------------------------------------------------------------------------
# Backup / restore
# ---------------------------------------------------------------------------

def create_backup(source_path: str, backup_dir: Optional[str] = None) -> str:
    src = Path(source_path).resolve()
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'{src.stem}.backup_{ts}{src.suffix}'
    dest_dir = Path(backup_dir) if backup_dir else src.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / backup_name
    shutil.copy2(src, dest)
    return str(dest)


def list_backups(source_path: str, backup_dir: Optional[str] = None) -> list[str]:
    src = Path(source_path).resolve()
    search_dir = Path(backup_dir) if backup_dir else src.parent
    return sorted(str(m) for m in search_dir.glob(f'{src.stem}.backup_*{src.suffix}'))


def restore_backup(backup_path: str, target_path: str) -> str:
    shutil.copy2(backup_path, target_path)
    return f"Restored '{target_path}' from '{backup_path}'"


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def print_report(
    input_file: str,
    collections: list[tuple[str, dict]],
    violations: list[Violation],
    aspects: list[str],
    strategy: str,
    normalize_tz: bool,
):
    print('\n' + '=' * 70)
    print('  ObservationCollection Consistency Report')
    print(f'  File     : {input_file}')
    print(f'  Aspects  : {", ".join(aspects)}')
    print(f'  Strategy : {strategy}')
    if normalize_tz:
        print('  Timezone : normalised (Z-suffix ignored for equality test)')
    print('  W3C SSN  : §5.5.2.2')
    print('=' * 70)

    print(f'\nFound {len(collections)} ObservationCollection(s):')
    for path, col in collections:
        members = get_members(col)
        props = col.get('properties', {})
        print(f'  {path}  ({len(members)} members)')
        # Show which aspects are set at collection level
        present = [a for a in aspects if _resolve(col, a)[1]]
        if present:
            for a in present:
                v, _ = _resolve(col, a)
                print(f'    {a}: {json.dumps(v)}')

    if not violations:
        print('\n✓ No consistency violations found.\n')
    else:
        groups = _group_violations(violations)
        print(f'\n✗ {len(violations)} violation(s) across '
              f'{len(groups)} collection×aspect group(s):\n')
        for (col_path, aspect), grp in groups.items():
            col_val = grp[0].collection_value
            print(f'  [{col_path}] | {aspect}')
            print(f'    Collection : {json.dumps(col_val)}')
            member_val_map: dict[str, list[int]] = {}
            for v in grp:
                k = json.dumps(v.member_value)
                member_val_map.setdefault(k, []).append(v.member_index)
            for val_str, idxs in member_val_map.items():
                idxs_repr = (
                    str(idxs) if len(idxs) <= 8
                    else f'[{idxs[0]}..{idxs[-1]}] ({len(idxs)} members)'
                )
                print(f'    Member {val_str}: {idxs_repr}')
            print()

    print('=' * 70 + '\n')


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_aspects(aspects_str: str) -> list[str]:
    parts = [p.strip() for p in aspects_str.split(',')]
    result = []
    for part in parts:
        lower = part.lower()
        if lower in ASPECT_ALIASES:
            result.extend(ASPECT_ALIASES[lower])
        elif part in ALL_ASPECTS:
            result.append(part)
        else:
            match = next((a for a in ALL_ASPECTS if a.lower() == lower), None)
            if match:
                result.append(match)
            else:
                print(f'[WARN] Unknown aspect "{part}", ignoring.')
    seen, deduped = set(), []
    for r in result:
        if r not in seen:
            seen.add(r)
            deduped.append(r)
    return deduped


# ---------------------------------------------------------------------------
# File resolution
# ---------------------------------------------------------------------------

_BACKUP_RE = re.compile(r'\.backup_\d{8}_\d{6}\.json$')


def _is_backup(path: Path) -> bool:
    return bool(_BACKUP_RE.search(path.name))


def resolve_targets(
    targets: list[str],
    extra_dirs: list[str],
    recursive: bool,
) -> list[Path]:
    """
    Expand targets (files, directories, globs) and --dir entries into a
    deduplicated, sorted list of .json Paths, excluding backup files.

    If no targets and no --dir are given, defaults to *.json in cwd.
    """
    collected: list[Path] = []

    def add_dir(d: Path):
        pattern = '**/*.json' if recursive else '*.json'
        for p in sorted(d.glob(pattern)):
            if p.is_file() and not _is_backup(p):
                collected.append(p.resolve())

    def add_glob(pattern: str):
        # Use Python's glob so it works cross-platform and with quoted globs
        matches = sorted(glob_module.glob(pattern, recursive=recursive))
        if not matches:
            print(f'[WARN] No files matched: {pattern}', file=sys.stderr)
        for m in matches:
            p = Path(m).resolve()
            if p.is_dir():
                add_dir(p)
            elif p.is_file() and p.suffix.lower() == '.json' and not _is_backup(p):
                collected.append(p)

    # --dir entries
    for d in extra_dirs:
        dp = Path(d)
        if not dp.exists():
            print(f'[WARN] Directory not found: {d}', file=sys.stderr)
        elif not dp.is_dir():
            print(f'[WARN] Not a directory: {d}', file=sys.stderr)
        else:
            add_dir(dp)

    # positional targets
    if targets:
        for t in targets:
            p = Path(t)
            if p.is_dir():
                add_dir(p)
            elif '*' in t or '?' in t or '[' in t:
                add_glob(t)
            elif p.exists() and p.is_file():
                if p.suffix.lower() == '.json' and not _is_backup(p):
                    collected.append(p.resolve())
                else:
                    print(f'[WARN] Skipping non-JSON or backup file: {t}',
                          file=sys.stderr)
            else:
                # Might be a glob that the shell didn't expand (quoted)
                add_glob(t)
    elif not extra_dirs:
        # Default: all *.json in cwd
        add_dir(Path.cwd())

    # Deduplicate preserving first-seen order
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in collected:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


# ---------------------------------------------------------------------------
# Per-file processing helpers
# ---------------------------------------------------------------------------

def process_file(
    input_file: Path,
    aspects: list[str],
    mode: str,
    strategy: str,
    normalize_tz: bool,
    open_end: bool,
    backup_dir: Optional[str],
    verbose: bool,
) -> dict:
    """
    Run analysis (and optionally fixes) on a single file.
    Returns a result dict for the multi-file summary.
    """
    result = {
        'file': str(input_file),
        'collections': 0,
        'violations': 0,
        'fixed': 0,
        'unresolvable': 0,
        'error': None,
        'skipped': False,
    }

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result['error'] = f'Invalid JSON: {e}'
        print(f'\n[ERROR] {input_file}: {e}', file=sys.stderr)
        return result
    except OSError as e:
        result['error'] = str(e)
        print(f'\n[ERROR] {input_file}: {e}', file=sys.stderr)
        return result

    collections, violations = analyse_file(data, aspects, verbose, normalize_tz)
    result['collections'] = len(collections)
    result['violations'] = len(violations)

    print_report(str(input_file), collections, violations, aspects,
                 strategy, normalize_tz)

    if not violations or mode not in ('edit', 'report-edit'):
        return result

    interactive = (mode == 'report-edit')
    modified_data, fix_log = apply_fixes(
        data, violations,
        strategy=strategy,
        interactive=interactive,
        normalize_tz=normalize_tz,
        open_end=open_end,
    )

    if fix_log:
        print('\nFix log:')
        for entry in fix_log:
            print(f'  {entry}')
        result['fixed'] = sum(1 for e in fix_log if e.startswith('[FIXED]'))
        result['unresolvable'] = sum(1 for e in fix_log if e.startswith('[CANNOT FIX]'))

    if json.dumps(data, sort_keys=True) == json.dumps(modified_data, sort_keys=True):
        print('\nNo changes made.')
        return result

    backup_path = create_backup(str(input_file), backup_dir)
    print(f'\nBackup created: {backup_path}')

    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(modified_data, f, indent=2, ensure_ascii=False)
    print(f'Updated file written: {input_file}')

    _, post_violations = analyse_file(
        modified_data, aspects, verbose=False, normalize_tz=normalize_tz
    )
    if post_violations:
        groups = _group_violations(post_violations)
        print(f'\n[WARN] {len(post_violations)} violation(s) remain '
              f'in {len(groups)} group(s):')
        for (cp, asp), grp in groups.items():
            print(f'  {cp} | {asp}: {len(grp)} member(s)')
    else:
        print('\n✓ All violations resolved.')

    return result


def print_summary(results: list[dict], aspects: list[str], strategy: str):
    """Print a one-line-per-file summary table."""
    total_files = len(results)
    total_cols = sum(r['collections'] for r in results)
    total_viols = sum(r['violations'] for r in results)
    total_fixed = sum(r['fixed'] for r in results)
    total_errors = sum(1 for r in results if r['error'])
    clean_files = sum(
        1 for r in results if r['violations'] == 0 and not r['error']
    )

    print('\n' + '=' * 70)
    print('  MULTI-FILE SUMMARY')
    print(f'  Aspects  : {", ".join(aspects)}')
    print(f'  Strategy : {strategy}')
    print('=' * 70)

    # Column widths
    max_name = max((len(Path(r['file']).name) for r in results), default=20)
    max_name = min(max(max_name, 20), 50)
    hdr = (f"  {'File':<{max_name}}  {'Colls':>5}  {'Viols':>5}"
           f"  {'Fixed':>5}  Status")
    print(hdr)
    print('  ' + '-' * (len(hdr) - 2))

    for r in results:
        name = Path(r['file']).name
        if len(name) > max_name:
            name = '…' + name[-(max_name - 1):]
        cols = r['collections']
        viols = r['violations']
        fixed = r['fixed']
        if r['error']:
            status = f'ERROR: {r["error"][:40]}'
        elif viols == 0:
            status = '✓ clean'
        elif fixed > 0 and viols == fixed:
            status = '✓ fixed'
        elif fixed > 0:
            status = f'⚠ partial ({viols - fixed} remain)'
        else:
            status = f'✗ {viols} violation(s)'
        print(f'  {name:<{max_name}}  {cols:>5}  {viols:>5}  {fixed:>5}  {status}')

    print('  ' + '-' * (len(hdr) - 2))
    print(f'  {"TOTAL":<{max_name}}  {total_cols:>5}  {total_viols:>5}  {total_fixed:>5}  '
          f'{clean_files}/{total_files} files clean'
          + (f', {total_errors} error(s)' if total_errors else ''))
    print('=' * 70 + '\n')


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        'targets',
        nargs='*',
        metavar='TARGET',
        help=(
            'Files, directories, or glob patterns to process. '
            'Omit to process all *.json in the current directory.'
        ),
    )
    p.add_argument(
        '--dir', '-d',
        dest='dirs',
        action='append',
        default=[],
        metavar='DIR',
        help='Directory to scan for *.json files (repeatable).',
    )
    p.add_argument(
        '--recursive', '-r',
        action='store_true',
        help='Descend into sub-directories when scanning directories.',
    )
    p.add_argument(
        '--mode',
        choices=['report', 'report-edit', 'edit', 'restore'],
        default='report',
        help='Operation mode (default: report)',
    )
    p.add_argument(
        '--strategy',
        choices=['collection-wins', 'member-wins'],
        default='collection-wins',
        help='Edit strategy when fixing violations (default: collection-wins)',
    )
    p.add_argument(
        '--aspects', default='all',
        help='Comma-separated aspects to check (default: all)',
    )
    p.add_argument(
        '--backup-dir',
        default=None,
        help='Directory for backups (default: same directory as each input file)',
    )
    p.add_argument(
        '--restore-from',
        default=None,
        help='Specific backup file to restore (use with --mode restore)',
    )
    p.add_argument(
        '--verbose', action='store_true',
        help='Show passing checks too',
    )
    p.add_argument(
        '--normalize-tz', action='store_true',
        help='Treat times differing only in Z/tz-suffix as equal',
    )
    p.add_argument(
        '--open-end', action='store_true',
        help='Under member-wins, produce open-ended time intervals (end="..")',
    )
    p.add_argument(
        '--summary', action='store_true',
        help=(
            'Print a per-file summary table at the end. '
            'Enabled automatically when processing multiple files.'
        ),
    )
    return p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = build_parser()
    args = parser.parse_args()

    aspects = parse_aspects(args.aspects)
    if not aspects:
        print('ERROR: No valid aspects specified.', file=sys.stderr)
        sys.exit(1)

    # ── RESTORE MODE — requires a single explicit file ─────────────────────
    if args.mode == 'restore':
        if len(args.targets) != 1 or args.dirs:
            print('ERROR: --mode restore requires exactly one file target.',
                  file=sys.stderr)
            sys.exit(1)
        input_file = args.targets[0]
        if not os.path.isfile(input_file):
            print(f'ERROR: File not found: {input_file}', file=sys.stderr)
            sys.exit(1)
        if args.restore_from:
            if not os.path.isfile(args.restore_from):
                print(f'ERROR: Backup not found: {args.restore_from}',
                      file=sys.stderr)
                sys.exit(1)
            print(restore_backup(args.restore_from, input_file))
        else:
            backups = list_backups(input_file, args.backup_dir)
            if not backups:
                print(f'No backups found for "{input_file}".')
                sys.exit(0)
            print(f'\nAvailable backups for "{input_file}":')
            for i, b in enumerate(backups, 1):
                print(f'  [{i}] {b}')
            choice = input('\nEnter number to restore (or q to quit): ').strip()
            if choice.lower() == 'q':
                sys.exit(0)
            try:
                idx = int(choice) - 1
                assert 0 <= idx < len(backups)
            except (ValueError, AssertionError):
                print('Invalid choice.')
                sys.exit(1)
            print(restore_backup(backups[idx], input_file))
        sys.exit(0)

    # ── Resolve target files ───────────────────────────────────────────────
    files = resolve_targets(args.targets, args.dirs, args.recursive)

    if not files:
        print('No JSON files found to process.', file=sys.stderr)
        sys.exit(1)

    multi = len(files) > 1
    show_summary = args.summary or multi

    if multi:
        print(f'\nProcessing {len(files)} file(s)...')

    # ── Process each file ──────────────────────────────────────────────────
    results = []
    exit_code = 0

    for file_path in files:
        if multi:
            print(f'\n{"━" * 70}')
            print(f'  {file_path}')
            print(f'{"━" * 70}')

        result = process_file(
            file_path,
            aspects=aspects,
            mode=args.mode,
            strategy=args.strategy,
            normalize_tz=args.normalize_tz,
            open_end=args.open_end,
            backup_dir=args.backup_dir,
            verbose=args.verbose,
        )
        results.append(result)

        if result['error']:
            exit_code = 1
        elif result['violations'] > 0 and args.mode == 'report':
            exit_code = 1

    # ── Summary table ──────────────────────────────────────────────────────
    if show_summary:
        print_summary(results, aspects, args.strategy)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()

