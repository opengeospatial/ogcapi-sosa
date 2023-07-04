
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
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  resultTime: http://www.w3.org/ns/sosa/resultTime
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  detects: http://www.w3.org/ns/ssn/detects
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hosts: http://www.w3.org/ns/sosa/hosts
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  Observation: http://www.w3.org/ns/sosa/Observation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasInput: http://www.w3.org/ns/ssn/hasInput
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasMember: http://www.w3.org/ns/sosa/hasMember
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  features: http://www.w3.org/ns/sosa/hasMember
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  observes: http://www.w3.org/ns/sosa/observes
  implements: http://www.w3.org/ns/ssn/implements
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy

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
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "Sample": "sosa:Sample",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "actsOnProperty": "sosa:actsOnProperty",
    "isSampleOf": "sosa:isSampleOf",
    "inDeployment": "ssn:inDeployment",
    "detects": "ssn:detects",
    "hasDeployment": "ssn:hasDeployment",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hosts": "sosa:hosts",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasSample": "sosa:hasSample",
    "deployedSystem": "ssn:deployedSystem",
    "madeSampling": "sosa:madeSampling",
    "hasSubSystem": "ssn:hasSubSystem",
    "madeObservation": "sosa:madeObservation",
    "madeActuation": "sosa:madeActuation",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "Observation": "sosa:Observation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasOutput": "ssn:hasOutput",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isObservedBy": "sosa:isObservedBy",
    "isProxyFor": "ssn:isProxyFor",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasProperty": "ssn:hasProperty",
    "hasInput": "ssn:hasInput",
    "forProperty": "ssn:forProperty",
    "hasMember": "sosa:hasMember",
    "madeByActuator": "sosa:madeByActuator",
    "madeBySampler": "sosa:madeBySampler",
    "inCondition": "ssn-system:inCondition",
    "implementedBy": "ssn:implementedBy",
    "isResultOf": "sosa:isResultOf",
    "observes": "sosa:observes",
    "implements": "ssn:implements",
    "isHostedBy": "sosa:isHostedBy"
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

