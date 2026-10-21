---
name: spec-examples-jsonld
description: Build and install the Turtle-to-JSON-LD transform for the SOSA spec examples, and (re)generate _sources/spec-examples/ as grouped child bblocks (observations, observation-collections, samplings, deployments, ...). Each group validates its transform output against a different target SOSA properties bblock using output profile validation. Use to add new spec examples, regroup them, or change the JSON-LD conversion.
---

# Spec examples → JSON-LD against the SOSA bblocks

The SOSA/SSN spec examples are Turtle. This skill converts each one into JSON that follows the
schema of the matching SOSA bblock (e.g. `ogc.sosa.properties.observation`). The output is
self-describing JSON-LD: its `@context` is `[<target context URL>, {local}]`. The target's
published context maps the schema terms (`featureType: Observation` → `sosa:Observation`, …).
`{local}` holds only what that context does not define: the example's own prefixes and typed
literal coercions for its non-SOSA properties. It never redefines a target term. Output profile
validation then checks the output against the target: JSON Schema, then JSON-LD uplift, then
SHACL. During uplift the postprocessor inlines the target context from the local build instead of
fetching the URL; this needs a postprocessor with the "own context reference" fix.

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
closures/<base>.ttl              hand-written, optional: see "Per-example SHACL closures"
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
- `target`: the target bblock id. The transform compacts with that block's assembled context
  (falling back to its own, which is the same because of the schema `$ref`) and references it by
  URL: the build's base URL plus the target's annotated `context.jsonld` path.
- Frames the root (`@embed: @once`) and compacts it.
- Times become plain strings:
  - `xsd:dateTimeStamp` values of SOSA time properties are retyped to `xsd:dateTime`;
  - a `phenomenonTime` blank-node `time:Instant` with a single `inXSDDateTime` or
    `inXSDDateTimeStamp` becomes an `xsd:dateTime` string.
  An Interval or any other temporal entity stays an object, using the time terms scoped to
  `phenomenonTime` in `sosa-ssn.jsonld` (`hasBeginning`, `hasEnd`, `inXSDDateTime`, …).
- Other typed literals: a non-SOSA property whose values all share one datatype gets a local
  coercion (e.g. `"qudt:value": {"@type": "xsd:decimal"}`), so its values are plain strings.
  Integers, doubles and booleans are native JSON. Any value object that remains uses `@type`,
  not the `featureType` alias.
- `suppressTerms`: context terms to avoid. Default: `features`, the GeoJSON alias of
  `sosa:hasMember`, so the schema's `hasMember` is used.
- Blank-node roots are skolemised just long enough to frame them, then the `id` is removed.

## Per-example SHACL closures

Put a Turtle file at `_sources/spec-examples/closures/<base-output-filename>.ttl`. A file named
`<stem>.ttl` applies to every root of a multi-root example. The sync step adds it as the example
snippet's `shacl-closure`. It is then used in two places:
- the postprocessor adds it to the data when validating the Turtle example;
- the transform reads it from the transform context (`snippet['shacl-closure']`, resolved
  against the block directory) and applies SOSA collection rule 2 (see below). This works with
  the published postprocessor; no closure pass-through to output validation is needed.

**Inheriting missing values from containing collections.** A closure supplies an example's
missing execution properties by putting the executions (or the example's own collections) in a
collection that has them:

```turtle
closure:tree-height a sosa:ObservationCollection ;
    sosa:resultTime "2017-01-01T00:00:00Z"^^xsd:dateTime ;
    sosa:hasMember ex:observation_1087 .
```

The SHACL rules let members inherit from their collections. The transform copies the inherited
values into its output so the output is complete on its own. This applies to the root and to
the example's resources that are direct members of closure collections. Each one takes a
property it lacks from the nearest containing collection that has it, only if that collection
has a single value. Results are never inherited.
- Use `closure:` (`https://example.org/closure/`) IRIs and the `2017-01-01T00:00:00Z` time for
  values the example doesn't imply. Use the example's own IRIs only where it identifies the value,
  e.g. the sensor a capability collection describes.
- Never give a collection a value that conflicts with one a member already states. Collection
  rules 2–3 require the member's value to be one of the collection's. Use a separate closure
  collection for the members that lack it.
- A closure may also give an example resource a value directly, e.g. a result (never inherited)
  or several values of a collection property (only single values are inherited). The transform
  copies direct values of the inherited properties into its output.
- Blank-node executions can only be reached through a named collection that contains them.
- Relative IRIs (e.g. `<Observation/1>`) resolve against the example's URL. Set the closure's
  `@base` to that URL (see `closures/ex6.ttl`). This needs a postprocessor that parses URL
  examples with their URL as the base; the transform does so itself.

The sync step lists the closures it used and warns about any that match no example.

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
