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
            $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/schema.yaml
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
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    observes:
      x-jsonld-id: http://www.w3.org/ns/sosa/observes
      x-jsonld-type: '@id'
    isObservedBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
      x-jsonld-type: '@id'
    madeObservation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
      x-jsonld-type: '@id'
    madeBySensor:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
      x-jsonld-type: '@id'
    actsOnProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
      x-jsonld-type: '@id'
    isActedOnBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
      x-jsonld-type: '@id'
    madeActuation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
      x-jsonld-type: '@id'
    madeByActuator:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
      x-jsonld-type: '@id'
    hasSample:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
      x-jsonld-type: '@id'
    isSampleOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
      x-jsonld-type: '@id'
    madeSampling:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
      x-jsonld-type: '@id'
    madeBySampler:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
      x-jsonld-type: '@id'
    hasFeatureOfInterest:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
      x-jsonld-type: '@id'
    isFeatureOfInterestOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
      x-jsonld-type: '@id'
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    resultTime: http://www.w3.org/ns/sosa/resultTime
    usedProcedure:
      x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
      x-jsonld-type: '@id'
    hosts:
      x-jsonld-id: http://www.w3.org/ns/sosa/hosts
      x-jsonld-type: '@id'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    detects: http://www.w3.org/ns/ssn/detects
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    implements: http://www.w3.org/ns/ssn/implements
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    features: http://www.w3.org/ns/sosa/hasMember
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
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
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    observes:
      x-jsonld-id: http://www.w3.org/ns/sosa/observes
      x-jsonld-type: '@id'
    isObservedBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
      x-jsonld-type: '@id'
    madeObservation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
      x-jsonld-type: '@id'
    madeBySensor:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
      x-jsonld-type: '@id'
    actsOnProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
      x-jsonld-type: '@id'
    isActedOnBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
      x-jsonld-type: '@id'
    madeActuation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
      x-jsonld-type: '@id'
    madeByActuator:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
      x-jsonld-type: '@id'
    hasSample:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
      x-jsonld-type: '@id'
    isSampleOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
      x-jsonld-type: '@id'
    madeSampling:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
      x-jsonld-type: '@id'
    madeBySampler:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
      x-jsonld-type: '@id'
    hasFeatureOfInterest:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
      x-jsonld-type: '@id'
    isFeatureOfInterestOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
      x-jsonld-type: '@id'
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    resultTime: http://www.w3.org/ns/sosa/resultTime
    usedProcedure:
      x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
      x-jsonld-type: '@id'
    hosts:
      x-jsonld-id: http://www.w3.org/ns/sosa/hosts
      x-jsonld-type: '@id'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    detects: http://www.w3.org/ns/ssn/detects
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    implements: http://www.w3.org/ns/ssn/implements
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
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
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    observes:
      x-jsonld-id: http://www.w3.org/ns/sosa/observes
      x-jsonld-type: '@id'
    isObservedBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
      x-jsonld-type: '@id'
    madeObservation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
      x-jsonld-type: '@id'
    actsOnProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
      x-jsonld-type: '@id'
    isActedOnBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
      x-jsonld-type: '@id'
    madeActuation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
      x-jsonld-type: '@id'
    madeByActuator:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
      x-jsonld-type: '@id'
    hasSample:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
      x-jsonld-type: '@id'
    isSampleOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
      x-jsonld-type: '@id'
    madeSampling:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
      x-jsonld-type: '@id'
    madeBySampler:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
      x-jsonld-type: '@id'
    isFeatureOfInterestOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
      x-jsonld-type: '@id'
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hosts:
      x-jsonld-id: http://www.w3.org/ns/sosa/hosts
      x-jsonld-type: '@id'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    detects: http://www.w3.org/ns/ssn/detects
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    implements: http://www.w3.org/ns/ssn/implements
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    features: http://www.w3.org/ns/sosa/hasMember
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
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
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    observes:
      x-jsonld-id: http://www.w3.org/ns/sosa/observes
      x-jsonld-type: '@id'
    isObservedBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
      x-jsonld-type: '@id'
    madeObservation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
      x-jsonld-type: '@id'
    actsOnProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
      x-jsonld-type: '@id'
    isActedOnBy:
      x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
      x-jsonld-type: '@id'
    madeActuation:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
      x-jsonld-type: '@id'
    madeByActuator:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
      x-jsonld-type: '@id'
    hasSample:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
      x-jsonld-type: '@id'
    isSampleOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
      x-jsonld-type: '@id'
    madeSampling:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
      x-jsonld-type: '@id'
    madeBySampler:
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
      x-jsonld-type: '@id'
    isFeatureOfInterestOf:
      x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
      x-jsonld-type: '@id'
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hosts:
      x-jsonld-id: http://www.w3.org/ns/sosa/hosts
      x-jsonld-type: '@id'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    detects: http://www.w3.org/ns/ssn/detects
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    implements: http://www.w3.org/ns/ssn/implements
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    features: http://www.w3.org/ns/sosa/hasMember
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/

```

Links to the schema:

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "sosa:observedProperty",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "sosa:madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "sosa:madeByActuator",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isResultOf": "sosa:isResultOf",
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id"
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "ssn:isProxyFor",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "detects": "ssn:detects",
    "hasProperty": "ssn:hasProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "forProperty": "ssn:forProperty",
    "implements": "ssn:implements",
    "implementedBy": "ssn:implementedBy",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "hasSubSystem": "ssn:hasSubSystem",
    "deployedSystem": "ssn:deployedSystem",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn:systems/inCondition",
    "hasSystemCapability": "ssn:systems/hasSystemCapability",
    "hasSystemProperty": "ssn:systems/hasSystemProperty",
    "hasOperatingRange": "ssn:systems/hasOperatingRange",
    "hasOperatingProperty": "ssn:systems/hasOperatingProperty",
    "hasSurvivalRange": "ssn:systems/hasSurvivalRange",
    "hasSurvivalProperty": "ssn:systems/hasSurvivalProperty",
    "qualityOfObservation": "ssn:systems/qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "features": {
      "@id": "sosa:hasMember",
      "@container": "@set",
      "@context": {
        "features": {
          "@container": "@set",
          "@id": "sosa:hasMember"
        }
      }
    },
    "position": {
      "@id": "geopose:position",
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      }
    },
    "angles": {
      "@id": "geopose:angles",
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      }
    },
    "distance": {
      "@id": "http://example.com/properties/distance",
      "@type": "http://www.w3.org/2001/XMLSchema#float"
    },
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      }
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
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

