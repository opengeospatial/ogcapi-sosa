
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
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  forProperty: http://www.w3.org/ns/ssn/forProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hosts: http://www.w3.org/ns/sosa/hosts
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  Sample: http://www.w3.org/ns/sosa/Sample
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  observes: http://www.w3.org/ns/sosa/observes
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  implements: http://www.w3.org/ns/ssn/implements
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  detects: http://www.w3.org/ns/ssn/detects
  hasResult: http://www.w3.org/ns/sosa/hasResult
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember

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
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "Feature": "geojson:Feature",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
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
    "hasMember": "sosa:hasMember"
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

