---
title: SOSA ObservationCollection Feature (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle
  - jsonld: JSON-LD

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

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/features/observationCollection/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example of SOSA ObservationCollection



```json
{
  "@context": {
    "resultschema": "http//example.org/resultchema/",
    "a": "resultschema:a",
    "b": {
      "@id": "resultschema:b",
      "@context": {
        "b1": "resultschema:b1",
        "b2": "resultschema:b2"
      }
    }
  },
  "@id": "c1",
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "resultTime": "1999"
  },
  "features": [
    {
      "@id": "pop1999",
      "type": "Feature",
      "geometry": null,
      "properties": {
        "comment": "Simple result case",
        "observedProperty": "https://dbpedia.org/ontology/population",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
        "hasSimpleResult": 15555.0
      }
    },
    {
      "@id": "something",
      "type": "Feature",
      "geometry": null,
      "properties": {
        "observedProperty": "https://example.org/someproperty",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
        "hasResult": {
          "a": 1,
          "b": {
            "b1": "rb1",
            "b2": "rb2"
          }
        }
      }
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/features/observationCollection/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Ffeatures%2FobservationCollection%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:pop1999, eg:pop2000 ;
  sosa:observedProperty <http://dbpedia.org/ontology/population> ;
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

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/features/observationCollection/example_1_2.ttl">Open in new window</a>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/context.jsonld",
    {
      "resultschema": "http//example.org/resultchema/",
      "a": "resultschema:a",
      "b": {
        "@id": "resultschema:b",
        "@context": {
          "b1": "resultschema:b1",
          "b2": "resultschema:b2"
        }
      }
    }
  ],
  "@id": "c1",
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "resultTime": "1999"
  },
  "features": [
    {
      "@id": "pop1999",
      "type": "Feature",
      "geometry": null,
      "properties": {
        "comment": "Simple result case",
        "observedProperty": "https://dbpedia.org/ontology/population",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
        "hasSimpleResult": 15555.0
      }
    },
    {
      "@id": "something",
      "type": "Feature",
      "geometry": null,
      "properties": {
        "observedProperty": "https://example.org/someproperty",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
        "hasResult": {
          "a": 1,
          "b": {
            "b1": "rb1",
            "b2": "rb2"
          }
        }
      }
    }
  ]
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/features/observationCollection/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Ffeatures%2FobservationCollection%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

eg:c1 a sosa:ObservationCollection ;
    sosa:hasMember eg:pop1999,
        eg:pop2000 ;
    sosa:observedProperty <http://dbpedia.org/ontology/population> .

<http://dbpedia.org/ontology/population> a skos:Concept ;
    skos:prefLabel "Population" .

eg:pop1999 a sosa:Observation ;
    sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 3275.0 ;
    sosa:resultTime "1999-01-01"^^xsd:date .

eg:pop2000 a sosa:Observation ;
    sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 4372.0 ;
    sosa:resultTime "2000"^^xsd:gYear .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/features/observationCollection/example_1_2.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection-lenient/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observationCollection/schema.yaml
      x-jsonld-id: '@nest'
    features:
      type: array
      items:
        oneOf:
        - $ref: ../observation/schema.yaml
        - type: string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
      x-jsonld-type: '@id'
x-jsonld-extra-terms:
  id: '@id'
  ActuatableProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/ActuatableProperty
    x-jsonld-type: '@id'
  Actuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/Actuation
    x-jsonld-type: '@id'
  Actuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/Actuator
    x-jsonld-type: '@id'
  Deployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/Deployment
    x-jsonld-type: '@id'
  FeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/FeatureOfInterest
    x-jsonld-type: '@id'
  Input:
    x-jsonld-id: http://www.w3.org/ns/sosa/Input
    x-jsonld-type: '@id'
  ObservableProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/ObservableProperty
    x-jsonld-type: '@id'
  Observation:
    x-jsonld-id: http://www.w3.org/ns/sosa/Observation
    x-jsonld-type: '@id'
  Output:
    x-jsonld-id: http://www.w3.org/ns/sosa/Output
    x-jsonld-type: '@id'
  Platform:
    x-jsonld-id: http://www.w3.org/ns/sosa/Platform
    x-jsonld-type: '@id'
  Property:
    x-jsonld-id: http://www.w3.org/ns/sosa/Property
    x-jsonld-type: '@id'
  'Procedure ':
    x-jsonld-id: http://www.w3.org/ns/sosa/Procedure
    x-jsonld-type: '@id'
  Result:
    x-jsonld-id: http://www.w3.org/ns/sosa/Result
    x-jsonld-type: '@id'
  Sample:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sample
    x-jsonld-type: '@id'
  Sampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sampler
    x-jsonld-type: '@id'
  Sampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sampling
    x-jsonld-type: '@id'
  Sensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sensor
    x-jsonld-type: '@id'
  Stimulus:
    x-jsonld-id: http://www.w3.org/ns/sosa/Stimulus
    x-jsonld-type: '@id'
  System:
    x-jsonld-id: http://www.w3.org/ns/sosa/System
    x-jsonld-type: '@id'
  actsOnProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
    x-jsonld-type: '@id'
  deployedOnPlatform:
    x-jsonld-id: http://www.w3.org/ns/sosa/deployedOnPlatform
    x-jsonld-type: '@id'
  deployedSystem:
    x-jsonld-id: http://www.w3.org/ns/sosa/deployedSystem
    x-jsonld-type: '@id'
  detects:
    x-jsonld-id: http://www.w3.org/ns/sosa/detects
    x-jsonld-type: '@id'
  forProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/forProperty
    x-jsonld-type: '@id'
  hasDeployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasDeployment
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasInput
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasOutput
    x-jsonld-type: '@id'
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasProperty
    x-jsonld-type: '@id'
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
    x-jsonld-type: '@id'
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  hasUltimateFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
    x-jsonld-type: '@id'
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  implementedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/implementedBy
    x-jsonld-type: '@id'
  implements:
    x-jsonld-id: http://www.w3.org/ns/sosa/implements
    x-jsonld-type: '@id'
  inDeployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/inDeployment
    x-jsonld-type: '@id'
  isActedOnBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  isHostedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isHostedBy
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  isPropertyOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isPropertyOf
    x-jsonld-type: '@id'
  isProxyFor:
    x-jsonld-id: http://www.w3.org/ns/sosa/isProxyFor
    x-jsonld-type: '@id'
  isResultOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOf
    x-jsonld-type: '@id'
  isSampleOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
    x-jsonld-type: '@id'
  madeActuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
    x-jsonld-type: '@id'
  madeByActuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
    x-jsonld-type: '@id'
  madeBySampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
    x-jsonld-type: '@id'
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  madeSampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
    x-jsonld-type: '@id'
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  phenomenonTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    x-jsonld-type: '@id'
  resultTime: http://www.w3.org/ns/sosa/resultTime
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  wasOriginatedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/wasOriginatedBy
    x-jsonld-type: '@id'
  inCondition:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/inCondition
    x-jsonld-type: '@id'
  Condition:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Condition
    x-jsonld-type: '@id'
  hasSystemCapability:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    x-jsonld-type: '@id'
  SystemCapability:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemCapability
    x-jsonld-type: '@id'
  hasSystemProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    x-jsonld-type: '@id'
  SystemProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemProperty
    x-jsonld-type: '@id'
  MeasurementRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/MeasurementRange
    x-jsonld-type: '@id'
  ActuationRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/ActuationRange
    x-jsonld-type: '@id'
  Accuracy:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Accuracy
    x-jsonld-type: '@id'
  DetectionLimit:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/DetectionLimit
    x-jsonld-type: '@id'
  Drift:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Drift
    x-jsonld-type: '@id'
  Frequency:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Frequency
    x-jsonld-type: '@id'
  Latency:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Latency
    x-jsonld-type: '@id'
  Precision:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Precision
    x-jsonld-type: '@id'
  Resolution:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Resolution
    x-jsonld-type: '@id'
  ResponseTime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/ResponseTime
    x-jsonld-type: '@id'
  Selectivity:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Selectivity
    x-jsonld-type: '@id'
  Sensitivity:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Sensitivity
    x-jsonld-type: '@id'
  hasOperatingRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    x-jsonld-type: '@id'
  OperatingRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingRange
    x-jsonld-type: '@id'
  hasOperatingProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    x-jsonld-type: '@id'
  OperatingProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingProperty
    x-jsonld-type: '@id'
  MaintenanceSchedule:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/MaintenanceSchedule
    x-jsonld-type: '@id'
  OperatingPowerRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingPowerRange
    x-jsonld-type: '@id'
  hasSurvivalRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    x-jsonld-type: '@id'
  SurvivalRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SurvivalRange
    x-jsonld-type: '@id'
  hasSurvivalProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    x-jsonld-type: '@id'
  SurvivalProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SurvivalProperty
    x-jsonld-type: '@id'
  SystemLifetime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemLifetime
    x-jsonld-type: '@id'
  BatteryLifetime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/BatteryLifetime
    x-jsonld-type: '@id'
  qualityOfObservation:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    x-jsonld-type: '@id'
  featureType: '@type'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn-system: http://www.w3.org/ns/ssn/systems/
  ssn: http://www.w3.org/ns/ssn/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Ffeatures%2FobservationCollection%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/schema.json" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "featureType": "geojson:collectionFeatureType",
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "features": {
      "@context": {
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        },
        "featureType": "@type"
      },
      "@container": "@set",
      "@id": "sosa:hasMember",
      "@type": "@id"
    },
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {},
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "resultTime": "sosa:resultTime",
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "hasMember": {
      "@context": {
        "featureType": "@type"
      },
      "@id": "sosa:hasMember",
      "@type": "@id"
    },
    "ActuatableProperty": {
      "@id": "sosa:ActuatableProperty",
      "@type": "@id"
    },
    "Actuation": {
      "@id": "sosa:Actuation",
      "@type": "@id"
    },
    "Actuator": {
      "@id": "sosa:Actuator",
      "@type": "@id"
    },
    "Deployment": {
      "@id": "sosa:Deployment",
      "@type": "@id"
    },
    "FeatureOfInterest": {
      "@id": "sosa:FeatureOfInterest",
      "@type": "@id"
    },
    "Input": {
      "@id": "sosa:Input",
      "@type": "@id"
    },
    "ObservableProperty": {
      "@id": "sosa:ObservableProperty",
      "@type": "@id"
    },
    "Observation": {
      "@id": "sosa:Observation",
      "@type": "@id"
    },
    "Output": {
      "@id": "sosa:Output",
      "@type": "@id"
    },
    "Platform": {
      "@id": "sosa:Platform",
      "@type": "@id"
    },
    "Property": {
      "@id": "sosa:Property",
      "@type": "@id"
    },
    "Procedure ": {
      "@id": "sosa:Procedure",
      "@type": "@id"
    },
    "Result": {
      "@id": "sosa:Result",
      "@type": "@id"
    },
    "Sample": {
      "@id": "sosa:Sample",
      "@type": "@id"
    },
    "Sampler": {
      "@id": "sosa:Sampler",
      "@type": "@id"
    },
    "Sampling": {
      "@id": "sosa:Sampling",
      "@type": "@id"
    },
    "Sensor": {
      "@id": "sosa:Sensor",
      "@type": "@id"
    },
    "Stimulus": {
      "@id": "sosa:Stimulus",
      "@type": "@id"
    },
    "System": {
      "@id": "sosa:System",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "deployedOnPlatform": {
      "@id": "sosa:deployedOnPlatform",
      "@type": "@id"
    },
    "deployedSystem": {
      "@id": "sosa:deployedSystem",
      "@type": "@id"
    },
    "detects": {
      "@id": "sosa:detects",
      "@type": "@id"
    },
    "forProperty": {
      "@id": "sosa:forProperty",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "sosa:hasDeployment",
      "@type": "@id"
    },
    "hasInput": {
      "@id": "sosa:hasInput",
      "@type": "@id"
    },
    "hasOutput": {
      "@id": "sosa:hasOutput",
      "@type": "@id"
    },
    "hasProperty": {
      "@id": "sosa:hasProperty",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "hasUltimateFeatureOfInterest": {
      "@id": "sosa:hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id",
      "@container": "@set"
    },
    "implementedBy": {
      "@id": "sosa:implementedBy",
      "@type": "@id"
    },
    "implements": {
      "@id": "sosa:implements",
      "@type": "@id"
    },
    "inDeployment": {
      "@id": "sosa:inDeployment",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isHostedBy": {
      "@id": "sosa:isHostedBy",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "isPropertyOf": {
      "@id": "sosa:isPropertyOf",
      "@type": "@id"
    },
    "isProxyFor": {
      "@id": "sosa:isProxyFor",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "sosa:isResultOf",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "sosa:madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "sosa:madeByActuator",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "wasOriginatedBy": {
      "@id": "sosa:wasOriginatedBy",
      "@type": "@id"
    },
    "inCondition": {
      "@id": "ssn-system:inCondition",
      "@type": "@id"
    },
    "Condition": {
      "@id": "ssn-system:Condition",
      "@type": "@id"
    },
    "hasSystemCapability": {
      "@id": "ssn-system:hasSystemCapability",
      "@type": "@id"
    },
    "SystemCapability": {
      "@id": "ssn-system:SystemCapability",
      "@type": "@id"
    },
    "hasSystemProperty": {
      "@id": "ssn-system:hasSystemProperty",
      "@type": "@id"
    },
    "SystemProperty": {
      "@id": "ssn-system:SystemProperty",
      "@type": "@id"
    },
    "MeasurementRange": {
      "@id": "ssn-system:MeasurementRange",
      "@type": "@id"
    },
    "ActuationRange": {
      "@id": "ssn-system:ActuationRange",
      "@type": "@id"
    },
    "Accuracy": {
      "@id": "ssn-system:Accuracy",
      "@type": "@id"
    },
    "DetectionLimit": {
      "@id": "ssn-system:DetectionLimit",
      "@type": "@id"
    },
    "Drift": {
      "@id": "ssn-system:Drift",
      "@type": "@id"
    },
    "Frequency": {
      "@id": "ssn-system:Frequency",
      "@type": "@id"
    },
    "Latency": {
      "@id": "ssn-system:Latency",
      "@type": "@id"
    },
    "Precision": {
      "@id": "ssn-system:Precision",
      "@type": "@id"
    },
    "Resolution": {
      "@id": "ssn-system:Resolution",
      "@type": "@id"
    },
    "ResponseTime": {
      "@id": "ssn-system:ResponseTime",
      "@type": "@id"
    },
    "Selectivity": {
      "@id": "ssn-system:Selectivity",
      "@type": "@id"
    },
    "Sensitivity": {
      "@id": "ssn-system:Sensitivity",
      "@type": "@id"
    },
    "hasOperatingRange": {
      "@id": "ssn-system:hasOperatingRange",
      "@type": "@id"
    },
    "OperatingRange": {
      "@id": "ssn-system:OperatingRange",
      "@type": "@id"
    },
    "hasOperatingProperty": {
      "@id": "ssn-system:hasOperatingProperty",
      "@type": "@id"
    },
    "OperatingProperty": {
      "@id": "ssn-system:OperatingProperty",
      "@type": "@id"
    },
    "MaintenanceSchedule": {
      "@id": "ssn-system:MaintenanceSchedule",
      "@type": "@id"
    },
    "OperatingPowerRange": {
      "@id": "ssn-system:OperatingPowerRange",
      "@type": "@id"
    },
    "hasSurvivalRange": {
      "@id": "ssn-system:hasSurvivalRange",
      "@type": "@id"
    },
    "SurvivalRange": {
      "@id": "ssn-system:SurvivalRange",
      "@type": "@id"
    },
    "hasSurvivalProperty": {
      "@id": "ssn-system:hasSurvivalProperty",
      "@type": "@id"
    },
    "SurvivalProperty": {
      "@id": "ssn-system:SurvivalProperty",
      "@type": "@id"
    },
    "SystemLifetime": {
      "@id": "ssn-system:SystemLifetime",
      "@type": "@id"
    },
    "BatteryLifetime": {
      "@id": "ssn-system:BatteryLifetime",
      "@type": "@id"
    },
    "qualityOfObservation": {
      "@id": "ssn-system:qualityOfObservation",
      "@type": "@id"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Ffeatures%2FobservationCollection%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/context.jsonld</a>

# Validation

## SHACL Shapes

The following sets of SHACL shapes are used for validating this building block:

* SOSA Observation <small><code>ogc.unstable.sosa.properties.observation</code></small>
  * [https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl](https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl)

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/features/observationCollection" target="_blank">_sources/features/observationCollection</a></code>

