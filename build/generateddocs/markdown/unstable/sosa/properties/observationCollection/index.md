
# SOSA ObservationCollection (Schema)

`ogc.unstable.sosa.properties.observationCollection` *v1.0*

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
## Examples

### Example of SOSA ObservationCollection
#### json
```json
{ 
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z"
}
```

#### json
```json
{ 
  "observedProperty": "p1",
  "resultTime": "2022-05-01T22:33:44Z",
  "hasMember": [
    { 
      "@id": "a1",
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 1995.2,
    }
  ]
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:a1 ;
  sosa:observedProperty eg:p1 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.

eg:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
.
eg:p1 a skos:Concept;
  skos:prefLabel "Some Observable Property";
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
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
      - $ref: ../observation/schema.yaml
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
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  forProperty: http://www.w3.org/ns/ssn/forProperty
  Observation: http://www.w3.org/ns/sosa/Observation
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasInput: http://www.w3.org/ns/ssn/hasInput
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hosts: http://www.w3.org/ns/sosa/hosts
  detects: http://www.w3.org/ns/ssn/detects
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  observes: http://www.w3.org/ns/sosa/observes
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  implements: http://www.w3.org/ns/ssn/implements
  Sample: http://www.w3.org/ns/sosa/Sample
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
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
    "hasMember": "sosa:hasMember",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "forProperty": "ssn:forProperty",
    "Observation": "sosa:Observation",
    "actsOnProperty": "sosa:actsOnProperty",
    "isHostedBy": "sosa:isHostedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "madeSampling": "sosa:madeSampling",
    "hasResult": "sosa:hasResult",
    "hasSample": "sosa:hasSample",
    "isResultOf": "sosa:isResultOf",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "implementedBy": "ssn:implementedBy",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "madeByActuator": "sosa:madeByActuator",
    "hosts": "sosa:hosts",
    "detects": "ssn:detects",
    "madeActuation": "sosa:madeActuation",
    "deployedSystem": "ssn:deployedSystem",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isSampleOf": "sosa:isSampleOf",
    "isProxyFor": "ssn:isProxyFor",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasOutput": "ssn:hasOutput",
    "hasProperty": "ssn:hasProperty",
    "isObservedBy": "sosa:isObservedBy",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "observes": "sosa:observes",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "madeObservation": "sosa:madeObservation",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeBySampler": "sosa:madeBySampler",
    "inCondition": "ssn-system:inCondition",
    "implements": "ssn:implements",
    "Sample": "sosa:Sample",
    "hasDeployment": "ssn:hasDeployment",
    "hasSystemProperty": "ssn-system:hasSystemProperty"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/observationCollection`

