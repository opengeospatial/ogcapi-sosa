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
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasResult: http://www.w3.org/ns/sosa/hasResult
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hosts: http://www.w3.org/ns/sosa/hosts
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  implements: http://www.w3.org/ns/ssn/implements
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasInput: http://www.w3.org/ns/ssn/hasInput
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  observes: http://www.w3.org/ns/sosa/observes
  detects: http://www.w3.org/ns/ssn/detects
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput

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
    "hasProperty": "ssn:hasProperty",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSample": "sosa:hasSample",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "deployedSystem": "ssn:deployedSystem",
    "inCondition": "ssn-system:inCondition",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "madeObservation": "sosa:madeObservation",
    "madeSampling": "sosa:madeSampling",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeBySampler": "sosa:madeBySampler",
    "hosts": "sosa:hosts",
    "implementedBy": "ssn:implementedBy",
    "isSampleOf": "sosa:isSampleOf",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "madeActuation": "sosa:madeActuation",
    "madeByActuator": "sosa:madeByActuator",
    "implements": "ssn:implements",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "observes": "sosa:observes",
    "detects": "ssn:detects",
    "actsOnProperty": "sosa:actsOnProperty",
    "isProxyFor": "ssn:isProxyFor",
    "hasSubSystem": "ssn:hasSubSystem",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isObservedBy": "sosa:isObservedBy",
    "hasMember": "sosa:hasMember",
    "isResultOf": "sosa:isResultOf",
    "hasDeployment": "ssn:hasDeployment",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput"
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

