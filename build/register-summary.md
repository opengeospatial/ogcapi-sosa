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

### `ogc.sosa.properties.asset` — Asset Properties

**Type:** schema

This building block defines the set of properties common to any SOSA Asset - the abstract physical or virtual entity that can be hosted, deployed, or host/deploy other Assets. It generalizes the properties shared by System and Platform and is not intended to be used directly by itself.

### `ogc.sosa.properties.deployment` — Deployment Properties

**Type:** schema

This building block defines the set of properties for a SOSA Deployment - the arrangement of one or more Assets to execute Procedures with respect to designated features of interest, typically for a period of time.

### `ogc.sosa.properties.execution` — Execution Properties

**Type:** schema

This building block defines the set of properties common to any SOSA Execution - the abstract act of carrying out a Procedure using a System. It generalizes the properties shared by Observation, Actuation and Sampling and is not intended to be used directly by itself.

### `ogc.sosa.properties.sample` — Sample Properties

**Type:** schema

This building block defines the set of properties for a SOSA Sample - a feature which is intended to be representative of a FeatureOfInterest on which Observations may be made, typically the result of a Sampling.

### `ogc.sosa.spec-examples` — Tests for SOSA specification

**Type:** schema

This BuildingBlock adds test cases from the SOSA specification to the base Observation properties model

### `ogc.sosa.properties.platform` — SOSA Platform

**Type:** schema

This building block defines the set of properties for an observation Platform according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

### `ogc.sosa.properties.system` — System Properties

**Type:** schema

This building block defines the set of properties common to any SOSA System - the abstract Asset that carries out Procedures (Observations, Actuations, or Samplings). It generalizes the properties shared by Sensor, Actuator and Sampler and is not intended to be used directly by itself.

### `ogc.sosa.properties.actuation` — Actuation Properties

**Type:** schema

This building block defines the set of properties for a SOSA Actuation - the Act of carrying out an Actuating Procedure to change the state of the world via an Actuator.

### `ogc.sosa.properties.executionCollection` — ExecutionCollection Properties

**Type:** schema

This building block defines the set of properties common to any SOSA ExecutionCollection - the abstract collection of Executions (Observations, Actuations, or Samplings). It generalizes ObservationCollection, ActuationCollection and SamplingCollection and is not intended to be used directly by itself.

### `ogc.sosa.properties.observation-owa` — Observation Properties (SOSA OWA)

**Type:** schema

This is set of properties defined by the SOSA ontology, assuming a "Open World Assumption" where mandatory properties may be provided by other related objects.

### `ogc.sosa.properties.sampling` — Sampling Properties

**Type:** schema

This building block defines the set of properties for a SOSA Sampling - the Act of carrying out a Sampling Procedure to create or transform one or more samples.

### `ogc.sosa.properties.sampleCollection` — SampleCollection Properties

**Type:** schema

This building block defines the set of properties for a SOSA SampleCollection - a collection of one or more Samples, whose members share a common value for one or more properties.

### `ogc.sosa.properties.actuator` — Actuator Properties

**Type:** schema

This building block defines the set of properties for a SOSA Actuator - a System that is used by, or implements, an Actuating Procedure that changes the state of the world.

### `ogc.sosa.properties.sampler` — Sampler Properties

**Type:** schema

This building block defines the set of properties for a SOSA Sampler - a System that is used by, or implements, a Sampling Procedure to create or transform one or more samples.

### `ogc.sosa.properties.sensor` — SOSA Sensor

**Type:** schema

An identifiable entity that can generate Observations pertaining to an ObservableProperty by implementing an ObservingProcedure. Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure. Sensors respond to a stimulus, e.g., a change in the environment, or input data composed from the results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.

### `ogc.sosa.properties.actuationCollection` — ActuationCollection Properties

**Type:** schema

This building block defines the set of properties for a SOSA ActuationCollection - a collection of one or more Actuations, whose members share a common value for one or more properties.

### `ogc.sosa.properties.observation` — Observation Properties

**Type:** schema

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

### `ogc.sosa.properties.samplingCollection` — SamplingCollection Properties

**Type:** schema

This building block defines the set of properties for a SOSA SamplingCollection - a collection of one or more Samplings, whose members share a common value for one or more properties.

