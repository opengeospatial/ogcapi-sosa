
# SOSA ObservationCollection Feature (Schema)

`ogc.unstable.sosa.features.observationCollection` *v1.0*

This building blocks defines an ObservationCollection Feature according to the SOSA/SSN v1.1 specification.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example of SOSA ObservationCollection
#### json
```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "hasMember": [
      "_:a1"
    ],
    "observedProperty": "_:p1",
    "resultTime": "2022-05-01T22:33:44Z"
  },
}
```

#### json
```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "observedProperty": "http://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "features": [
      { 
        "@id": "pop1999",
        "comment": "Example of an inline membership - would entail hasMember relations",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
        "hasSimpleResult": 15555.0
      },
       { 
        "@id": "pop1999",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
        "hasSimpleResult": 3275.0
      }
    ]
  },
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:pop1999, eg:pop2000 ;
  sosa:observedProperty <http://dbpedia.org/ontology/population> ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.

eg:pop1999 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 3275.0 ;
  sosa:resultTime "1999-01-01"^^xsd:date
.

 eg:pop2000 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 4372.0 ;
  sosa:resultTime "2000"^^xsd:gYear
.

<http://dbpedia.org/ontology/population> a skos:Concept;
  skos:prefLabel "Population";
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observationCollection/schema.yaml
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

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/schema.yaml)


# JSON-LD Context

```jsonld
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
    "hasMember": "sosa:hasMember",
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
    "hasSimpleResult": "sosa:hasSimpleResult",
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
    "hasResult": "sosa:hasResult",
    "Observation": "sosa:Observation"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observationCollection`

