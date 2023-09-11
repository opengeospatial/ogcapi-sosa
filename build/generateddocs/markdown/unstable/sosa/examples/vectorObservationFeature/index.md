
# Example SOSA Vector Observation Feature (Schema)

`ogc.unstable.sosa.examples.vectorObservationFeature` *v1.0*

This building block defines an example SOSA Observation Feature for a Vector Observation

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### VectorObservation - specialisation example.
#### json
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

#### jsonld
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

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/features/vector-obs-1> a geojson:Feature ;
    sosa:hasFeatureOfInterest <eg:Traverse-P1-P2> ;
    sosa:hasResult [ ] ;
    sosa:resultTime "2023-05-22T16:41:00+2" ;
    geojson:geometry [ a geojson:LineString ;
            geojson:coordinates ( ( -1.116718e+02 4.005671e+01 ) ( -1.116718e+02 4.005671e+01 ) ) ] .


```


### VectorObservationCollection
#### json
```json
{
    "@context": {
    "resultschema": "http//example.org/resultschema/",
    "pose": "resultschema:pose",
    "distance": {
      "@id": "resultschema:distance"
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
  ]
}
```

#### jsonld
```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld",
    {
      "resultschema": "http//example.org/resultschema/",
      "pose": "resultschema:pose",
      "distance": {
        "@id": "resultschema:distance"
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

#### ttl
```ttl
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix resultschema: <http//example.org/resultschema/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/features/c1> a sosa:ObservationCollection,
        geojson:FeatureCollection ;
    sosa:hasMember <http://example.com/features/vector-obs-1> ;
    sosa:resultTime "1999" .

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
            geojson:coordinates ( ( -1.116718e+02 4.005671e+01 ) ( -1.116718e+02 4.005671e+01 ) ) ] .


```

## Schema

```yaml
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

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": {
      "@id": "@nest",
      "@context": {
        "features": "sosa:hasMember",
        "properties": "@nest"
      }
    },
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
      "@id": "sosa:hasMember",
      "@context": {
        "properties": {
          "@id": "@nest",
          "@context": {
            "features": "sosa:hasMember",
            "properties": "@nest"
          }
        },
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        },
        "Observation": "sosa:Observation",
        "Sample": "sosa:Sample",
        "observedProperty": "sosa:observedProperty",
        "phenomenonTime": "sosa:phenomenonTime",
        "hasResult": "sosa:hasResult",
        "isResultOf": "sosa:isResultOf",
        "hasSimpleResult": "sosa:hasSimpleResult",
        "resultTime": "sosa:resultTime",
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
        "featureType": "@type"
      }
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observedProperty": "sosa:observedProperty",
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
    "hasMember": "sosa:hasMember",
    "featureType": "@type",
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
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/examples/vectorObservationFeature`

