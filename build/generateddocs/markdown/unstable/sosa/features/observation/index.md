
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
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  observes: http://www.w3.org/ns/sosa/observes
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  Sample: http://www.w3.org/ns/sosa/Sample
  hasInput: http://www.w3.org/ns/ssn/hasInput
  resultTime: http://www.w3.org/ns/sosa/resultTime
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  detects: http://www.w3.org/ns/ssn/detects
  features: http://www.w3.org/ns/sosa/hasMember
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hosts: http://www.w3.org/ns/sosa/hosts
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  forProperty: http://www.w3.org/ns/ssn/forProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  implements: http://www.w3.org/ns/ssn/implements
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasResult: http://www.w3.org/ns/sosa/hasResult
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform

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
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "Sample": "sosa:Sample",
    "hasInput": "ssn:hasInput",
    "madeSampling": "sosa:madeSampling",
    "isProxyFor": "ssn:isProxyFor",
    "hasSample": "sosa:hasSample",
    "madeBySampler": "sosa:madeBySampler",
    "detects": "ssn:detects",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "deployedSystem": "ssn:deployedSystem",
    "isActedOnBy": "sosa:isActedOnBy",
    "hosts": "sosa:hosts",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeObservation": "sosa:madeObservation",
    "madeByActuator": "sosa:madeByActuator",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "forProperty": "ssn:forProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "implementedBy": "ssn:implementedBy",
    "Observation": "sosa:Observation",
    "hasMember": "sosa:hasMember",
    "hasOutput": "ssn:hasOutput",
    "inDeployment": "ssn:inDeployment",
    "actsOnProperty": "sosa:actsOnProperty",
    "implements": "ssn:implements",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isResultOf": "sosa:isResultOf",
    "isHostedBy": "sosa:isHostedBy",
    "hasSubSystem": "ssn:hasSubSystem",
    "isObservedBy": "sosa:isObservedBy",
    "inCondition": "ssn-system:inCondition",
    "isSampleOf": "sosa:isSampleOf",
    "madeActuation": "sosa:madeActuation",
    "hasProperty": "ssn:hasProperty",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "deployedOnPlatform": "ssn:deployedOnPlatform"
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

