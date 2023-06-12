
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

#### ttl
```ttl
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
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasResult: http://www.w3.org/ns/sosa/hasResult
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  Sample: http://www.w3.org/ns/sosa/Sample
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hosts: http://www.w3.org/ns/sosa/hosts
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasInput: http://www.w3.org/ns/ssn/hasInput
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  resultTime: http://www.w3.org/ns/sosa/resultTime
  detects: http://www.w3.org/ns/ssn/detects
  hasMember: http://www.w3.org/ns/sosa/hasMember
  Observation: http://www.w3.org/ns/sosa/Observation
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  implements: http://www.w3.org/ns/ssn/implements
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  observes: http://www.w3.org/ns/sosa/observes
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime

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
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isObservedBy": "sosa:isObservedBy",
    "hasProperty": "ssn:hasProperty",
    "isSampleOf": "sosa:isSampleOf",
    "isResultOf": "sosa:isResultOf",
    "inDeployment": "ssn:inDeployment",
    "isActedOnBy": "sosa:isActedOnBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeActuation": "sosa:madeActuation",
    "hasDeployment": "ssn:hasDeployment",
    "hasSubSystem": "ssn:hasSubSystem",
    "Sample": "sosa:Sample",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "actsOnProperty": "sosa:actsOnProperty",
    "hosts": "sosa:hosts",
    "madeSampling": "sosa:madeSampling",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasOutput": "ssn:hasOutput",
    "deployedSystem": "ssn:deployedSystem",
    "isHostedBy": "sosa:isHostedBy",
    "madeBySampler": "sosa:madeBySampler",
    "madeByActuator": "sosa:madeByActuator",
    "forProperty": "ssn:forProperty",
    "hasSample": "sosa:hasSample",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasInput": "ssn:hasInput",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isProxyFor": "ssn:isProxyFor",
    "detects": "ssn:detects",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "madeObservation": "sosa:madeObservation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "implements": "ssn:implements",
    "implementedBy": "ssn:implementedBy",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "observes": "sosa:observes"
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

