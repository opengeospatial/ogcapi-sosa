
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
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: features/observation/schema.yaml
  - type: object
    properties:
      properties:
        $ref: examples/vectorObservation/schema.yaml
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
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hosts: http://www.w3.org/ns/sosa/hosts
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    implements: http://www.w3.org/ns/ssn/implements
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
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
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hosts: http://www.w3.org/ns/sosa/hosts
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    implements: http://www.w3.org/ns/ssn/implements
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
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
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hosts: http://www.w3.org/ns/sosa/hosts
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    implements: http://www.w3.org/ns/ssn/implements
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
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
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hosts: http://www.w3.org/ns/sosa/hosts
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    implements: http://www.w3.org/ns/ssn/implements
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation

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
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "forProperty": "ssn:forProperty",
    "madeObservation": "sosa:madeObservation",
    "isPropertyOf": "ssn:isPropertyOf",
    "inDeployment": "ssn:inDeployment",
    "hasSubSystem": "ssn:hasSubSystem",
    "hosts": "sosa:hosts",
    "inCondition": "ssn-system:inCondition",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOutput": "ssn:hasOutput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isActedOnBy": "sosa:isActedOnBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "isResultOf": "sosa:isResultOf",
    "isProxyFor": "ssn:isProxyFor",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isObservedBy": "sosa:isObservedBy",
    "hasSample": "sosa:hasSample",
    "isSampleOf": "sosa:isSampleOf",
    "hasInput": "ssn:hasInput",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeSampling": "sosa:madeSampling",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "madeActuation": "sosa:madeActuation",
    "implements": "ssn:implements",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeByActuator": "sosa:madeByActuator",
    "madeBySampler": "sosa:madeBySampler",
    "hasProperty": "ssn:hasProperty",
    "detects": "ssn:detects",
    "Observation": "sosa:Observation",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
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
    "rotations": "geopose:rotations",
    "latitude": "geo:lat",
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
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "Feature": "geojson:Feature",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
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

