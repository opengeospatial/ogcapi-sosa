
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
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  detects: http://www.w3.org/ns/ssn/detects
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hosts: http://www.w3.org/ns/sosa/hosts
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  Observation: http://www.w3.org/ns/sosa/Observation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasInput: http://www.w3.org/ns/ssn/hasInput
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasMember: http://www.w3.org/ns/sosa/hasMember
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  features: http://www.w3.org/ns/sosa/hasMember
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  observes: http://www.w3.org/ns/sosa/observes
  implements: http://www.w3.org/ns/ssn/implements
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy

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
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "Sample": "sosa:Sample",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "actsOnProperty": "sosa:actsOnProperty",
    "isSampleOf": "sosa:isSampleOf",
    "inDeployment": "ssn:inDeployment",
    "detects": "ssn:detects",
    "hasDeployment": "ssn:hasDeployment",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hosts": "sosa:hosts",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasSample": "sosa:hasSample",
    "deployedSystem": "ssn:deployedSystem",
    "madeSampling": "sosa:madeSampling",
    "hasSubSystem": "ssn:hasSubSystem",
    "madeObservation": "sosa:madeObservation",
    "madeActuation": "sosa:madeActuation",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "Observation": "sosa:Observation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasOutput": "ssn:hasOutput",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isObservedBy": "sosa:isObservedBy",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasResult": "sosa:hasResult",
    "isProxyFor": "ssn:isProxyFor",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasProperty": "ssn:hasProperty",
    "hasInput": "ssn:hasInput",
    "forProperty": "ssn:forProperty",
    "hasMember": "sosa:hasMember",
    "madeByActuator": "sosa:madeByActuator",
    "madeBySampler": "sosa:madeBySampler",
    "inCondition": "ssn-system:inCondition",
    "features": "sosa:hasMember",
    "implementedBy": "ssn:implementedBy",
    "isResultOf": "sosa:isResultOf",
    "observes": "sosa:observes",
    "implements": "ssn:implements",
    "isHostedBy": "sosa:isHostedBy"
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

