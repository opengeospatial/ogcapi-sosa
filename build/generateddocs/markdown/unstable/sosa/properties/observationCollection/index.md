
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
  observes: http://www.w3.org/ns/sosa/observes
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  Sample: http://www.w3.org/ns/sosa/Sample
  hasInput: http://www.w3.org/ns/ssn/hasInput
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  detects: http://www.w3.org/ns/ssn/detects
  features: http://www.w3.org/ns/sosa/hasMember
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hosts: http://www.w3.org/ns/sosa/hosts
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  implements: http://www.w3.org/ns/ssn/implements
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasResult: http://www.w3.org/ns/sosa/hasResult
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform

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
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "Sample": "sosa:Sample",
    "hasInput": "ssn:hasInput",
    "madeSampling": "sosa:madeSampling",
    "isProxyFor": "ssn:isProxyFor",
    "hasSample": "sosa:hasSample",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "madeBySampler": "sosa:madeBySampler",
    "detects": "ssn:detects",
    "features": "sosa:hasMember",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "deployedSystem": "ssn:deployedSystem",
    "isActedOnBy": "sosa:isActedOnBy",
    "hosts": "sosa:hosts",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeObservation": "sosa:madeObservation",
    "madeByActuator": "sosa:madeByActuator",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "forProperty": "ssn:forProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "implementedBy": "ssn:implementedBy",
    "Observation": "sosa:Observation",
    "hasMember": "sosa:hasMember",
    "hasOutput": "ssn:hasOutput",
    "inDeployment": "ssn:inDeployment",
    "actsOnProperty": "sosa:actsOnProperty",
    "implements": "ssn:implements",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isResultOf": "sosa:isResultOf",
    "isHostedBy": "sosa:isHostedBy",
    "hasSubSystem": "ssn:hasSubSystem",
    "isObservedBy": "sosa:isObservedBy",
    "hasResult": "sosa:hasResult",
    "inCondition": "ssn-system:inCondition",
    "isSampleOf": "sosa:isSampleOf",
    "madeActuation": "sosa:madeActuation",
    "hasProperty": "ssn:hasProperty",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "deployedOnPlatform": "ssn:deployedOnPlatform"
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

