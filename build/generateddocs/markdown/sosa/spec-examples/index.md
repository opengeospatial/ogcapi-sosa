
# Tests for SOSA specification (Schema)

`ogc.sosa.spec-examples` *v1.0*

This BuildingBlock adds test cases from the SOSA specification to the base Observation properties model

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SOSA Specification Examples

This building block runs tests against the SOSA specification examples.

As TTL files these examples are validated against the SHACL rules inherited from the building blocks for elements of the specification

## Examples

### Example forecast.jsonld
Example included in the SOSA/SSN specification section(s): [ModelTimes](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [forecast.jsonld](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/forecast.jsonld)
#### jsonld
```jsonld
{
  "@graph" : [ {
    "@id" : "_:b0",
    "hasBeginnning" : "_:b2",
    "hasEnd" : "_:b1"
  }, {
    "@id" : "_:b1",
    "inXSDDateTime" : "2024-03-09T12:00:00+10:00"
  }, {
    "@id" : "_:b2",
    "inXSDDateTime" : "2024-03-09T11:00:00+10:00"
  }, {
    "@id" : "ex:EarthAtmosphere",
    "@type" : "sosa:FeatureOfInterest",
    "sameAs" : "https://www.wikidata.org/wiki/Q3230"
  }, {
    "@id" : "ex:Observation299876",
    "@type" : "sosa:Observation",
    "hasFeatureOfInterest" : "ex:EarthAtmosphere",
    "hasResult" : "ex:forecast/grid/299876",
    "observedProperty" : "https://si-digital-framework.org/quantities/TEMC",
    "phenomenonTime" : "_:b0",
    "resultTime" : "2024-03-06T12:00:00+10:00"
  }, {
    "@id" : "ex:forecast/",
    "@type" : "owl:Ontology"
  } ],
  "@context" : {
    "resultTime" : {
      "@id" : "http://www.w3.org/ns/sosa/resultTime",
      "@type" : "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "phenomenonTime" : {
      "@id" : "http://www.w3.org/ns/sosa/phenomenonTime",
      "@type" : "@id"
    },
    "observedProperty" : {
      "@id" : "http://www.w3.org/ns/sosa/observedProperty",
      "@type" : "@id"
    },
    "hasResult" : {
      "@id" : "http://www.w3.org/ns/sosa/hasResult",
      "@type" : "@id"
    },
    "hasFeatureOfInterest" : {
      "@id" : "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type" : "@id"
    },
    "hasEnd" : {
      "@id" : "http://www.w3.org/2006/time#hasEnd",
      "@type" : "@id"
    },
    "hasBeginnning" : {
      "@id" : "http://www.w3.org/2006/time#hasBeginnning",
      "@type" : "@id"
    },
    "inXSDDateTime" : {
      "@id" : "http://www.w3.org/2006/time#inXSDDateTime",
      "@type" : "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "sameAs" : {
      "@id" : "http://www.w3.org/2002/07/owl#sameAs",
      "@type" : "@id"
    },
    "ex" : "http://example.org/data/",
    "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "owl" : "http://www.w3.org/2002/07/owl#",
    "xsd" : "http://www.w3.org/2001/XMLSchema#",
    "rdfs" : "http://www.w3.org/2000/01/rdf-schema#",
    "time" : "http://www.w3.org/2006/time#",
    "sosa" : "http://www.w3.org/ns/sosa/"
  }
}

```

#### ttl
```ttl
@prefix ex: <http://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Observation299876 a sosa:Observation ;
    sosa:hasFeatureOfInterest ex:EarthAtmosphere ;
    sosa:hasResult <http://example.org/data/forecast/grid/299876> ;
    sosa:observedProperty <https://si-digital-framework.org/quantities/TEMC> ;
    sosa:phenomenonTime [ time:hasBeginnning [ time:inXSDDateTime "2024-03-09T11:00:00+10:00"^^xsd:dateTime ] ;
            time:hasEnd [ time:inXSDDateTime "2024-03-09T12:00:00+10:00"^^xsd:dateTime ] ] ;
    sosa:resultTime "2024-03-06T12:00:00+10:00"^^xsd:dateTime .

<http://example.org/data/forecast/> a owl:Ontology .

ex:EarthAtmosphere a sosa:FeatureOfInterest ;
    owl:sameAs <https://www.wikidata.org/wiki/Q3230> .


```


### Example Temperature-of-interest-specialization.ttl
Example included in the SOSA/SSN specification section(s): [ModelPropertyDefinition](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [Temperature-of-interest-specialization.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/Temperature-of-interest-specialization.ttl)
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix saref: <https://saref.etsi.org/core/> .

qk:Temperature
  a saref:Property ;
.
ex:SickChildA
  a saref:FeatureOfInterest ;
.
ex:SickChildATemperature
  a saref:PropertyOfInterest ;
  saref:hasPropertyKind qk:Temperature ;
  saref:isPropertyOfInterestOf ex:SickChildA ;
.
```


### Example IBS-TH2-PLUS-brief.ttl
Example included in the SOSA/SSN specification section(s): [ModelComplexSystem](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [IBS-TH2-PLUS-brief.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/IBS-TH2-PLUS-brief.ttl)
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sensor: <https://example.org/sensor/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@base <https://example.org/data/TH2-PLUS-b/> .

sensor:IBS-TH2-Plus a owl:Class ;
  rdfs:subClassOf sosa:System ;
  prov:wasDerivedFrom <https://inkbird.com/products/ibs-th2-plus> ;
  rdfs:label "IBS-TH2 PLUS Temperature and Humidity Sensor System" ;
.
sensor:IBS-TH2-Plus-H a owl:Class ;
  rdfs:subClassOf sosa:Sensor ;
  rdfs:label "IBS-TH2 PLUS Humidity Sensor type" ;
.
sensor:IBS-TH2-Plus-T a owl:Class ;
  rdfs:subClassOf sosa:Sensor ;
  rdfs:label "IBS-TH2 PLUS Temperature Sensor type" ;
.
ex:12gth456a-23190 a sensor:IBS-TH2-Plus ; 
  sosa:hasSubSystem ex:12gth456a-23190-H ;
  sosa:hasSubSystem ex:12gth456a-23190-T ;
. 
ex:12gth456a-23190-H a sensor:IBS-TH2-Plus-H ; 
  sosa:observes qk:RelativeHumidity ;
. 
ex:12gth456a-23190-T a sensor:IBS-TH2-Plus-T ; 
  sosa:observes qk:Temperature ;
. 

```


### Example IBS-TH2-PLUS.ttl
Example included in the SOSA/SSN specification section(s): [ModelSystemType](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [IBS-TH2-PLUS.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/IBS-TH2-PLUS.ttl)
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sensor: <https://example.org/sensor/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix sosa-cap: <http://www.w3.org/ns/sosa/system-capability-properties#> .
@base <https://example.org/data/TH2-PLUS/> .

sensor:IBS-TH2-Plus
  a owl:Class ;
  rdfs:label "IBS-TH2 PLUS Temperature and Humidity Sensor System" ;
  rdfs:subClassOf sosa:System ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:hasValue sensor:IBS-TH2-Plus-systemCapability ;
      owl:onProperty sosa:hasSystemCapability ;
    ] ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:onProperty sosa:hasSubSystem ;
      owl:someValuesFrom sensor:IBS-TH2-Plus-H ;
    ] ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:onProperty sosa:hasSubSystem ;
      owl:someValuesFrom sensor:IBS-TH2-Plus-T ;
    ] ;
  prov:wasDerivedFrom <https://inkbird.com/products/ibs-th2-plus> ;
