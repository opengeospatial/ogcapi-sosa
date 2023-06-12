
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

#### ttl
```ttl
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
  sosa:resultTime "1999-01-01"^^xsd:dateTime
.

 eg:pop2000 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 4372.0 ;
  sosa:resultTime "2000"^^xsd:dateTime
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
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isObservedBy": "sosa:isObservedBy",
    "hasProperty": "ssn:hasProperty",
    "isSampleOf": "sosa:isSampleOf",
    "isResultOf": "sosa:isResultOf",
    "inDeployment": "ssn:inDeployment",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasResult": "sosa:hasResult",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeActuation": "sosa:madeActuation",
    "hasDeployment": "ssn:hasDeployment",
    "hasSubSystem": "ssn:hasSubSystem",
    "Sample": "sosa:Sample",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSimpleResult": "sosa:hasSimpleResult",
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
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/features/observationCollection/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observationCollection`

