# SOSA Observation Feature (Schema)

*Version 1.0*

This building blocks defines a GeoJSON feature containing a SOSA Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Examples

### Example of SOSA observation
#### json
```json
{ 
  "@id": "_:a1",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "properties": {
    "hasFeatureOfInterest": "http://example.com/fois/1",
    "hasSimpleResult": 33,
    "resultTime": "2022-05-01T22:33:44Z"
    }
}
```

#### ttl
```ttl
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
_:a1 a geojson:Feature;
  geojson:properties [
    sosa:hasFeatureOfInterest <http://example.com/fois/1> ;
    sosa:hasSimpleResult 33 ;
    sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime
  ]
.
```

## Schema

[schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/_sources/features/observation/schema.yaml)

```yaml
"$schema": https://json-schema.org/draft/2020-12/schema
description: 'SOSA Observation Feature'
x-jsonld-context: ../../../sosa-ssn.jsonld
type: object
allOf:
  - $ref: bblocks://r1.geo.features.feature
  - $ref: ../../properties/observation/schema.yaml
```
## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