.
sensor:IBS-TH2-Plus-systemCapability a sosa:ObservationCollection ;
  qudt:hasUnit unit:HZ ;
  sosa:hasMember [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MaxFrequency ;
      sosa:hasSimpleResult 0.1 ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MinFrequency ;
      sosa:hasSimpleResult ".0005556"^^xsd:decimal ;
  ]
.
sensor:IBS-TH2-Plus-H
  a owl:Class ;
  rdfs:label "IBS-TH2 PLUS Humidity Sensor type" ;
  rdfs:subClassOf sosa:Sensor ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:hasValue qk:RelativeHumidity ;
      owl:onProperty sosa:observes ;
    ] ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:hasValue sensor:IBS-TH2-Plus-H-systemCapability ;
      owl:onProperty sosa:hasSystemCapability ;
    ] ;
.
sensor:IBS-TH2-Plus-T
  a owl:Class ;
  rdfs:label "IBS-TH2 PLUS Temperature Sensor type" ;
  rdfs:subClassOf sosa:Sensor ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:hasValue qk:Temperature ;
      owl:onProperty sosa:observes ;
    ] ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:hasValue sensor:IBS-TH2-Plus-T-systemCapability ;
      owl:onProperty sosa:hasSystemCapability ;
    ] ;
.
sensor:IBS-TH2-Plus-H-systemCapability a sosa:ObservationCollection ;
  qudt:hasUnit unit:PERCENT ;
  sosa:hasMember [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:HumidityAccuracy ;
      sosa:hasSimpleResult 4.5 ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MaxMeasurableHumidity ;
      sosa:hasSimpleResult 99.0 ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MinMeasurableHumidity ;
      sosa:hasSimpleResult 0.0 ;
  ]
