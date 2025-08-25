
# Tests for SOSA specification (Schema)

`ogc.sosa.properties.spec-examples` *v1.0*

This BuildingBlock adds test cases from the SOSA specification to the base Observation properties model

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SOSA Specification Examples

This building block runs tests against the SOSA specification examples.

As TTL files these examples are validated against the SHACL rules inherited from the building blocks for elements of the specification

## Examples

### Example apartment-134.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <https://example.org/data/apt134/> .

# Electricity consumption of apartment #134

# The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later

ex:Observation_235714 rdf:type sosa:Observation ;
  sosa:observedProperty  ex:Apartment_134_electricConsumption ;
  sosa:madeBySensor ex:sensor_926 ; 
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:value "22.4"^^xsd:decimal ;
     qudt:hasUnit unit:KiloW-HR ] ;
  sosa:phenomenonTime [
    time:hasBeginning [ 
      time:inXSDDateTimeStamp "2017-04-15T23:59:30+00:00"^^xsd:dateTime ] ;
    time:hasEnd [ 
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTime ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTime ;
.
# Sensor #926 observes the electric consumption of apartment #134, and we know that 
# it made some observations

ex:sensor_926 rdf:type sosa:Sensor ;
  sosa:observes  ex:Apartment_134_electricConsumption ;
  sosa:madeObservation ex:Observation_235714, ex:Observation_235715, ex:Observation_235716 ;
.
# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. 

ex:tempSensor_23 rdf:type sosa:Sensor ;
  sosa:observes  ex:tempSensor_23_temperature ;
  sosa:madeObservation ex:tempSensor_23_4572, ex:tempSensor_23_4573, ex:tempSensor_23_4574 ;
.
# Sensor #926 observes the electric consumption of apartment #134

ex:sensor_926 rdf:type sosa:Sensor ;
  sosa:observes  ex:Apartment_134_electricConsumption ;
.
# This is equivalent to saying that the electric consumption of apartment #134 is 
# observed by Sensor #926

ex:Apartment_134_electricConsumption rdf:type sosa:Property ;
  sosa:isObservedBy ex:sensor_926  ;
.
# This is equivalent to saying that these observations have been made by sensor #926

ex:Observation_235714 rdf:type sosa:Observation ;
  sosa:madeBySensor ex:sensor_926 ;
.
ex:Observation_235754 rdf:type sosa:Observation ;
  sosa:madeBySensor ex:sensor_926 ;
.
# Actuation
# the window opening state is a Property
# SSN allows to explicitly say that ex:window_104#state is a property of ex:window

ex:window rdf:type sosa:FeatureOfInterest ;
  sosa:hasProperty ex:window_104_state ;
.
ex:window_104_state rdf:type sosa:Property ;
  sosa:wasActedOnBy ex:actuation_188 ;
.
# WindowCloser #987 made actuation #188
# SSN allows to explicitly say that ex:windowCloser_987 is designed to automatically open and close window #104

ex:windowCloser_987 rdf:type sosa:Actuator ;
  sosa:madeActuation ex:actuation_188 ;
  sosa:actsOn ex:window_104_state ;
.
# Actuation #188 acted on the state of window #104 and returned 'true'

ex:actuation_188 rdf:type sosa:Actuation ;
  sosa:actsOnProperty ex:window_104_state ;
  sosa:madeByActuator ex:windowCloser_987 ; 
  sosa:hasSimpleResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTime ;
.  
```


### Example dht22-deployment.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfp: <https://w3id.org/rdfp/>.
@base <https://example.org/data/dht22d/> .

#     This example shows how the conditions (temperature and humidity) in a room can be measured using one or
#     more sensors.
#     Each sensor observes the conditions in its immediate vicinity, and the values are then used to characterize
#     the room. 
#
# In Room 145, one of the walls is external in the building, so there is expected to be a temperature gradient
#     across the room, and there are two sensors on different walls.
#     In Room 245, there is one sensor on the south wall.
#     Each of these locations corresponds to a sosa:Sample of the entire room.
#     The wall also serves as a sosa:Platform on which the sensors are mounted. 


ex:Room145 a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample ex:Room145_east ;
  sosa:hasSample ex:Room145_south ;
.
ex:Room145_east a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
  rdfs:label "East wall of room #145."@en ;
  rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
  sosa:hosts ex:PCBBoard1 ;
.
ex:Room145_south a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
  rdfs:label "South wall of room #145."@en ;
  rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
  sosa:hosts ex:PCBBoard2 ;
.
ex:Room245 a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty qk:Temperature , qk:RelativeHumidity ;
  sosa:hasSample ex:Room245_south ;
.
ex:Room245_south a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
  rdfs:label "South wall of room #245."@en ;
  sosa:hosts ex:PCBBoard3 ;
.
ex:PCBBoard1 a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts ex:DHT22_4578 ;
  sosa:hasSubSystem ex:DHT22_4578 ;
.
ex:DHT22_4578 a sosa:System ;
  rdfs:label "DHT22 sensor #4578"@en ;
  sosa:isHostedBy ex:PCBBoard1 ;
.
ex:PCBBoard2 a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts ex:DHT22_4578 ;
  sosa:hasSubSystem ex:DHT22_4578 ;
.
ex:DHT22_4579 a sosa:System ;
  rdfs:label "DHT22 sensor #4579."@en ;
  sosa:isHostedBy ex:PCBBoard2 ;
.
ex:PCBBoard3 a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts ex:DHT22_4578 ;
  sosa:hasSubSystem ex:DHT22_4578 ;
.
ex:DHT22_4580 a sosa:System ;
  rdfs:label "DHT22 sensor #4580."@en ;
  sosa:isHostedBy ex:PCBBoard3 ;
.
ex:Room245Deployment a sosa:Deployment ;
  rdfs:comment "Deployment of PCB Board 3 on the south wall of room #245 for the purpose of observing the temperature and humidity of room #245."@en ;
  sosa:deployedOnPlatform ex:Room245_south ;
  sosa:deployedSystem ex:PCBBoard3 ;
  sosa:forProperty qk:Temperature , qk:RelativeHumidity ;
.
ex:Room145Deployment a sosa:Deployment ;
  rdfs:comment "Deployment of PCB Board 1 and 2 on the east and south wall of room #145, respectively, for the purpose of observing the temperature and humidity of room #145."@en ;
  sosa:deployedOnPlatform ex:Room245_east , ex:Room245_south ;
  sosa:deployedSystem ex:PCBBoard1 , ex:PCBBoard2 ;
  sosa:forProperty qk:Temperature , qk:RelativeHumidity ;
.
```


### Example dht22.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix et: <http://vocabs.lter-europe.net/EnvThes/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix iop: <https://w3id.org/iadopt/ont/1.1.0> .
@prefix uom: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix schema: <http://schema.org/>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfp: <https://w3id.org/rdfp/>.
@base <https://example.org/data/dht22/> .

# Complex sensor capabilities -- DHT22

ex:DHT22_Procedure a sosa:ObservingProcedure ;
  sosa:hasOutput ex:DHT22_output ;
.

ex:DHT22_output a rdfp:GraphDescription ;
  rdfs:comment "The output is a RDF Graph that describes both the temperature and the humidity. It can be validated by a SHACL shapes graph."@en ;
  rdfp:presentedBy [
    a rdfp:GraphDescription ;
    rdfp:validationRule ex:shacl_shapes_graph ;
  ] ;
.

# System objects; a DHT22 sensor instance, serial number 4578
ex:DHT22_4578 a sosa:System ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> ;
  sosa:hasSubSystem ex:DHT22_4578_TemperatureSensor,ex:DHT22_4578_HumiditySensor ;
  sosa:hasOperatingConditions ex:DHT22_4578_TemperatureSensorNormalOperatingConditions, ex:DHT22_4578_HumiditySensorNormalOperatingConditions ;
  ex:serialNumber "4578" ;
.

ex:DHT22_4578_TemperatureSensor a sosa:Sensor , sosa:System ;
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en ;
  sosa:hasSystemCapability ex:DHT22_4578_TemperatureSensorCapabilities ;
  sosa:hasOperatingConditions ex:DHT22_4578_TemperatureSensorNormalOperatingConditions ;
  sosa:implements ex:DHT22_Procedure ;
.

ex:DHT22_4578_HumiditySensor a sosa:Sensor , sosa:System ;
  rdfs:comment "The embedded humidity sensor, a specific instance of humidity sensor."@en ;
  sosa:hasSystemCapability ex:DHT22_4578_HumiditySensorCapabilities ;
  sosa:hasOperatingConditions ex:DHT22_4578_HumiditySensorNormalOperatingConditions;
  sosa:implements ex:DHT22_Procedure ;
.

# These are operating conditions under which the sensor can properly function. These are seperate from capabilites in that not
# all of the condition observations may be sensed by the sensor itself, e.g., supply voltage. 

ex:DHT22_4578_HumiditySensorNormalOperatingConditions a sosa:ObservationCollection ;
 rdf:type sosa:NormalOperatingConditions ;
 rdfs:comment "The conditions in which the DHT22 system is expected to operate."@en ;
 sosa:hasMember ex:minimumOperatingTemperature, ex:maximumOperatingTemperature, ex:minimumOperatingHumidity, ex:maximumOperatingHumidity, ex:mimimalOperatingInputVoltage, ex:maximumOperatingInputVoltage, ex:nominalOperatingInputVoltage .

ex:DHT22_4578_TemperatureSensorNormalOperatingConditions a sosa:ObservationCollection ;
 rdf:type sosa:NormalOperatingConditions ;
 rdfs:comment "The conditions in which the DHT22 system is expected to operate."@en ;
 sosa:hasMember ex:minimumOperatingTemperature, ex:maximumOperatingTemperature, ex:mimimalOperatingInputVoltage, ex:maximumOperatingInputVoltage, ex:nominalOperatingInputVoltage .

# The minimum / maxinum operating temperatures in this case are the temperature of the System itself
# as heat transfer from the mechanical mounting will directly impact the sensor rather than the
# ambient air. 

ex:minimumOperatingTemperature a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578 ;
 sosa:observedProperty ex:minimumSensorTemperatureLimit ;
 sosa:hasSimpleResult "-40.0"^^xsd:decimal ;
 qudt:hasUnit unit:DEG_C .

ex:minimumSensorTemperatureLimit a iop:Variable, sosa:Property;
 iop:hasStatisticalModifier uom:minimum ;
 iop:hasObjectOfInterest ex:DHT22_4578;
 iop:hasProperty qk:Temperature .

ex:maximumOperatingTemperature a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578 ;
 sosa:observedProperty ex:maximumSensorTemperatureLimit ;
 sosa:hasResult [
   qudt:value 80.0 ;
   qudt:hasUnit unit:DEG_C ] .

ex:maximumSensorTemperatureLimit a iop:Variable, sosa:Property;
 iop:hasStatisticalModifier uom:maximum ;
 iop:hasObjectOfInterest ex:DHT22_4578 ;
 iop:hasProperty qk:Temperature .

# Unlike temperature, the operating condition of the System are affected by the relative humidity of the air around the sensor. 
# Percentage is not a unit, however this is present in QUDT and used here as a convinience for display purposes.


ex:minimumOperatingHumidity a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578;
 sosa:observedProperty ex:minSensorEnvironmentHumidityLimit ;
 sosa:hasResult [
   qudt:value 0.0 ;
   qudt:hasUnit unit:PERCENT ] .

ex:minSensorEnvironmentHumidityLimit a iop:Variable, sosa:Property;
 iop:hasStatisticalModifier uom:minimum ;
 iop:hasObjectOfInterest ex:airAround_DHT22_4578;
 iop:hasProperty qk:RelativeHumidity .

ex:maximumOperatingHumidity a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578 ;
 sosa:observedProperty ex:maxSensorEnvironmentHumidityLimit ; 
 sosa:hasResult [
   qudt:value 100.0 ;
   qudt:hasUnit unit:PERCENT ] .

ex:maxSensorEnvironmentHumidityLimit a iop:Variable, sosa:Property;
 iop:hasStatisticalModifier uom:maximum ;
 iop:hasObjectOfInterest ex:airAround_DHT22_4578;
 iop:hasProperty qk:RelativeHumidity .

ex:airAround_DHT22_4578 skos:broader et:23;
  rdfs:label "The air immediatly around the DHT22 sensor." 
.
  
et:23 rdfs:label "air" .

#
#
ex:DHT22_4578_inputVoltage a sosa:FeatureOfInterest ;
 rdfs:comment "The DC voltage being supplied to the sensor"@en ;.

ex:mimimalOperatingInputVoltage  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:DHT22_4578_inputVoltage ;
  sosa:observedProperty ex:mimOperatingInputVoltageRestriction ;
  sosa:hasSimpleResult 3.3 ;
  qudt:hasUnit unit:V .

ex:mimOperatingInputVoltageRestriction a iop:Variable, sosa:Property;
  iop:hasStatisticalModifier uom:minimum ;
  iop:hasObjectOfInterest ex:DHT22_4578 ;
  iop:hasProperty qk:Voltage .

ex:maximumOperatingInputVoltage a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:DHT22_4578_inputVoltage ;
  sosa:observedProperty ex:maxOperatingInputVoltageRestriction ;
  sosa:hasSimpleResult 6.0 ;
  qudt:hasUnit unit:V .

ex:maxOperatingInputVoltageRestriction a iop:Variable, sosa:Property;
  iop:hasStatisticalModifier uom:maximum ;
  iop:hasObjectOfInterest ex:DHT22_4578 ;
  iop:hasProperty qk:Voltage .

ex:nominalOperatingInputVoltage  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:DHT22_4578_inputVoltage ;
  sosa:observedProperty ex:nominalOperatingInputVoltageRestriction ;
  sosa:hasSimpleResult 5.0 ;
  qudt:hasUnit unit:V .

# A complaint may be that the time period of the averaging period is unspecified; 
ex:nominalOperatingInputVoltageRestriction a iop:Variable, sosa:Property;
  iop:hasStatisticalModifier uom:average ;
  iop:hasObjectOfInterest ex:DHT22_4578 ;
  iop:hasProperty qk:Voltage .

#
# These are the system capabilities
#

ex:DHT22_4578_TemperatureSensorCapabilities a sosa:ObservationCollection;
 sosa:hasValidityContext ex:DHT22_4578_TemperatureSensorNormalOperatingConditions ;
 sosa:hasMember ex:DHT22_4578_minimumMeasureableTemperature, ex:DHT22_4578_maximumMeasureableTemperature, ex:DHT22_4578_TemperatureMeasurementAccuracy, ex:DHT22_4578_TemperatureMeasurementSensitivity, ex:DHT22_4578_TemperatureMeasurementFrequency .

ex:DHT22_4578_HumiditySensorCapabilities a sosa:ObservationCollection;
 sosa:hasValidityContext ex:DHT22_4578_HumiditySensorNormalOperatingConditions ;
 sosa:hasMember ex:DHT22_4578_minimumMeasureableRelativeHumidity, ex:DHT22_4578_maximumMeasureableRelativeHumidity, ex:DHT22_4578_RelativeHumidityFrequency .

ex:DHT22_4578_minimumMeasureableTemperature a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_TemperatureSensor ;
 sosa:observedProperty ex:DHT22_4578_minimumMeasureableTemperatureLimit;
 sosa:hasSimpleResult "-40.0"^^xsd:decimal ;
 qudt:hasUnit unit:DEG_C .

ex:DHT22_4578_minimumMeasureableTemperatureLimit a iop:Variable, sosa:Property;
 iop:hasStatisticalModifier uom:minimum ;
 iop:hasObjectOfInterest ex:airAround_DHT22_4578;
 iop:hasProperty qk:Temperature .

ex:DHT22_4578_maximumMeasureableTemperature a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_TemperatureSensor ;
 sosa:observedProperty ex:DHT22_4578_maximumMeasureableTemperatureLimit;
 sosa:hasResult [
   qudt:value 80.0 ;
   qudt:hasUnit unit:DEG_C ] .

ex:DHT22_4578_maximumMeasureableTemperatureLimit a iop:Variable, sosa:Property;
 iop:hasStatisticalModifier uom:maximum ;
 iop:hasObjectOfInterest ex:airAround_DHT22_4578;
 iop:hasProperty qk:Temperature .

ex:DHT22_4578_TemperatureMeasurementAccuracy a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_TemperatureSensor;
 sosa:observedProperty ex:Accuracy ;
 sosa:hasResult [
   qudt:value 0.5 ;
   qudt:hasUnit unit:DEG_C ] .


ex:DHT22_4578_TemperatureMeasurementSensitivity a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_TemperatureSensor;
 sosa:observedProperty ex:Sensitivity , ex:Resolution ;
 sosa:hasResult [
   qudt:value 0.1 ;
   qudt:hasUnit unit:DEG_C ] .

ex:DHT22_4578_TemperatureMeasurementFrequency a sosa:Observation ;
 rdfs:comment "The smallest possible time between one observation and the next is 2 s on average."@en ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_TemperatureSensor;
 sosa:observedProperty ex:DHT22_4578_TemperatureMeasurementFrequencyLimit ;
 sosa:hasResult [
   qudt:value 2.0 ;
   qudt:hasUnit unit:SEC ] .

# TODO Likely wrong

ex:DHT22_4578_TemperatureMeasurementFrequencyLimit  a iop:Variable, sosa:Property;
  iop:hasStatisticalModifier uom:average ;
  iop:hasObjectOfInterest ex:airAround_DHT22_4578;
  iop:hasProperty qk:Period .

# These are very close to the system conditions and the same limits can be reused.
ex:DHT22_4578_minimumMeasureableRelativeHumidity a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_HumiditySensor;
 sosa:observedProperty ex:minSensorEnvironmentHumidityLimit;
 sosa:hasResult [
   qudt:value 0.0 ;
   qudt:hasUnit unit:PERCENT ] .

ex:DHT22_4578_maximumMeasureableRelativeHumidity a sosa:Observation ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_HumiditySensor;
 sosa:observedProperty ex:maxSensorEnvironmentHumidityLimit;
 sosa:hasResult [
   qudt:value 100.0 ;
   qudt:hasUnit unit:PERCENT ] .

ex:DHT22_4578_RelativeHumidityFrequency a sosa:Observation ;
 rdfs:comment "The smallest possible time between one observation and the next is 2 s on average."@en ;
 sosa:hasFeatureOfInterest ex:DHT22_4578_HumiditySensor;
 sosa:observedProperty ex:DHT22_4578_RelativeHumidityFrequencyLimit ;
 sosa:hasResult [
   qudt:value 2.0 ;
   qudt:hasUnit unit:SEC ] .

ex:DHT22_4578_RelativeHumidityFrequencyLimit  a iop:Variable, sosa:Property;
  iop:hasStatisticalModifier uom:average ;
  iop:hasObjectOfInterest ex:DHT22_4578_HumiditySensor;
  iop:hasProperty qk:Period .

# Some results
ex:observation_1087 rdf:type sosa:Observation ;
  sosa:observedProperty et:23;
  sosa:madeBySensor ex:DHT22_4578_TemperatureSensor ;
  sosa:usedProcedure ex:DHT22_Procedure ;
  sosa:resultQuality ex:observation_1087_quality ;
  sosa:hasResult [ 
    qudt:hasUnit unit:DEG_C ; 
    qudt:value 21.4 ] ;
.

# use some other ontology to further qualify this quality

ex:observation_1087_quality 
  ex:evaluatedBy ex:Tom ;
  ex:confidenceValue "6"^^xsd:integer ;
  rdfs:comment """Tom gave a confidence value of 6 out of 10 on this observation."""@en ;
.
# use some quantity ontology

@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

ex:observation_1087_quality rdf:type qudt:Quantity ;
  qudt:quantityValue [
    rdf:type qudt:QuantityValue ;
    qudt:value 98.4 ;
    qudt:hasUnit unit:PERCENT ] .

```


### Example diet.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:O299877
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:Community2998 ;
  sosa:hasResult ex:d77 ;
  sosa:observedProperty ex:diet ;
  sosa:phenomenonTime [
      time:hasBeginning [
          time:inTimePosition [
              time:hasTRS ex:BP ;
              time:numericPosition 12000 ;
            ] ;
        ] ;
      time:hasDuration [
          time:numericDuration 500 ;
          time:unitType time:unitYear ;
        ] ;
    ] ;
  sosa:resultTime "2015-06-06T12:00:00+10:00"^^xsd:dateTime ;
.
ex:d77 
  a ex:diet ;
  rdfs:comment "mainly seafood" ;
.
ex:BP
  a time:TRS ;
  skos:definition "Years before 1950, positive backwards" ;
.
```


### Example forecast.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix siq: <https://si-digital-framework.org/quantities/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/forecast/> .

ex:Observation299876
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:EarthAtmosphere ;
  sosa:hasResult <grid/299876> ;
  sosa:observedProperty siq:TEMC ;
  sosa:phenomenonTime [
    time:hasBeginnning [ 
      time:inXSDDateTime "2024-03-09T11:00:00+10:00"^^xsd:dateTime ;
    ];
    time:hasEnd [  
      time:inXSDDateTime "2024-03-09T12:00:00+10:00"^^xsd:dateTime ;
    ];
  ];
  sosa:resultTime "2024-03-06T12:00:00+10:00"^^xsd:dateTime ;
.

ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
. 
siq:TEMC a sosa:Property ;
  rdfs:label "Celsius temperature" ;
.
```


### Example GeometryResult.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/geor/> .

ex:ObsGeo1 a sosa:Observation ;
    sosa:madeBySensor ex:MyGPS736   ;
    sosa:hasFeatureOfInterest ex:AbbysCar ;
    sosa:phenomenonTime [
        a time:Instant ;
        time:inXSDDateTimeStamp "2023-06-20T21:49:18+00:00"^^xsd:dateTime ;
    ] ;
    sosa:resultTime "2023-06-20T21:49:18+00:00"^^xsd:dateTime ;
    sosa:observedProperty <https://vocab.nerc.ac.uk/collection/S06/current/S0600255/>  ;
    sosa:hasResult [
        a geo:Geometry ;
        geo:asWKT "Point (145.042316 -37.919134)"^^geo:wktLiteral ;
     ] .
     
ex:MyGPS736 
    a sosa:Sensor ;
.
ex:AbbysCar 
    a sosa:FeatureOfInterest ;
.
<https://vocab.nerc.ac.uk/collection/S06/current/S0600255/> 
    a sosa:Property ;
    rdfs:label "Location (geographic coordinates)"@en ;
.
```


### Example GeometryResultSimple.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:ObsGeo1 a sosa:Observation ;
    sosa:madeBySensor ex:MyGPS736   ;
    sosa:hasFeatureOfInterest ex:AbbysCar ;
    sosa:resultTime "2023-06-20T21:49:18+00:00"^^xsd:dateTime ;
    sosa:observedProperty <https://vocab.nerc.ac.uk/collection/S06/current/S0600255/>  ;
    sosa:hasSimpleResult  "Point (145.042316 -37.919134)"^^geo:wktLiteral ;
.
```


### Example historical-airtemp.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/htemp/> .

ex:T99 a sosa:Sensor , ex:Mercury-in-glass-thermometer ;
  rdfs:label "Mercury in glass thermometer #99"@en ;
  sosa:observes ex:airTemperature ;
.
ex:SHW a sosa:Platform , sosa:FeatureOfInterest;
  rdfs:label "Station Hohe Warte"@en ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (16.355804145468635 48.248491274780754)"^^geo:WktLiteral ;
  ] ;
  sosa:hosts ex:T99 ;
.
ex:airTemperature a sosa:Property ;
  rdfs:label "air temperature"@en ;
  sosa:isPropertyOf ex:EarthAtmosphere ;
  skos:broader qk:Temperature ;
.
ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
. 
ex:SHW_T_1872-04-04T15 a sosa:Observation ;
  sosa:madeBySensor ex:T99 ; 
  sosa:hasFeatureOfInterest ex:SHW ;
  sosa:observedProperty ex:airTemperature ;
  sosa:phenomenonTime [
    time:inXSDDateTime "1872-04-04T15:00:00+01:00"^^xsd:dateTime ;
  ] ;
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:value "22.5"^^xsd:decimal ;
     qudt:hasUnit unit:DEG_C ] ;
  sosa:resultTime "1872-04-04T15:00:00+01:00"^^xsd:dateTime ;
.
```


### Example IBS-TH2-PLUS-brief.ttl
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
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sensor: <https://example.org/sensor/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
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
  sosa:hasMember [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MaxFrequency ;
      sosa:hasSimpleResult "0.1 Hz"^^cdt:ucum ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MinFrequency ;
      sosa:hasSimpleResult "5.556e-4 Hz"^^cdt:ucum ;
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
  sosa:hasMember [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:HumidityAccuracy ;
      sosa:hasSimpleResult "4.5 %"^^cdt:ucum ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MaxMeasurableHumidity ;
      sosa:hasSimpleResult "99.0 %"^^cdt:ucum ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MinMeasurableHumidity ;
      sosa:hasSimpleResult "0.0 %"^^cdt:ucum ;
  ]
.
sensor:IBS-TH2-Plus-T-systemCapability a sosa:ObservationCollection ;
  sosa:hasMember [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:TemperatureAccuracy ;
      sosa:hasSimpleResult "0.5 Cel"^^cdt:ucum ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MaxMeasurableTemperature ;
      sosa:hasSimpleResult "60.0 Cel"^^cdt:ucum ;
  ] ,
  [
      a sosa:Observation ;
      sosa:observedProperty sosa-cap:MinMeasurableTemperature ;
      sosa:hasSimpleResult "-40.0 Cel"^^cdt:ucum ;
  ]
.


```


### Example IDEAS.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#>.
@prefix sosa: <http://www.w3.org/ns/sosa#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.
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
   sosa:hasSimpleResult "92.5 %"^^cdt:ucum ;
   sosa:resultTime "2017-06-02T15:00:00-07:00"^^xsd:dateTime ;
   sosa:observedProperty ex:RelativeHumidity ;
   sosa:usedProcedure ex:MeasuringRelativeHumidity ;
.
```


### Example InkBird-IBS-TH2-Range.ttl
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


### Example ip68.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix schema: <http://schema.org/>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfp: <https://w3id.org/rdfp/>.
@prefix gr: <http://purl.org/goodrelations/v1#> .
@prefix prov: <http://www.w3.org/ns/prov#>.
@prefix seas: <https://w3id.org/seas/>.
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.
@prefix sosa-cap: <http://www.w3.org/ns/sosa/system-capability-properties#> .
@prefix sosa-env: <http://www.w3.org/ns/sosa/system-environment-properties#> .
@base <https://data.grandlyon.com/> .

# This example describes the IP68 Smart Sensor that and some of its capabilities and operating ranges.
# A specific IP68 Smart Sensor observes the air temperature, and its own battery state.

ex:Organization_1 a prov:Organization ;
    skos:exactMatch <http://dbpedia.org/page/Metropolis_of_Lyon> ;
.
ex:Air a sosa:FeatureOfInterest ;
  rdfs:label "The air."@en ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
. 
ex:IP68_Outdoor_Temperature_Sensor a owl:Class , gr:ProductOrServiceModel ;
  rdfs:label "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:subClassOf [
    owl:onProperty sosa:hasOperatingConditions ;
    owl:hasValue ex:IP68_Outdoor_Temperature_Sensor_operatingRange ] ;
  rdfs:subClassOf [
    owl:onProperty sosa:hasSystemCapability ;
    owl:hasValue ex:IP68_Outdoor_Temperature_Sensor_systemCapability ] ;
.
ex:Sensor_SL-T-P1_battery a sosa:Battery;
 rdfs:label "The battery powering the IP68 Outdoor Temperature Sensor"@en .

ex:IP68_Outdoor_Temperature_Sensor_operatingRange a sosa:ObservationCollection , sosa:NormalOperatingConditions ;
    rdfs:comment "An environment temperature range of -20 to 70 Celsius."@en ;
    sosa:hasMember [
      sosa:observedProperty sosa-env:MinAmbientTemperature ;
      sosa:hasResult [ 
        qudt:value -20.0 ;
        qudt:hasUnit unit:DEG_C ;
      ] ;
    ] , [
      sosa:observedProperty sosa-env:MaxAmbientTemperature ;
      sosa:hasResult [ 
        qudt:value 70.0 ;
        qudt:hasUnit unit:DEG_C ;
      ] ;
    ]
.
ex:IP68_Outdoor_Temperature_Sensor_systemCapability a sosa:ObservationCollection ;
  rdfs:comment "The sensor capability in normal operating conditions."@en ;
  sosa:hasMember [
    sosa:observedProperty sosa-cap:RFSensitivity ;
    sosa:hasResult [ qudt:value -137.0 ; qudt:hasUnit unit:DeciB-MilliW ] ;
  ] , [
    sosa:observedProperty sosa-cap:TemperatureAccuracy ;
    sosa:hasResult [ qudt:value 0.2 ; qudt:hasUnit unit:DEG_C ] ;
  ] , [ 
    sosa:observedProperty sosa-cap:TemperatureResolution ;
    sosa:hasResult [ qudt:value 0.0625 ; qudt:hasUnit unit:DEG_C ] ;
  ] , [ 
    sosa:observedProperty sosa-cap:BatteryResolution ;
    sosa:hasResult [ qudt:value 3.937e-3 ; qudt:hasUnit unit:PERCENT ] ;
  ] ;
  sosa:hasValidityContext ex:IP68_Outdoor_Temperature_Sensor_operatingRange ;
.
ex:Air_4575_485 a sosa:Sample ;
  rdfs:label "The air at lat 45.75 and long 4.85."@en ;
  sosa:isSampleOf ex:Air ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (4.85 45.75)"^^geo:WktLiteral ;
  ] ;
  sosa:hasProperty qk:Temperature ;
.
ex:Sensor_SL-T-P1 a gr:ProductOrService, sosa:Sensor , seas:LoRaCommunicationDevice , ex:IP68_Outdoor_Temperature_Sensor ;
    gr:hasBrand [ a gr:Brand ; gr:name "Sensing Labs"@en ] ;
    geo:alt 100.0 ;
    geo:lat 45.75 ;
    geo:lon 4.85 ;
    sosa:implements ex:IP68_Outdoor_Temperature_Sensor_temperatureSensingProcedure ;
    sosa:implements ex:IP68_Outdoor_Temperature_Sensor_batterySensingProcedure ;
    sosa:observes ex:Sensor_SL-T-P1_battery ;
    sosa:observes qk:Temperature ;
.
ex:Deployment_SL-T-P1_2017-06-06 a sosa:Deployment ;
  sosa:deployedSystem ex:Sensor_SL-T-P1 ;
  sosa:startTime "2017-06-06"^^xsd:date ;
  prov:wasAssociatedWith ex:Organization_1 ;
  sosa:deployedOnPlatform ex:Tree_1 ;
.
ex:Observation_5872357_temperature a sosa:Observation ;
    sosa:hasSimpleResult "64.5244681928429 Cel"^^cdt:ucum ;
    sosa:madeBySensor ex:Sensor_SL-T-P1 ;
    sosa:hasFeatureOfInterest ex:Air_4575_485 ;
    sosa:observedProperty qk:Temperature ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime ;
.
ex:Observation_5872357_battery a sosa:Observation ;
    sosa:hasSimpleResult "73.2 %"^^cdt:ucum ;
    sosa:madeBySensor ex:Sensor_SL-T-P1 ;
    sosa:hasFeatureOfInterest ex:Sensor_SL-T-P1 ;
    sosa:observedProperty ex:Sensor_SL-T-P1_battery ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime ;
.
```


### Example iphone_barometer-sosa.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/iphone_barometer/> .

# iPhone Barometer

ex:iphone_barometer-sosa a owl:Ontology ;
  rdfs:comment "The barometric readings from a Bosch Sensortec BMP282 sensor in an Apple IPhone 7 observed on June 6 2017 using only the SOSA core."@en ;
.
# The barometric readings from a Bosch Sensortec BMP282 sensor in an Apple IPhone 7 observed on June 6 2017
# using only the SOSA core

ex:EarthAtmosphere rdf:type sosa:FeatureOfInterest ;
  rdfs:label "Atmosphere of Earth"@en ;
.
# An iPhone 7 as the Platform that hosts several sensors, among others the Bosch Sensortec BMP282 atmospheric pressure sensor

ex:iphone7_35-207306-844818-0 a sosa:Platform ;
  rdfs:label "IPhone 7 - IMEI 35-207306-844818-0"@en ;
  rdfs:comment "IPhone 7 - IMEI 35-207306-844818-0 - John Doe"@en ;
  sosa:hosts ex:sensor_35-207306-844818-0_BMP282 ;
.
ex:sensor_35-207306-844818-0_BMP282 rdf:type sosa:Sensor ;
  rdfs:label "Bosch Sensortec BMP282"@en ;
  sosa:observes qk:AtmosphericPressure ;
.
# An observation made by the Bosch Sensortec BMP282 atmospheric pressure sensor

ex:Observation_346344 rdf:type sosa:Observation ;
  sosa:observedProperty qk:AtmosphericPressure ;
  sosa:hasFeatureOfInterest ex:EarthAtmosphere ;
  sosa:madeBySensor ex:sensor_35-207306-844818-0_BMP282 ;
  sosa:hasSimpleResult "1021.45 hPa"^^cdt:ucum ;
  sosa:resultTime "2017-06-06T12:36:12+00:00"^^xsd:dateTime ;
.
# Another observation made a second later by the Bosch Sensortec BMP282 atmospheric pressure sensor

<Observation/346345> rdf:type sosa:Observation ;
  sosa:observedProperty qk:AtmosphericPressure ;
  sosa:hasFeatureOfInterest ex:EarthAtmosphere ;
  sosa:madeBySensor ex:sensor_35-207306-844818-0_BMP282 ;
  sosa:hasResult [
    rdf:type qudt:QuantityValue ;
    qudt:value "101936"^^xsd:decimal ;
    qudt:hasUnit unit:PA ] ;
  sosa:resultTime "2017-06-06T12:36:13+00:00"^^xsd:dateTime ;
.
```


### Example LocatedDeployment.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:TH2-56-2024 a sosa:Deployment ;
  sosa:deployedSystem ex:IBS-TH2-56 ;
  sosa:deployedOnPlatform ex:Room31C ;
  sosa:startTime "2024-01-01T00:00:00+00:00"^^xsd:dateTime ;
  sosa:endTime "2024-12-31T23:59:59+00:00"^^xsd:dateTime ;
.
ex:Room31C a sosa:Platform ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (-73.877244 45.511672)"^^geo:WktLiteral ;
  ] ;
