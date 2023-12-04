---
title: SOSA Sensor (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA Sensor</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA Sensor (Schema)
---


# SOSA Sensor `ogc.unstable.sosa.properties.sensor`

An identifiable entity that can generate Observations pertaining to an ObservableProperty by implementing an ObservingProcedure. Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure. Sensors respond to a stimulus, e.g., a change in the environment, or input data composed from the results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/properties/sensor/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA Platform Properties

This building block describes the canonical set of properties for a System object.

These properties are independent of the feature (or object) model implementation 

these properties may be combined with other sets of properties for polymorphic objects - for example a Sensor that has a complex result, but can be broken down into a set of subSystems (a System) or hosted Sensors (a Platform)

Property sets are mix-in aspects that for example may be included in the "properties" component of a GeoJSON object, or used in any other schema.

The "id" property is assumed to be common and compatible with other mix-in aspects.





# Examples

## Example of of a basic sensor



```json
{         "@context": { "eg": "http://example.org/sensors",
            "sensorType": {
                  "type": "@id",
                  "@id": "sosa:sensorKind"
                } },
          "id": "eg:sensor1",
          "sensorType": "eg:gnss-pair"
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/sensor/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fsensor%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/context.jsonld",
    {
      "eg": "http://example.org/sensors",
      "sensorType": {
        "type": "@id",
        "@id": "sosa:sensorKind"
      }
    }
  ],
  "id": "eg:sensor1",
  "sensorType": "eg:gnss-pair"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/sensor/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fsensor%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .

<eg:sensor1> sosa:sensorKind "eg:gnss-pair" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/sensor/example_1_1.ttl">Open in new window</a>
</blockquote>



## Example of of a compound sensor using the System polymorphism option



```json
{
  "@context": {
    "eg": "http://example.org/sensors",
    "sensorType": {
      "type": "@id",
      "@id": "sosa:sensorKind"
    },
    "description": "eg:description",
    "lastCalibrated": "eg:calibrationDate",
    "purpose": "eg.purpose"
  },
  "id": "eg:gnss-pair-1",
  "sensorType": "eg:gnss-pair",
  "hasSubSystem": [
    {
      "sensorType": "eg:gnss",
      "id": "eg:785439870523",
      "description": "Leica Viva GS10",
      "lastCalibrated": "2022-09-14T15:32:45",
      "purpose": "eg:base"
    },
    {
      "sensorType": "eg:gnss",
      "id": "eg:785439870524",
      "description": "Leica Viva GS10",
      "lastCalibrated": "2022-09-14T15:35:05",
      "purpose": "eg:rover"
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/sensor/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fsensor%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/context.jsonld",
    {
      "eg": "http://example.org/sensors",
      "sensorType": {
        "type": "@id",
        "@id": "sosa:sensorKind"
      },
      "description": "eg:description",
      "lastCalibrated": "eg:calibrationDate",
      "purpose": "eg.purpose"
    }
  ],
  "id": "eg:gnss-pair-1",
  "sensorType": "eg:gnss-pair",
  "hasSubSystem": [
    {
      "sensorType": "eg:gnss",
      "id": "eg:785439870523",
      "description": "Leica Viva GS10",
      "lastCalibrated": "2022-09-14T15:32:45",
      "purpose": "eg:base"
    },
    {
      "sensorType": "eg:gnss",
      "id": "eg:785439870524",
      "description": "Leica Viva GS10",
      "lastCalibrated": "2022-09-14T15:35:05",
      "purpose": "eg:rover"
    }
  ]
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/sensor/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fsensor%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix ns1: <http://example.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

<eg:gnss-pair-1> sosa:hasSubSystem <eg:785439870523>,
        <eg:785439870524> ;
    sosa:sensorKind "eg:gnss-pair" .

<eg:785439870523> <eg.purpose> "eg:base" ;
    ns1:sensorscalibrationDate "2022-09-14T15:32:45" ;
    ns1:sensorsdescription "Leica Viva GS10" ;
    sosa:sensorKind "eg:gnss" .

<eg:785439870524> <eg.purpose> "eg:rover" ;
    ns1:sensorscalibrationDate "2022-09-14T15:35:05" ;
    ns1:sensorsdescription "Leica Viva GS10" ;
    sosa:sensorKind "eg:gnss" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/sensor/example_2_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Sensor
$definitions:
  Sensor:
    anyOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    - type: object
      properties:
        id:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          x-jsonld-id: '@id'
        name:
          type: string
allOf:
- $ref: '#/$definitions/Sensor'
x-jsonld-extra-terms:
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  System: http://www.w3.org/ns/sosa/System
  Platform: http://www.w3.org/ns/sosa/Platform
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  actsOnProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
    x-jsonld-type: '@id'
  isActedOnBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
    x-jsonld-type: '@id'
  madeActuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
    x-jsonld-type: '@id'
  madeByActuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
    x-jsonld-type: '@id'
  hasSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
    x-jsonld-type: '@id'
  isSampleOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
    x-jsonld-type: '@id'
  madeSampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
    x-jsonld-type: '@id'
  madeBySampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  resultTime: http://www.w3.org/ns/sosa/resultTime
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isProxyFor: http://www.w3.org/ns/sosa/isProxyFor
  wasOriginatedBy: http://www.w3.org/ns/sosa/wasOriginatedBy
  detects: http://www.w3.org/ns/sosa/detects
  hasProperty: http://www.w3.org/ns/sosa/hasProperty
  isPropertyOf: http://www.w3.org/ns/sosa/isPropertyOf
  forProperty: http://www.w3.org/ns/sosa/forProperty
  implements: http://www.w3.org/ns/sosa/implements
  implementedBy: http://www.w3.org/ns/sosa/implementedBy
  hasInput: http://www.w3.org/ns/sosa/hasInput
  hasOutput: http://www.w3.org/ns/sosa/hasOutput
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  deployedSystem: http://www.w3.org/ns/sosa/deployedSystem
  hasDeployment: http://www.w3.org/ns/sosa/hasDeployment
  deployedOnPlatform: http://www.w3.org/ns/sosa/deployedOnPlatform
  inDeployment: http://www.w3.org/ns/sosa/inDeployment
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  features: http://www.w3.org/ns/sosa/hasMember
  properties: '@nest'
  featureType: '@type'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn-system: http://www.w3.org/ns/ssn/systems/
  ssn: http://www.w3.org/ns/ssn/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Fproperties%2Fsensor%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/schema.yaml" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/schema.json" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "System": "sosa:System",
    "Platform": "sosa:Platform",
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "phenomenonTime": "sosa:phenomenonTime",
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "sosa:madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "sosa:madeByActuator",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "isResultOf": "sosa:isResultOf",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "resultTime": "sosa:resultTime",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id",
      "@container": "@set"
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "sosa:isProxyFor",
    "wasOriginatedBy": "sosa:wasOriginatedBy",
    "detects": "sosa:detects",
    "hasProperty": "sosa:hasProperty",
    "isPropertyOf": "sosa:isPropertyOf",
    "forProperty": "sosa:forProperty",
    "implements": "sosa:implements",
    "implementedBy": "sosa:implementedBy",
    "hasInput": "sosa:hasInput",
    "hasOutput": "sosa:hasOutput",
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "deployedSystem": "sosa:deployedSystem",
    "hasDeployment": "sosa:hasDeployment",
    "deployedOnPlatform": "sosa:deployedOnPlatform",
    "inDeployment": "sosa:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "features": "sosa:hasMember",
    "properties": "@nest",
    "featureType": "@type",
    "id": "@id",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Fproperties%2Fsensor%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/context.jsonld" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/sensor/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/properties/sensor" target="_blank">_sources/properties/sensor</a></code>