.
sensor:IBS-TH2-Plus-T-systemCapability a sosa:ObservationCollection ;
  qudt:hasUnit unit:DEG_C ;
  sosa:hasMember [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:TemperatureAccuracy ;
      sosa:hasSimpleResult 0.5 ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MaxMeasurableTemperature ;
      sosa:hasSimpleResult 60.0 ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MinMeasurableTemperature ;
      sosa:hasSimpleResult -40.0 ;
  ]
.


```


### Example InkBird-IBS-TH2-properties.ttl
Example included in the SOSA/SSN specification section(s): [System-capabilities](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [InkBird-IBS-TH2-properties.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/InkBird-IBS-TH2-properties.ttl)
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix sosa-env: <http://www.w3.org/ns/sosa/system-environment-properties#> .

ex:IBSTH2HumidityAccuracy a sosa:Property ;
    rdfs:label "Humidity Accuracy (25°C/77°C, 20%~80%RH)"@en ;
    sosa:hasValidityContext [ 
      a sosa:ObservationCollection ;
      sosa:hasMember [
        sosa:observedProperty sosa-env:AmbientTemperature ;
        sosa:hasResult [ 
          qudt:value 25.0 ;
          qudt:hasUnit unit:DEG_C ;
        ] ;
      ] , [
        sosa:observedProperty sosa-env:MinAmbientRelativeHumidity ;
        sosa:hasResult [ 
          qudt:value 20.0 ;
          qudt:hasUnit unit:PERCENT ;
        ] ;
      ] , [
        sosa:observedProperty sosa-env:MaxAmbientRelativeHumidity ;
        sosa:hasResult [ 
          qudt:value 80.0 ;
          qudt:hasUnit unit:PERCENT ;
        ] ;
      ]
    ]
.

```