.
ex:IBS-TH2-56 
    a sosa:Sensor ;
    rdfs:label "12gth456a-23190"^^ex:serialNumber ;
  . 
ex:serialNumber a rdfs:Datatype ;
    rdfs:subClassOf xsd:string ;
.
```


### Example LocatedPlatform.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Room31C a sosa:Platform ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (-73.877244 45.511672)"^^geo:WktLiteral ;
  ] ;
  sosa:hosts ex:IBS-TH2-56 ;
.
ex:IBS-TH2-56 
    a sosa:Sensor ;
    rdfs:label "12gth456a-23190"^^ex:serialNumber ;
  . 
ex:serialNumber a rdfs:Datatype ;
    rdfs:subClassOf xsd:string ;
.
```


### Example LocatedSample.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

ex:EarthAtmosphere_StE a sosa:Sample ;
  sosa:isSampleOf ex:EarthAtmosphere ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (4.387611 45.437772)"^^geo:WktLiteral ;
  ] ;
.
ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
. 
```


### Example LocatedSampling.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

ex:EarthAtmosphere_StE a sosa:Sample ;
  sosa:isSampleOf ex:EarthAtmosphere ;
  sosa:isResultOf ex:AirSampling_StE ; 
.
ex:AirSampling_StE a sosa:Sampling ;
  sosa:hasFeatureOfInterest ex:EarthAtmosphere ;
  sosa:hasInputValue [ 
    a geo:Point ;
    geo:asWKT "POINT (4.387611 45.437772)"^^geo:WktLiteral ;
  ] ;
.
ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
. 
```


