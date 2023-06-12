
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

#### ttl
```ttl
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
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  Observation: http://www.w3.org/ns/sosa/Observation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  implements: http://www.w3.org/ns/ssn/implements
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  observes: http://www.w3.org/ns/sosa/observes
  detects: http://www.w3.org/ns/ssn/detects
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  Sample: http://www.w3.org/ns/sosa/Sample
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hosts: http://www.w3.org/ns/sosa/hosts
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasResult: http://www.w3.org/ns/sosa/hasResult

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
    "hasSample": "sosa:hasSample",
    "isPropertyOf": "ssn:isPropertyOf",
    "isSampleOf": "sosa:isSampleOf",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Observation": "sosa:Observation",
    "isProxyFor": "ssn:isProxyFor",
    "implements": "ssn:implements",
    "deployedSystem": "ssn:deployedSystem",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "forProperty": "ssn:forProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isResultOf": "sosa:isResultOf",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "madeByActuator": "sosa:madeByActuator",
    "isObservedBy": "sosa:isObservedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasDeployment": "ssn:hasDeployment",
    "hasMember": "sosa:hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeBySampler": "sosa:madeBySampler",
    "isHostedBy": "sosa:isHostedBy",
    "madeSampling": "sosa:madeSampling",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "observes": "sosa:observes",
    "detects": "ssn:detects",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "actsOnProperty": "sosa:actsOnProperty",
    "hosts": "sosa:hosts",
    "deployedOnPlatform": "ssn:deployedOnPlatform"
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