### Example i-adopt.ttl
Example included in the SOSA/SSN specification section(s): [System-capabilities](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [i-adopt.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/i-adopt.ttl)
#### ttl
```ttl
@prefix ex:   <http://example.org/>.
@prefix sosa: <https://www.w3.org/TR/vocab-ssn/>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#>.
@prefix qudt: <http://qudt.org/schema/qudt/>.
@prefix unit: <http://qudt.org/vocab/unit/>.
@prefix iop:  <https://w3id.org/iadopt/ont/>.
@prefix uom: <http://www.ontology-of-units-of-measure.org/resource/om-2/>.
@prefix qk: <http://qudt.org/vocab/quantitykind/>.
@prefix et: <http://vocabs.lter-europe.net/EnvThes/>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.


ex:SensorCapabilityObservation a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:Sensor ;
  sosa:observedProperty ex:SensorMinimumLimit;
  sosa:hasResult [ 
    qudt:value -40.0 ;
    qudt:hasUnit unit:DEG_C ;
  ] ;
.
ex:SensorMinimumLimit a iop:Variable, sosa:Property;
  iop:hasStatisticalModifier uom:minimum ;
  iop:hasObjectOfInterest et:23 ;
  iop:hasProperty qk:ThermodynamicTemperature ;
.
qk:ThermodynamicTemperature
    a iop:Property ;
    rdfs:label "thermodynamic temperature" 
.		
et:23
    a iop:Entity ;
    rdfs:label "air" 
.
uom:minimum
    a iop:StatisticalModifier ;
    rdfs:label "minimum" 
.
```


### Example dqv.ttl
Example included in the SOSA/SSN specification section(s): [System-capabilities](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [dqv.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/dqv.ttl)
#### ttl
```ttl
@prefix ex:   <http://example.org/>.
@prefix sosa: <https://www.w3.org/TR/vocab-ssn/>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#>.
@prefix qudt: <http://qudt.org/schema/qudt/>.
@prefix unit: <http://qudt.org/vocab/unit/>.
@prefix sosa-cap: <http://www.w3.org/ns/sosa/system-capability-properties#> .
@prefix sosa-env: <http://www.w3.org/ns/sosa/system-environment-properties#> .

ex:observation_233 a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:TheAir;
  sosa:observedProperty sosa-env:AmbientTemperature;
  sosa:madeBySensor ex:TemperatureSensor ;
  sosa:resultQuality ex:observation_233_MeasurementAccuracy ;
  sosa:hasResult [ 
    qudt:value 21.4 ;
    qudt:hasUnit unit:DEG_C ;
  ] ;
.
   
ex:observation_233_MeasurementAccuracy a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:observation_233 ;
  sosa:observedProperty sosa-cap:TemperatureAccuracy ;
  sosa:hasResult [ 
    qudt:value 1.5 ;
    qudt:hasUnit unit:DEG_C ;
  ] ;
.

```


### Example InkBird-IBS-TH2-Range.ttl
Example referenced from the SOSA/SSN specification section(s): [System-capabilities](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [InkBird-IBS-TH2-Range.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/InkBird-IBS-TH2-Range.ttl)
#### ttl
```ttl
@prefix equipment: <https://rdf.ag/o/equipment/> .
@prefix ex: <https://example.org/data/> .
@prefix gs1: <https://gs1.org/voc/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix sosa-env: <http://www.w3.org/ns/sosa/system-environment-properties#> .
@base <https://rdf.ag/o/equipment/> .

# This example is a partial specification for a common over-the-shelf temperature and humidity sensor.  Different instantions can
# be derived for each specific physical the product. 

ex:InkBird-IBS-TH2 a owl:Class;
    rdfs:label "Inkbird IBS-TH2"@en ;
    rdfs:subClassOf gs1:Product, sosa:Platform, equipment:Equipment, <https://w3id.org/seas/BluetoothCommunicationDevice>;
    gs1:pip <https://inkbird.com/products/hygrometer-ibs-th2> ;
    rdfs:subClassOf [ a owl:Restriction ;
                      owl:onProperty sosa:hosts ;
                      owl:allValuesFrom ex:IBSTH2TemperatureSensor 
                    ] ;
.
ex:IBSTH2TemperatureSensor rdfs:subClassOf sosa:Sensor ;
    rdfs:label "Inkbird IBS-TH2 built-in Temperature Sensor"@en ;
    sosa:observes ex:airTemperature ;
    rdfs:subClassOf [ a owl:Restriction ;
                      owl:onProperty sosa:hasOperatingConditions ;
                      owl:allValuesFrom ex:IBSTH2TemperatureSensorLimits 
                    ] ;
    rdfs:subClassOf [ a owl:Restriction ;
                      owl:onProperty sosa:hasOperatingConditions ;
                      owl:allValuesFrom ex:IBSTH2SurvivalRange 
                    ] ;
.
ex:IBSTH2TemperatureSensorLimits a sosa:ObservationCollection , sosa:NormalOperatingConditions ;
    rdfs:label "Inkbird IBS-TH2 Temperature Sensor Limits"@en ;
    sosa:hasMember [
      sosa:observedProperty sosa-env:MinAmbientTemperature ;
      sosa:hasResult [ 
        qudt:value -40.0 ;
        qudt:hasUnit unit:DEG_C ;
      ] ;
    ] , [
      sosa:observedProperty sosa-env:MaxAmbientTemperature ;
      sosa:hasResult [ 
        qudt:value 60.0 ;
        qudt:hasUnit unit:DEG_C ;
      ] ;
    ]
.
# Physical limits of the sensor (and platform) where structural failure occurs.
ex:IBSTH2SurvivalRange a sosa:ObservationCollection , sosa:SurvivableConditions ;
    rdfs:label "Inkbird IBS-TH2 Failiure limits"@en ;
    sosa:hasMember [
      sosa:observedProperty sosa-env:MinAmbientTemperature ;
      sosa:hasResult [ 
        qudt:value -273.0 ;
        qudt:hasUnit unit:DEG_C ;
      ] ;
    ] , [
      sosa:observedProperty sosa-env:MaxAmbientTemperature ;
      sosa:hasResult [ 
        qudt:value 80.0 ;
        qudt:hasUnit unit:DEG_C ;
      ] ;
    ]
.
```


### Example IDEAS.ttl
Example referenced from the SOSA/SSN specification section(s): [CompleteExamples](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [IDEAS.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/IDEAS.ttl)
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#>.
@prefix sosa: <http://www.w3.org/ns/sosa#> .
@prefix unit: <http://qudt.org/vocab/unit/>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/IDEA/> .

# Temperature and Humidity at Coal Oil Point Reserve

 ex:COPR a sosa:FeatureOfInterest ;
   sosa:hasSample ex:COPR_SL ;
   rdfs:comment "Coal Oil Point Reserve: UC Santa Barbara Natural Reserve System"@en ;
   rdfs:label "Coal Oil Point Reserve"@en ;
.
ex:COPR_SL a sosa:Sample ;
   rdfs:label "Air around COPR Station"@en ;
   sosa:isSampleOf ex:COPR ;
.
ex:COPR_Station a sosa:Platform ;
   rdfs:comment "Station at Coal Oil Point Reserve, CA (see http://www.geog.ucsb.edu/ideas/COPR.html for details)"@en ;
   rdfs:label "Coal Oil Point Reserve Wx Station"@en ;
   rdfs:seeAlso <http://www.geog.ucsb.edu/ideas/COPR.html> ;
   sosa:hosts ex:COPR-HMP45C-L ;
.
ex:COPR-HMP45C-L a sosa:Platform ;
   rdfs:label "HMP45C-L Temperature and Relative Humidity Probe at Coal Oil Point, UCSB, CA"@en ;
   sosa:hosts ex:HUMICAP-H ;
   sosa:isHostedBy ex:COPR_Station ;
.
ex:HUMICAP-H a sosa:Sensor ;
   rdfs:label "Vaisala HUMICAP H-chip"@en ;
   sosa:observes ex:RelativeHumidity ;
   sosa:isHostedBy ex:COPR-HMP45C-L ;
.
ex:RelativeHumidity a sosa:Property ;
   rdfs:comment "Humidity is a measure of the moisture content of air."@en ;
   rdfs:label "Relative Humidity"@en ;
   skos:exactMatch qk:RelativeHumidity ;
.
ex:MeasuringRelativeHumidity a sosa:ObservingProcedure ;
   rdfs:comment "Instructions for measuring relative humidity"@en ;
   rdfs:comment "Relative humidity as averaged over 15min."@en ;
.
ex:RH_avg_1_COPR_15min_201706020300PM a sosa:Observation ;
   rdfs:label "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"@en ;
   sosa:madeBySensor ex:HUMICAP-H ;
   sosa:hasFeatureOfInterest ex:COPR_SL ;
   sosa:hasResult [
      a qudt:QuantityValue ;
      qudt:hasUnit unit:PERCENT ;
      qudt:value 92.5 ;
   ] ;
   sosa:resultTime "2017-06-02T15:00:00-07:00"^^xsd:dateTime ;
   sosa:observedProperty ex:RelativeHumidity ;
   sosa:usedProcedure ex:MeasuringRelativeHumidity ;
.
```


### Example Temperature-i-adopt.ttl
Example referenced from the SOSA/SSN specification section(s): [CompleteExamples](https://w3c.github.io/sdw-sosa-ssn/ssn/). Source: [Temperature-i-adopt.ttl](https://w3c.github.io/sdw-sosa-ssn/ssn/rdf/examples/Temperature-i-adopt.ttl)
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix iop: <https://w3id.org/iadopt/ont/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

ex:SickChildTemperature
    a iop:Variable, sosa:Property;
    rdfs:label "Temperature of sick child" ;
    rdfs:comment """Temperature of the body of a sick child""" ;
    iop:hasObjectOfInterest <http://hadatac.org/ont/chear#Child> ;
    iop:hasProperty qk:Temperature ;
    iop:hasConstraint 
        [ a iop:Constraint, <http://semanticscience.org/resource/SIO_000954> ;
             rdfs:label "state: sick" ;
             iop:constrains <http://hadatac.org/ont/chear#Child> ;
        ] 
.
<http://hadatac.org/ont/chear#Child>
    a iop:Entity ;
    rdfs:label "child" 
.
qk:Temperature a iop:Property ;
    rdfs:label "temperature" 
.

```

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/rob-metalinkage/ogcapi-sosa](https://github.com/rob-metalinkage/ogcapi-sosa)
* Path: `_sources/spec-examples`

