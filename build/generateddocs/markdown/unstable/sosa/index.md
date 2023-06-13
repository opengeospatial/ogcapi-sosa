
# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

`ogc.unstable.sosa` *v1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

Building Blocks for implementing the core classes of the [Observations and Measurements model]

Each class is implemented using a schema is tied to the equivalent semantic description using the SOSA (Sensor, Observation, Sample, and Actuator) ontology.

An [aggregate schema](schema.yaml) is provided allowing any of these elements to be combined in a single payload, or each class may be used independently using the relevant schema.

TBD: Convenience API paths may be defined to support traversal of relationships - such as inverse relationships `hasResult`/`isResultOf` , `hasSample`/`isSampleOf` etc. where only one property is present in the data and the inverse is not otherwise accessible.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Sensor, Observation, Sample, and Actuator (SOSA)
anyOf:
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: properties/observation/schema.yaml
  - type: object
    properties:
      hasResult:
        properties:
          pose:
            $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-ypr/schema.yaml
          distance:
            type: number
            x-jsonld-id: http://example.com/properties/distance
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
    required:
    - hasResult
    not:
      required:
      - hasSimpleResult
  x-jsonld-extra-terms: {}
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: features/observation/schema.yaml
  - type: object
    properties:
      properties:
        $ref: examples/vectorObservation/schema.yaml
  x-jsonld-extra-terms: {}
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  type: object
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observation/schema.yaml
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    hosts: http://www.w3.org/ns/sosa/hosts
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    implements: http://www.w3.org/ns/ssn/implements
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    detects: http://www.w3.org/ns/ssn/detects
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  allOf:
  - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observationCollection/schema.yaml
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    hosts: http://www.w3.org/ns/sosa/hosts
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    implements: http://www.w3.org/ns/ssn/implements
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    detects: http://www.w3.org/ns/ssn/detects
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
- $schema: https://json-schema.org/draft/2020-12/schema
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
    hosts: http://www.w3.org/ns/sosa/hosts
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    implements: http://www.w3.org/ns/ssn/implements
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    detects: http://www.w3.org/ns/ssn/detects
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA ObservationCollection
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
    hasMember:
      type: array
      items:
        oneOf:
        - $ref: properties/observation/schema.yaml
        - type: string
      minItems: 1
      x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
  required:
  - hasMember
  not:
    anyOf:
    - required:
      - hasResult
    - required:
      - hasSimpleResult
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    hosts: http://www.w3.org/ns/sosa/hosts
    Observation: http://www.w3.org/ns/sosa/Observation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    implements: http://www.w3.org/ns/ssn/implements
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    detects: http://www.w3.org/ns/ssn/detects
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/schema.yaml)


# JSON-LD Context

```jsonld
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
    "hosts": "sosa:hosts",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "madeObservation": "sosa:madeObservation",
    "hasOutput": "ssn:hasOutput",
    "isSampleOf": "sosa:isSampleOf",
    "madeByActuator": "sosa:madeByActuator",
    "hasSubSystem": "ssn:hasSubSystem",
    "observes": "sosa:observes",
    "madeSampling": "sosa:madeSampling",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "inCondition": "ssn-system:inCondition",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeBySampler": "sosa:madeBySampler",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "implements": "ssn:implements",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "detects": "ssn:detects",
    "isObservedBy": "sosa:isObservedBy",
    "hasProperty": "ssn:hasProperty",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "deployedSystem": "ssn:deployedSystem",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSample": "sosa:hasSample",
    "isResultOf": "sosa:isResultOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "actsOnProperty": "sosa:actsOnProperty",
    "Sample": "sosa:Sample",
    "inDeployment": "ssn:inDeployment",
    "forProperty": "ssn:forProperty",
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "ssn:isProxyFor",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasInput": "ssn:hasInput",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "geopose:position",
    "angles": "geopose:angles",
    "yaw": "geopose:yaw",
    "pitch": "geopose:pitch",
    "roll": "geopose:roll",
    "lat": "geopose:lat",
    "lon": "geopose:lon",
    "h": "geopose:h",
    "latitude": "geo:lat",
    "rotations": "geopose:rotations",
    "height": "geopose:height",
    "longitude": "geo:long",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": "geojson:coordinates"
      },
      "@id": "geojson:geometry"
    },
    "bbox": "geojson:bbox",
    "Feature": "geojson:Feature",
    "MultiPoint": "geojson:MultiPoint",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPolygon": "geojson:MultiPolygon",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "Polygon": "geojson:Polygon",
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "links": "rdfs:seeAlso"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/build/annotated/unstable/sosa/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources`

