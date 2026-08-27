# Observations (ISO 19156, OGC/W3C SOSA)

Building blocks for implementation of OGC Observations Measurements and Samples (ISO 19156 aka OMS) using the OGC API Features schema and the OGC/W3C SOSA ontology

Each building block defines a reusable JSON schema that is mapped to the equivalent SOSA concept (and transitively mapped to OMS requirements via SOSA).

Each fragment allows for transparent and validatable use of JSON-LD contexts to map schema elements to equivalent terms from the SOSA ontology. 

 _These components are under review by the OMS SWG as candidate canonical implementations._ 

 Each building block allows for examples transformed to RDF, which in turn allows for the use of SHACL rules to enforce the semantics of the SOSA and OMS specifications.


## Building Blocks

### `ogc.sosa` — Sensor, Observation, Sample, and Actuator (SOSA)

**Type:** api

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

### `ogc.sosa.properties.observation-owa` — Observation Properties (SOSA OWA)

**Type:** schema

This is set of properties defined by the SOSA ontology, assuming a "Open World Assumption" where mandatory properties may be provided by other related objects.

### `ogc.sosa.spec-examples` — Tests for SOSA specification

**Type:** schema

This BuildingBlock adds test cases from the SOSA specification to the base Observation properties model

### `ogc.sosa.properties.sensor` — SOSA Sensor

**Type:** schema

An identifiable entity that can generate Observations pertaining to an ObservableProperty by implementing an ObservingProcedure. Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure. Sensors respond to a stimulus, e.g., a change in the environment, or input data composed from the results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.

### `ogc.sosa.properties.observation` — Observation Properties

**Type:** schema

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

### `ogc.sosa.properties.platform` — SOSA Platform

**Type:** schema

This building block defines the set of properties for an observation Platform according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

### `ogc.sosa.properties.observationCollection` — ObservationCollection Properties

**Type:** schema

This building block defines an ObservationCollection according to the SOSA/SSN v1.1 specification. It defines a set of logical rules regarding presence of mandatory properties anywhere within a potentially nested collection hierarchy. (implemented in SHACL, exploiting the semantic mapping to SOSA)

### `ogc.sosa.features.observation` — SOSA Observation Feature

**Type:** schema

This building blocks defines a GeoJSON feature containing a SOSA Observation, using the properties defined in the Observation Properties schema

### `ogc.sosa.features.observationCollection` — SOSA ObservationCollection Feature

**Type:** schema

This building blocks defines an ObservationCollection Feature according to the SOSA/SSN v1.1 specification.

