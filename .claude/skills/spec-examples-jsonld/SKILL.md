---
name: spec-examples-jsonld
description: Build and install the Turtle-to-JSON-LD transform for the SOSA spec examples, and (re)generate _sources/spec-examples/ as grouped child bblocks (observations, observation-collections, samplings, deployments, ...). Each group validates its transform output against a different target SOSA properties bblock using output profile validation. Use to add new spec examples, regroup them, or change the JSON-LD conversion.
---

# Spec examples → JSON-LD against the SOSA bblocks

The SOSA/SSN spec examples are Turtle. This skill converts each one into JSON that follows the
schema of the matching SOSA bblock (e.g. `ogc.sosa.properties.observation`). The output carries
an `@context` that holds only the prefixes it needs. Output profile validation then checks it
against that bblock: JSON Schema, then JSON-LD uplift with the target's context, then SHACL. The
uplifted `.jsonld` written by the validator is the canonical JSON-LD. Its `@context` is
`[<target context URL>, {prefixes}]`.

Run `spec-examples-check` first to see what is missing.

## Pieces

| file | role |
|------|------|
| `scripts/classify_examples.py` | collects document examples and existing bblock examples, parses each one, finds its **root** SOSA resource(s), assigns a group, writes `plan.yaml` |
| `scripts/sync_spec_example_blocks.py` | turns the plan into the child blocks and installs the transform |
| `assets/ttl_to_sosa_json.py` | the transform (python, runs inside bblocks-postprocess: rdflib + pyld) |

Generated under `_sources/spec-examples/`:

```
examples.yaml                    'other' examples (no SOSA root): Turtle validation only
transforms/ttl_to_sosa_json.py   installed copy of the transform
<group>/bblock.json              ogc.sosa.spec-examples.<group>
<group>/schema.yaml              $ref: bblocks://<target>  (inherits target context + SHACL)
<group>/examples.yaml            URL refs into the spec, base-output-filename per example
<group>/transforms.yaml          ttl-to-jsonld, ref ../transforms/ttl_to_sosa_json.py,
                                 outputs.profiles: [bblocks://<target>]
<group>/description.md
```

## Grouping rules (classify_examples.py `GROUPS`)

Groups are checked in priority order. The first group with at least one root wins:
observation-collections → sample-collections → observations → samplings → actuations →
deployments → samples (incl. MaterialSample) → platforms → systems (Sensor/Actuator/Sampler/System).
Anything else goes to `other`.

An instance counts as a **root** unless it is embedded:
- it is a blank node that something else references, or
- something references it through a non-SOSA/SSN predicate (e.g. `owl:hasValue` in a restriction,
  as in the system-type examples), or
- an instance of the same or a higher-priority class references it through a SOSA/SSN predicate.
  Inverse links from lower-priority resources don't count, so a Sample's `isResultOf` does not
  hide its Sampling.

If an example has several roots, the sync step writes one example per root, each with
`x-root: <IRI>`, which the transform reads from `context.example`. JSON-LD originals (e.g.
`forecast.jsonld`) stay in the parent block as RDF-only examples, with output name `<name>-jsonld`.

## Transform behaviour (transforms.yaml `metadata`)

- `rootClasses` / `containerClasses`: root selection, the same rule as the classifier.
- Frames the root (`@embed: @once`), compacts it with the block's own assembled context (from
  `jsonld_context_path`, which is the target's context because of the schema `$ref`), then drops
  that context.
- `coerce`: optional typed-literal coercions added to the local `@context`, for terms a target
  schema constrains to plain strings but its context doesn't coerce. None are needed now:
  `sosa-ssn.jsonld` coerces `resultTime`, `startTime` and `endTime` to `xsd:dateTime`.
- `suppressTerms`: context terms to avoid. Default: `features`, the GeoJSON alias of
  `sosa:hasMember`, so the schema's `hasMember` is used.
- Blank-node roots are skolemised just long enough to frame them, then the `id` is removed.

## Run it

```bash
# 1. plan (use a local clone for speed: git fetch it first)
python .claude/skills/spec-examples-jsonld/scripts/classify_examples.py \
    --spec-dir ../sdw-sosa-ssn/ssn --out <scratch>/plan.yaml
# review the stderr table; edit plan.yaml 'group' values to override a classification
# 2. generate blocks + install transform
python .claude/skills/spec-examples-jsonld/scripts/sync_spec_example_blocks.py --plan <scratch>/plan.yaml
# 3. build locally (build-local/ is gitignored; don't overwrite the committed build/)
MSYS_NO_PATHCONV=1 docker run --rm --pull=always --workdir /workspace -v "$(pwd -W):/workspace" \
  ghcr.io/opengeospatial/bblocks-postprocess:latest --clean true \
  --base-url http://localhost:9090/register/ --register-file build-local/register.json \
  --annotated-path build-local/annotated --generated-docs-path build-local/generateddocs \
  --test-outputs-path build-local/tests
# 4. summarise
python .claude/skills/spec-examples-jsonld/scripts/summarize_results.py --tests build-local/tests
```

Needs local Python with `rdflib` and `pyyaml`. `pyld` is only needed to try the transform outside
the postprocessor. On Linux or macOS, use `$(pwd)` and drop `MSYS_NO_PATHCONV`.

## Where results land

`build-local/tests/sosa/spec-examples/<group>/`:
- `<base>.ttl` / `<base>.validation_{passed,failed}.txt`: the Turtle example against the target's SHACL
- `transforms/<base>.ttl-to-jsonld.json`: the transform output
- `transforms/ogc.sosa.properties.<x>/<base>.ttl-to-jsonld.{jsonld,ttl}`: uplift with the target context
- `transforms/ogc.sosa.properties.<x>/<base>.ttl-to-jsonld.validation_*.txt` and `_report.json`: profile validation

## Interpreting failures

A failure in profile validation means one of three things:
- **The target bblock's schema, context or shapes don't fit a spec-conformant example.** Report it
  against the target bblock.
- **The spec example is wrong.** Check the classifier warnings, e.g. a non-standard SOSA
  namespace. Report it upstream.
- **The transform's framing isn't right for that example.** Override its group in the plan, or set
  `x-root`.

Don't weaken the target schemas to make the outputs pass.