### `ogc.sosa.features.asset` — Asset Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA Asset - the abstract physical or virtual entity that can be hosted, deployed, or host/deploy other Assets, using the properties defined in the Asset Properties schema. It generalizes the feature-level building blocks shared by System and Platform and is not intended to be used directly by itself.

### `ogc.sosa.features.deployment` — Deployment Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA Deployment, using the properties defined in the Deployment Properties schema.

### `ogc.sosa.features.execution` — Execution Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA Execution - the abstract act of carrying out a Procedure using a System, using the properties defined in the Execution Properties schema. It generalizes the feature-level building blocks shared by Observation, Actuation and Sampling and is not intended to be used directly by itself.

### `ogc.sosa.features.sample` — Sample Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA Sample, using the properties defined in the Sample Properties schema.

### `ogc.sosa.properties.observationCollection` — ObservationCollection Properties

**Type:** schema

This building block defines an ObservationCollection according to the SOSA/SSN v1.1 specification. It defines a set of logical rules regarding presence of mandatory properties anywhere within a potentially nested collection hierarchy. (implemented in SHACL, exploiting the semantic mapping to SOSA)

### `ogc.sosa.features.executionCollection` — ExecutionCollection Feature

**Type:** schema

This building block defines a GeoJSON FeatureCollection containing a SOSA ExecutionCollection - the abstract collection of Executions, using the properties defined in the ExecutionCollection Properties schema. It generalizes the feature-level building blocks shared by ObservationCollection, ActuationCollection and SamplingCollection and is not intended to be used directly by itself.

### `ogc.sosa.features.platform` — Platform Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA Platform - an Asset that hosts other Assets - using the properties defined in the Platform Properties schema.

### `ogc.sosa.features.system` — System Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA System - the abstract Asset that carries out Procedures, using the properties defined in the System Properties schema. It generalizes the feature-level building blocks shared by Sensor, Actuator and Sampler and is not intended to be used directly by itself.

### `ogc.sosa.features.actuation` — Actuation Feature

**Type:** schema

This building block defines a GeoJSON feature for a SOSA Actuation - the Act of carrying out an Actuating Procedure to change the state of the world via an Actuator. Uses the properties defined in the Actuation Properties schema.

### `ogc.sosa.features.observation` — SOSA Observation Feature

**Type:** schema

This building blocks defines a GeoJSON feature containing a SOSA Observation, using the properties defined in the Observation Properties schema

### `ogc.sosa.features.sampling` — Sampling Feature

**Type:** schema

This building block defines a GeoJSON feature for a SOSA Sampling - the Act of carrying out a Sampling Procedure to create or transform one or more samples. Uses the properties defined in the Sampling Properties schema.

### `ogc.sosa.features.sampleCollection` — SampleCollection Feature

**Type:** schema

This building block defines a GeoJSON FeatureCollection containing a SOSA SampleCollection, using the properties defined in the SampleCollection Properties schema.

### `ogc.sosa.features.actuator` — Actuator Feature

**Type:** schema

This building block defines a GeoJSON feature for a SOSA Actuator - a System that is used by, or implements, an Actuating Procedure that changes the state of the world. Uses the properties defined in the Actuator Properties schema.

### `ogc.sosa.features.sampler` — Sampler Feature

**Type:** schema

This building block defines a GeoJSON feature for a SOSA Sampler - a System that is used by, or implements, a Sampling Procedure to create or transform one or more samples. Uses the properties defined in the Sampler Properties schema.

### `ogc.sosa.features.sensor` — Sensor Feature

**Type:** schema

This building block defines a GeoJSON feature containing a SOSA Sensor - a System that implements, or is used by, a Sensing/Observing Procedure - using the properties defined in the Sensor Properties schema.

### `ogc.sosa.features.actuationCollection` — ActuationCollection Feature

**Type:** schema

This building block defines the set of a GeoJSON FeatureCollection containing a SOSA ActuationCollection - a collection of one or more Actuations, whose members share a common value for one or more properties.

### `ogc.sosa.features.observationCollection` — SOSA ObservationCollection Feature

**Type:** schema

This building blocks defines an ObservationCollection Feature according to the SOSA/SSN v1.1 specification.

### `ogc.sosa.features.samplingCollection` — SamplingCollection Feature

**Type:** schema

This building block defines the set of a GeoJSON FeatureCollection containing a SOSA SamplingCollection - a collection of one or more Samplings, whose members share a common value for one or more properties.

