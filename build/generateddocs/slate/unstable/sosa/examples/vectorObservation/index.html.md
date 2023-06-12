---
title: Example SOSA Vector Observation (Schema)


toc_footers:
  - Version 1.0
  - <a href='#'>Example SOSA Vector Observation</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Example SOSA Vector Observation (Schema)
---


# Example SOSA Vector Observation `ogc.unstable.sosa.examples.vectorObservation`

This building block defines an example SOSA Vector Observation

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/examples/vectorObservation/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example 1

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


# JSON Schema

```yaml--schema
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

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/schema.json</a>


# JSON-LD Context

```json--ldContext
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/examples/vectorObservation`

