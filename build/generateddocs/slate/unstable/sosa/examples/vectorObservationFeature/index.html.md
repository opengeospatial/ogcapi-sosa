---
title: Example SOSA Vector Observation Feature (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

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

This building block defines an example SOSA Observation Feature using another schema to define a result set - in this case the GeoPose model

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/examples/vectorObservationFeature/" target="_blank">valid</a></strong>
</aside>

# Examples

## VectorObservation - specialisation example.



```json
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
        -111.71,
        40.156709946862874
      ]
    ]
  },
  "time": null,
  "place": null,
  "properties": {
    "hasFeatureOfInterest": "eg:Traverse-P1-P2",
    "observedProperty": "Geopose (or a URI for this concept)",
    "resultTime": "2023-05-22T16:41:00+2",
    "hasResult": {
      "@context": {
        "resultschema": "http://example.org/resultschema/",
        "pose": "resultschema:pose",
        "distance": {
          "@id": "resultschema:distance"
        }
      },
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
  }
}

```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/examples/vectorObservationFeature/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




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
        -111.71,
        40.156709946862875
      ]
    ]
  },
  "time": null,
  "place": null,
  "properties": {
    "hasFeatureOfInterest": "eg:Traverse-P1-P2",
    "observedProperty": "Geopose (or a URI for this concept)",
    "resultTime": "2023-05-22T16:41:00+2",
    "hasResult": {
      "@context": {
        "resultschema": "http://example.org/resultschema/",
        "pose": "resultschema:pose",
        "distance": {
          "@id": "resultschema:distance"
        }
      },
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

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/examples/vectorObservationFeature/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix ns1: <http://example.org/resultschema/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/features/vector-obs-1> a geojson:Feature ;
    sosa:hasFeatureOfInterest <eg:Traverse-P1-P2> ;
    sosa:hasResult [ ns1:distance 6.889234e+06 ;
            ns1:pose [ geopose:angles [ geopose:pitch -1e-02 ;
                            geopose:roll 0 ;
                            geopose:yaw 1.535e+01 ] ;
                    geopose:position [ geopose:h 5e-01 ;
                            geo1:lat -1.116718e+02 ;
                            geo1:long 4.005671e+01 ] ] ] ;
    sosa:observedProperty <http://example.com/features/> ;
    sosa:resultTime "2023-05-22T16:41:00+2" ;
    geojson:geometry [ a geojson:LineString ;
            geojson:coordinates ( "[-111.67183507997295, 40.056709946862874]" "[-111.71, 40.156709946862875]" ) ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/examples/vectorObservationFeature/example_1_1.ttl">Open in new window</a>
</blockquote>



## VectorObservationCollection



```json
{
  "@context": {
    "resultschema": "http://example.org/resultschema/",
    "pose": "resultschema:pose",
    "distance": {
      "@id": "resultschema:distance"
    }
  },
  "@id": "c1",
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "observedProperty": "Geopose (or a URI for this concept)",
  "properties": {
    "resultTime": "1999"
  },
  "features": [
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
      }
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/examples/vectorObservationFeature/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld",
    {
      "resultschema": "http://example.org/resultschema/",
      "pose": "resultschema:pose",
      "distance": {
        "@id": "resultschema:distance"
      }
    }
  ],
  "@id": "c1",
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "observedProperty": "Geopose (or a URI for this concept)",
  "properties": {
    "resultTime": "1999"
  },
  "features": [
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
      }
    }
  ]
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/examples/vectorObservationFeature/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix resultschema: <http://example.org/resultschema/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/features/c1> a sosa:ObservationCollection,
        geojson:FeatureCollection ;
    sosa:observedProperty <http://example.com/features/> ;
    sosa:resultTime "1999" ;
    geojson:features <http://example.com/features/vector-obs-1> .

<http://example.com/features/vector-obs-1> a geojson:Feature ;
    sosa:hasFeatureOfInterest <eg:Traverse-P1-P2> ;
    sosa:hasResult [ resultschema:distance 6.889234e+06 ;
            resultschema:pose [ geopose:angles [ geopose:pitch -1e-02 ;
                            geopose:roll 0 ;
                            geopose:yaw 1.535e+01 ] ;
                    geopose:position [ geopose:h 5e-01 ;
                            geo1:lat -1.116718e+02 ;
                            geo1:long 4.005671e+01 ] ] ] ;
    sosa:resultTime "2023-05-22T16:41:00+2" ;
    geojson:geometry [ a geojson:LineString ;
            geojson:coordinates ( "[-111.67183507997295, 40.056709946862874]" "[-111.67183507997295, 40.056709946862874]" ) ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/examples/vectorObservationFeature/example_2_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Observation Specialisation - a vector bearing and distance
$defs:
  VectorObservation:
    allOf:
    - $ref: ../../features/observation/schema.yaml
    - type: object
      properties:
        properties:
          $ref: ../vectorObservation/schema.yaml
  VectorObservationCollection:
    allOf:
    - $ref: ../../features/observationCollection/schema.yaml
    - type: object
      properties:
        features:
          type: array
          items:
            $ref: '#/$defs/VectorObservation'
anyOf:
- $ref: '#/$defs/VectorObservation'
- $ref: '#/$defs/VectorObservationCollection'

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.json" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "phenomenonTime": "sosa:phenomenonTime",
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
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
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
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "isResultOf": "sosa:isResultOf",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "resultTime": "sosa:resultTime",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
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
    "hasMember": {
      "@context": {
        "features": "sosa:hasMember"
      },
      "@id": "sosa:hasMember"
    },
    "features": {
      "@context": {
        "features": "sosa:hasMember"
      },
      "@id": "geojson:features",
      "@container": "@set"
    },
    "featureType": "@type",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "properties": "@nest",
    "type": "@type",
    "id": "@id",
    "links": {
      "@context": {
        "href": "oa:hasTarget",
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
    "geometry": "geojson:geometry",
    "position": {
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      },
      "@id": "geopose:position"
    },
    "angles": {
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      },
      "@id": "geopose:angles"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld</a>

# Validation

## SHACL Shapes

The following sets of SHACL shapes are used for validating this building block:

* Example SOSA Vector Observation Feature <small><code>ogc.unstable.sosa.examples.vectorObservationFeature</code></small>
  * [https://opengeospatial.github.io/ogcapi-sosa/_sources/examples/vectorObservationFeature/rules.shacl](https://opengeospatial.github.io/ogcapi-sosa/_sources/examples/vectorObservationFeature/rules.shacl)
* SOSA Observation <small><code>ogc.unstable.sosa.properties.observation</code></small>
  * [https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl](https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl)

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/examples/vectorObservationFeature" target="_blank">_sources/examples/vectorObservationFeature</a></code>