### Example LocatedSensor.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:IBS-TH2-56 
    a sosa:Sensor ;
    rdfs:label "12gth456a-23190"^^ex:serialNumber ;
    geo:hasGeometry [ 
        a geo:Point ;
        geo:asWKT "POINT (-73.877244 45.511672)"^^geo:WktLiteral ;
    ] ;
. 
ex:serialNumber a rdfs:Datatype ;
    rdfs:subClassOf xsd:string ;
.

```


### Example obs-sample-foi.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

ex:Bubble873 a sosa:Sample ;
  sosa:isSampleOf ex:EarthAtmosphere;
.
ex:Ob873c4 a sosa:Observation ;
  sosa:observedProperty ex:CO2-Concentration ;
  sosa:hasFeatureOfInterest ex:Bubble873 ;
  sosa:hasUltimateFeatureOfInterest ex:EarthAtmosphere ;
  sosa:hasSimpleResult "240 [ppm]"^^cdt:ucum ;
.
ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
  . 
ex:CO2-Concentration a sosa:Property ;
  skos:exactMatch <http://purl.obolibrary.org/obo/ENVO_04000004> ;
  skos:prefLabel "concentration of carbon dioxide in air" ;
. 

```


### Example open-window.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/open-window/> .

ex:window98 rdf:type sosa:FeatureOfInterest ;
    sosa:hasProperty ex:openState ;
