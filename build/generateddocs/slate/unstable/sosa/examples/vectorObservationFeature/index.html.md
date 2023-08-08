---
title: Example SOSA Vector Observation Feature (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - ttl: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>Example SOSA Vector Observation Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Example SOSA Vector Observation Feature (Schema)
---


# Example SOSA Vector Observation Feature `ogc.unstable.sosa.examples.vectorObservationFeature`

This building block defines an example SOSA Observation Feature for a Vector Observation

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/examples/vectorObservationFeature/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example 1

```json
{
  "@id": "vector-obs-1",
  "type":"Feature",
  "geometry":{
    "type":"LineString",
    "coordinates":[
      [
        -111.67183507997295,
        40.056709946862874
      ],
      [
        -111.67183507997295,
        40.056709946862874
      ]
    ]
  },
  "time":null,
  "place":null,
  "properties":{
    "hasFeatureOfInterest":"eg:Traverse-P1-P2",
    "resultTime":"2023-05-22T16:41:00+2",
    "hasResult":{
      "pose":{
        "position":{
          "lat":-111.67183507997295,
          "lon":40.056709946862874,
          "h":0.5
        },
        "angles":{
          "yaw":15.35,
          "pitch":-0.01,
          "roll":0
        }
      },
      "distance":6889234.2
    }
  }
}

```

```jsonld
{
  "@id": "vector-obs-1",
  "type": "Feature",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [
        -111.67183507997295,
        40.056709946862874
      ],
      [
        -111.67183507997295,
        40.056709946862874
      ]
    ]
  },
  "time": null,
  "place": null,
  "properties": {
    "hasFeatureOfInterest": "eg:Traverse-P1-P2",
    "resultTime": "2023-05-22T16:41:00+2",
    "hasResult": {
      "pose": {
        "position": {
          "lat": -111.67183507997295,
          "lon": 40.056709946862874,
          "h": 0.5
        },
        "angles": {
          "yaw": 15.35,
          "pitch": -0.01,
          "roll": 0
        }
      },
      "distance": 6889234.2
    }
  },
  "@context": "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld"
}
```

```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://example.com/properties/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/features/vector-obs-1> a geojson:Feature ;
    geojson:geometry [ a geojson:LineString ;
            geojson:coordinates ( ( -1.116718e+02 4.005671e+01 ) ( -1.116718e+02 4.005671e+01 ) ) ] ;
    geojson:properties [ sosa:hasFeatureOfInterest <eg:Traverse-P1-P2> ;
            sosa:hasResult [ ns1:distance "6889234.2"^^xsd:float ] ;
            sosa:resultTime "2023-05-22T16:41:00+2" ] .


```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Vector Observation
allOf:
- $ref: ../../features/observation/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../vectorObservation/schema.yaml

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.json" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {}
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
    "features": {
      "@container": "@set",
      "@id": "sosa:hasMember"
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
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
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
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
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isResultOf": "sosa:isResultOf",
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id"
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "ssn:isProxyFor",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "detects": "ssn:detects",
    "hasProperty": "ssn:hasProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "forProperty": "ssn:forProperty",
    "implements": "ssn:implements",
    "implementedBy": "ssn:implementedBy",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "hasSubSystem": "ssn:hasSubSystem",
    "deployedSystem": "ssn:deployedSystem",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn:systems/inCondition",
    "hasSystemCapability": "ssn:systems/hasSystemCapability",
    "hasSystemProperty": "ssn:systems/hasSystemProperty",
    "hasOperatingRange": "ssn:systems/hasOperatingRange",
    "hasOperatingProperty": "ssn:systems/hasOperatingProperty",
    "hasSurvivalRange": "ssn:systems/hasSurvivalRange",
    "hasSurvivalProperty": "ssn:systems/hasSurvivalProperty",
    "qualityOfObservation": "ssn:systems/qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "position": {
      "@id": "geopose:position",
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      }
    },
    "angles": {
      "@id": "geopose:angles",
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      }
    },
    "distance": {
      "@id": "http://example.com/properties/distance",
      "@type": "http://www.w3.org/2001/XMLSchema#float"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/examples/vectorObservationFeature`

