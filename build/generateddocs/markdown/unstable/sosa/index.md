
# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

`ogc.unstable.sosa` *v1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Status*](http://www.opengis.net/def/status): Under development

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
            $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/schema.yaml
          distance:
            type: number
    required:
    - hasResult
    not:
      required:
      - hasSimpleResult
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Observation Specialisation - a vector bearing and distance
  $defs:
    VectorObservation:
      allOf:
      - $ref: features/observation/schema.yaml
      - type: object
        properties:
          properties:
            $ref: examples/vectorObservation/schema.yaml
    VectorObservationCollection:
      allOf:
      - $ref: features/observationCollection/schema.yaml
      - type: object
        properties:
          features:
            type: array
            items:
              $ref: examples/vectorObservationFeature/schema.yaml/#/$defs/VectorObservation
  anyOf:
  - $ref: examples/vectorObservationFeature/schema.yaml/#/$defs/VectorObservation
  - $ref: examples/vectorObservationFeature/schema.yaml/#/$defs/VectorObservationCollection
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  type: object
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observation/schema.yaml
        x-jsonld-id: '@nest'
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    System: http://www.w3.org/ns/sosa/System
    Platform: http://www.w3.org/ns/sosa/Platform
    observedProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
      x-jsonld-type: '@id'
    id: '@id'
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
      x-jsonld-container: '@set'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
    detects: http://www.w3.org/ns/sosa/detects
    hasProperty: http://www.w3.org/ns/sosa/hasProperty
    isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
    forProperty: http://www.w3.org/ns/sosa/forProperty
    implements: http://www.w3.org/ns/sosa/implements
    implementedBy: http://www.w3.org/ns/sosa/implementedBy
    hasInput: http://www.w3.org/ns/sosa/hasInput
    hasOutput: http://www.w3.org/ns/sosa/hasOutput
    hasSubSystem:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
      x-jsonld-type: '@id'
      x-jsonld-container: '@set'
    deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
    hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/sosa/inDeployment
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
    featureType: '@type'
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn-system: http://www.w3.org/ns/ssn/systems/
    ssn: http://www.w3.org/ns/ssn/
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection-lenient/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observationCollection/schema.yaml
        x-jsonld-id: '@nest'
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
    System: http://www.w3.org/ns/sosa/System
    Platform: http://www.w3.org/ns/sosa/Platform
    observedProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
      x-jsonld-type: '@id'
    id: '@id'
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
      x-jsonld-container: '@set'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
    detects: http://www.w3.org/ns/sosa/detects
    hasProperty: http://www.w3.org/ns/sosa/hasProperty
    isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
    forProperty: http://www.w3.org/ns/sosa/forProperty
    implements: http://www.w3.org/ns/sosa/implements
    implementedBy: http://www.w3.org/ns/sosa/implementedBy
    hasInput: http://www.w3.org/ns/sosa/hasInput
    hasOutput: http://www.w3.org/ns/sosa/hasOutput
    hasSubSystem:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
      x-jsonld-type: '@id'
      x-jsonld-container: '@set'
    deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
    hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/sosa/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    featureType: '@type'
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn-system: http://www.w3.org/ns/ssn/systems/
    ssn: http://www.w3.org/ns/ssn/
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
      x-jsonld-type: '@id'
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
  anyOf:
  - required:
    - hasResult
  - required:
    - hasSimpleResult
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    System: http://www.w3.org/ns/sosa/System
    Platform: http://www.w3.org/ns/sosa/Platform
    id: '@id'
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
      x-jsonld-container: '@set'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
    detects: http://www.w3.org/ns/sosa/detects
    hasProperty: http://www.w3.org/ns/sosa/hasProperty
    isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
    forProperty: http://www.w3.org/ns/sosa/forProperty
    implements: http://www.w3.org/ns/sosa/implements
    implementedBy: http://www.w3.org/ns/sosa/implementedBy
    hasInput: http://www.w3.org/ns/sosa/hasInput
    hasOutput: http://www.w3.org/ns/sosa/hasOutput
    hasSubSystem:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
      x-jsonld-type: '@id'
      x-jsonld-container: '@set'
    deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
    hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/sosa/inDeployment
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
    properties: '@nest'
    featureType: '@type'
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn-system: http://www.w3.org/ns/ssn/systems/
    ssn: http://www.w3.org/ns/ssn/
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA ObservationCollection
  $defs:
    collection:
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
          x-jsonld-type: '@id'
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
            anyOf:
            - $ref: properties/observationCollection/schema.yaml/#/$defs/collection
            - $ref: properties/observation/schema.yaml
            - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
  allOf:
  - $ref: properties/observationCollection/schema.yaml/#/$defs/collection
  - not:
      anyOf:
      - required:
        - hasResult
      - required:
        - hasSimpleResult
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    System: http://www.w3.org/ns/sosa/System
    Platform: http://www.w3.org/ns/sosa/Platform
    id: '@id'
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
      x-jsonld-container: '@set'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
    detects: http://www.w3.org/ns/sosa/detects
    hasProperty: http://www.w3.org/ns/sosa/hasProperty
    isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
    forProperty: http://www.w3.org/ns/sosa/forProperty
    implements: http://www.w3.org/ns/sosa/implements
    implementedBy: http://www.w3.org/ns/sosa/implementedBy
    hasInput: http://www.w3.org/ns/sosa/hasInput
    hasOutput: http://www.w3.org/ns/sosa/hasOutput
    hasSubSystem:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
      x-jsonld-type: '@id'
      x-jsonld-container: '@set'
    deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
    hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/sosa/inDeployment
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    features: http://www.w3.org/ns/sosa/hasMember
    properties: '@nest'
    featureType: '@type'
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn-system: http://www.w3.org/ns/ssn/systems/
    ssn: http://www.w3.org/ns/ssn/
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Platform
  $definitions:
    Platform:
      anyOf:
      - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
      - type: object
        properties:
          hosts:
            type: array
            items:
              anyOf:
              - $ref: properties/platform/schema.yaml/#/$definitions/Platform
              - $ref: properties/sensor/schema.yaml#/$definitions/Sensor
            x-jsonld-id: http://www.w3.org/ns/sosa/hosts
            x-jsonld-type: '@id'
            x-jsonld-container: '@set'
  allOf:
  - $ref: properties/platform/schema.yaml/#/$definitions/Platform
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    System: http://www.w3.org/ns/sosa/System
    Platform: http://www.w3.org/ns/sosa/Platform
    observedProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
      x-jsonld-type: '@id'
    id: '@id'
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
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
    detects: http://www.w3.org/ns/sosa/detects
    hasProperty: http://www.w3.org/ns/sosa/hasProperty
    isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
    forProperty: http://www.w3.org/ns/sosa/forProperty
    implements: http://www.w3.org/ns/sosa/implements
    implementedBy: http://www.w3.org/ns/sosa/implementedBy
    hasInput: http://www.w3.org/ns/sosa/hasInput
    hasOutput: http://www.w3.org/ns/sosa/hasOutput
    hasSubSystem:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
      x-jsonld-type: '@id'
      x-jsonld-container: '@set'
    deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
    hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/sosa/inDeployment
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
    properties: '@nest'
    featureType: '@type'
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn-system: http://www.w3.org/ns/ssn/systems/
    ssn: http://www.w3.org/ns/ssn/
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Sensor
  $definitions:
    Sensor:
      anyOf:
      - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
      - type: object
        properties:
          id:
            $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
            x-jsonld-id: '@id'
          name:
            type: string
  allOf:
  - $ref: properties/sensor/schema.yaml/#/$definitions/Sensor
  x-jsonld-extra-terms:
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    System: http://www.w3.org/ns/sosa/System
    Platform: http://www.w3.org/ns/sosa/Platform
    observedProperty:
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
      x-jsonld-type: '@id'
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
      x-jsonld-container: '@set'
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
    wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
    detects: http://www.w3.org/ns/sosa/detects
    hasProperty: http://www.w3.org/ns/sosa/hasProperty
    isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
    forProperty: http://www.w3.org/ns/sosa/forProperty
    implements: http://www.w3.org/ns/sosa/implements
    implementedBy: http://www.w3.org/ns/sosa/implementedBy
    hasInput: http://www.w3.org/ns/sosa/hasInput
    hasOutput: http://www.w3.org/ns/sosa/hasOutput
    hasSubSystem:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
      x-jsonld-type: '@id'
      x-jsonld-container: '@set'
    deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
    hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
    inDeployment: http://www.w3.org/ns/sosa/inDeployment
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
    properties: '@nest'
    featureType: '@type'
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn-system: http://www.w3.org/ns/ssn/systems/
    ssn: http://www.w3.org/ns/ssn/

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
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
    "System": "sosa:System",
    "Platform": "sosa:Platform",
    "id": "@id",
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
      "@type": "@id",
      "@container": "@set",
      "@context": {}
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "sosa:isProxyFor",
    "wasOriginatedBy": "sosa:wasOriginatedBy",
    "detects": "sosa:detects",
    "hasProperty": "sosa:hasProperty",
    "isPropertyOf": "sosa:isPropertyOf",
    "forProperty": "sosa:forProperty",
    "implements": "sosa:implements",
    "implementedBy": "sosa:implementedBy",
    "hasInput": "sosa:hasInput",
    "hasOutput": "sosa:hasOutput",
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "deployedSystem": "sosa:deployedSystem",
    "hasDeployment": "sosa:hasDeployment",
    "deployedOnPlatform": "sosa:deployedOnPlatform",
    "inDeployment": "sosa:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasMember": {
      "@context": {
        "featureType": "@type"
      },
      "@id": "sosa:hasMember"
    },
    "features": {
      "@context": {
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        },
        "featureType": "@type"
      },
      "@container": "@set",
      "@id": "sosa:hasMember"
    },
    "properties": "@nest",
    "featureType": "geojson:collectionFeatureType",
    "position": {
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      },
      "@id": "geopose:position"
    },
    "angles": {
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      },
      "@id": "geopose:angles"
    },
    "type": "@type",
    "geometry": {
      "@context": {},
      "@id": "geojson:geometry"
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
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources`

