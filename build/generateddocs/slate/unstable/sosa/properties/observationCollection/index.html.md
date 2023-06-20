---
title: SOSA ObservationCollection (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA ObservationCollection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA ObservationCollection (Schema)
---


# SOSA ObservationCollection `ogc.unstable.sosa.properties.observationCollection`

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/properties/observationCollection/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
# Examples

## Example of SOSA ObservationCollection

```json
{ 
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z"
}
```

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


# JSON Schema

```yaml--schema
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
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  forProperty: http://www.w3.org/ns/ssn/forProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hosts: http://www.w3.org/ns/sosa/hosts
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  Sample: http://www.w3.org/ns/sosa/Sample
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  observes: http://www.w3.org/ns/sosa/observes
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  implements: http://www.w3.org/ns/ssn/implements
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  detects: http://www.w3.org/ns/ssn/detects
  hasResult: http://www.w3.org/ns/sosa/hasResult
  Observation: http://www.w3.org/ns/sosa/Observation

```

Links to the schema:

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "forProperty": "ssn:forProperty",
    "madeObservation": "sosa:madeObservation",
    "isPropertyOf": "ssn:isPropertyOf",
    "inDeployment": "ssn:inDeployment",
    "hasSubSystem": "ssn:hasSubSystem",
    "hosts": "sosa:hosts",
    "inCondition": "ssn-system:inCondition",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOutput": "ssn:hasOutput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isActedOnBy": "sosa:isActedOnBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "isResultOf": "sosa:isResultOf",
    "isProxyFor": "ssn:isProxyFor",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isObservedBy": "sosa:isObservedBy",
    "hasSample": "sosa:hasSample",
    "isSampleOf": "sosa:isSampleOf",
    "hasInput": "ssn:hasInput",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeSampling": "sosa:madeSampling",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "implements": "ssn:implements",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeByActuator": "sosa:madeByActuator",
    "madeBySampler": "sosa:madeBySampler",
    "hasProperty": "ssn:hasProperty",
    "detects": "ssn:detects",
    "hasResult": "sosa:hasResult",
    "Observation": "sosa:Observation"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/properties/observationCollection`

