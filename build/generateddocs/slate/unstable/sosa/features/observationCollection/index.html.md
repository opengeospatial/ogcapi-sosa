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
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "hasMember": [
      "_:a1"
    ],
    "observedProperty": "_:p1",
    "resultTime": "2022-05-01T22:33:44Z"
  },
}
```

```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "observedProperty": "http://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "features": [
      { 
        "@id": "pop1999",
        "comment": "Example of an inline membership - would entail hasMember relations",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
        "hasSimpleResult": 15555.0
      },
       { 
        "@id": "pop1999",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
        "hasSimpleResult": 3275.0
      }
    ]
  },
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
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  observes: http://www.w3.org/ns/sosa/observes
  hasMember: http://www.w3.org/ns/sosa/hasMember
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
    "links": "rdfs:seeAlso",
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": "geojson:coordinates"
      },
      "@id": "geojson:geometry"
    },
    "bbox": "geojson:bbox",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "features": "geojson:features",
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observationCollection`

