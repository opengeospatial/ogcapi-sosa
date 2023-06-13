---
title: SOSA Observation Feature (Schema)

language_tabs:
  - json: JSON
  - ttl: RDF/Turtle

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

```ttl
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
  hosts: http://www.w3.org/ns/sosa/hosts
  Observation: http://www.w3.org/ns/sosa/Observation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  observes: http://www.w3.org/ns/sosa/observes
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasResult: http://www.w3.org/ns/sosa/hasResult
  implements: http://www.w3.org/ns/ssn/implements
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  detects: http://www.w3.org/ns/ssn/detects
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  resultTime: http://www.w3.org/ns/sosa/resultTime
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasInput: http://www.w3.org/ns/ssn/hasInput

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
    "Feature": "geojson:Feature",
    "MultiPoint": "geojson:MultiPoint",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPolygon": "geojson:MultiPolygon",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "Polygon": "geojson:Polygon",
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
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
    "hosts": "sosa:hosts",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "madeObservation": "sosa:madeObservation",
    "hasOutput": "ssn:hasOutput",
    "isSampleOf": "sosa:isSampleOf",
    "madeByActuator": "sosa:madeByActuator",
    "hasSubSystem": "ssn:hasSubSystem",
    "observes": "sosa:observes",
    "madeSampling": "sosa:madeSampling",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "inCondition": "ssn-system:inCondition",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeBySampler": "sosa:madeBySampler",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "implements": "ssn:implements",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "detects": "ssn:detects",
    "isObservedBy": "sosa:isObservedBy",
    "hasProperty": "ssn:hasProperty",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "deployedSystem": "ssn:deployedSystem",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSample": "sosa:hasSample",
    "isResultOf": "sosa:isResultOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "actsOnProperty": "sosa:actsOnProperty",
    "Sample": "sosa:Sample",
    "inDeployment": "ssn:inDeployment",
    "forProperty": "ssn:forProperty",
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "ssn:isProxyFor",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasInput": "ssn:hasInput"
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

