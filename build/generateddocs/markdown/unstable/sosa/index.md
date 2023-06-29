
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
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSample: http://www.w3.org/ns/sosa/hasSample
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
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
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    implements: http://www.w3.org/ns/ssn/implements
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    observes: http://www.w3.org/ns/sosa/observes
    detects: http://www.w3.org/ns/ssn/detects
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
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
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSample: http://www.w3.org/ns/sosa/hasSample
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
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
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    Observation: http://www.w3.org/ns/sosa/Observation
    Sample: http://www.w3.org/ns/sosa/Sample
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    implements: http://www.w3.org/ns/ssn/implements
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    observes: http://www.w3.org/ns/sosa/observes
    detects: http://www.w3.org/ns/ssn/detects
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
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
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput

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
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "isResultOf": "sosa:isResultOf",
    "hasDeployment": "ssn:hasDeployment",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput",
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
    "height": "geopose:height",
    "latitude": "geo:lat",
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
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "features": "geojson:features",
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

