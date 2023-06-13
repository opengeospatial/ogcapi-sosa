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
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  Observation: http://www.w3.org/ns/sosa/Observation
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  implements: http://www.w3.org/ns/ssn/implements
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  resultTime: http://www.w3.org/ns/sosa/resultTime
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  observes: http://www.w3.org/ns/sosa/observes
  detects: http://www.w3.org/ns/ssn/detects
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  Sample: http://www.w3.org/ns/sosa/Sample
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hosts: http://www.w3.org/ns/sosa/hosts
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasResult: http://www.w3.org/ns/sosa/hasResult

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
    "hasSample": "sosa:hasSample",
    "isPropertyOf": "ssn:isPropertyOf",
    "isSampleOf": "sosa:isSampleOf",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Observation": "sosa:Observation",
    "isProxyFor": "ssn:isProxyFor",
    "implements": "ssn:implements",
    "deployedSystem": "ssn:deployedSystem",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "forProperty": "ssn:forProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isResultOf": "sosa:isResultOf",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "madeByActuator": "sosa:madeByActuator",
    "isObservedBy": "sosa:isObservedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasDeployment": "ssn:hasDeployment",
    "hasMember": "sosa:hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeBySampler": "sosa:madeBySampler",
    "isHostedBy": "sosa:isHostedBy",
    "madeSampling": "sosa:madeSampling",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "observes": "sosa:observes",
    "detects": "ssn:detects",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "actsOnProperty": "sosa:actsOnProperty",
    "hosts": "sosa:hosts",
    "deployedOnPlatform": "ssn:deployedOnPlatform"
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