.
ex:openState rdf:type sosa:Property ;
.
ex:closer-987 rdf:type ex:WindowCloser , sosa:Actuator ;
.
ex:WindowCloser rdfs:subClassOf sosa:Actuator ;
.
ex:A188 rdf:type sosa:Actuation ;
  sosa:hasFeatureOfInterest ex:window98 ;
  sosa:actsOnProperty  ex:openState ;
  sosa:madeByActuator ex:closer-987 ; 
  sosa:hasSimpleResult true ;
  sosa:startTime "2017-04-18T17:23:00+02:00"^^xsd:dateTime ;
  sosa:endTime "2017-04-18T17:24:00+02:00"^^xsd:dateTime ;
.

```


### Example paleo-atmosphere.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix unit: <http://qudt.org/vocab/unit/>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

ex:Bubble873 a sosa:Sample , sosa:MaterialSample ;
  sosa:isSampleOf ex:IceCore12 , ex:EarthAtmosphere;
  sosa:isSampleOfUltimateFOI ex:Antarctic_ice_sheet ;
  sosa:isResultOf ex:CoreEx1923 ;
.
ex:Ob873t2 a sosa:Observation ;
  sosa:observedProperty ex:C14-Age ;
  sosa:hasFeatureOfInterest ex:Bubble873 ;
  sosa:hasUltimateFeatureOfInterest ex:EarthAtmosphere ;
  sosa:hasSimpleResult "7530 a"^^cdt:ucum ;
  sosa:resultTime "2018-01-09T14:15:00+00:00"^^xsd:dateTime ;
.
ex:Ob873c4 a sosa:Observation ;
  sosa:observedProperty ex:CO2-Concentration ;
  sosa:hasFeatureOfInterest ex:Bubble873 ;
  sosa:hasUltimateFeatureOfInterest ex:EarthAtmosphere ;
  sosa:hasSimpleResult "240 [ppm]"^^cdt:ucum ;
  sosa:resultTime "2018-01-09T14:16:00+00:00"^^xsd:dateTime ;
.
ex:Oatc349 a sosa:Observation ;
  sosa:observedProperty ex:CO2-Concentration ;
  sosa:hasFeatureOfInterest ex:EarthAtmosphere ;
  sosa:hasSimpleResult "240 [ppm]"^^cdt:ucum ;
  sosa:phenomenonTime [ 
    time:inTimePosition [
      time:hasTRS ex:BP ;
      time:numericPosition 7530 ;
    ] ;
  ] ;   
  sosa:resultTime "2018-01-09T14:16:00+00:00"^^xsd:dateTime ;
  sosa:hasInputValue ex:Ob873t2 , ex:Ob873c4 ;
.
ex:BP
  a time:TRS ;
  skos:definition "Years before 1950, positive backwards" ;
.
ex:Antarctic_ice_sheet a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q571430> ;
. 
ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q3230> ;
  . 
ex:C14-Age a sosa:Property ;
  skos:exactMatch <http://vocab.nerc.ac.uk/collection/S06/current/S0600001/> ;
  skos:definition "The age of an object, determined by radiocarbon dating, expressed relative to a datum of AD 1950." ;
  skos:prefLabel "14C age" ;
.
ex:CO2-Concentration a sosa:Property ;
  skos:exactMatch <http://purl.obolibrary.org/obo/ENVO_04000004> ;
  skos:prefLabel "concentration of carbon dioxide in air" ;
. 

```


