---
title: SOSA Observation (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle
  - jsonld: JSON-LD

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

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/unstable/sosa/properties/observation/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA Observation Properties

This building block describes the canonical set of properties for an Observation object.

These properties are independent of the feature model implementation - for example may be included in the "properties" component of a GeoJSON object, or used in any other schema.

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."


# Examples

## Example of SOSA observation with simple result



```json
{ 
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "observedProperty": "p1",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z"
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fobservation%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
  sosa:observedProperty <http://example.com/p1> ;
.
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_1_2.ttl">Open in new window</a>
</blockquote>




```jsonld
{
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "observedProperty": "p1",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z",
  "@context": "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fobservation%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a sosa:Observation ;
    sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 33 ;
    sosa:observedProperty <http://example.com/p1> ;
    sosa:resultTime "2022-05-01T22:33:44+00:00"^^xsd:dateTime .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_1_2.ttl">Open in new window</a>
</blockquote>



## Example of SOSA observation with object result



```json
{
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "observedProperty": "p1",
  "hasResult": {
    "@context": {
      "comment": "rdfs:comment",
    },
    "comment": "I feel good"
  },
  "resultTime": "2022-05-01T22:33:44Z"
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fobservation%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "observedProperty": "p1",
  "hasResult": {
    "@context": {
      "comment": "rdfs:comment"
    },
    "comment": "I feel good"
  },
  "resultTime": "2022-05-01T22:33:44Z",
  "@context": "https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Ftests%2Funstable%2Fsosa%2Fproperties%2Fobservation%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix ns1: <rdfs:> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

[] sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasResult [ ns1:comment "I feel good" ] ;
    sosa:observedProperty <file:///github/workspace/p1> ;
    sosa:resultTime "2022-05-01T22:33:44Z" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/unstable/sosa/properties/observation/example_2_1.ttl">Open in new window</a>
</blockquote>



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
    x-jsonld-type: '@id'
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
    x-jsonld-type: '@id'
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
anyOf:
- required:
  - hasResult
- required:
  - hasSimpleResult
x-jsonld-extra-terms:
  id: '@id'
  ActuatableProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/ActuatableProperty
    x-jsonld-type: '@id'
  Actuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/Actuation
    x-jsonld-type: '@id'
  Actuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/Actuator
    x-jsonld-type: '@id'
  Deployment:
    x-jsonld-id: http://www.w3.org/ns/sosa/Deployment
    x-jsonld-type: '@id'
  FeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/FeatureOfInterest
    x-jsonld-type: '@id'
  Input:
    x-jsonld-id: http://www.w3.org/ns/sosa/Input
    x-jsonld-type: '@id'
  ObservableProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/ObservableProperty
    x-jsonld-type: '@id'
  Observation:
    x-jsonld-id: http://www.w3.org/ns/sosa/Observation
    x-jsonld-type: '@id'
  Output:
    x-jsonld-id: http://www.w3.org/ns/sosa/Output
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
  Result:
    x-jsonld-id: http://www.w3.org/ns/sosa/Result
    x-jsonld-type: '@id'
  Sample:
    x-jsonld-id: http://www.w3.org/ns/sosa/Sample
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
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasInput
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasOutput
    x-jsonld-type: '@id'
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasProperty
    x-jsonld-type: '@id'
  hasSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
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
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  madeSampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
    x-jsonld-type: '@id'
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  wasOriginatedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/wasOriginatedBy
    x-jsonld-type: '@id'
  inCondition:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/inCondition
    x-jsonld-type: '@id'
  Condition:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Condition
    x-jsonld-type: '@id'
  hasSystemCapability:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    x-jsonld-type: '@id'
  SystemCapability:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemCapability
    x-jsonld-type: '@id'
  hasSystemProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    x-jsonld-type: '@id'
  SystemProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemProperty
    x-jsonld-type: '@id'
  MeasurementRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/MeasurementRange
    x-jsonld-type: '@id'
  ActuationRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/ActuationRange
    x-jsonld-type: '@id'
  Accuracy:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/Accuracy
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
  hasOperatingRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    x-jsonld-type: '@id'
  OperatingRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingRange
    x-jsonld-type: '@id'
  hasOperatingProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    x-jsonld-type: '@id'
  OperatingProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingProperty
    x-jsonld-type: '@id'
  MaintenanceSchedule:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/MaintenanceSchedule
    x-jsonld-type: '@id'
  OperatingPowerRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/OperatingPowerRange
    x-jsonld-type: '@id'
  hasSurvivalRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    x-jsonld-type: '@id'
  SurvivalRange:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SurvivalRange
    x-jsonld-type: '@id'
  hasSurvivalProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    x-jsonld-type: '@id'
  SurvivalProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SurvivalProperty
    x-jsonld-type: '@id'
  SystemLifetime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/SystemLifetime
    x-jsonld-type: '@id'
  BatteryLifetime:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/BatteryLifetime
    x-jsonld-type: '@id'
  qualityOfObservation:
    x-jsonld-id: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    x-jsonld-type: '@id'
  properties: '@nest'
  featureType: '@type'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn-system: http://www.w3.org/ns/ssn/systems/
  ssn: http://www.w3.org/ns/ssn/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Fproperties%2Fobservation%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/schema.yaml" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/schema.json" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
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
    "id": "@id",
    "ActuatableProperty": {
      "@id": "sosa:ActuatableProperty",
      "@type": "@id"
    },
    "Actuation": {
      "@id": "sosa:Actuation",
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
    "FeatureOfInterest": {
      "@id": "sosa:FeatureOfInterest",
      "@type": "@id"
    },
    "Input": {
      "@id": "sosa:Input",
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
    "Output": {
      "@id": "sosa:Output",
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
    "Result": {
      "@id": "sosa:Result",
      "@type": "@id"
    },
    "Sample": {
      "@id": "sosa:Sample",
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
    "hasInput": {
      "@id": "sosa:hasInput",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "sosa:hasMember",
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
    "hasSample": {
      "@id": "sosa:hasSample",
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
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "wasOriginatedBy": {
      "@id": "sosa:wasOriginatedBy",
      "@type": "@id"
    },
    "inCondition": {
      "@id": "ssn-system:inCondition",
      "@type": "@id"
    },
    "Condition": {
      "@id": "ssn-system:Condition",
      "@type": "@id"
    },
    "hasSystemCapability": {
      "@id": "ssn-system:hasSystemCapability",
      "@type": "@id"
    },
    "SystemCapability": {
      "@id": "ssn-system:SystemCapability",
      "@type": "@id"
    },
    "hasSystemProperty": {
      "@id": "ssn-system:hasSystemProperty",
      "@type": "@id"
    },
    "SystemProperty": {
      "@id": "ssn-system:SystemProperty",
      "@type": "@id"
    },
    "MeasurementRange": {
      "@id": "ssn-system:MeasurementRange",
      "@type": "@id"
    },
    "ActuationRange": {
      "@id": "ssn-system:ActuationRange",
      "@type": "@id"
    },
    "Accuracy": {
      "@id": "ssn-system:Accuracy",
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
    "hasOperatingRange": {
      "@id": "ssn-system:hasOperatingRange",
      "@type": "@id"
    },
    "OperatingRange": {
      "@id": "ssn-system:OperatingRange",
      "@type": "@id"
    },
    "hasOperatingProperty": {
      "@id": "ssn-system:hasOperatingProperty",
      "@type": "@id"
    },
    "OperatingProperty": {
      "@id": "ssn-system:OperatingProperty",
      "@type": "@id"
    },
    "MaintenanceSchedule": {
      "@id": "ssn-system:MaintenanceSchedule",
      "@type": "@id"
    },
    "OperatingPowerRange": {
      "@id": "ssn-system:OperatingPowerRange",
      "@type": "@id"
    },
    "hasSurvivalRange": {
      "@id": "ssn-system:hasSurvivalRange",
      "@type": "@id"
    },
    "SurvivalRange": {
      "@id": "ssn-system:SurvivalRange",
      "@type": "@id"
    },
    "hasSurvivalProperty": {
      "@id": "ssn-system:hasSurvivalProperty",
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
    "BatteryLifetime": {
      "@id": "ssn-system:BatteryLifetime",
      "@type": "@id"
    },
    "qualityOfObservation": {
      "@id": "ssn-system:qualityOfObservation",
      "@type": "@id"
    },
    "properties": "@nest",
    "featureType": "@type",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fogcapi-sosa%2Fbuild%2Fannotated%2Funstable%2Fsosa%2Fproperties%2Fobservation%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/context.jsonld" target="_blank">https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/context.jsonld</a>

# Validation

## SHACL Shapes

The following sets of SHACL shapes are used for validating this building block:

* SOSA Observation <small><code>ogc.unstable.sosa.properties.observation</code></small>
  * [https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl](https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl)

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/properties/observation" target="_blank">_sources/properties/observation</a></code>

