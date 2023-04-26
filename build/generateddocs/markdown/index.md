# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

*Version 1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Description

Building Blocks for implementing the core classes of the []Observations and Measurements model]

Each class is implemented using a schema is tied to the equivalent semantic description using the SOSA (Sensor, Observation, Sample, and Actuator) ontology.

An [aggregate schema](schema.yaml) is provided allowing any of these elements to be combined in a single payload, or each class may be used independently using the relevant schema.

TBD: Convenience API paths may be defined to support traversal of relationships - such as inverse relationships `hasResult`/`isResultOf` , `hasSample`/`isSampleOf` etc. where only one property is present in the data and the inverse is not otherwise accessible.

## Schema

[schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/_sources/schema.yaml)

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Sensor, Observation, Sample, and Actuator (SOSA)
oneOf:
- description: SOSA Observation
  x-jsonld-context: ../../../sosa-ssn.jsonld
  type: object
  properties:
    hasResult: {}
    hasSimpleResult: {}
    resultTime:
      type: string
      format: date-time
    phenomenonTime:
      type:
      - object
      - string
    hasFeatureOfInterest:
      type:
      - object
      - string
    observedProperty:
      type:
      - object
      - string
    usedProcedure:
      type:
      - object
      - string
    madeBySensor:
      type:
      - object
      - string
  required:
  - resultTime
  - hasFeatureOfInterest
  oneOf:
  - required:
    - hasResult
  - required:
    - hasSimpleResult
- description: Sensor, Observation, Sample, and Actuator (SOSA)
  oneOf:
  - description: SOSA Observation
    x-jsonld-context: ../../../sosa-ssn.jsonld
    type: object
    properties:
      hasResult: {}
      hasSimpleResult: {}
      resultTime:
        type: string
        format: date-time
      phenomenonTime:
        type:
        - object
        - string
      hasFeatureOfInterest:
        type:
        - object
        - string
      observedProperty:
        type:
        - object
        - string
      usedProcedure:
        type:
        - object
        - string
      madeBySensor:
        type:
        - object
        - string
    required:
    - resultTime
    - hasFeatureOfInterest
    oneOf:
    - required:
      - hasResult
    - required:
      - hasSimpleResult
  - description: Sensor, Observation, Sample, and Actuator (SOSA)
    oneOf:
    - description: SOSA Observation
      x-jsonld-context: ../../../sosa-ssn.jsonld
      type: object
      properties:
        hasResult: {}
        hasSimpleResult: {}
        resultTime:
          type: string
          format: date-time
        phenomenonTime:
          type:
          - object
          - string
        hasFeatureOfInterest:
          type:
          - object
          - string
        observedProperty:
          type:
          - object
          - string
        usedProcedure:
          type:
          - object
          - string
        madeBySensor:
          type:
          - object
          - string
      required:
      - resultTime
      - hasFeatureOfInterest
      oneOf:
      - required:
        - hasResult
      - required:
        - hasSimpleResult
    - description: Sensor, Observation, Sample, and Actuator (SOSA)
      oneOf:
      - description: SOSA Observation
        x-jsonld-context: ../../../sosa-ssn.jsonld
        type: object
        properties:
          hasResult: {}
          hasSimpleResult: {}
          resultTime:
            type: string
            format: date-time
          phenomenonTime:
            type:
            - object
            - string
          hasFeatureOfInterest:
            type:
            - object
            - string
          observedProperty:
            type:
            - object
            - string
          usedProcedure:
            type:
            - object
            - string
          madeBySensor:
            type:
            - object
            - string
        required:
        - resultTime
        - hasFeatureOfInterest
        oneOf:
        - required:
          - hasResult
        - required:
          - hasSimpleResult
      - description: Sensor, Observation, Sample, and Actuator (SOSA)
        oneOf:
        - description: SOSA Observation
          x-jsonld-context: ../../sosa-ssn.jsonld
          type: object
          properties:
            hasResult: {}
            hasSimpleResult: {}
            resultTime:
              type: string
              format: date-time
            phenomenonTime:
              type:
              - object
              - string
            hasFeatureOfInterest:
              type:
              - object
              - string
            observedProperty:
              type:
              - object
              - string
            usedProcedure:
              type:
              - object
              - string
            madeBySensor:
              type:
              - object
              - string
          required:
          - resultTime
          - hasFeatureOfInterest
          oneOf:
          - required:
            - hasResult
          - required:
            - hasSimpleResult

```
## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
