
# SOSA Observation Feature (Schema)

`ogc.unstable.sosa.features.observation` *v1.0*

This building blocks defines a GeoJSON feature containing a SOSA Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example of SOSA observation
#### json
```json
{ 
  "@id": "_:a1",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": {
    "type": "Point",
    "coordinates": [43.457475012484124, -3.7684047847661435]
  },
  "properties": {
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
    "hasSimpleResult": 33,
    "resultTime": "2022-05-01T22:33:44Z"
    }
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
_:a1 a geojson:Feature;
  geojson:properties [
    sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 33 ;
    sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime
  ]
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
type: object
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observation/schema.yaml
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  detects: http://www.w3.org/ns/ssn/detects
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasResult: http://www.w3.org/ns/sosa/hasResult
  Observation: http://www.w3.org/ns/sosa/Observation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hosts: http://www.w3.org/ns/sosa/hosts
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  observes: http://www.w3.org/ns/sosa/observes
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSample: http://www.w3.org/ns/sosa/hasSample
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  implements: http://www.w3.org/ns/ssn/implements
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/schema.yaml)


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
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "features": "geojson:features",
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
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "implementedBy": "ssn:implementedBy",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "Sample": "sosa:Sample",
    "madeByActuator": "sosa:madeByActuator",
    "madeSampling": "sosa:madeSampling",
    "madeBySampler": "sosa:madeBySampler",
    "deployedSystem": "ssn:deployedSystem",
    "isSampleOf": "sosa:isSampleOf",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "detects": "ssn:detects",
    "isObservedBy": "sosa:isObservedBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "Observation": "sosa:Observation",
    "isProxyFor": "ssn:isProxyFor",
    "inCondition": "ssn-system:inCondition",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hosts": "sosa:hosts",
    "hasDeployment": "ssn:hasDeployment",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "observes": "sosa:observes",
    "isResultOf": "sosa:isResultOf",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeObservation": "sosa:madeObservation",
    "madeActuation": "sosa:madeActuation",
    "hasSample": "sosa:hasSample",
    "hasInput": "ssn:hasInput",
    "hasMember": "sosa:hasMember",
    "hasOutput": "ssn:hasOutput",
    "isActedOnBy": "sosa:isActedOnBy",
    "forProperty": "ssn:forProperty",
    "isHostedBy": "sosa:isHostedBy",
    "hasProperty": "ssn:hasProperty",
    "inDeployment": "ssn:inDeployment",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "implements": "ssn:implements",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observation`

