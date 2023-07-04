
# Example SOSA Vector Observation Feature (Schema)

`ogc.unstable.sosa.examples.vectorObservationFeature` *v1.0*

This building block defines an example SOSA Observation Feature for a Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example 1
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

## Schema

```yaml
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

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "https://purl.org/geojson/vocab#properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": {
          "@id": "https://purl.org/geojson/vocab#coordinates",
          "@container": "@list"
        }
      },
      "@id": "https://purl.org/geojson/vocab#geometry"
    },
    "bbox": {
      "@id": "https://purl.org/geojson/vocab#bbox",
      "@container": "@list"
    },
    "MultiPoint": "geojson:MultiPoint",
    "GeometryCollection": "geojson:GeometryCollection",
    "Feature": "geojson:Feature",
    "Polygon": "geojson:Polygon",
    "features": "sosa:hasMember",
    "MultiPolygon": "geojson:MultiPolygon",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiLineString": "geojson:MultiLineString",
    "Point": "geojson:Point",
    "LineString": "geojson:LineString",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
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
    "hasResult": {
      "@id": "http://www.w3.org/ns/sosa/hasResult",
      "@context": {
        "distance": {
          "@id": "http://example.com/properties/distance",
          "@type": "http://www.w3.org/2001/XMLSchema#float"
        }
      }
    },
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "observes": "sosa:observes",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "isProxyFor": "ssn:isProxyFor",
    "madeObservation": "sosa:madeObservation",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasMember": "sosa:hasMember",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasDeployment": "ssn:hasDeployment",
    "hasProperty": "ssn:hasProperty",
    "Sample": "sosa:Sample",
    "isSampleOf": "sosa:isSampleOf",
    "madeSampling": "sosa:madeSampling",
    "forProperty": "ssn:forProperty",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "detects": "ssn:detects",
    "hasInput": "ssn:hasInput",
    "madeBySampler": "sosa:madeBySampler",
    "hasOutput": "ssn:hasOutput",
    "implements": "ssn:implements",
    "deployedSystem": "ssn:deployedSystem",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "madeActuation": "sosa:madeActuation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isResultOf": "sosa:isResultOf",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "isObservedBy": "sosa:isObservedBy",
    "hasSample": "sosa:hasSample",
    "hosts": "sosa:hosts",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "http://example.com/geopose/position",
    "angles": "http://example.com/geopose/angles",
    "yaw": "http://example.com/geopose/yaw",
    "pitch": "http://example.com/geopose/pitch",
    "roll": "http://example.com/geopose/roll",
    "lat": "http://example.com/geopose/lat",
    "lon": "http://example.com/geopose/lon",
    "h": "http://example.com/geopose/h",
    "rotations": "geopose:rotations",
    "longitude": "geo:long",
    "latitude": "geo:lat",
    "height": "geopose:height"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservationFeature/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/examples/vectorObservationFeature`

