---
title: Sensor, Observation, Sample, and Actuator (SOSA) (Api)

toc_footers:
  - Version 1.0
  - <a href='#'>Sensor, Observation, Sample, and Actuator (SOSA)</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Sensor, Observation, Sample, and Actuator (SOSA) (Api)
---


# Sensor, Observation, Sample, and Actuator (SOSA) `ogc.unstable.sosa`

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

Building Blocks for implementing the core classes of the [Observations and Measurements model]

Each class is implemented using a schema is tied to the equivalent semantic description using the SOSA (Sensor, Observation, Sample, and Actuator) ontology.

An [aggregate schema](schema.yaml) is provided allowing any of these elements to be combined in a single payload, or each class may be used independently using the relevant schema.

TBD: Convenience API paths may be defined to support traversal of relationships - such as inverse relationships `hasResult`/`isResultOf` , `hasSample`/`isSampleOf` etc. where only one property is present in the data and the inverse is not otherwise accessible.


# JSON Schema

```yaml--schema
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
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    implements: http://www.w3.org/ns/ssn/implements
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
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
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    implements: http://www.w3.org/ns/ssn/implements
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
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
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    implements: http://www.w3.org/ns/ssn/implements
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
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
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    forProperty: http://www.w3.org/ns/ssn/forProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    implements: http://www.w3.org/ns/ssn/implements
    detects: http://www.w3.org/ns/ssn/detects
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange

```

Links to the schema:

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "hasDeployment": "ssn:hasDeployment",
    "isObservedBy": "sosa:isObservedBy",
    "hasInput": "ssn:hasInput",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeActuation": "sosa:madeActuation",
    "hasSubSystem": "ssn:hasSubSystem",
    "isPropertyOf": "ssn:isPropertyOf",
    "madeByActuator": "sosa:madeByActuator",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "madeObservation": "sosa:madeObservation",
    "madeBySampler": "sosa:madeBySampler",
    "forProperty": "ssn:forProperty",
    "inDeployment": "ssn:inDeployment",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "Observation": "sosa:Observation",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "observes": "sosa:observes",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "implements": "ssn:implements",
    "detects": "ssn:detects",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasProperty": "ssn:hasProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasSample": "sosa:hasSample",
    "isSampleOf": "sosa:isSampleOf",
    "isProxyFor": "ssn:isProxyFor",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "inCondition": "ssn-system:inCondition",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
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
    "rotations": "geopose:rotations",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "longitude": "geo:long",
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
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "Feature": "geojson:Feature",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "links": "rdfs:seeAlso"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources`

