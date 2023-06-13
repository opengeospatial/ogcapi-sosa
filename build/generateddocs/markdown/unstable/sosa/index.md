
# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

`ogc.unstable.sosa` *v1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

Building Blocks for implementing the core classes of the []Observations and Measurements model]

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
  x-jsonld-extra-terms: {}
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: features/observation/schema.yaml
  - type: object
    properties:
      properties:
        $ref: examples/vectorObservation/schema.yaml
  x-jsonld-extra-terms: {}
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
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    Sample: http://www.w3.org/ns/sosa/Sample
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasResult: http://www.w3.org/ns/sosa/hasResult
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observationCollection/schema.yaml
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    Sample: http://www.w3.org/ns/sosa/Sample
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasResult: http://www.w3.org/ns/sosa/hasResult
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
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    Sample: http://www.w3.org/ns/sosa/Sample
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasResult: http://www.w3.org/ns/sosa/hasResult
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
    hasMember:
      type: array
      items:
        oneOf:
        - $ref: properties/observation/schema.yaml
        - type: string
      minItems: 1
      x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
  required:
  - hasMember
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
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    implements: http://www.w3.org/ns/ssn/implements
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    Sample: http://www.w3.org/ns/sosa/Sample
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasResult: http://www.w3.org/ns/sosa/hasResult

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
    "hasSample": "sosa:hasSample",
    "isPropertyOf": "ssn:isPropertyOf",
    "isSampleOf": "sosa:isSampleOf",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Observation": "sosa:Observation",
    "isProxyFor": "ssn:isProxyFor",
    "implements": "ssn:implements",
    "deployedSystem": "ssn:deployedSystem",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "forProperty": "ssn:forProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isResultOf": "sosa:isResultOf",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "madeByActuator": "sosa:madeByActuator",
    "isObservedBy": "sosa:isObservedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasDeployment": "ssn:hasDeployment",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeBySampler": "sosa:madeBySampler",
    "isHostedBy": "sosa:isHostedBy",
    "madeSampling": "sosa:madeSampling",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "observes": "sosa:observes",
    "detects": "ssn:detects",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "actsOnProperty": "sosa:actsOnProperty",
    "hosts": "sosa:hosts",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "geopose:position",
    "angles": "geopose:angles",
    "yaw": "geopose:yaw",
    "pitch": "geopose:pitch",
    "roll": "geopose:roll",
    "lat": "geopose:lat",
    "lon": "geopose:lon",
    "h": "geopose:h",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": "geojson:coordinates"
      },
      "@id": "geojson:geometry"
    },
    "bbox": "geojson:bbox",
    "links": "rdfs:seeAlso"
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

