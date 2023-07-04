
# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

`ogc.unstable.sosa` *v1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

Building Blocks for implementing the core classes of the [Observations and Measurements model]

Each class is implemented using a schema is tied to the equivalent semantic description using the SOSA (Sensor, Observation, Sample, and Actuator) ontology.

An [aggregate schema](schema.yaml) is provided allowing any of these elements to be combined in a single payload, or each class may be used independently using the relevant schema.

TBD: Convenience API paths may be defined to support traversal of relationships - such as inverse relationships `hasResult`/`isResultOf` , `hasSample`/`isSampleOf` etc. where only one property is present in the data and the inverse is not otherwise accessible.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Sensor, Observation, Sample, and Actuator (SOSA)
anyOf:
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: properties/observation/schema.yaml
  - type: object
    properties:
      hasResult:
        properties:
          pose:
            $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-ypr/schema.yaml
          distance:
            type: number
            x-jsonld-id: http://example.com/properties/distance
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
    required:
    - hasResult
    not:
      required:
      - hasSimpleResult
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: features/observation/schema.yaml
  - type: object
    properties:
      properties:
        $ref: examples/vectorObservation/schema.yaml
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  type: object
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observation/schema.yaml
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    observes: http://www.w3.org/ns/sosa/observes
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasMember: http://www.w3.org/ns/sosa/hasMember
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    detects: http://www.w3.org/ns/ssn/detects
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasInput: http://www.w3.org/ns/ssn/hasInput
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    features: http://www.w3.org/ns/sosa/hasMember
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hosts: http://www.w3.org/ns/sosa/hosts
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observationCollection/schema.yaml
      features:
        type: array
        items:
          oneOf:
          - $ref: features/observation/schema.yaml
          - type: string
        x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    observes: http://www.w3.org/ns/sosa/observes
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasMember: http://www.w3.org/ns/sosa/hasMember
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    detects: http://www.w3.org/ns/ssn/detects
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasInput: http://www.w3.org/ns/ssn/hasInput
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hosts: http://www.w3.org/ns/sosa/hosts
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation
  type: object
  properties:
    resultTime:
      type: string
      format: date-time
      x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    phenomenonTime:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    hasFeatureOfInterest:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
      x-jsonld-type: '@id'
    observedProperty:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    usedProcedure:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
      x-jsonld-type: '@id'
    madeBySensor:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
      x-jsonld-type: '@id'
    hasResult:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
    hasSimpleResult:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSimpleResult
  oneOf:
  - required:
    - hasResult
  - required:
    - hasSimpleResult
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    observes: http://www.w3.org/ns/sosa/observes
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    detects: http://www.w3.org/ns/ssn/detects
    hasInput: http://www.w3.org/ns/ssn/hasInput
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    features: http://www.w3.org/ns/sosa/hasMember
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hosts: http://www.w3.org/ns/sosa/hosts
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA ObservationCollection
  type: object
  properties:
    resultTime:
      type: string
      format: date-time
      x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    phenomenonTime:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    hasFeatureOfInterest:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
      x-jsonld-type: '@id'
    observedProperty:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    usedProcedure:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
      x-jsonld-type: '@id'
    madeBySensor:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
      x-jsonld-type: '@id'
  not:
    anyOf:
    - required:
      - hasResult
    - required:
      - hasSimpleResult
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    observes: http://www.w3.org/ns/sosa/observes
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    detects: http://www.w3.org/ns/ssn/detects
    hasInput: http://www.w3.org/ns/ssn/hasInput
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    features: http://www.w3.org/ns/sosa/hasMember
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hosts: http://www.w3.org/ns/sosa/hosts

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "resultTime": "http://www.w3.org/ns/sosa/resultTime",
    "phenomenonTime": "http://www.w3.org/ns/sosa/phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "http://www.w3.org/ns/sosa/observedProperty",
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "hasResult": "http://www.w3.org/ns/sosa/hasResult",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "observes": "sosa:observes",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "isProxyFor": "ssn:isProxyFor",
    "madeObservation": "sosa:madeObservation",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasMember": "sosa:hasMember",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasDeployment": "ssn:hasDeployment",
    "hasProperty": "ssn:hasProperty",
    "Sample": "sosa:Sample",
    "isSampleOf": "sosa:isSampleOf",
    "madeSampling": "sosa:madeSampling",
    "forProperty": "ssn:forProperty",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "detects": "ssn:detects",
    "hasInput": "ssn:hasInput",
    "madeBySampler": "sosa:madeBySampler",
    "hasOutput": "ssn:hasOutput",
    "implements": "ssn:implements",
    "deployedSystem": "ssn:deployedSystem",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "madeActuation": "sosa:madeActuation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "features": "http://www.w3.org/ns/sosa/hasMember",
    "isResultOf": "sosa:isResultOf",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "isObservedBy": "sosa:isObservedBy",
    "hasSample": "sosa:hasSample",
    "hosts": "sosa:hosts",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "http://example.com/geopose/position",
    "angles": "http://example.com/geopose/angles",
    "yaw": "http://example.com/geopose/yaw",
    "pitch": "http://example.com/geopose/pitch",
    "roll": "http://example.com/geopose/roll",
    "lat": "http://example.com/geopose/lat",
    "lon": "http://example.com/geopose/lon",
    "h": "http://example.com/geopose/h",
    "rotations": "geopose:rotations",
    "longitude": "geo:long",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "https://purl.org/geojson/vocab#properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": {
          "@id": "https://purl.org/geojson/vocab#coordinates",
          "@container": "@list"
        }
      },
      "@id": "https://purl.org/geojson/vocab#geometry"
    },
    "bbox": {
      "@id": "https://purl.org/geojson/vocab#bbox",
      "@container": "@list"
    },
    "MultiPoint": "geojson:MultiPoint",
    "GeometryCollection": "geojson:GeometryCollection",
    "Feature": "geojson:Feature",
    "Polygon": "geojson:Polygon",
    "MultiPolygon": "geojson:MultiPolygon",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiLineString": "geojson:MultiLineString",
    "Point": "geojson:Point",
    "LineString": "geojson:LineString",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources`

