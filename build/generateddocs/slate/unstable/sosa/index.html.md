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
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    features: http://www.w3.org/ns/sosa/hasMember
    Sample: http://www.w3.org/ns/sosa/Sample
    implements: http://www.w3.org/ns/ssn/implements
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    detects: http://www.w3.org/ns/ssn/detects
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    resultTime: http://www.w3.org/ns/sosa/resultTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
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
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    Sample: http://www.w3.org/ns/sosa/Sample
    implements: http://www.w3.org/ns/ssn/implements
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    detects: http://www.w3.org/ns/ssn/detects
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    resultTime: http://www.w3.org/ns/sosa/resultTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
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
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    features: http://www.w3.org/ns/sosa/hasMember
    Sample: http://www.w3.org/ns/sosa/Sample
    implements: http://www.w3.org/ns/ssn/implements
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    detects: http://www.w3.org/ns/ssn/detects
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
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
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    features: http://www.w3.org/ns/sosa/hasMember
    Sample: http://www.w3.org/ns/sosa/Sample
    implements: http://www.w3.org/ns/ssn/implements
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    detects: http://www.w3.org/ns/ssn/detects
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasProperty: http://www.w3.org/ns/ssn/hasProperty

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
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hosts": "sosa:hosts",
    "madeObservation": "sosa:madeObservation",
    "isHostedBy": "sosa:isHostedBy",
    "hasSample": "sosa:hasSample",
    "madeActuation": "sosa:madeActuation",
    "hasDeployment": "ssn:hasDeployment",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasMember": "sosa:hasMember",
    "isPropertyOf": "ssn:isPropertyOf",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "features": "http://www.w3.org/ns/sosa/hasMember",
    "Sample": "sosa:Sample",
    "implements": "ssn:implements",
    "hasInput": "ssn:hasInput",
    "hasSubSystem": "ssn:hasSubSystem",
    "inDeployment": "ssn:inDeployment",
    "Observation": "sosa:Observation",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeSampling": "sosa:madeSampling",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isObservedBy": "sosa:isObservedBy",
    "isActedOnBy": "sosa:isActedOnBy",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isSampleOf": "sosa:isSampleOf",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "observes": "sosa:observes",
    "madeByActuator": "sosa:madeByActuator",
    "detects": "ssn:detects",
    "deployedSystem": "ssn:deployedSystem",
    "forProperty": "ssn:forProperty",
    "isResultOf": "sosa:isResultOf",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "madeBySampler": "sosa:madeBySampler",
    "hasOutput": "ssn:hasOutput",
    "hasProperty": "ssn:hasProperty",
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources`