### Example sample-relations.ttl
#### ttl
```ttl
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix relex: <https://example.org/data/sample-relations#> .
@prefix sosa-rel: <http://www.w3.org/ns/sosa/sampling/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/sample-relations> .

<https://example.org/data/sample-relations>
  rdf:type owl:Ontology ;
  owl:imports <http://www.w3.org/ns/sosa/sam/> ;
.
relex:CSRWA25569
  rdf:type sosa:Sample ;
  rdfs:label "Specimen CSRWA25569" ;
.
relex:CSRWA25569-mount7
  rdf:type sosa:Sample ;
  rdfs:label "CSRWA25569 mount 7" ;
  sosa:isSampleOf relex:CSRWA25569 ;
.
relex:CSRWA25569-mount7-spot1
  rdf:type sosa:Sample ;
  rdfs:label "spot 1" ;
  sosa-rel:hasSampleRelationship [
      rdf:type sosa-rel:SampleRelationship ;
      sosa-rel:natureOfRelationship [
          rdf:type sosa-rel:RelationshipNature ;
          rdfs:comment "probe spot on polished mount" ;
        ] ;
      sosa-rel:relatedSample relex:CSRWA25569-mount7 ;
    ] ;
.

```


### Example seismograph.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/seis/> .

# Seismograph measuring ground displacement speed
#
# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time

