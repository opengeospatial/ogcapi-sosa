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
  observes: http://www.w3.org/ns/sosa/observes
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasMember: http://www.w3.org/ns/sosa/hasMember
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
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  features: http://www.w3.org/ns/sosa/hasMember
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  Observation: http://www.w3.org/ns/sosa/Observation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hosts: http://www.w3.org/ns/sosa/hosts

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
    "features": "sosa:hasMember",
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
<a href="https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/context.jsonld" target="_blank">https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/properties/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/properties/observation`

