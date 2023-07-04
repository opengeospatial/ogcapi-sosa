
# SOSA Observation Feature (Schema)

`ogc.unstable.sosa.features.observation` *v1.0*

This building blocks defines a GeoJSON feature containing a SOSA Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example of SOSA observation
#### json
```json
{
  "@id": "pop1999",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "properties": {
    "observedProperty": "https://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "@id": "pop1999",
    "comment": "Example of an inline membership - would entail hasMember relations",
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
    "hasSimpleResult": 15555.0
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
  observes: http://www.w3.org/ns/sosa/observes
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  resultTime: http://www.w3.org/ns/sosa/resultTime
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasMember: http://www.w3.org/ns/sosa/hasMember
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  forProperty: http://www.w3.org/ns/ssn/forProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  detects: http://www.w3.org/ns/ssn/detects
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasInput: http://www.w3.org/ns/ssn/hasInput
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  implements: http://www.w3.org/ns/ssn/implements
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  features: http://www.w3.org/ns/sosa/hasMember
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  Observation: http://www.w3.org/ns/sosa/Observation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hosts: http://www.w3.org/ns/sosa/hosts

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
    "hasResult": "http://www.w3.org/ns/sosa/hasResult",
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
    "hosts": "sosa:hosts"
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

