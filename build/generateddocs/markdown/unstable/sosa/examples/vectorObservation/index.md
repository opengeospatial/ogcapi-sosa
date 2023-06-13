
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
x-jsonld-extra-terms: {}

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
    "hasInput": "ssn:hasInput",
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
    "latitude": "geo:lat",
    "rotations": "geopose:rotations",
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

