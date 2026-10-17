#!/usr/bin/env python3
"""
Summarise spec-examples validation after a postprocessor run: per group, the Turtle
example validation and the ttl-to-jsonld output profile validation, with the first
error lines of each failure.

Usage:
  python summarize_results.py [--tests build-local/tests] [--errors N] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ERROR_LINE = re.compile(r'^\s*(?:\*|ERROR|Validation Result|Message|Focus Node|Result Path|Value Node)', re.I)


def status_of(base: Path, stem: str) -> tuple[str, Path | None]:
    for st in ('failed', 'passed'):
        f = base / f'{stem}.validation_{st}.txt'
        if f.exists():
            return st, f
    return 'missing', None


def errors(path: Path | None, n: int) -> list[str]:
    if not path:
        return []
    lines, section = [], None
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        if line.startswith('=== ') and not line.startswith('=== End'):
            section = line.strip('= ').strip()
        if section in ('JSON Schema', 'SHACL', 'JSON-LD', 'Unknown', 'Turtle') and line.strip() \
                and not line.startswith('===') and (ERROR_LINE.search(line) or section != 'SHACL'):
            lines.append(f'[{section}] {line.strip()}')
    return lines[:n]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--tests', default='build-local/tests')
    ap.add_argument('--errors', type=int, default=4, help='error lines shown per failure')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()
    root = Path(args.tests) / 'sosa' / 'spec-examples'
    if not root.is_dir():
        print(f'No spec-examples test outputs under {root}', file=sys.stderr)
        return 2

    result = {}
    for d in sorted([root] + [p for p in root.iterdir() if p.is_dir() and p.name != 'transforms']):
        group = 'other' if d == root else d.name
        rows = []
        for ttl_report in sorted(d.glob('*.validation_*.txt')):
            stem = ttl_report.name.split('.validation_')[0]
            if '.ttl-to-jsonld' in stem:
                continue
            ex_status, ex_file = status_of(d, stem)
            row = {'example': stem, 'ttl': ex_status, 'ttl_errors': errors(ex_file, args.errors)
                   if ex_status == 'failed' else []}
            tdir = d / 'transforms'
            out = tdir / f'{stem}.ttl-to-jsonld.json'
            if group != 'other':
                row['transform'] = 'ok' if out.exists() else 'no output'
                for prof in [p for p in tdir.iterdir() if p.is_dir()] if tdir.is_dir() else []:
                    pst, pfile = status_of(prof, f'{stem}.ttl-to-jsonld')
                    row['profile'] = prof.name
                    row['profile_status'] = pst
                    row['profile_errors'] = errors(pfile, args.errors) if pst == 'failed' else []
            rows.append(row)
        if rows:
            result[group] = rows

    if args.json:
        print(json.dumps(result, indent=2))
        return 0
    totals = {'ttl': [0, 0], 'profile': [0, 0], 'no output': 0}
    for group, rows in result.items():
        print(f'\n## {group}')
        for r in rows:
            line = f"  {r['example']:46} ttl={r['ttl']:7}"
            totals['ttl'][r['ttl'] == 'passed'] += 1
            if 'transform' in r:
                if r['transform'] != 'ok':
                    totals['no output'] += 1
                    line += ' transform=NO OUTPUT'
                else:
                    line += f" profile={r.get('profile_status', 'missing')}"
                    totals['profile'][r.get('profile_status') == 'passed'] += 1
            print(line)
            for e in r['ttl_errors'] + r.get('profile_errors', []):
                print(f'      {e[:220]}')
    print(f"\nTurtle examples: {totals['ttl'][1]} passed, {totals['ttl'][0]} failed/missing")
    print(f"JSON-LD outputs: {totals['profile'][1]} passed profile validation, "
          f"{totals['profile'][0]} failed/missing, {totals['no output']} transform produced no output")
    return 0


if __name__ == '__main__':
    sys.exit(main())
