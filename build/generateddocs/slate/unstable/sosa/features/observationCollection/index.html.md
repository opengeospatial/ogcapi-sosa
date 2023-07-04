---
title: SOSA ObservationCollection Feature (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA ObservationCollection Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA ObservationCollection Feature (Schema)
---


# SOSA ObservationCollection Feature `ogc.unstable.sosa.features.observationCollection`

This building blocks defines an ObservationCollection Feature according to the SOSA/SSN v1.1 specification.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/features/observationCollection/" target="_blank">failed</a></strong>
</aside>

# Examples

## Example of SOSA ObservationCollection

```json
{
  "@id": "c1",
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "observedProperty": "https://dbpedia.org/ontology/population",
    "resultTime": "1999"
  },
  "features": [
    {
      "@id": "pop1999",
      "type": "Feature",
      "geometry": null,
      "properties": null,
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
      "hasSimpleResult": 15555.0
    },
    {
      "@id": "pop1999",
      "type": "Feature",
      "geometry": null,
      "properties": null,
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 3275.0
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
  sosa:hasMember eg:pop1999, eg:pop2000 ;
  sosa:observedProperty <http://dbpedia.org/ontology/population> ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.

eg:pop1999 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 3275.0 ;
  sosa:resultTime "1999-01-01"^^xsd:date
.

 eg:pop2000 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 4372.0 ;
  sosa:resultTime "2000"^^xsd:gYear
.

<http://dbpedia.org/ontology/population> a skos:Concept;
  skos:prefLabel "Population";
.
```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observationCollection/schema.yaml
    features:
      type: array
      items:
        oneOf:
        - $ref: ../observation/schema.yaml
        - type: string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  observes: http://www.w3.org/ns/sosa/observes
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  Sample: http://www.w3.org/ns/sosa/Sample
  hasInput: http://www.w3.org/ns/ssn/hasInput
  resultTime: http://www.w3.org/ns/sosa/resultTime
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  detects: http://www.w3.org/ns/ssn/detects
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hosts: http://www.w3.org/ns/sosa/hosts
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  forProperty: http://www.w3.org/ns/ssn/forProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  implements: http://www.w3.org/ns/ssn/implements
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
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

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "features": "http://www.w3.org/ns/sosa/hasMember",
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observationCollection`

