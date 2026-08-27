# `obs_collection_check.py` — Usage Summary

Checks JSON files for **SOSA/SSN ObservationCollection consistency** per
[W3C SSN §5.5.2.2](https://w3c.github.io/sdw-sosa-ssn/ssn/#SOSAObservationCollection).

---

## The Rule

If a property is declared on an `ObservationCollection`, every member observation must either **omit** that property (inheriting the collection value) or declare the **same** value. The seven governed properties are:

| Property | Alias |
|---|---|
| `hasFeatureOfInterest` | `foi` |
| `hasUltimateFeatureOfInterest` | — |
| `madeBySensor` | `sensor` |
| `observedProperty` | `property` |
| `phenomenonTime` | `time` |
| `resultTime` | `time` |
| `usedProcedure` | `procedure` |

---

## Input Targets

The script accepts **files, directories, and glob patterns** in any combination as positional arguments. If no targets are given it defaults to all `*.json` files in the current working directory. Backup files (`*.backup_*.json`) are always excluded automatically.

| Invocation | Files processed |
|---|---|
| *(no arguments)* | All `*.json` in the current directory |
| `data.json` | Single explicit file |
| `a.json b.json c.json` | Multiple explicit files |
| `surveys/` | All `*.json` directly inside `surveys/` |
| `"surveys/**/*.json"` | Glob pattern (quote to prevent shell expansion) |
| `--dir surveys/` | Equivalent to passing `surveys/` positionally |
| `--dir surveys/ --recursive` | Descends into all sub-directories |

`--dir` is repeatable and can be mixed with positional targets:

```bash
python obs_collection_check.py a.json --dir extra/ --dir archive/
```

---

## Quick Start

```bash
# Report violations for all *.json in the current directory
python obs_collection_check.py

# Report violations for all files in a specific directory
python obs_collection_check.py /path/to/surveys/

# Recurse into sub-directories
python obs_collection_check.py /path/to/surveys/ --recursive

# Fix all files in a directory automatically
python obs_collection_check.py /path/to/surveys/ --mode edit

# Restore one specific file
python obs_collection_check.py data.json --mode restore
```

---

## Modes

| `--mode` | Behaviour |
|---|---|
| `report` | Print violations only. No changes. *(default)* |
| `report-edit` | Print violations, then prompt **Y/n** before each fix. |
| `edit` | Apply all fixes automatically. Creates a backup per file first. |
| `restore` | Restore one file from a timestamped backup. Requires exactly one file target. |

---

## Edit Strategies

Select with `--strategy`. Only relevant for `report-edit` and `edit` modes.

### `collection-wins` *(default)*

The collection value is authoritative. Conflicting member values are **removed**; members then inherit from the collection.

```bash
python obs_collection_check.py surveys/ --mode edit --strategy collection-wins
```

Use this when the collection metadata is deliberately set and members should conform to it.

### `member-wins`

Member values are promoted upward to the collection.

- **All members agree** → collection is updated to that single value; the property is removed from all members (clean inheritance).
- **Members have different time values** → collection is set to an **ISO 8601 interval** spanning the full range; member values are kept as-is (the collection provides a bounding envelope).
- **Members have different non-time values** → flagged as unresolvable; manual intervention required.

```bash
python obs_collection_check.py surveys/ --mode edit --strategy member-wins
```

Use this when members are the ground truth and the collection header needs updating to reflect them.

---

## Time Intervals

Under `member-wins`, when member times differ the collection receives an interval:

```json
"resultTime": { "interval": ["2014-12-01T09:00:00Z", "2014-12-12T00:00:00Z"] }
```

Add `--open-end` to leave the end of the interval unbounded:

```json
"resultTime": { "interval": ["2014-12-01T09:00:00Z", ".."] }
```

Once an interval is set on the collection, member point values that fall **within** the interval are no longer flagged as violations.

---

## Options Reference

| Option | Description |
|---|---|
| `targets` | Files, directories, or glob patterns (positional, repeatable) |
| `--dir DIR` | Directory to scan; repeatable; combinable with positional targets |
| `--recursive` / `-r` | Descend into sub-directories when scanning directories |
| `--mode` | `report` \| `report-edit` \| `edit` \| `restore` |
| `--strategy` | `collection-wins` \| `member-wins` |
| `--aspects` | Comma-separated properties to check (default: `all`) |
| `--normalize-tz` | Treat times differing only in `Z`/timezone suffix as equal |
| `--open-end` | Under `member-wins`, produce open-ended intervals (`".."`) |
| `--backup-dir DIR` | Directory for backup files (default: same as each input file) |
| `--restore-from FILE` | Restore from a specific backup file path |
| `--summary` | Print summary table; auto-enabled when processing multiple files |
| `--verbose` | Show passing checks as well as violations |

---

## Multi-File Summary Table

When more than one file is processed a summary table is printed automatically:

```
======================================================================
  MULTI-FILE SUMMARY
  Aspects  : hasFeatureOfInterest, ..., resultTime, usedProcedure
  Strategy : collection-wins
======================================================================
  File                     Colls  Viols  Fixed  Status
  ----------------------------------------------------
  extended-example.json        2      0      0  ✓ clean
  parcels-angles.json          1      1      0  ✗ 1 violation(s)
  secondary-parcel.json        1     34     34  ✓ fixed
  topographic-string.json      1      4      4  ✓ fixed
  ----------------------------------------------------
  TOTAL                        5     39     38  2/4 files clean
======================================================================
```

Force the summary table for a single file with `--summary`.

---

## Aspect Filtering

Check only a subset of the seven properties:

```bash
# Only time-related aspects
python obs_collection_check.py surveys/ --aspects time

# Multiple specific aspects
python obs_collection_check.py surveys/ --aspects resultTime,usedProcedure,madeBySensor

# All (default)
python obs_collection_check.py surveys/ --aspects all
```

**Aliases:** `time` → `phenomenonTime, resultTime` · `procedure` → `usedProcedure` · `sensor` → `madeBySensor` · `property` → `observedProperty` · `foi` → `hasFeatureOfInterest`

---

## Timezone Normalisation

Times like `2022-05-22T00:00:00` and `2022-05-22T00:00:00Z` are semantically identical but string-different, causing violations under strict comparison. Use `--normalize-tz` to treat them as equal:

```bash
# Detect real conflicts only, ignoring Z-suffix differences
python obs_collection_check.py surveys/

# Fix: have members inherit the collection's Z-form value
python obs_collection_check.py surveys/ --mode edit \
  --strategy collection-wins --normalize-tz
```

---

## Backups and Restore

A timestamped backup is created **per file** before any file is modified:

```
data.backup_20260323_143022.json
```

Backup files are excluded from directory scans and glob expansion so they are never processed as input.

To restore:

```bash
# Interactive picker — lists all available backups for this file
python obs_collection_check.py data.json --mode restore

# Restore from a specific backup
python obs_collection_check.py data.json --mode restore \
  --restore-from data.backup_20260323_143022.json

# Store all backups in a central directory
python obs_collection_check.py surveys/ --mode edit \
  --backup-dir ./backups/
```

> `--mode restore` requires exactly one file target — it cannot be used with directory or glob targets.

---

## Collection Detection

ObservationCollections are detected automatically anywhere in the JSON tree by checking:

- `featureType` containing `ObservationCollection` or `sosa:ObservationCollection`
- `@type` or `type` fields with the same markers
- Presence of a `hasMember` key (structural heuristic)

Member observations are found under `features`, `hasMember`, or `members` arrays. Collection-level shared properties are resolved from a `properties` sub-object or the collection's top level.

---

## Exit Codes

| Code | Meaning |
|---|---|
| `0` | All files clean, or all violations fixed |
| `1` | One or more violations found (report mode), or a file could not be read |

---

## Common Recipes

```bash
# Inspect all files in the current directory
python obs_collection_check.py

# Inspect a whole project tree
python obs_collection_check.py --dir /path/to/project/ --recursive

# Fix Z-suffix mismatches across an entire directory
python obs_collection_check.py surveys/ --mode edit \
  --strategy collection-wins --normalize-tz

# Member times span a range — set collection to a covering interval
python obs_collection_check.py surveys/ --mode edit \
  --strategy member-wins --aspects time

# Same, but leave the interval end open
python obs_collection_check.py surveys/ --mode edit \
  --strategy member-wins --aspects time --open-end

# Review each fix interactively before applying
python obs_collection_check.py surveys/ --mode report-edit \
  --strategy member-wins

# Check only sensor and procedure consistency
python obs_collection_check.py surveys/ --aspects sensor,procedure

# Mix a specific file with an entire directory
python obs_collection_check.py special.json --dir bulk/

# Process a glob of files matching a prefix
python obs_collection_check.py "CSD_2024_*.json"

# Recursive scan across multiple directories
python obs_collection_check.py --dir surveys/ --dir archive/ --recursive

# Central backup directory, edit in place
python obs_collection_check.py surveys/ --mode edit \
  --backup-dir /backups/surveys/

# Force the summary table even for a single file
python obs_collection_check.py data.json --summary
```