ex:VCAB-DP1-BP-40 a sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
  sosa:observes ex:groundDisplacementSpeed ;
.
ex:VCAB-DP1-BP-40_location a sosa:Sample ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (-120.6195831 35.8648067)"^^geo:WktLiteral ;
  ] ;
  sosa:isSampleOf ex:Earth ;
.
ex:Earth a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q2> ;
  rdfs:label "Earth" ;
.
ex:groundDisplacementSpeed a sosa:Property ;
  rdfs:label "ground displacement speed"@en ;
  skos:broader qk:Speed ;
.
ex:VCAB-DP1-BP-40_t2017-04-18T08%3A23%3A00-07%3A00 a sosa:Observation ;
  sosa:madeBySensor ex:VCAB-DP1-BP-40 ; 
  sosa:hasFeatureOfInterest ex:VCAB-DP1-BP-40_location ;
  sosa:observedProperty ex:groundDisplacementSpeed ;
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:value "5e-4"^^xsd:double ;
     qudt:hasUnit unit:CentiM-PER-SEC ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTime ;
.
```


### Example smiley.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/smiley/> .

# Determing the color of a smiley face sticker, including sampling from a population of smiley stickers

# First setting up all the basics: FeatureOfInterest, Property, Procedure, Sensor, Platform

ex:SmileySticker  
  rdf:type	sosa:FeatureOfInterest ;
  rdfs:label "Smiley face sticker"@en ;
  sosa:hasProperty ex:stickerColor ;
.
ex:StickerColor  
  rdf:type	sosa:Property;
  rdfs:label "The color of a sticker"@en ;
.
ex:ColorDetermination 
  rdf:type	sosa:ObservingProcedure ;
  rdfs:label "Procedure for determining the color of a sticker"@en ;
  sosa:forProperty ex:StickerColor ;
.
ex:ColorDeterminer 
  rdf:type	sosa:Sensor;
  rdfs:label "Sensor for determining the color of a sticker"@en ;
  sosa:observes ex:StickerColor ;
.
ex:StickerAssayOffice 
  rdf:type	sosa:Platform;  
  rdfs:label "Assay office for determining the color of a sticker"@en ;
  sosa:hosts ex:ColorDeterminer ;
.
# Adding an Observation

ex:Observation-Smiley-Color 
  rdf:type sosa:Observation ;
  sosa:hasFeatureOfInterest  ex:SmileySticker ;
  sosa:observedProperty  ex:StickerColor ;
  sosa:madeBySensor ex:ColorDeterminer ;
  sosa:usedProcedure ex:ColorDetermination ;
  sosa:hasSimpleResult "Yellow"^^xsd:string ;
  sosa:phenomenonTime [
	  rdf:type time:Instant ;
	  time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTime 
    ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTime ;
.
# Sampling of the SmileySticker from a wider population of smiley face stickers

# First setting up all the basics: FeatureOfInterest, Sampler, Procedure

ex:SmileyPopulation  
  rdf:type	sosa:FeatureOfInterest ;
  rdfs:label "A population of smiley face stickers"@en ;
  sosa:hasProperty ex:stickerColor ;
.
ex:SmileySamplingProcedure 
  rdf:type sosa:SamplingProcedure ;
  rdfs:label "Procedure for sampling smiley stickers"@en ;
.
ex:SmileySampler 
  rdf:type sosa:Sampler ;
  rdfs:label "Smiley sticker sampler"@en ;
  sosa:implements ex:SmileySamplingProcedure ;
.
# Adding a Sampling act

ex:SmileySampling 
  rdf:type sosa:Sampling ;
  rdfs:label "Sampling of a representative Smiley Sticker from a Collection of Smiley Stickers"@en ;
  sosa:hasFeatureOfInterest ex:SmileyPopulation ;
  sosa:usedProcedure ex:SmileySamplingProcedure ;
  sosa:madeBySampler ex:SmileySampler ;
  sosa:hasResult ex:SmileySticker ;
.
```


