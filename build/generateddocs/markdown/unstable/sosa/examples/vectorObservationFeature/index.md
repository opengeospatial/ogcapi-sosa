
# Example SOSA Vector Observation Feature (Schema)

`ogc.unstable.sosa.examples.vectorObservationFeature` *v1.0*

This building block defines an example SOSA Observation Feature for a Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example 1
#### json
```json
{
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
x-jsonld-extra-terms: {}

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
    "hasResult": {
      "@id": "sosa:hasResult",
      "@context": {
        "distance": {
          "@id": "http://example.com/properties/distance",
          "@type": "http://www.w3.org/2001/XMLSchema#float"
        }
      }
    },
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
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "geopose:position",
    "angles": "geopose:angles",
    "yaw": "geopose:yaw",
    "pitch": "geopose:pitch",
    "roll": "geopose:roll",
    "lat": "geopose:lat",
    "lon": "geopose:lon",
    "h": "geopose:h"
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

