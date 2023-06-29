
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
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    detects: http://www.w3.org/ns/ssn/detects
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSample: http://www.w3.org/ns/sosa/hasSample
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
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
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    detects: http://www.w3.org/ns/ssn/detects
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasResult: http://www.w3.org/ns/sosa/hasResult
    Observation: http://www.w3.org/ns/sosa/Observation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hosts: http://www.w3.org/ns/sosa/hosts
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    observes: http://www.w3.org/ns/sosa/observes
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSample: http://www.w3.org/ns/sosa/hasSample
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
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
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
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
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
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

