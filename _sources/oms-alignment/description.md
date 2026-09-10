# Alignment with ISO 19156 (OMS)

## Purpose and scope

This register uses SOSA (Sensor, Observation, Sample, and Actuator) as the RDF/OWL **formalism**
through which its building blocks realize the ISO 19156:2023 *Observations, Measurements and
Samples* (OMS) conceptual model — published jointly by ISO/TC 211 and OGC as OGC Abstract
Specification Topic 20, *Observations, Measurements and Samples* (O&M 3.0).

Every building block under `features/*` (a GeoJSON Feature) and `properties/*` (the bare property
set used inside that Feature, or embeddable elsewhere) carries the `rdfType` of a single SOSA class.
SOSA/SSN 2.0 in turn declares, in its
[SOSA-OMS extension module](https://github.com/w3c/sdw-sosa-ssn/blob/gh-pages/ssn/rdf/ontology/extensions/sosa-oms.ttl),
that each such SOSA class `ogc-ms:implements` one or more specific ISO 19156:2023 requirement
classes. This page collects those declarations so a reader checking conformance to OMS can trace,
class by class, which OGC requirement class each building block instantiates — and which building
blocks are SOSA/SSN-only generalizations that OMS does not define.

Not every SOSA class used here has a direct OMS counterpart. O&M 3.0 formally standardizes only the
*Observation* and *Sampling* branches of the model. *Actuation*, and the abstract generalizations
SOSA/SSN 2.0 introduces to unify Observation, Actuation and Sampling under one pattern (`Execution`,
`System`, `Asset`, and their `*Collection` counterparts), are SOSA/SSN extensions with no formal ISO
19156 class. These are marked "No OMS counterpart" below, with the reason.

## How to read the table

- **SOSA class** — the `sosa:` class implemented by the building block (see its `rdfType`).
- **Building blocks** — the Feature and Properties building blocks in this register that carry that
  `rdfType`.
- **OMS requirement class** — the ISO 19156:2023 / OGC Topic 20 (O&M 3.0) requirement class the SOSA
  class `ogc-ms:implements`, given as its requirement-class path under
  `http://www.opengis.net/spec/om/3.0/req/`.
- **Note** — clarification, including the reason where there is no formal OMS counterpart.

Each note below is also carried, as the opening clause, in the `abstract` of the corresponding
building block.

## Class alignment table

| SOSA class | Building blocks | OMS requirement class (O&M 3.0 / ISO 19156:2023) | Note |
|---|---|---|---|
| `sosa:Observation` | `features.observation`, `properties.observation`, `properties.observation-owa` | `obs-cpt/Observation` | Direct realization of `OM_Observation`. The `observation-owa` block is an Open World Assumption profile of the same requirement class. |
| `sosa:ObservationCollection` | `features.observationCollection`, `properties.observationCollection` | `obs-basic/ObservationCollection` | |
| `sosa:Sample` | `features.sample`, `properties.sample` | `sam-cpt/Sample` | |
| `sosa:SampleCollection` | `features.sampleCollection`, `properties.sampleCollection` | `sam-basic/SampleCollection` | |
| `sosa:Sampling` | `features.sampling`, `properties.sampling` | `sam-cpt/Sampling` | |
| `sosa:SamplingCollection` | `features.samplingCollection`, `properties.samplingCollection` | *No OMS counterpart* | Generalizes the `sam-basic/SampleCollection` collection pattern to acts of sampling; OMS defines no dedicated sampling-collection requirement class. |
| `sosa:Sensor` | `features.sensor`, `properties.sensor` | `obs-cpt/Observer` | The ISO 19156:2023 UML class is named `Observer`; SOSA keeps the name `Sensor` for backward compatibility with existing deployments. |
| `sosa:Sampler` | `features.sampler`, `properties.sampler` | `sam-cpt/Sampler` | |
| `sosa:Actuator` | `features.actuator`, `properties.actuator` | *No OMS counterpart* | Actuation is outside the scope of O&M/OMS, which standardizes observation and sampling only. |
| `sosa:Platform` | `features.platform`, `properties.platform` | `obs-cpt/Host` | |
| `sosa:Deployment` | `features.deployment`, `properties.deployment` | `obs-cpt/Deployment` | |
| `sosa:Actuation` | `features.actuation`, `properties.actuation` | *No OMS counterpart* | See `sosa:Actuator`, above. |
| `sosa:ActuationCollection` | `features.actuationCollection`, `properties.actuationCollection` | *No OMS counterpart* | See `sosa:Actuator`, above. |
| `sosa:System` | `features.system`, `properties.system` | *No OMS counterpart* | SOSA/SSN 2.0 abstraction over `Sensor`/`Actuator`/`Sampler` introduced to unify their shared properties; OMS keeps `Observer` and `Sampler` as unrelated peers rather than subclasses of a common superclass. |
| `sosa:Asset` | `features.asset`, `properties.asset` | *No OMS counterpart* | SOSA/SSN 2.0 abstraction over `System`/`Platform`. The nearest OMS concept is `obs-cpt/Host`, but OMS does not generalize hosting this broadly. |
| `sosa:Execution` | `features.execution`, `properties.execution` | *No OMS counterpart* | SOSA/SSN 2.0 abstraction generalizing `Observation`, `Actuation` and `Sampling` as acts of carrying out a `Procedure`; OMS has no equivalent abstract superclass. |
| `sosa:ExecutionCollection` | `features.executionCollection`, `properties.executionCollection` | *No OMS counterpart* | Generalizes `ObservationCollection`, `ActuationCollection` and `SamplingCollection`, none of which OMS treats uniformly. |

## Normative sources

- ISO 19156:2023, *Geographic information — Observations, measurements and samples*
- OGC Abstract Specification Topic 20, *Observations, Measurements and Samples* (O&M 3.0)
- W3C/OGC, *Semantic Sensor Network Ontology* — 2023 Edition (SOSA/SSN 2.0)
- The SOSA-OMS extension module (`sosa-oms.ttl`), which declares the `ogc-ms:implements` axioms this
  page is derived from