### Example spinning-cups.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/wind/> .

# Wind sensor spinning cups
#
# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor

ex:windSensor_14 rdf:type sosa:Sensor ;
  sosa:observes ex:windSpeed ;
.
ex:windSpeed a sosa:Property ;
  rdfs:label "wind speed"@en ;
  skos:broader qk:Speed ;
.
ex:location_4687 a sosa:Platform ;
  sosa:hosts ex:windSensor_14 ;
.
# observation #147 was originated by the movement of the spinning cups of sensor #14

ex:observation_147 rdf:type sosa:Observation ;
  sosa:observedProperty ex:windSpeed ;
  sosa:madeBySensor ex:windSensor_14 ;
  sosa:wasOriginatedBy ex:observation_147_spinningCupsMovement ;
  sosa:resultTime "2017-04-12T12:00:00+00:00"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^cdt:ucum ;
.
# wind sensor #14 detected some movement of spinning cups, from which originated the
# observations #147 and #148

ex:windSensor_14 rdf:type sosa:Sensor ;
  sosa:madeObservation ex:observation_147 , ex:observation_148 ; 
  sosa:detects ex:observation_147_spinningCupsMovement , ex:observation_148_spinningCupsMovement ;
.
# observation #147 was originated by the movement of the spinning cups of sensor #14

ex:observation_147_spinningCupsMovement rdf:type sosa:Stimulus ;
  sosa:isProxyFor ex:windSpeed ;
.
ex:observation_148 rdf:type sosa:Observation ;
  sosa:observedProperty ex:windSpeed ;
  sosa:madeBySensor ex:windSensor_14 ;
  sosa:wasOriginatedBy ex:observation_148_spinningCupsMovement ;
  sosa:resultTime "2017-04-12T12:01:00+00:00"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^cdt:ucum ;
.
ex:observation_148_spinningCupsMovement rdf:type sosa:Stimulus ;
  sosa:isProxyFor ex:windSpeed ;
.

```


### Example sunspots.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/sunspot/> .

# Number of sunspots
# The result of an observation of the sunspot number is available a few minutes 
# after the phenomenon time, due to the light travel duration

<Observation/7536> rdf:type sosa:Observation ;
  sosa:observedProperty  ex:sunspotCount ;
  sosa:hasFeatureOfInterest ex:Sun ;
  sosa:hasSimpleResult 66 ;
  sosa:phenomenonTime [
    rdf:type time:Instant ;
    time:inXSDDateTimeStamp "2017-03-31T11:51:42+00:00"^^xsd:dateTime ] ;
  sosa:resultTime "2017-03-31T12:00:00+00:00"^^xsd:dateTime ;
.
ex:sunspotCount rdf:type sosa:Property ;
  skos:broader qk:Count ;
.
ex:Sun a sosa:FeatureOfInterest ;
  skos:exactMatch <https://www.wikidata.org/wiki/Q525> ;
  rdfs:label "Sun" ;
.
```


### Example Temperature-i-adopt.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix iop: <https://w3id.org/iadopt/ont/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

ex:SickChildTemperature 
  a iop:Variable , sosa:Property;
  iop:hasProperty qk:Temperature ;
  iop:hasObjectOfInterest ex:Child ;
  iop:hasConstraint [ 
    a iop:Constraint, ex:Sick ;
    iop:constrains ex:Child ] ;
    skos:prefLabel "sick child" ;
.
qk:Temperature
  a iop:Property , sosa:Property ;
  skos:prefLabel "Temperature"@en ;
.
ex:Child skos:exactMatch <http://hadatac.org/ont/chear#Child> .
ex:Sick skos:exactMatch <http://semanticscience.org/resource/SIO_000954> .

<http://hadatac.org/ont/chear#Child>
  a iop:Entity ;
  skos:prefLabel "Child"@en ;
.
<http://semanticscience.org/resource/SIO_000954>
  skos:prefLabel "Sick"@en , "Krank"@de ; 
  skos:altLabel "Unwell"@en , "Poorly"@en ;
.

```


### Example Temperature-of-interest-specialization.ttl
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


### Example Thermometer.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sensor: <https://example.org/sensor/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

qk:Temperature
  a sosa:Property ;
.
sensor:TemperatureSensor
  a owl:Class ;
  rdfs:label "A generic temperature sensor" ;
  rdfs:subClassOf sosa:Sensor ;
  rdfs:subClassOf [
      a owl:Restriction ;
      owl:hasValue qk:Temperature ;
      owl:onProperty sosa:observes ;
    ] ;
.
sensor:Mercury-in-glass-thermometer
  a owl:Class ;
  rdfs:label "Mercury in glass thermometer" ;
  rdfs:comment "Temperature sensor based on the expansion of a column of mercury inside a glass tube" ;
  rdfs:subClassOf sensor:TemperatureSensor ;
.
ex:Mums-clinical-thermometer
  a sosa:Sensor ;
  a sensor:TemperatureSensor ;
  a sensor:Mercury-in-glass-thermometer ;
.
ex:SickChildA
  a sosa:FeatureOfInterest ;
.
ex:SickChildATempObs
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:SickChildA ;
  sosa:hasSimpleResult "38.2 Cel"^^cdt:ucum ;
  sosa:madeBySensor ex:Mums-clinical-thermometer ;
  sosa:observedProperty qk:Temperature ;
.

```


