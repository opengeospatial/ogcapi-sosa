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


# SOSA Sensor `ogc.sosa.properties.sensor`

An identifiable entity that can generate Observations pertaining to an ObservableProperty by implementing an ObservingProcedure. Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure. Sensors respond to a stimulus, e.g., a change in the environment, or input data composed from the results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/sosa/properties/sensor/" target="_blank">valid</a></strong>
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
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/sensor/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Fsosa%2Fproperties%2Fsensor%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/context.jsonld",
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
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/sensor/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Fsosa%2Fproperties%2Fsensor%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .

[] sosa:sensorKind "eg:gnss-pair" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/sensor/example_1_1.ttl">Open in new window</a>
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
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/sensor/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Fsosa%2Fproperties%2Fsensor%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/context.jsonld",
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
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/sensor/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Fsosa%2Fproperties%2Fsensor%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix ns1: <http://example.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

[] sosa:hasSubSystem [ <eg.purpose> "eg:base" ;
            ns1:sensorscalibrationDate "2022-09-14T15:32:45" ;
            ns1:sensorsdescription "Leica Viva GS10" ;
            sosa:sensorKind "eg:gnss" ],
        [ <eg.purpose> "eg:rover" ;
            ns1:sensorscalibrationDate "2022-09-14T15:35:05" ;
            ns1:sensorsdescription "Leica Viva GS10" ;
            sosa:sensorKind "eg:gnss" ] ;
    sosa:sensorKind "eg:gnss-pair" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/sensor/example_2_1.ttl">Open in new window</a>
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
        name:
          type: string
