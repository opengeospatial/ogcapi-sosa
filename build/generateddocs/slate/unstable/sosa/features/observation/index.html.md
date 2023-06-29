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
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "forProperty": "ssn:forProperty",
    "Observation": "sosa:Observation",
    "actsOnProperty": "sosa:actsOnProperty",
    "isHostedBy": "sosa:isHostedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "madeSampling": "sosa:madeSampling",
    "hasSample": "sosa:hasSample",
    "isResultOf": "sosa:isResultOf",
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
    "hasMember": "sosa:hasMember",
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observation`