### Example timeseries-oc.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix unit: <http://qudt.org/vocab/unit/>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/tsoc/> .

ex:ts159c
  a sosa:ObservationCollection ;
  sosa:hasFeatureOfInterest ex:station223 ;
  sosa:observedProperty ex:p1 ;
  sosa:madeBySensor ex:fooglemeter39 ;
  sosa:phenomenonTime [
    a time:Interval ;
    time:hasBeginning [ 
      a time:Instant ;
      time:inXSDDateTime "2017-04-15T20:00:00+00:00"^^xsd:dateTime
    ] ;
    time:hasEnd [ 
      a time:Instant ;
      time:inXSDDateTime "2017-04-15T20:03:00+00:00"^^xsd:dateTime 
    ] ;
  ] ;
  sosa:resultTime "2017-04-15T20:03:30+00:00"^^xsd:dateTime ;
  sosa:hasMember ex:t1 ;
  sosa:hasMember ex:t2 ;
  sosa:hasMember ex:t3 ;
  sosa:hasMember ex:t4 ;
.
ex:t1
  a sosa:Observation ;
  sosa:phenomenonTime [
    a time:Instant ;
    time:inXSDDateTime "2017-04-15T20:00:00+00:00"^^xsd:dateTime ;
  ] ;
  sosa:hasSimpleResult "3.24 m/s"^^cdt:ucum ;
.
ex:t2
  a sosa:Observation ;
  sosa:phenomenonTime [
    a time:Instant ;
    time:inXSDDateTime "2017-04-15T20:01:00+00:00"^^xsd:dateTime ;
  ] ;
  sosa:hasSimpleResult "3.21 m/s"^^cdt:ucum ;
.
ex:t3
  a sosa:Observation ;
  sosa:phenomenonTime [
    a time:Instant ;
    time:inXSDDateTime "2017-04-15T20:02:00+00:00"^^xsd:dateTime ;
  ] ;
  sosa:hasSimpleResult "3.15 m/s"^^cdt:ucum ;
.
ex:t4
  a sosa:Observation ;
  sosa:phenomenonTime [
    a time:Instant ;
    time:inXSDDateTime "2017-04-15T20:03:00+00:00"^^xsd:dateTime ;
  ] ;
  sosa:hasSimpleResult "3.15 m/s"^^cdt:ucum ;
.
ex:station223 a sosa:FeatureOfInterest .
ex:p1 a sosa:Property .
ex:fooglemeter39 a sosa:Sensor .

```


### Example timeseries-result-inline.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/tsoi/> .

ex:ts159i
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:station223 ;
  sosa:observedProperty ex:p1 ;
  sosa:madeBySensor ex:fooglemeter39 ;
  sosa:phenomenonTime [
    a time:Interval ;
    time:hasBeginning [ 
      a time:Instant ;
      time:inXSDDateTime "2017-04-15T20:00:00+00:00"^^xsd:dateTime
    ] ;
    time:hasEnd [ 
      a time:Instant ;
      time:inXSDDateTime "2017-04-15T20:03:00+00:00"^^xsd:dateTime 
    ] ;
  ] ;
  sosa:resultTime "2017-04-15T20:03:30+00:00"^^xsd:dateTime ;
  sosa:hasSimpleResult """2017-04-15T20:00:00+00:00,3.24
  2017-04-15T20:01:00+00:00,3.21
  2017-04-15T20:02:00+00:00,3.15
  2017-04-15T20:03:00+00:00,3.15"""^^ex:SpeedObservationCSVRecord ;
  rdfs:comment """The result of this observation is encoded as a CSV literal.  
  The CSV has four rows each representing a member of the time-series.  
  The CSV structure is defined in the datatype definition."""@en ;
.
ex:station223 a sosa:FeatureOfInterest .
ex:p1 a sosa:Property .
ex:fooglemeter39 a sosa:Sensor .

ex:SpeedObservationCSVRecord a rdfs:Datatype ;
  rdfs:comment """Datatype definition for CSV-encoded data records conforming to the speed observation data model.
  The speed observation data model is defined using the OGC SWE Data Model given as the object of ex:asSWEDataModel.
  The formal definition of this datatype (a lexical space, value space, lexical-to-value mapping) is left unspecified in this example.""" ;
  ex:asSWEDataModel """{
  "type": "DataRecord",
  "label": "Speed Observation",
  "fields": [
      {
          "name": "time",
          "type": "Time",
          "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
          "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
          "label": "Sampling Time",
          "uom": {
              "href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
          }
      },
      {
          "name": "speed",
          "type": "Quantity",
          "definition": "http://qudt.org/vocab/quantitykind/Speed",
          "label": "Vehicle Speed",
          "uom": {
              "code": "m/s",
              "href": "https://qudt.org/vocab/unit/M-PER-SEC"
          }
      }
  ]
}"""^^rdf:JSON ;
.
```


### Example timeseries-result-link.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@base <https://example.org/data/tsol/> .

ex:ts159l
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:station223 ;
  sosa:observedProperty ex:p1 ;
  sosa:madeBySensor ex:fooglemeter39 ;
  sosa:phenomenonTime [
    a time:Interval ;
    time:hasBeginning [ 
      a time:Instant ;
      time:inXSDDateTime "2017-04-15T20:00:00+00:00"^^xsd:dateTime
    ] ;
    time:hasEnd [ 
      a time:Instant ;
      time:inXSDDateTime "2017-04-15T20:03:00+00:00"^^xsd:dateTime 
    ] ;
  ] ;
  sosa:resultTime "2017-04-15T20:03:30+00:00"^^xsd:dateTime ;
  sosa:hasResult <https://example.org/data/tso/netcdf/ts159> ;
  rdfs:comment "The result of the observation is accessed using the URI https://example.org/data/tso/netcdf/ts159 (notional)."@en ;
.
ex:station223 a sosa:FeatureOfInterest .
ex:p1 a sosa:Property .
ex:fooglemeter39 a sosa:Sensor .
```


### Example tree-height.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <https://example.org/data/tree/> .

# Tree height measurement

ex:rangefinder_30 a sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en ;
.
ex:observation_1087 a sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest ex:tree_124 ;
  sosa:observedProperty qk:Height ;
  sosa:madeBySensor ex:rangefinder_30 ;
  sosa:hasResult [ 
    qudt:hasUnit unit:M ; 
    qudt:value "15.3"^^xsd:decimal ] ;
.
ex:tree_124 a sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en ;
  sosa:hasProperty qk:Height ;
.
```


### Example UOM-cdt.ttl
#### ttl
```ttl
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix ex: <https://example.org/data/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

ex:Obs234534
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:apt134 ;
  sosa:observedProperty qk:Temperature ;
  sosa:hasSimpleResult "24.9 Cel"^^cdt:ucum ;
.
cdt:ucum 
  a rdfs:Datatype ;
.
ex:apt134
  a sosa:FeatureOfInterest ;
.
qk:Temperature
  a sosa:Property ;
.
```


### Example UOM-qudt-object.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix qk: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

ex:Obs234534
  a sosa:Observation ;
  sosa:hasFeatureOfInterest ex:apt134 ;
  sosa:observedProperty qk:Temperature ;
  sosa:hasResult [
      a qudt:QuantityValue ;
      qudt:hasUnit unit:DEG_C ;
      qudt:value 24.9 ;
    ] ;
.
ex:apt134
  a sosa:FeatureOfInterest ;
.
qk:Temperature
  a sosa:Property ;
.
```

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/spec-examples`