allOf:
- $ref: '#/$definitions/Sensor'
x-jsonld-extra-terms:
  properties: '@nest'
  featureType: '@type'
  ActuatableProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/ActuatableProperty
    x-jsonld-type: '@id'
  Actuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/Actuation
    x-jsonld-type: '@id'
  ActuationCollection:
    x-jsonld-id: http://www.w3.org/ns/sosa/ActuationCollection
    x-jsonld-type: '@id'
  Actuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/Actuator
    x-jsonld-type: '@id'
  Deployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/Deployment
    x-jsonld-type: '@id'
  Execution:
    x-jsonld-id: http://www.w3.org/ns/sosa/Execution
    x-jsonld-type: '@id'
  FeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/FeatureOfInterest
    x-jsonld-type: '@id'
  ObservableProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/ObservableProperty
    x-jsonld-type: '@id'
  Observation:
    x-jsonld-id: http://www.w3.org/ns/sosa/Observation
    x-jsonld-type: '@id'
  ObservationCollection:
    x-jsonld-id: http://www.w3.org/ns/sosa/ObservationCollection
    x-jsonld-type: '@id'
  Platform:
    x-jsonld-id: http://www.w3.org/ns/sosa/Platform
    x-jsonld-type: '@id'
  Property:
    x-jsonld-id: http://www.w3.org/ns/sosa/Property
    x-jsonld-type: '@id'
  'Procedure ':
    x-jsonld-id: http://www.w3.org/ns/sosa/Procedure
    x-jsonld-type: '@id'
  Sample:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sample
    x-jsonld-type: '@id'
  SampleCollection:
    x-jsonld-id: http://www.w3.org/ns/sosa/SampleCollection
    x-jsonld-type: '@id'
  Sampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sampler
    x-jsonld-type: '@id'
  Sampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sampling
    x-jsonld-type: '@id'
  Sensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sensor
    x-jsonld-type: '@id'
  Stimulus:
    x-jsonld-id: http://www.w3.org/ns/sosa/Stimulus
    x-jsonld-type: '@id'
  System:
    x-jsonld-id: http://www.w3.org/ns/sosa/System
    x-jsonld-type: '@id'
  actsOnProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
    x-jsonld-type: '@id'
  deployedOnPlatform:
    x-jsonld-id: http://www.w3.org/ns/sosa/deployedOnPlatform
    x-jsonld-type: '@id'
  deployedSystem:
    x-jsonld-id: http://www.w3.org/ns/sosa/deployedSystem
    x-jsonld-type: '@id'
  detects:
    x-jsonld-id: http://www.w3.org/ns/sosa/detects
    x-jsonld-type: '@id'
  features:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  forProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/forProperty
    x-jsonld-type: '@id'
  hasDeployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasDeployment
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasInput
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  hasOriginalSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasOriginalSample
    x-jsonld-type: '@id'
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasOutput
    x-jsonld-type: '@id'
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasProperty
    x-jsonld-type: '@id'
  hasResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
    x-jsonld-type: '@id'
  hasResultQuality:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResultQuality
    x-jsonld-type: '@id'
  hasSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
    x-jsonld-type: '@id'
  hasSampledFeature:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSampledFeature
    x-jsonld-type: '@id'
  hasSimpleResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSimpleResult
    x-jsonld-type: '@id'
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSubSystem
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  hasUltimateFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
    x-jsonld-type: '@id'
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
    x-jsonld-container: '@set'
  implementedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/implementedBy
    x-jsonld-type: '@id'
  implements:
    x-jsonld-id: http://www.w3.org/ns/sosa/implements
    x-jsonld-type: '@id'
  inDeployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/inDeployment
    x-jsonld-type: '@id'
  isActedOnBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  isHostedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isHostedBy
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  isPropertyOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isPropertyOf
    x-jsonld-type: '@id'
  isProxyFor:
    x-jsonld-id: http://www.w3.org/ns/sosa/isProxyFor
    x-jsonld-type: '@id'
  isResultOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOf
    x-jsonld-type: '@id'
  isResultOfMadeBySampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOfMadeBySampler
    x-jsonld-type: '@id'
  isResultOfUsedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOfUsedProcedure
    x-jsonld-type: '@id'
  isSampleOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
    x-jsonld-type: '@id'
  madeActuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
    x-jsonld-type: '@id'
  madeByActuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
    x-jsonld-type: '@id'
  madeBySampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
    x-jsonld-type: '@id'
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  madeSampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
    x-jsonld-type: '@id'
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  phenomenonTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    x-jsonld-type: '@id'
  resultTime: http://www.w3.org/ns/sosa/resultTime
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  wasOriginatedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/wasOriginatedBy
    x-jsonld-type: '@id'
  Accuracy:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Accuracy
    x-jsonld-type: '@id'
  ActuationRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/ActuationRange
    x-jsonld-type: '@id'
  BatteryLifetime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/BatteryLifetime
    x-jsonld-type: '@id'
  DetectionLimit:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/DetectionLimit
    x-jsonld-type: '@id'
  Drift:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Drift
    x-jsonld-type: '@id'
  Frequency:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Frequency
    x-jsonld-type: '@id'
  Latency:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Latency
    x-jsonld-type: '@id'
  MaintenanceSchedule:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/MaintenanceSchedule
    x-jsonld-type: '@id'
  MeasurementRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/MeasurementRange
    x-jsonld-type: '@id'
  OperatingPowerRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingPowerRange
    x-jsonld-type: '@id'
  OperatingProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingProperty
    x-jsonld-type: '@id'
  OperatingRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingRange
    x-jsonld-type: '@id'
  Precision:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Precision
    x-jsonld-type: '@id'
  Resolution:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Resolution
    x-jsonld-type: '@id'
  ResponseTime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/ResponseTime
    x-jsonld-type: '@id'
  Selectivity:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Selectivity
    x-jsonld-type: '@id'
  Sensitivity:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Sensitivity
    x-jsonld-type: '@id'
  SurvivalProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SurvivalProperty
    x-jsonld-type: '@id'
  SystemLifetime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemLifetime
    x-jsonld-type: '@id'
  SurvivalRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SurvivalRange
    x-jsonld-type: '@id'
  SystemCapability:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemCapability
    x-jsonld-type: '@id'
  SystemProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemProperty
    x-jsonld-type: '@id'
  hasOperatingProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    x-jsonld-type: '@id'
  hasOperatingRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    x-jsonld-type: '@id'
  hasSurvivalProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    x-jsonld-type: '@id'
  hasSystemCapability:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    x-jsonld-type: '@id'
  hasSystemProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    x-jsonld-type: '@id'
  hasSurvivalRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    x-jsonld-type: '@id'
  inCondition:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/inCondition
    x-jsonld-type: '@id'
  qualityOfObservation:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn-system: http://www.w3.org/ns/ssn/systems/
  ssn: http://www.w3.org/ns/ssn/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Fsosa%2Fproperties%2Fsensor%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/schema.yaml" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/schema.json" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "properties": "@nest",
    "featureType": "@type",
    "ActuatableProperty": {
      "@id": "sosa:ActuatableProperty",
      "@type": "@id"
    },
    "Actuation": {
      "@id": "sosa:Actuation",
      "@type": "@id"
    },
    "ActuationCollection": {
      "@id": "sosa:ActuationCollection",
      "@type": "@id"
    },
    "Actuator": {
      "@id": "sosa:Actuator",
      "@type": "@id"
    },
    "Deployment": {
      "@id": "sosa:Deployment",
      "@type": "@id"
    },
    "Execution": {
      "@id": "sosa:Execution",
      "@type": "@id"
    },
    "FeatureOfInterest": {
      "@id": "sosa:FeatureOfInterest",
      "@type": "@id"
    },
    "ObservableProperty": {
      "@id": "sosa:ObservableProperty",
      "@type": "@id"
    },
    "Observation": {
      "@id": "sosa:Observation",
      "@type": "@id"
    },
    "ObservationCollection": {
      "@id": "sosa:ObservationCollection",
      "@type": "@id"
    },
    "Platform": {
      "@id": "sosa:Platform",
      "@type": "@id"
    },
    "Property": {
      "@id": "sosa:Property",
      "@type": "@id"
    },
    "Procedure ": {
      "@id": "sosa:Procedure",
      "@type": "@id"
    },
    "Sample": {
      "@id": "sosa:Sample",
      "@type": "@id"
    },
    "SampleCollection": {
      "@id": "sosa:SampleCollection",
      "@type": "@id"
    },
    "Sampler": {
      "@id": "sosa:Sampler",
      "@type": "@id"
    },
    "Sampling": {
      "@id": "sosa:Sampling",
      "@type": "@id"
    },
    "Sensor": {
      "@id": "sosa:Sensor",
      "@type": "@id"
    },
    "Stimulus": {
      "@id": "sosa:Stimulus",
      "@type": "@id"
    },
    "System": {
      "@id": "sosa:System",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "deployedOnPlatform": {
      "@id": "sosa:deployedOnPlatform",
      "@type": "@id"
    },
    "deployedSystem": {
      "@id": "sosa:deployedSystem",
      "@type": "@id"
    },
    "detects": {
      "@id": "sosa:detects",
      "@type": "@id"
    },
    "features": {
      "@id": "sosa:hasMember",
      "@type": "@id"
    },
    "forProperty": {
      "@id": "sosa:forProperty",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "sosa:hasDeployment",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "hasInput": {
      "@id": "sosa:hasInput",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "sosa:hasMember",
      "@type": "@id"
    },
    "hasOriginalSample": {
      "@id": "sosa:hasOriginalSample",
      "@type": "@id"
    },
    "hasOutput": {
      "@id": "sosa:hasOutput",
      "@type": "@id"
    },
    "hasProperty": {
      "@id": "sosa:hasProperty",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "sosa:hasResult",
      "@type": "@id"
    },
    "hasResultQuality": {
      "@id": "sosa:hasResultQuality",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "hasSampledFeature": {
      "@id": "sosa:hasSampledFeature",
      "@type": "@id"
    },
    "hasSimpleResult": {
      "@id": "sosa:hasSimpleResult",
      "@type": "@id"
    },
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "hasUltimateFeatureOfInterest": {
      "@id": "sosa:hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id",
      "@container": "@set"
    },
    "implementedBy": {
      "@id": "sosa:implementedBy",
      "@type": "@id"
    },
    "implements": {
      "@id": "sosa:implements",
      "@type": "@id"
    },
    "inDeployment": {
      "@id": "sosa:inDeployment",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isHostedBy": {
      "@id": "sosa:isHostedBy",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "isPropertyOf": {
      "@id": "sosa:isPropertyOf",
      "@type": "@id"
    },
    "isProxyFor": {
      "@id": "sosa:isProxyFor",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "sosa:isResultOf",
      "@type": "@id"
    },
    "isResultOfMadeBySampler": {
      "@id": "sosa:isResultOfMadeBySampler",
      "@type": "@id"
    },
    "isResultOfUsedProcedure": {
      "@id": "sosa:isResultOfUsedProcedure",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
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
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "@id"
    },
    "resultTime": "sosa:resultTime",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "wasOriginatedBy": {
      "@id": "sosa:wasOriginatedBy",
      "@type": "@id"
    },
    "Accuracy": {
      "@id": "ssn-system:Accuracy",
      "@type": "@id"
    },
    "ActuationRange": {
      "@id": "ssn-system:ActuationRange",
      "@type": "@id"
    },
    "BatteryLifetime": {
      "@id": "ssn-system:BatteryLifetime",
      "@type": "@id"
    },
    "DetectionLimit": {
      "@id": "ssn-system:DetectionLimit",
      "@type": "@id"
    },
    "Drift": {
      "@id": "ssn-system:Drift",
      "@type": "@id"
    },
    "Frequency": {
      "@id": "ssn-system:Frequency",
      "@type": "@id"
    },
    "Latency": {
      "@id": "ssn-system:Latency",
      "@type": "@id"
    },
    "MaintenanceSchedule": {
      "@id": "ssn-system:MaintenanceSchedule",
      "@type": "@id"
    },
    "MeasurementRange": {
      "@id": "ssn-system:MeasurementRange",
      "@type": "@id"
    },
    "OperatingPowerRange": {
      "@id": "ssn-system:OperatingPowerRange",
      "@type": "@id"
    },
    "OperatingProperty": {
      "@id": "ssn-system:OperatingProperty",
      "@type": "@id"
    },
    "OperatingRange": {
      "@id": "ssn-system:OperatingRange",
      "@type": "@id"
    },
    "Precision": {
      "@id": "ssn-system:Precision",
      "@type": "@id"
    },
    "Resolution": {
      "@id": "ssn-system:Resolution",
      "@type": "@id"
    },
    "ResponseTime": {
      "@id": "ssn-system:ResponseTime",
      "@type": "@id"
    },
    "Selectivity": {
      "@id": "ssn-system:Selectivity",
      "@type": "@id"
    },
    "Sensitivity": {
      "@id": "ssn-system:Sensitivity",
      "@type": "@id"
    },
    "SurvivalProperty": {
      "@id": "ssn-system:SurvivalProperty",
      "@type": "@id"
    },
    "SystemLifetime": {
      "@id": "ssn-system:SystemLifetime",
      "@type": "@id"
    },
    "SurvivalRange": {
      "@id": "ssn-system:SurvivalRange",
      "@type": "@id"
    },
    "SystemCapability": {
      "@id": "ssn-system:SystemCapability",
      "@type": "@id"
    },
    "SystemProperty": {
      "@id": "ssn-system:SystemProperty",
      "@type": "@id"
    },
    "hasOperatingProperty": {
      "@id": "ssn-system:hasOperatingProperty",
      "@type": "@id"
    },
    "hasOperatingRange": {
      "@id": "ssn-system:hasOperatingRange",
      "@type": "@id"
    },
    "hasSurvivalProperty": {
      "@id": "ssn-system:hasSurvivalProperty",
      "@type": "@id"
    },
    "hasSystemCapability": {
      "@id": "ssn-system:hasSystemCapability",
      "@type": "@id"
    },
    "hasSystemProperty": {
      "@id": "ssn-system:hasSystemProperty",
      "@type": "@id"
    },
    "hasSurvivalRange": {
      "@id": "ssn-system:hasSurvivalRange",
      "@type": "@id"
    },
    "inCondition": {
      "@id": "ssn-system:inCondition",
      "@type": "@id"
    },
    "qualityOfObservation": {
      "@id": "ssn-system:qualityOfObservation",
      "@type": "@id"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Fsosa%2Fproperties%2Fsensor%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/context.jsonld" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/sosa/properties/sensor/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/properties/sensor" target="_blank">_sources/properties/sensor</a></code>

