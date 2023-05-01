# SOSA Observation (Schema)

*Version 1.0*

This building blocks defines an observation according to the SOSA/SSN specification.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Description

## SOSA Observation

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."
## Examples

### Example of SOSA observation
#### json
```json
{
  "type": "Feature",
  "featureType": "sosa:Observation",
  "properties": {
    "hasFeatureOfInterest": "http://example.com/fois/1",
    "hasSimpleResult": 33,
    "resultTime": "2022-05-01T22:33:44Z"
}
```

#### ttl
```ttl
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <http://example.com/fois/1> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
```

## Schema

[schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/unstable/sosa/_sources/features/observation/schema.yaml)

```yaml
"$schema": https://json-schema.org/draft/2020-12/schema
description: 'SOSA Observation'
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

```
## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
