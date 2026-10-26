---
name: spec-examples-check
description: Check that the spec-examples building blocks (_sources/spec-examples/**) are up to date with the examples in the latest SOSA/SSN specification document (w3c/sdw-sosa-ssn gh-pages). Reports examples missing from the bblocks, bblock examples no longer in the spec, duplicates, broken refs, non-passing builds. Use when asked whether spec-examples is current, after the SOSA spec changes, or before regenerating spec-example blocks.
---

# Check spec-examples against the SOSA/SSN document

The spec-examples blocks reference example files by URL
(`https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/...`), so file *content* is always the latest.
What drifts is the **set** of examples. This skill compares that set with the document.

## What counts as "in the document"

The document is the respec source in `w3c/sdw-sosa-ssn`, branch `gh-pages`, folder `ssn/`:

| kind | how it is found | required in bblocks? |
|------|-----------------|----------------------|
| `included` | `<pre class="example ..." data-include="./rdf/...">` in a chapter that `index.html` includes via `data-include` | yes |
| `linked` | `<a href="...rdf/examples/x.ttl">` in an included chapter | yes |
| `folder` | file in `ssn/rdf/examples/`, when a chapter links to the folder itself (CompleteExamples does) | no, allowed |

HTML comments are ignored. Chapters not included by `index.html` (e.g. `System-capabilities-0.html`)
are ignored.

## Run it

From the repo root:

```bash
python .claude/skills/spec-examples-check/scripts/check_spec_examples.py
```

Needs Python with `pyyaml`. By default it reads the live `gh-pages` source from
raw.githubusercontent.com and lists the examples folder through the GitHub API.
Options:

- `--spec-dir ../sdw-sosa-ssn/ssn`: use a local clone instead. Run `git fetch` first and check it
  is at `origin/gh-pages`, otherwise the result is not "latest".
- `--no-network`: skip the HEAD check of every bblock ref.
- `--strict`: also flag bblock examples that are only in the examples folder.
- `--build-dir build-local`: read test results from a local build instead of the committed `build/`.
- `--json`: machine-readable report.

Exit code: 0 in sync, 1 out of date, 2 error.

## Reading the report

- **MISSING from bblocks**: in the document, not in any `examples.yaml`. To add them, run the
  `spec-examples-jsonld` skill. It classifies the examples and regenerates the grouped blocks.
  Do not hand-add them to the parent block.
- **IN bblocks but NOT included in document**:
  - `[in examples folder]`: still published and reachable from the document's examples folder
    link. Keep it.
  - `[STALE: not in spec]`: the file is gone from the spec. Remove it (regenerating removes it).
- **DUPLICATED across blocks**: the same URL appears in two group blocks. Usually a sign that the
  blocks were hand-edited after generation.
- **BROKEN refs**: the URL no longer resolves. The spec renamed or moved the file.
- **Build status not 'passed'**: reads `<build-dir>/tests/sosa/spec-examples/<group>/<base>.validation_*.txt`
  (default: the committed `build/`). "not built" means the example was added after the last CI build.

## Reporting back

Summarise counts and list each missing or stale example with its spec chapter. If anything is
missing, offer to run `spec-examples-jsonld`. If the classifier (run by that skill) warns about a
non-standard SOSA namespace, that is a bug in the spec example. Report it upstream to
w3c/sdw-sosa-ssn. Don't work around it here.
