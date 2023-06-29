---
title: SOSA Observation (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA Observation</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA Observation (Schema)
---


# SOSA Observation `ogc.unstable.sosa.properties.observation`

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/properties/observation/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA Observation

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."
# Examples

## Example of SOSA observation

```json
{ 
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z"
}
```

```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
```


# JSON Schema

```yaml--schema
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
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  detects: http://www.w3.org/ns/ssn/detects
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasResult: http://www.w3.org/ns/sosa/hasResult
  Observation: http://www.w3.org/ns/sosa/Observation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hosts: http://www.w3.org/ns/sosa/hosts
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  observes: http://www.w3.org/ns/sosa/observes
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSample: http://www.w3.org/ns/sosa/hasSample
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

* YAML version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/schema.yaml" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/schema.yaml</a>
* JSON version: <a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/schema.json" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/schema.json</a>


# JSON-LD Context

```json--ldContext
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/properties/observation`

