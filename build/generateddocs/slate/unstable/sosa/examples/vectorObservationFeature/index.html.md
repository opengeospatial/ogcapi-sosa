---
title: Example SOSA Vector Observation Feature (Schema)


toc_footers:
  - Version 1.0
  - <a href='#'>Example SOSA Vector Observation Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Example SOSA Vector Observation Feature (Schema)
---

# Overview

This building block defines an example SOSA Observation Feature for a Vector Observation

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

# Examples

## Example 1

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

# Schema

[schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/_sources/examples/vectorObservationFeature/schema.yaml)
# Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
