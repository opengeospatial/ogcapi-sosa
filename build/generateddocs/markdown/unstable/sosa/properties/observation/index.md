
# SOSA Observation (Schema)

`ogc.unstable.sosa.properties.observation` *v1.0*

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

## SOSA Observation

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."
## Examples

### Example of SOSA observation
#### json
```json
{ 
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z"
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation
type: object
properties:
  resultTime:
    type: string
    format: date-time
    x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
  phenomenonTime:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
  hasFeatureOfInterest:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  observedProperty:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
  usedProcedure:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  madeBySensor:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  hasResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
  hasSimpleResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSimpleResult
oneOf:
- required:
  - hasResult
- required:
  - hasSimpleResult
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  forProperty: http://www.w3.org/ns/ssn/forProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  Observation: http://www.w3.org/ns/sosa/Observation
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  observes: http://www.w3.org/ns/sosa/observes
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  implements: http://www.w3.org/ns/ssn/implements
  detects: http://www.w3.org/ns/ssn/detects
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hosts: http://www.w3.org/ns/sosa/hosts
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  Sample: http://www.w3.org/ns/sosa/Sample
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/schema.yaml)


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
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasDeployment": "ssn:hasDeployment",
    "isObservedBy": "sosa:isObservedBy",
    "hasInput": "ssn:hasInput",
    "hasMember": "sosa:hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeActuation": "sosa:madeActuation",
    "hasSubSystem": "ssn:hasSubSystem",
    "isPropertyOf": "ssn:isPropertyOf",
    "madeByActuator": "sosa:madeByActuator",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "madeObservation": "sosa:madeObservation",
    "madeBySampler": "sosa:madeBySampler",
    "forProperty": "ssn:forProperty",
    "inDeployment": "ssn:inDeployment",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "Observation": "sosa:Observation",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "observes": "sosa:observes",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "implements": "ssn:implements",
    "detects": "ssn:detects",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasProperty": "ssn:hasProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasSample": "sosa:hasSample",
    "isSampleOf": "sosa:isSampleOf",
    "isProxyFor": "ssn:isProxyFor",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "inCondition": "ssn-system:inCondition",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/observation`

