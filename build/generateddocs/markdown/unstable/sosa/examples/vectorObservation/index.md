
# Example SOSA Vector Observation (Schema)

`ogc.unstable.sosa.examples.vectorObservation` *v1.0*

This building block defines an example SOSA Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example 1
#### json
```json
{
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "resultTime": "2023-05-22T16:41:00+2",
  "hasResult": {
    "pose": {
      "position": {
        "lat": 43.46498208387333,
        "lon": -3.803638278687769,
        "h": 0.5
      },
      "angles": {
        "yaw": 5.553,
        "pitch": -0.92,
        "roll": 0.33
      }
    }
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Vector Observation
allOf:
- $ref: ../../properties/observation/schema.yaml
- type: object
  properties:
    hasResult:
      properties:
        pose:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-ypr/schema.yaml
        distance:
          type: number
          x-jsonld-id: http://example.com/properties/distance
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
  required:
  - hasResult
  not:
    required:
    - hasSimpleResult

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
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
      "@context": {
        "distance": {
          "@id": "http://example.com/properties/distance",
          "@type": "http://www.w3.org/2001/XMLSchema#float"
        }
      }
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "forProperty": "ssn:forProperty",
    "madeObservation": "sosa:madeObservation",
    "isPropertyOf": "ssn:isPropertyOf",
    "inDeployment": "ssn:inDeployment",
    "hasSubSystem": "ssn:hasSubSystem",
    "hosts": "sosa:hosts",
    "inCondition": "ssn-system:inCondition",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOutput": "ssn:hasOutput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isActedOnBy": "sosa:isActedOnBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "isResultOf": "sosa:isResultOf",
    "isProxyFor": "ssn:isProxyFor",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isObservedBy": "sosa:isObservedBy",
    "hasSample": "sosa:hasSample",
    "isSampleOf": "sosa:isSampleOf",
    "hasInput": "ssn:hasInput",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeSampling": "sosa:madeSampling",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "implements": "ssn:implements",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeByActuator": "sosa:madeByActuator",
    "madeBySampler": "sosa:madeBySampler",
    "hasProperty": "ssn:hasProperty",
    "detects": "ssn:detects",
    "Observation": "sosa:Observation",
    "hasMember": "sosa:hasMember",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "geopose:position",
    "angles": "geopose:angles",
    "yaw": "geopose:yaw",
    "pitch": "geopose:pitch",
    "roll": "geopose:roll",
    "lat": "geopose:lat",
    "lon": "geopose:lon",
    "h": "geopose:h",
    "rotations": "geopose:rotations",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "longitude": "geo:long"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/examples/vectorObservation`

