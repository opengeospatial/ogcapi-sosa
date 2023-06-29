---
title: SOSA Observation Feature (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA Observation Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA Observation Feature (Schema)
---


# SOSA Observation Feature `ogc.unstable.sosa.features.observation`

This building blocks defines a GeoJSON feature containing a SOSA Observation

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/features/observation/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example of SOSA observation

```json
{ 
  "@id": "_:a1",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": {
    "type": "Point",
    "coordinates": [43.457475012484124, -3.7684047847661435]
  },
  "properties": {
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
    "hasSimpleResult": 33,
    "resultTime": "2022-05-01T22:33:44Z"
    }
}
```

```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
_:a1 a geojson:Feature;
  geojson:properties [
    sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 33 ;
    sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime
  ]
.
```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
type: object
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observation/schema.yaml
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSample: http://www.w3.org/ns/sosa/hasSample
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasResult: http://www.w3.org/ns/sosa/hasResult
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hosts: http://www.w3.org/ns/sosa/hosts
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  implements: http://www.w3.org/ns/ssn/implements
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasInput: http://www.w3.org/ns/ssn/hasInput
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  observes: http://www.w3.org/ns/sosa/observes
  detects: http://www.w3.org/ns/ssn/detects
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput

```

Links to the schema:

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
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
    "links": "rdfs:seeAlso",
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
    "hasProperty": "ssn:hasProperty",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSample": "sosa:hasSample",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "deployedSystem": "ssn:deployedSystem",
    "inCondition": "ssn-system:inCondition",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "madeObservation": "sosa:madeObservation",
    "madeSampling": "sosa:madeSampling",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeBySampler": "sosa:madeBySampler",
    "hosts": "sosa:hosts",
    "implementedBy": "ssn:implementedBy",
    "isSampleOf": "sosa:isSampleOf",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "madeActuation": "sosa:madeActuation",
    "madeByActuator": "sosa:madeByActuator",
    "implements": "ssn:implements",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "observes": "sosa:observes",
    "detects": "ssn:detects",
    "actsOnProperty": "sosa:actsOnProperty",
    "isProxyFor": "ssn:isProxyFor",
    "hasSubSystem": "ssn:hasSubSystem",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isObservedBy": "sosa:isObservedBy",
    "hasMember": "sosa:hasMember",
    "isResultOf": "sosa:isResultOf",
    "hasDeployment": "ssn:hasDeployment",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observation`

