# Example SOSA Vector Observation Feature (Schema)

*Version 1.0*

This building block defines an example SOSA Observation Feature for a Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Examples

### Example 1
#### json
```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [43.457475012484124, -3.7684047847661435]
  },
  "properties": {
    "hasFeatureOfInterest": "http://example.com/features/33",
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
}
```

## Schema

[schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/examples/vectorObservationFeature/schema.yaml)

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
## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
