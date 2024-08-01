---
title: Tests for SOSA specification (Schema)


toc_footers:
  - Version 1.0
  - <a href='#'>Tests for SOSA specification</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Tests for SOSA specification (Schema)
---


# Tests for SOSA specification `ogc.sosa.properties.spec-examples`

This BuildingBlock adds test cases from the SOSA specification to the base Observation properties model

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/master/build/tests/sosa/properties/spec-examples/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA Specification Examples

This building block runs tests against the SOSA specification examples.

As TTL files these examples are validated against the SHACL rules inherited from the building blocks for elements of the specification

# Examples

## Example ice-core.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
@base <http://example.org/data/> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. 

<http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
  sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .

<iceCore/12> rdf:type sosa:Sample ;
  sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
  sosa:isResultOf <WellDrilling/4578> ;
  sosa:madeBySampler <thermalDrill/2> .

  <WellDrilling/4578> a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult <iceCore/12> ;
    sosa:madeBySampler <thermalDrill/2> ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .

<iceCore/12#observation> a sosa:Observation ;
  sosa:observedProperty <iceCore/12#CO2> ;
  sosa:hasSimpleResult 240 .

# using SSN one can explicitly state that <iceCore/12#CO2> is the property of <iceCore/12> .

<iceCore/12#CO2> sosa:isPropertyOf <iceCore/12> .
  
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_1_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex15.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time.

<earth>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "earth"@en .

<VCAB-DP1-BP-40> rdf:type sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
  sosa:observes <VCAB-DP1-BP-40#groundDisplacementSpeed> .

<VCAB-DP1-BP-40#location> rdf:type sosa:FeatureOfInterest ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:lat 35.8648067 ;
  geo:long -120.6195831 ;
  geo:alt 12.75 ;
  sosa:isSampleOf <earth> .

<VCAB-DP1-BP-40#groundDisplacementSpeed>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
  sosa:isObservedBy <VCAB-DP1-BP-40> .

<VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00> rdf:type sosa:Observation ;
  sosa:madeBySensor <VCAB-DP1-BP-40> ; 
  sosa:hasFeatureOfInterest  <VCAB-DP1-BP-40#location> ;
  sosa:observedProperty  <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
  sosa:hasResult [
     rdf:type qudt-1-1:QuantityValue ;
     qudt:numericValue "5e-4"^^xsd:double ;
     qudt:hasUnit unit:CentiM-PER-SEC ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_2_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex23.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .

@base <http://example.org/data/> .


<Room145> a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample <Room145/east> ;
  sosa:hasSample <Room145/south> .

  <Room145/east> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "East wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
    sosa:hosts <PCBBoard1> .

  <Room145/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
    sosa:hosts <PCBBoard2> .


<Room245> a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty <Room245#temperature> , <Room245#humidity> ;
  sosa:hasSample <Room245/south> .

  <Room245/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #245."@en ;
    sosa:hosts <PCBBoard3> .





<PCBBoard1> a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts <DHT22/4578> ;
  sosa:hasSubSystem <DHT22/4578> .

  <DHT22/4578> a sosa:System ;
    rdfs:label "DHT22 sensor #4578"@en ;
    sosa:isHostedBy <PCBBoard1> .


<PCBBoard2> a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts <DHT22/4578> ;
  sosa:hasSubSystem <DHT22/4578> .

  <DHT22/4579> a sosa:System ;
    rdfs:label "DHT22 sensor #4579."@en ;
    sosa:isHostedBy <PCBBoard2> .


<PCBBoard3> a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts <DHT22/4578> ;
  sosa:hasSubSystem <DHT22/4578> .

  <DHT22/4580> a sosa:System ;
    rdfs:label "DHT22 sensor #4580."@en ;
    sosa:isHostedBy <PCBBoard3> .




<Room245Deployment> a sosa:Deployment ;
  rdfs:comment "Deployment of PCB Board 3 on the south wall of room #245 for the purpose of observing the temperature and humidity of room #245."@en ;
  sosa:deployedOnPlatform <Room245/south> ;
  sosa:deployedSystem <PCBBoard3> ;
  sosa:forProperty <Room245#temperature> , <Room245#humidity> .


<Room145Deployment> a sosa:Deployment ;
  rdfs:comment "Deployment of PCB Board 1 and 2 on the east and south wall of room #145, respectively, for the purpose of observing the temperature and humidity of room #145."@en ;
  sosa:deployedOnPlatform <Room245/east> , <Room245/south> ;
  sosa:deployedSystem <PCBBoard1> , <PCBBoard2> ;
  sosa:forProperty <Room145#temperature> , <Room145#humidity> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_3_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex25.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix gr: <http://purl.org/goodrelations/v1#> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix schema: <http://schema.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix prov: <http://www.w3.org/ns/prov#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix seas: <https://w3id.org/seas/>.
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.

@base <https://data.grandlyon.com/> .

<Organization/1> a org:Organization ;
    owl:sameAs <http://dbpedia.org/page/Metropolis_of_Lyon> .

<Air> a sosa:FeatureOfInterest ;
  rdfs:label "The air."@en .

<IP68_Outdoor_Temperature_Sensor> a owl:Class , gr:ProductOrServiceModel ;
  gr:name "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:label "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:subClassOf [
    owl:onProperty ssn-system:hasOperatingRange ;
    owl:hasValue <IP68_Outdoor_Temperature_Sensor#operatingRange> ] ;
  rdfs:subClassOf [
    owl:onProperty ssn-system:hasSystemCapability ;
    owl:hasValue <IP68_Outdoor_Temperature_Sensor#systemCapability> ] .

<IP68_Outdoor_Temperature_Sensor#operatingRange> a ssn-system:OperatingRange , sosa:Property ;
  ssn-system:inCondition <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> .

<IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A temperature range of -20 to 70 Celsius."@en ;
  schema:minValue -20.0 ;
  schema:maxValue 70.0 ;
  schema:unitCode unit:DegreeCelsius .

<IP68_Outdoor_Temperature_Sensor#systemCapability> a sosa:Property , ssn-system:SystemCapability ;
  rdfs:comment "The sensor capability in normal operating conditions."@en ;
  ssn-system:hasSystemProperty <IP68_Outdoor_Temperature_Sensor#RFSensitivity> , <IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy> , <IP68_Outdoor_Temperature_Sensor#TemperatureResolution> , <IP68_Outdoor_Temperature_Sensor#BatteryAccuracy> , <IP68_Outdoor_Temperature_Sensor#BatteryResolution> ;
  ssn-system:inCondition <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> .

<IP68_Outdoor_Temperature_Sensor#RFSensitivity> a sosa:Property , ssn-system:Sensitivity , schema:PropertyValue ;
  schema:value -137 ;
  schema:unitCode unit:DecibelReferredToOneMilliwatt .

<IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy> a sosa:Property , ssn-system:Accuracy , schema:PropertyValue ;
  sosa:forProperty <Air?lat=45.75&long=4.85#temperature> ;
  schema:minValue -0.2 ;
  schema:maxValue 0.2 ;
  schema:unitCode unit:DegreeCelsius .

<IP68_Outdoor_Temperature_Sensor#TemperatureResolution> a sosa:Property , ssn-system:Resolution , schema:PropertyValue ;
  sosa:forProperty <Air?lat=45.75&long=4.85#temperature> ;
  schema:value 0.0625 ;
  schema:unitCode unit:DegreeCelsius .

<IP68_Outdoor_Temperature_Sensor#BatteryResolution> a sosa:Property , ssn-system:Resolution , schema:PropertyValue ;
  sosa:forProperty <Sensor/SL-T-P1#battery> ;
  schema:value 3.937e-3 ;
  schema:unitCode unit:PERCENT .

<Air?lat=45.75&long=4.85> a sosa:Sample ;
  rdfs:label "The air at lat 45.75 and long 4.85."@en ;
  sosa:isSampleOf <Air> ;
  sosa:hasProperty <Air?lat=45.75&long=4.85#temperature> .

<Air?lat=45.75&long=4.85#temperature> a sosa:Property , sosa:ObservableProperty ;
  sosa:isPropertyOf <Air?lat=45.75&long=4.85> .

<Sensor/SL-T-P1> a gr:ProductOrService, sosa:Sensor , seas:LoRaCommunicationDevice , <IP68_Outdoor_Temperature_Sensor> ;
    gr:hasBrand [ a gr:Brand ; gr:name "Sensing Labs"@en ] ;
    geo:alt 100.0 ;
    geo:lat 45.75 ;
    geo:lon 4.85 ;
    sosa:implements <IP68_Outdoor_Temperature_Sensor#temperatureSensingProcedure> ;
    sosa:implements <IP68_Outdoor_Temperature_Sensor#batterySensingProcedure> ;
    sosa:observes <Sensor/SL-T-P1#battery> ;
    sosa:observes <Air?lat=45.75&long=4.85#temperature> .

<Deployment/SL-T-P1/2017-06-06> a sosa:Deployment ;
  sosa:deployedSystem <Sensor/SL-T-P1> ;
  prov:startedAtTime "2017-06-06"^^xsd:date ;
  prov:wasAssociatedWith <Organization/1> ;
  sosa:deployedOnPlatform <Tree/1> .

<Observation/5872357#temperature> a sosa:Observation ;
    sosa:hasSimpleResult "64.5244681928429 Cel"^^cdt:ucum ;
    sosa:madeBySensor <Sensor/SL-T-P1> ;
    sosa:hasFeatureOfInterest <Air?lat=45.75&long=4.85> ;
    sosa:observedProperty <Air?lat=45.75&long=4.85#temperature> ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .

<Observation/5872357#battery> a sosa:Observation ;
    sosa:hasSimpleResult "73.2 %"^^cdt:ucum ;
    sosa:madeBySensor <Sensor/SL-T-P1> ;
    sosa:hasFeatureOfInterest <Sensor/SL-T-P1> ;
    sosa:observedProperty <Sensor/SL-T-P1#battery> ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_4_1.ttl">Open in new window</a>
</blockquote>



## Example sample-relations.ttl



```turtle
# baseURI: http://example.org/data/sample-relations
# imports: http://www.w3.org/ns/sosa/sampling
# prefix: relex

@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix relex: <http://example.org/data/sample-relations#> .
@prefix sampling: <http://www.w3.org/ns/sosa/sampling/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.org/data/sample-relations>
  rdf:type owl:Ontology ;
  owl:imports sosa:sampling ;
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
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship [
          rdf:type sampling:RelationshipNature ;
          rdfs:comment "probe spot on polished mount" ;
        ] ;
      sampling:relatedSample relex:CSRWA25569-mount7 ;
    ] ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_5_1.ttl">Open in new window</a>
</blockquote>



## Example dht22-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .

@prefix rdfp: <https://w3id.org/rdfp/>.

@base <http://example.org/data/> .


<DHT22#Procedure> a sosa:Procedure .

<DHT22/4578> a sosa:Platform ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> .


<DHT22/4578#TemperatureSensor> a sosa:Sensor ;
  sosa:isHostedBy <DHT22/4578> ;
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en .


<observation/1087> a sosa:Observation ;
  sosa:madeBySensor <DHT22/4578#TemperatureSensor> ;
  sosa:usedProcedure <DHT22#Procedure> .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_6_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex14.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time.

<earth>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "earth"@en .

<VCAB-DP1-BP-40> rdf:type sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
  sosa:observes <VCAB-DP1-BP-40#groundDisplacementSpeed> .

<VCAB-DP1-BP-40#location> rdf:type sosa:FeatureOfInterest ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:lat 35.8648067 ;
  geo:long -120.6195831 ;
  geo:alt 12.75 ;
  sosa:isSampleOf <earth> .

<VCAB-DP1-BP-40#groundDisplacementSpeed>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
  sosa:isObservedBy <VCAB-DP1-BP-40> .

<VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00> rdf:type sosa:Observation ;
  sosa:madeBySensor <VCAB-DP1-BP-40> ; 
  sosa:hasFeatureOfInterest  <VCAB-DP1-BP-40#location> ;
  sosa:observedProperty  <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:numericValue "5e-4"^^xsd:double ;
     qudt:hasUnit unit:CentiM-PER-SEC ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .

# using SSN one can explicitly state that <VCAB-DP1-BP-40#groundDisplacementSpeed> is the property of <VCAB-DP1-BP-40#location> .

<VCAB-DP1-BP-40#location> sosa:hasProperty <VCAB-DP1-BP-40#groundDisplacementSpeed> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_7_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex18.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <http://example.org/data/> .

# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:observes <location/4687#windSpeed> .

# wind sensor #14 made observations #147 and #148.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:madeObservation <observation/147> , <observation/148> .

# the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure.

<observation/147> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^<speed> .

<observation/148> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "43 km/h"^^<speed> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_8_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex24.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .

@base <http://example.org/data/> .


<Room145> a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample <Room145/east> ;
  sosa:hasSample <Room145/south> .

  <Room145/east> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "East wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
    sosa:hosts <PCBBoard1> .

  <Room145/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
    sosa:hosts <PCBBoard2> .


<Room245> a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty <Room245#temperature> , <Room245#humidity> ;
  sosa:hasSample <Room245/south> .

  <Room245/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #245."@en ;
    sosa:hosts <PCBBoard3> .


<PCBBoard1> a sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently."@en ;
  sosa:hosts <DHT22/4578> .

  <DHT22/4578> a sosa:Platform ;
    rdfs:label "DHT22 sensor #4578"@en ;
    sosa:isHostedBy <PCBBoard1> .


<PCBBoard2> a sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanentlys."@en ;
  sosa:hosts <DHT22/4578> .

  <DHT22/4579> a sosa:Platform ;
    rdfs:label "DHT22 sensor #4579."@en ;
    sosa:isHostedBy <PCBBoard2> .


<PCBBoard3> a sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently."@en ;
  sosa:hosts <DHT22/4578> .

  <DHT22/4580> a sosa:Platform ;
    rdfs:label "DHT22 sensor #4580."@en ;
    sosa:isHostedBy <PCBBoard3> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_9_1.ttl">Open in new window</a>
</blockquote>



## Example vistavital-a-sdo.ttl



```turtle
# baseURI: http://example.org/vistavital-a
# imports: http://www.w3.org/2006/time
# imports: http://www.w3.org/ns/prov-o#
# imports: http://www.w3.org/ns/ssn/
# imports: https://raw.githubusercontent.com/schemaorg/schemaorg/master/data/releases/3.3/all-layers.ttl
# prefix: vistavital-a

@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <http://example.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix vistavital-a: <http://example.org/vistavital-a#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:entered-by
  rdf:type owl:ObjectProperty ;
  rdfs:comment "This simple property is defined to be equivalent to prov:qualifiedAssociation with the value of prov:hadRole fixed to \"Entered by\"" ;
  rdfs:label "Data entered by" ;
  rdfs:subPropertyOf prov:wasAssociatedWith ;
  owl:propertyChainAxiom (
      [
        rdf:type owl:ObjectProperty ;
        rdfs:range [
            rdf:type owl:Class ;
            rdfs:subClassOf prov:Association ;
            rdfs:subClassOf [
                rdf:type owl:Restriction ;
                owl:hasValue [
                    rdf:type prov:Role ;
                    rdfs:label "Entered by" ;
                  ] ;
                owl:onProperty prov:hadRole ;
              ] ;
          ] ;
        rdfs:subPropertyOf prov:qualifiedAssociation ;
      ]
      prov:agent
    ) ;
.
ex:error-entered-by
  rdf:type owl:ObjectProperty ;
  rdfs:comment "This simple property is defined to be equivalent to prov:qualifiedAssociation with the value of prov:hadRole fixed to \"Error entered by\"" ;
  rdfs:label "Error entered by" ;
  rdfs:subPropertyOf prov:wasAssociatedWith ;
  owl:propertyChainAxiom (
      [
        rdf:type owl:ObjectProperty ;
        rdfs:range [
            rdf:type owl:Class ;
            rdfs:subClassOf prov:Association ;
            rdfs:subClassOf [
                rdf:type owl:Restriction ;
                owl:hasValue [
                    rdf:type prov:Role ;
                    rdfs:label "Error entered by" ;
                  ] ;
                owl:onProperty prov:hadRole ;
              ] ;
          ] ;
        rdfs:subPropertyOf prov:qualifiedAssociation ;
      ]
      prov:agent
    ) ;
.
ex:vistavital-a
  rdf:type owl:Ontology ;
  dcterms:created "2017-10-18" ;
  dcterms:creator "Simon Cox" ;
  rdfs:comment """This document shows how a vital-signs observation can be represented using SOSA. 
Three variants are included:
1. SOSA + schema.org
2. SOSA + prov-o
3. SOSA + prov-o + customized properties derived from prov-o but which make the serialization more compact 

The example data comes from the Vista example developed by Rafael Richards - see <https://github.com/vistadataproject/documents/blob/master/Background/presentations/pdf/2014-Linked_Vitals-Linked_Data_Linked_FHIR.pdf> """ ;
  rdfs:seeAlso <https://github.com/vistadataproject/documents/blob/master/Background/presentations/pdf/2014-Linked_Vitals-Linked_Data_Linked_FHIR.pdf> ;
  owl:imports <http://www.w3.org/2006/time> ;
  owl:imports <http://www.w3.org/ns/prov-o#> ;
  owl:imports <http://www.w3.org/ns/ssn/> ;
  owl:imports <https://raw.githubusercontent.com/schemaorg/schemaorg/master/data/releases/3.3/all-layers.ttl> ;
.
vistavital-a:Observation_1_ex
  rdf:type sosa:Observation ;
  ex:entered-by <http://example.org/NEW-PERSON/NOTHER,NADA> ;
  ex:error-entered-by <http://example.org/NEW-PERSON/MANAGER,SYSTEM> ;
  schema:status "error" ;
  rdfs:comment "Example of how to encode a Vital Signs measurement comparable to Vista example" ;
  rdfs:comment "This version uses schema.org and prov for elements not available in SOSA, with some locally defined specializations of prov Associations to formally bind roles to simple properties" ;
  rdfs:label "Example BP measurement" ;
  rdfs:seeAlso <https://github.com/vistadataproject/documents/blob/master/Background/presentations/pdf/2014-Linked_Vitals-Linked_Data_Linked_FHIR.pdf> ;
  prov:atLocation <http://example.org/HOSPITAL-LOCATION/4-SOUTH-MED> ;
  sosa:hasFeatureOfInterest <http://example.org/patient/jones-christopher> ;
  sosa:hasResult "150/10" ;
  sosa:observedProperty <VA:4500634> ;
  sosa:observedProperty <http://example.org/GMRV-VITAL-TYPE/BLOOD-PRESSURE> ;
  sosa:phenomenonTime [
      rdf:type time:Instant ;
      time:inXSDDateTime "2005-09-01T13:00:00Z"^^xsd:dateTime ;
    ] ;
  sosa:resultTime "2005-12-28T13:48:44Z"^^xsd:dateTime ;
.
vistavital-a:Observation_1_prov
  rdf:type sosa:Observation ;
  schema:status "error" ;
  rdfs:comment "Example of how to encode a Vital Signs measurement comparable to Vista example" ;
  rdfs:comment "This version uses prov for elements not included in SOSA" ;
  rdfs:label "Example BP measurement" ;
  rdfs:seeAlso <https://github.com/vistadataproject/documents/blob/master/Background/presentations/pdf/2014-Linked_Vitals-Linked_Data_Linked_FHIR.pdf> ;
  prov:atLocation <http://example.org/HOSPITAL-LOCATION/4-SOUTH-MED> ;
  prov:qualifiedAssociation [
      rdf:type prov:Association ;
      prov:agent <http://example.org/NEW-PERSON/MANAGER,SYSTEM> ;
      prov:hadRole [
          rdf:type prov:Role ;
          rdfs:label "Error entered by" ;
        ] ;
    ] ;
  prov:qualifiedAssociation [
      rdf:type prov:Association ;
      prov:agent <http://example.org/NEW-PERSON/NOTHER,NADA> ;
      prov:hadRole [
          rdf:type prov:Role ;
          rdfs:label "Entered by" ;
        ] ;
    ] ;
  sosa:hasFeatureOfInterest <http://example.org/patient/jones-christopher> ;
  sosa:hasResult "150/10" ;
  sosa:observedProperty <VA:4500634> ;
  sosa:observedProperty <http://example.org/GMRV-VITAL-TYPE/BLOOD-PRESSURE> ;
  sosa:phenomenonTime [
      rdf:type time:Instant ;
      time:inXSDDateTime "2005-09-01T13:00:00Z"^^xsd:dateTime ;
    ] ;
  sosa:resultTime "2005-12-28T13:48:44Z"^^xsd:dateTime ;
.
vistavital-a:Observation_1_sdo
  rdf:type sosa:Observation ;
  schema:agent <http://example.org/NEW-PERSON/NOTHER,NADA> ;
  schema:location <http://example.org/HOSPITAL-LOCATION/4-SOUTH-MED> ;
  schema:participant <http://example.org/NEW-PERSON/MANAGER,SYSTEM> ;
  schema:status "error" ;
  rdfs:comment "Example of how to encode a Vital Signs measurement comparable to Vista example" ;
  rdfs:comment "This version uses schema.org elements for elements not part of SOSA" ;
  rdfs:label "Example BP measurement" ;
  rdfs:seeAlso <https://github.com/vistadataproject/documents/blob/master/Background/presentations/pdf/2014-Linked_Vitals-Linked_Data_Linked_FHIR.pdf> ;
  sosa:hasFeatureOfInterest <http://example.org/patient/jones-christopher> ;
  sosa:hasResult "150/10" ;
  sosa:observedProperty <VA:4500634> ;
  sosa:observedProperty <http://example.org/GMRV-VITAL-TYPE/BLOOD-PRESSURE> ;
  sosa:phenomenonTime [
      rdf:type time:Instant ;
      time:inXSDDateTime "2005-09-01T13:00:00Z"^^xsd:dateTime ;
    ] ;
  sosa:resultTime "2005-12-28T13:48:44Z"^^xsd:dateTime ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_10_1.ttl">Open in new window</a>
</blockquote>



## Example observation.ttl



```turtle
@prefix sensor: <https://example.com/sensors/> .
@prefix property: <https://example.com/properties/> .

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix dct: <http://purl.org/dc/terms/> .

_:obs75134 a sosa:Observation ;
  sosa:madeBySensor [
    a sensor:BME280 ;
    dct:identifier "SN/2313Q432"
  ] ;
  sosa:observedProperty property:pm10 ;
  sosa:hasSimpleResult 0.323 ;
.
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_11_1.ttl">Open in new window</a>
</blockquote>



## Example sensor-catalog.ttl



```turtle
@prefix sensor: <https://example.com/sensors/> .
@prefix property: <https://example.com/properties/> .
@prefix procedure: <https://example.com/procedures/> .

@prefix dct: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qb: <http://purl.org/linked-data/cube#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

sensor:BME280 a owl:Class ;
    dct:description """This sensor measures:
     - temperature in degrees celsius
     - PM10
    """ ;
    rdfs:subClassOf sosa:Sensor ;
    skos:prefLabel "BME280" ;
    sosa:observes [ qudt:hasUnit unit:DEG_C ;
            skos:broader property:temperature ] ,
          [ qudt:hasUnit unit:MicroGM-PER-M3 ;
            skos:broader property:pm10 ;
            ssn:implements [ qb:order 1 ;
                    skos:broader procedure:pm-humidity-correction ] ] ;
.

property:pm10 a sosa:ObservableProperty ;
  rdfs:label "Particulate matter < 10 µm" ;
.

property:temperature a sosa:ObservableProperty ;
  rdfs:label "Air temperature" ;
.

procedure:pm-humidity-correction a sosa:Procedure ;
  rdfs:label "Humidity correction for Particulate Matter" ;
.
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_12_1.ttl">Open in new window</a>
</blockquote>



## Example entailments.shacl.ttl



```turtle
ex:ObservationEntailments
  a sh:NodeShape ;
  sh:targetClass sosa:Observation ;
  sh:rule [
    a sh:SPARQLRule ;
    sh:construct """
        CONSTRUCT {
            $this sosa:hasResult [
                  qudt:numericValue ?simpleResult ;
                  qudt:unit ?unit ;
                ] ;
                sosa:usedProcedure ?procedure ;
            .
        } WHERE {
            $this sosa:madeBySensor/rdf:type ?sensorClass ;
                sosa:observedProperty ?observedProperty ;
                sosa:hasSimpleResult ?simpleResult .
            {
              ?sensorClass rdfs:subClassOf sosa:Sensor ;
                sosa:observes ?observedProperty .
              OPTIONAL { ?sensorClass qudt:unit ?unit }
              OPTIONAL { ?sensorClass sosa:implements ?procedure }
            } UNION {
              ?sensorClass rdfs:subClassOf sosa:Platform ;
                owl:equivalentClass ?restriction .
              ?restriction a owl:Restriction ;
                owl:onProperty sosa:hosts ;
                owl:allValuesFrom/owl:unionOf/rdf:rest*/rdf:first ?actualSensorClass .
              ?actualSensorClass sosa:observes ?observedProperty .
              OPTIONAL { ?actualSensorClass qudt:unit ?unit }
              OPTIONAL { ?actualSensorClass sosa:implements ?procedure }
            }
        }
    """ ;
  ] ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_13_1.ttl">Open in new window</a>
</blockquote>



## Example observation-inferred.ttl



```turtle
@prefix sensor: <https://example.com/sensors/> .
@prefix property: <https://example.com/properties/> .
@prefix procedure: <https://example.com/procedures/> .

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix qb: <http://purl.org/linked-data/cube#> .
@prefix unit: <http://qudt.org/vocab/unit/> .

_:obs75134 a sosa:Observation ;
  sosa:madeBySensor [
    a sensor:BME280 ;
    dct:identifier "SN/2313Q432"
  ] ;
  sosa:observedProperty property:pm10 ;
  sosa:hasSimpleResult 0.323 ;
  sosa:hasResult [
    qudt:numericValue 0.323 ;
    qudt:unit unit:MicroGM-PER-M3 ;
  ] ;
  sosa:usedProcedure [ qb:order 1 ; skos:broader procedure:pm-humidity-correction ] ;
.
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_14_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex7.ttl



```turtle
ex:TemperatureSensor a owl:Class ;
  rdfs:subClassOf sosa:System .

<TemperatureSensor/1> a ex:TemperatureSensor , sosa:System .

<Observation/1> a sosa:Observation ;
  sosa:madeBySensor <TemperatureSensor/1> .

<TemperatureSensor/2> a ex:TemperatureSensor , sosa:System .

<Observation/2> a sosa:Observation ;
  sosa:madeBySensor <TemperatureSensor/2> .

# describing the system capabilities and operating/survival range can be done at the level of 
# the class or at the level of each instance with this modeling choice:

ex:TemperatureSensor  rdfs:subClassOf [
    owl:onProperty ssn-system:hasOperatingRange ;
    owl:hasValue ex:TemperatureSensorOperatingRange ] .

<TemperatureSensor/1> 
  ssn-system:hasOperatingRange ex:TemperatureSensorOperatingRange ; # this axiom can be inferred
  ssn-system:hasOperatingRange <moreSpecificTemperatureSensorOperatingRange> .

<moreSpecificTemperatureSensorOperatingRange> a ssn-system:OperatingRange ;
  ssn-system:inCondition <modeSpecificTemperatureCondition> , <modeSpecificHumidityCondition> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_15_1.ttl">Open in new window</a>
</blockquote>



## Example tree-height-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# rangefinder #30 is a laser range finder sensor that was used 
# to observe the height of tree #124 and #125.

<rangefinder/30>        rdf:type           sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .

# rangefinder #30 made observation #1087 of the height of tree #124.

<observation/1087>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest  <tree/124> ;
  sosa:observedProperty  <tree/124/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:hasUnit unit:M ; 
    qudt:numericValue "15.3"^^xsd:double ] .

<tree/124>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en .

<tree/124#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #124"@en .

# rangefinder #30 made observation #1088 of the height of tree #125.

<observation/1088>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1088"@en ;
  sosa:hasFeatureOfInterest  <tree/125> ;
  sosa:observedProperty  <tree/125/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:numericValue "23.0"^^xsd:double ;
    qudt:hasUnit unit:M ] .

<tree/125>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #125"@en .

<tree/125#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #125"@en .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_16_1.ttl">Open in new window</a>
</blockquote>



## Example ice-core-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
@base <http://example.org/data/> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. 

<http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
  sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .

<iceCore/12> rdf:type sosa:Sample ;
  sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
  sosa:isResultOf <WellDrilling/4578> ;
  sosa:madeBySampler <thermalDrill/2> .

  <WellDrilling/4578> a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult <iceCore/12> ;
    sosa:madeBySampler <thermalDrill/2> ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .

<iceCore/12#observation> a sosa:Observation ;
  sosa:observedProperty <iceCore/12#CO2> ;
  sosa:hasSimpleResult 240 .

  
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_17_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex22.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .

@prefix rdfp: <https://w3id.org/rdfp/>.

@base <http://example.org/data/> .


<DHT22#Procedure> a sosa:Procedure .

<DHT22/4578> a sosa:Platform ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> .


<DHT22/4578#TemperatureSensor> a sosa:Sensor ;
  sosa:isHostedBy <DHT22/4578> ;
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en .


<observation/1087> a sosa:Observation ;
  sosa:madeBySensor <DHT22/4578#TemperatureSensor> ;
  sosa:usedProcedure <DHT22#Procedure> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_18_1.ttl">Open in new window</a>
</blockquote>



## Example 02-homo-vs-summar-collection.ttl



```turtle
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

@prefix ex: <http://example.org/> .

ex:OC1
  a sosa:ObservationCollection ;
  sosa:hasFeatureOfInterest ex:Sample_1 ;
  sosa:observedProperty ex:op2 ;
  sosa:usedProcedure ex:p3 ;
  sosa:hasMember ex:O2 ;
  sosa:hasMember ex:O3 ;
  sosa:hasMember ex:O4 ;
  sosa:hasMember ex:O5 ;
  skos:note """homogeneous collection - member observations have a common FoI, oP and Procedure""" ;
.
ex:OC2
  a sosa:ObservationCollection ;
  sosa:hasFeatureOfInterest ex:Sample_1 ;
  sosa:observedProperty ex:op2 ;
  sosa:usedProcedure ex:p3 ;
  sosa:madeBySensor ex:s4 ;
  sosa:madeBySensor ex:s5 ;
  sosa:phenomenonTime [
      time:hasBeginning [
          time:inXSDDateTime "2018-03-10T15:09:00+10:00"^^xsd:dateTime ;
        ] ;
      time:hasEnd [
          time:inXSDDateTime "2018-03-10T15:12:00+10:00"^^xsd:dateTime ;
        ] ;
    ] ;
  sosa:hasMember ex:O2 ;
  sosa:hasMember ex:O3 ;
  sosa:hasMember ex:O4 ;
  sosa:hasMember ex:O5 ;
  skos:note """general collection - member observations have a common FoI, oP and Procedure
  `madeBySensor` is repeated to enumerate the sensors used in the member observations
  `phenomenonTime` is a time interval that encompasses the times of the member observations""" ;
.
ex:O2
  a sosa:Observation ;
  sosa:madeBySensor ex:s4 ;
  sosa:hasResult ex:r96 ;
  sosa:phenomenonTime [
      time:inXSDDateTime "2018-03-10T15:09:00+10:00"^^xsd:dateTime ;
    ] ;
.
ex:O3
  a sosa:Observation ;
  sosa:madeBySensor ex:s4 ;
  sosa:hasResult ex:r97 ;
  sosa:phenomenonTime [
      time:inXSDDateTime "2018-03-10T15:10:00+10:00"^^xsd:dateTime ;
    ] ;
.
ex:O4
  a sosa:Observation ;
  sosa:madeBySensor ex:s5 ;
  sosa:hasResult ex:r98 ;
  sosa:phenomenonTime [
      time:inXSDDateTime "2018-03-10T15:11:00+10:00"^^xsd:dateTime ;
    ] ;
.
ex:O5
  a sosa:Observation ;
  sosa:madeBySensor ex:s5 ;
  sosa:hasResult ex:r99 ;
  sosa:phenomenonTime [
      time:inXSDDateTime "2018-03-10T15:12:00+10:00"^^xsd:dateTime ;
    ] ;
.
ex:Sample_1
  a sosa:Sample ;
  sosa:isSampleOf ex:foia ;
.
ex:foia
  a sosa:FeatureOfInterest ;
  sosa:hasProperty ex:op2 ;
.
ex:s4
  a sosa:Sensor ;
  sosa:implements ex:p3 ;
.
ex:s5
  a sosa:Sensor ;
  sosa:implements ex:p3 ;
.
ex:op2
  a sosa:ObservableProperty ;
.
ex:p3
  a sosa:Procedure ;
.
ex:examples-collection-obs
  a owl:Ontology ;
  dcterms:created "2023-11-04"^^xsd:date ;
  dcterms:creator <http://orcid.org/0000-0002-3884-3420> ;
  rdfs:comment "Small dataset to test rules in SOSA Collections" ;
  owl:imports <http://www.w3.org/ns/sosa-collections/> , 
    <http://www.w3.org/2006/time> , 
    <http://purl.org/dc/elements/1.1/> ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_19_1.ttl">Open in new window</a>
</blockquote>



## Example ip68.ttl



```turtle
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix gr: <http://purl.org/goodrelations/v1#> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix schema: <http://schema.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix prov: <http://www.w3.org/ns/prov#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix seas: <https://w3id.org/seas/>.
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

@base <https://data.grandlyon.com/> .

<Organization/1> a org:Organization ;
    owl:sameAs <http://dbpedia.org/page/Metropolis_of_Lyon> .

<Air> a sosa:FeatureOfInterest ;
  rdfs:label "The air."@en .

<IP68_Outdoor_Temperature_Sensor> a owl:Class , gr:ProductOrServiceModel ;
  gr:name "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:label "IP68 Outdoor Temperature Sensor"@en ;
  rdfs:subClassOf [
    owl:onProperty ssn-system:hasOperatingRange ;
    owl:hasValue <IP68_Outdoor_Temperature_Sensor#operatingRange> ] ;
  rdfs:subClassOf [
    owl:onProperty ssn-system:hasSystemCapability ;
    owl:hasValue <IP68_Outdoor_Temperature_Sensor#systemCapability> ] .

<IP68_Outdoor_Temperature_Sensor#operatingRange> a ssn-system:OperatingRange , sosa:Property ;
  ssn-system:inCondition <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> .

<IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A temperature range of -20 to 70 Celsius."@en ;
  schema:minValue -20.0 ;
  schema:maxValue 70.0 ;
  schema:unitCode unit:DegreeCelsius .

<IP68_Outdoor_Temperature_Sensor#systemCapability> a sosa:Property , ssn-system:SystemCapability ;
  rdfs:comment "The sensor capability in normal operating conditions."@en ;
  ssn-system:hasSystemProperty <IP68_Outdoor_Temperature_Sensor#RFSensitivity> , <IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy> , <IP68_Outdoor_Temperature_Sensor#TemperatureResolution> , <IP68_Outdoor_Temperature_Sensor#BatteryAccuracy> , <IP68_Outdoor_Temperature_Sensor#BatteryResolution> ;
  ssn-system:inCondition <IP68_Outdoor_Temperature_Sensor#normalOperatingCondition> .

<IP68_Outdoor_Temperature_Sensor#RFSensitivity> a sosa:Property , ssn-system:Sensitivity , schema:PropertyValue ;
  schema:value -137 ;
  schema:unitCode unit:DecibelReferredToOneMilliwatt .

<IP68_Outdoor_Temperature_Sensor#TemperatureAccuracy> a sosa:Property , ssn-system:Accuracy , schema:PropertyValue ;
  sosa:forProperty <Air?lat=45.75&long=4.85#temperature> ;
  schema:minValue -0.2 ;
  schema:maxValue 0.2 ;
  schema:unitCode unit:DegreeCelsius .

<IP68_Outdoor_Temperature_Sensor#TemperatureResolution> a sosa:Property , ssn-system:Resolution , schema:PropertyValue ;
  sosa:forProperty <Air?lat=45.75&long=4.85#temperature> ;
  schema:value 0.0625 ;
  schema:unitCode unit:DegreeCelsius .

<IP68_Outdoor_Temperature_Sensor#BatteryResolution> a sosa:Property , ssn-system:Resolution , schema:PropertyValue ;
  sosa:forProperty <Sensor/SL-T-P1#battery> ;
  schema:value 3.937e-3 ;
  schema:unitCode unit:PERCENT .

<Air?lat=45.75&long=4.85> a sosa:Sample ;
  rdfs:label "The air at lat 45.75 and long 4.85."@en ;
  sosa:isSampleOf <Air> ;
  sosa:hasProperty <Air?lat=45.75&long=4.85#temperature> .

<Air?lat=45.75&long=4.85#temperature> a sosa:Property , sosa:ObservableProperty ;
  sosa:isPropertyOf <Air?lat=45.75&long=4.85> .

<Sensor/SL-T-P1> a gr:ProductOrService, sosa:Sensor , seas:LoRaCommunicationDevice , <IP68_Outdoor_Temperature_Sensor> ;
    gr:hasBrand [ a gr:Brand ; gr:name "Sensing Labs"@en ] ;
    geo:alt 100.0 ;
    geo:lat 45.75 ;
    geo:lon 4.85 ;
    sosa:implements <IP68_Outdoor_Temperature_Sensor#temperatureSensingProcedure> ;
    sosa:implements <IP68_Outdoor_Temperature_Sensor#batterySensingProcedure> ;
    sosa:observes <Sensor/SL-T-P1#battery> ;
    sosa:observes <Air?lat=45.75&long=4.85#temperature> .

<Deployment/SL-T-P1/2017-06-06> a sosa:Deployment ;
  sosa:deployedSystem <Sensor/SL-T-P1> ;
  prov:startedAtTime "2017-06-06"^^xsd:date ;
  prov:wasAssociatedWith <Organization/1> ;
  sosa:deployedOnPlatform <Tree/1> .

<Observation/5872357#temperature> a sosa:Observation ;
    sosa:hasSimpleResult "64.5244681928429 Cel"^^cdt:ucum ;
    sosa:madeBySensor <Sensor/SL-T-P1> ;
    sosa:hasFeatureOfInterest <Air?lat=45.75&long=4.85> ;
    sosa:observedProperty <Air?lat=45.75&long=4.85#temperature> ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .

<Observation/5872357#battery> a sosa:Observation ;
    sosa:hasSimpleResult "73.2 %"^^cdt:ucum ;
    sosa:madeBySensor <Sensor/SL-T-P1> ;
    sosa:hasFeatureOfInterest <Sensor/SL-T-P1> ;
    sosa:observedProperty <Sensor/SL-T-P1#battery> ;
    sosa:resultTime "2017-06-20T21:49:18+00:00"^^xsd:dateTime .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_20_1.ttl">Open in new window</a>
</blockquote>



## Example dht22-deployment-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .

@base <http://example.org/data/> .


<Room145> a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample <Room145/east> ;
  sosa:hasSample <Room145/south> .

  <Room145/east> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "East wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
    sosa:hosts <PCBBoard1> .

  <Room145/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
    sosa:hosts <PCBBoard2> .


<Room245> a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty <Room245#temperature> , <Room245#humidity> ;
  sosa:hasSample <Room245/south> .

  <Room245/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #245."@en ;
    sosa:hosts <PCBBoard3> .


<PCBBoard1> a sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently."@en ;
  sosa:hosts <DHT22/4578> .

  <DHT22/4578> a sosa:Platform ;
    rdfs:label "DHT22 sensor #4578"@en ;
    sosa:isHostedBy <PCBBoard1> .


<PCBBoard2> a sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanentlys."@en ;
  sosa:hosts <DHT22/4578> .

  <DHT22/4579> a sosa:Platform ;
    rdfs:label "DHT22 sensor #4579."@en ;
    sosa:isHostedBy <PCBBoard2> .


<PCBBoard3> a sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently."@en ;
  sosa:hosts <DHT22/4578> .

  <DHT22/4580> a sosa:Platform ;
    rdfs:label "DHT22 sensor #4580."@en ;
    sosa:isHostedBy <PCBBoard3> .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_21_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex12.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# rangefinder #30 is a laser range finder sensor that was used 
# to observe the height of tree #124 and #125.

<rangefinder/30>        rdf:type           sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .

# rangefinder #30 made observation #1087 of the height of tree #124.

<observation/1087>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest  <tree/124> ;
  sosa:observedProperty  <tree/124/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:hasUnit unit:M ; 
    qudt:numericalValue "15.3"^^xsd:double ] .

# using SSN, one can explicitly link a property and its feature of interest.
 
<tree/124>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en ;
  sosa:hasProperty <tree/124#height> .

<tree/124#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #124"@en ;
  sosa:isPropertyOf <tree/124> .

# rangefinder #30 made observation #1088 of the height of tree #125.

<observation/1088>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1088"@en ;
  sosa:hasFeatureOfInterest  <tree/125> ;
  sosa:observedProperty  <tree/125/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:numericValue "23.0"^^xsd:double ;
    qudt:hasUnit unit:M ] .

# using SSN, one can explicitly link a property and its feature of interest.
 
<tree/125>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #125"@en ;
  sosa:hasProperty <tree/125#height> .

<tree/125#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #125"@en ;
  sosa:isPropertyOf <tree/124> .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_22_1.ttl">Open in new window</a>
</blockquote>



## Example sunspots.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <http://example.org/data/> .

# The result of an observation of the sunspot number is available a few minutes 
# after the phenomenon time, due to the light travel duration.

<Observation/7536> rdf:type sosa:Observation ;
  sosa:observedProperty  <Sun#sunspotNumber> ;
  sosa:hasSimpleResult 66 ;
  sosa:phenomenonTime [
    rdf:type time:Instant ;
    time:inXSDDateTimeStamp "2017-03-31T11:51:42+00:00"^^xsd:dateTimeStamp ] ;
  sosa:resultTime "2017-03-31T12:00:00+00:00"^^xsd:dateTimeStamp .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_23_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex20.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
@base <http://example.org/data/> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. 

<http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
  sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .

<iceCore/12> rdf:type sosa:Sample ;
  sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
  sosa:isResultOf <WellDrilling/4578> ;
  sosa:madeBySampler <thermalDrill/2> .

  <WellDrilling/4578> a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult <iceCore/12> ;
    sosa:madeBySampler <thermalDrill/2> ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .

<iceCore/12#observation> a sosa:Observation ;
  sosa:observedProperty <iceCore/12#CO2> ;
  sosa:hasSimpleResult 240 .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_24_1.ttl">Open in new window</a>
</blockquote>



## Example spinning-cups.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <http://example.org/data/> .

# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:observes <location/4687#windSpeed> .

# wind sensor #14 detected some movement of spinning cups, from which originated the
# observations #147 and #148.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:madeObservation <observation/147> , <observation/148> ; 
  sosa:detects <observation/147#spinningCupsMovement> , <observation/148#spinningCupsMovement> .

# observation #147 was originated by the movement of the spinning cups of sensor #14.
# the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure.

<observation/147> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:wasOriginatedBy <observation/147#spinningCupsMovement> ;
  sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^<speed> .

<observation/147#spinningCupsMovement> rdf:type sosa:Stimulus ;
  sosa:isProxyFor <location/4687#windSpeed> .

<observation/148> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:wasOriginatedBy <observation/148#spinningCupsMovement> ;
  sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "43 km/h"^^<speed> .

<observation/148#spinningCupsMovement> rdf:type sosa:Stimulus ;
  sosa:isProxyFor <location/4687#windSpeed> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_25_1.ttl">Open in new window</a>
</blockquote>



## Example house134.ttl



```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .
@prefix sampling: <http://www.w3.org/ns/sosa/sampling/> .
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix rdfp: <https://w3id.org/rdfp/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix schema: <http://schema.org/> .
@prefix qudt: <http://qudt.org/schema/qudt#> .
@prefix qudt: <http://qudt.org/1.1/schema/qudt> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base  <http://example.org/> .


<house/134> a sosa:FeatureOfInterest ;
	rdfs:comment "House #134."@en .

<floralCouch> a sosa:FeatureOfInterest ;
	rdfs:comment "The lumpy 2-seater couch with the floral pattern."@en .

<roofInsulation> a sosa:FeatureOfInterest ;
	rdfs:comment "The insulation material in the roof of house #134."@en .

# the window opening state is an ActuatableProperty.
# SSN allows to explicitly say that <window/104#state> is a property of <window>

<window> a sosa:FeatureOfInterest ;
	sosa:hasProperty <window/104#state> .

<window/104#state> a sosa:ActuatableProperty ;
	sosa:isActedOnBy <actuation/188> .

<house/134/kitchen> a sosa:Sample, sosa:Platform ;
	rdfs:label "House #134 Kitchen."@en ;
	rdfs:comment "House #134 Kitchen that hosts PCBoard1 and PCBoard2."@en ;
	sosa:hosts <PCBBoard1>, <PCBBoard2> ;
	sosa:isSampleOf <house/134> .

<house/134/bedroom> a sosa:Sample ;
	sosa:isSampleOf <house/134> .

<AtmosphericTemperature> rdfs:subClassOf sosa:ObservableProperty .
 
<AmbientTemperature> rdfs:subClassOf <AtmosphericTemperature> .

<temperature> a sosa:ObservableProperty, qudt:QuantityKind ;
	rdfs:label "Thermodynamic Temperature"@en .
  
<airTemperature> a sosa:Property, sosa:ObservableProperty, qudt:QuantityKind, <AmbientTemperature> ;
	qudt:generalization <temperature> ;
	sosa:isPropertyOf <house/134/bedroom>, <house/134/kitchen> .
 
<soilTemperature> a sosa:ObservableProperty, qudt:QuantityKind ;
	qudt:generalization <temperature> .
 
<waterTemperature> a sosa:ObservableProperty, qudt:QuantityKind ;
	qudt:generalization <temperature> .
 
<tapWaterTemperature> a sosa:ObservableProperty, qudt:QuantityKind ;
	qudt:generalization <waterTemperature> .
 
<poolWaterTemperature> a sosa:ObservableProperty, qudt:QuantityKind ;
	qudt:generalization <waterTemperature> .

<nest/D1AA22A8211> a sosa:Platform ;
	rdfs:label "3rd gen Nest Learning Thermostat D1AA22A8211"@en ;
	rdfs:comment "Nest Thermostat in bedroom of house #134"@en ;
	sosa:hosts <sensor/926> .

<sensor/926> a sosa:Sensor ;
	rdfs:label "Nest temperature sensor #1"@en ;
	sosa:observes  <airTemperature> ;
	sosa:madeObservation <observation/235714>, <observation/235715>, <observation/235716> .
  
<PCBBoard1> a sosa:System ;
	rdfs:label "PCB Board 1"@en ;
	rdfs:comment "PCB Board 1 hosts DHT22 temperature sensor #1."@en ;
	sosa:hosts <DHT22/1> .
    
<PCBBoard2> a sosa:System ;
	rdfs:label "PCB Board 2"@en ;
	rdfs:comment "PCB Board 2 hosts DHT22 temperature sensor #2."@en ;
	sosa:hosts <DHT22/2> .
	
<DHT22/4578#TemperatureSensor> a sosa:Sensor, sosa:System ;
	rdfs:comment "The DHT22 #4578 embedded temperature sensor."@en ;
	ssn-system:hasSystemCapability <DHT22TempCapability> .
  
<DHT22TempCapability> a sosa:Property, ssn-system:SystemCapability ;
	rdfs:comment "The capabilities of the temperature sensor in normal temperature conditions."@en;
	ssn-system:inCondition <normalTemp> ;
	ssn-system:hasSystemProperty <DHT22TempSensitivity> .
  
<normalTemp> a ssn-system:Condition, schema:PropertyValue ;
	rdfs:comment "A temperature range of -40 to 80 Celsius."@en ;
	schema:minValue -40.0 ;
	schema:maxValue 80.0 ;
	schema:unitCode unit:DegreeCelsius .

<DHT22TempSensitivity> a sosa:Property, ssn-system:Sensitivity, ssn-system:Resolution, schema:PropertyValue ;
	rdfs:comment "The sensitivity and resolution of the temperature sensor is 0.1 °C in normal temperature and humidity conditions."@en ;
	schema:value 0.1 ;
	schema:unitCode unit:DegreeCelsius .

<house/134/deployment> a sosa:Deployment ;
	rdfs:comment "Deployment of PCB Board 1 and 2 in the kitchen for the purpose of observing the temperature."@en ;
	sosa:deployedOnPlatform <house/134/kitchen> ;
	sosa:deployedSystem <PCBBoard1>, <PCBBoard2> ;
	sosa:forProperty <airTemperature> .

<sensor/927> a sosa:Sensor ;
	sosa:implements <summingHourlyConsumptionProcedure> .
	
<summingHourlyConsumptionProcedure> a sosa:Procedure ;
	sosa:hasOutput <electricityConsumption> ;
	sosa:hasOutput [
		rdfp:presentedBy [ 
			rdfp:validationRule <consumption.schema.json> ;
			rdfp:liftingRule <lifting-rule.rqg>
		]
	] .

<observation/235714> a sosa:Observation ;
	sosa:hasFeatureOfInterest <house/134/bedroom> ;
	sosa:observedProperty <airTemperature> ;
	sosa:madeBySensor <sensor/926> ;
	sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp ;
	sosa:phenomenonTime [
		a time:Interval ;
		time:hasBeginning [ 
			a time:Instant ;
			time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp
		] ;
    	time:hasEnd [ 
			a time:Instant ;
			time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp
		]
	] .

# The air temperature in the kitchen of house #134 was 23.9°C.

<observation/235715> a sosa:Observation ;
	sosa:resultTime "2017-11-15T14:35:13Z"^^xsd:dateTime ;
	sosa:hasSimpleResult "23.9 DEG"^^cdt:temperature .
   
<observation/235716> a sosa:Observation ;
	sosa:hasResult [
		a qudt:QuantityValue ;
		qudt:hasUnit unit:DegreeCelsius ;
		qudt:numericValue "22.9"^^xsd:double
	] .

# The electric consumption in the kitchen of house #134 was 22.4 kWh as 
# observed by sensor #927.

<observation/235727> a sosa:Observation ;
	sosa:hasFeatureOfInterest <house/134/kitchen> ;
	sosa:observedProperty <electricConsumption> ;
	sosa:madeBySensor <sensor/927> ; 
	sosa:hasSimpleResult "22.4 kWh"^^cdt:ucum ;
	sosa:hasResult <observation/235727/result> .
	
# The air temperature in the kitchen of house #134 was observed by the DHT22 #4578 embedded temperature sensor.

<observation/235728> a sosa:Observation ;
  sosa:hasFeatureOfInterest <house/134/kitchen> ;
  sosa:observedProperty <airTemperature> ;
  sosa:madeBySensor <DHT22/4578#TemperatureSensor> .
	
<observation/s1/5> a sosa:Observation ;
	sosa:hasFeatureOfInterest <sample/134g1> ;
	sosa:observedProperty <soil-pH> ;
	sosa:phenomenonTime [ 
		a time:Instant ; 
		time:inXSDDateTimeStamp "2017-12-04T08:14:00:00+10:00"^^xsd:dateTimeStamp ;
	] ;
	sosa:resultTime "2017-12-12T10:24:00:00+10:00"^^xsd:dateTime ;
	sosa:hasSimpleResult "6.1"^^cdt:pH .  
  
<sampling/4578> a sosa:Sampling ;
	geo:lat -37.9076 ; 
	geo:long 145.0294 ;
	sosa:madeBySampler <trowel> ;
	sosa:hasFeatureOfInterest <house/134/garden> ;
	sosa:resultTime "2017-12-04T08:14:00:00+10:00"^^xsd:dateTime ;
	sosa:hasResult <sample/134g1> .
  
<sample/134g1> a sosa:Sample ;
	sosa:isSampleOf <house/134/garden> ;
	sosa:isResultOf <sampling/4578> .
	
<sample/134g1/organics> a sosa:Sample ;
	rdfs:label "Soil sample 134g1 organic fraction" ;
	sampling:hasSampleRelationship [
		a sampling:SampleRelationship ;
		sampling:natureOfRelationship <http://soil.example.org/rel/organic-fraction> ;
		sampling:relatedSample <sample/134g1> ;
	] ;
	sosa:isResultOf <sampling/4650> .

<sampling/4650> a sosa:Sampling ;
    sosa:featureOfInterest <sample/134g1> ;
    sosa:usedProcedure <procedure/soil-organic-fraction/78> . 
    
<procedure/soil-organic-fraction/78> a sosa:Procedure ;
    rdfs:comment "... details of procedure to separate the organic fraction of a soil sample ..." .


# WindowCloser #987 made actuation #188
# SSN allows to explicitly say that <windowCloser/987> is designed to automatically open and close window #104.

<windowCloser/987> rdf:type sosa:Actuator ;
	sosa:madeActuation <actuation/188> ;
	sosa:forProperty <window/104#state> .

# Actuation #188 acted on the state of window #104 and returned 'true'.

<actuation/188> a sosa:Actuation ;
	sosa:actsOnProperty <window/104#state> ;
	sosa:actuationMadeBy <windowCloser/987> ;
	sosa:hasFeatureOfInterest  <window/104> ;
	sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp ;
	sosa:hasSimpleResult true ;
	sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_26_1.ttl">Open in new window</a>
</blockquote>



## Example seismograph.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time.

<earth>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "earth"@en .

<VCAB-DP1-BP-40> rdf:type sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
  sosa:observes <VCAB-DP1-BP-40#groundDisplacementSpeed> .

<VCAB-DP1-BP-40#location> rdf:type sosa:FeatureOfInterest ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:lat 35.8648067 ;
  geo:long -120.6195831 ;
  geo:alt 12.75 ;
  sosa:isSampleOf <earth> .

<VCAB-DP1-BP-40#groundDisplacementSpeed>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
  sosa:isObservedBy <VCAB-DP1-BP-40> .

<VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00> rdf:type sosa:Observation ;
  sosa:madeBySensor <VCAB-DP1-BP-40> ; 
  sosa:hasFeatureOfInterest  <VCAB-DP1-BP-40#location> ;
  sosa:observedProperty  <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:numericValue "5e-4"^^xsd:double ;
     qudt:hasUnit unit:CentiM-PER-SEC ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .

# Using SSN one can explicitly state that <VCAB-DP1-BP-40#groundDisplacementSpeed> is the property of <VCAB-DP1-BP-40#location> .

<VCAB-DP1-BP-40#location> sosa:hasProperty <VCAB-DP1-BP-40#groundDisplacementSpeed> .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_27_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex16.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <http://example.org/data/> .

# The result of an observation of the sunspot number is available a few minutes 
# after the phenomenon time, due to the light travel duration.

<Observation/7536> rdf:type sosa:Observation ;
  sosa:observedProperty  <Sun#sunspotNumber> ;
  sosa:hasSimpleResult 66 ;
  sosa:phenomenonTime [
    rdf:type time:Instant ;
    time:inXSDDateTimeStamp "2017-03-31T11:51:42+00:00"^^xsd:dateTimeStamp ] ;
  sosa:resultTime "2017-03-31T12:00:00+00:00"^^xsd:dateTimeStamp .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_28_1.ttl">Open in new window</a>
</blockquote>



## Example apartment-134.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# The electric consumption of appartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:observedProperty  <Appartment/134/electricConsumption> ;
  sosa:madeBySensor <sensor/926> ; 
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:numericValue "22.4"^^xsd:double ;
     qudt:hasUnit unit:Kilowatthour ] ;
  sosa:phenomenonTime [
    rdf:type time:Interval ;
    time:hasBeginning [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
    time:hasEnd [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .


# Sensor #926 observes the electric consumption of appartment #134, and we know that 
# it made some observations.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <Appartment/134/electricConsumption> ;
  sosa:madeObservation <Observation/235714>, <Observation/235715>, <Observation/235716> .

# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. 

<tempSensor/23> rdf:type sosa:Sensor ;
  sosa:observes  <tempSensor/23#temperature> ;
  sosa:madeObservation <tempSensor/23/4572>, <tempSensor/23/4573>, <tempSensor/23/4574> .


# Sensor #926 observes the electric consumption of appartment #134

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <Appartment/134/electricConsumption> .

# This is equivalent to saying that the electric consumption of appartment #134 is 
# observed by Sensor #926

<Appartment/134/electricConsumption> rdf:type sosa:ObservableProperty ;
  sosa:isObservedBy <sensor/926>  .


# Sensor #926 made observations identified by <Observation/235714> and <Observation/235715>.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:madeObservation <Observation/235714>, <Observation/235715> .

# This is equivalent to saying that these observations have been made by sensor #926.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .

<Observation/235754> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .


# the window opening state is an ActuatableProperty.
# SSN allows to explicitly say that <window/104#state> is a property of <window>

<window> rdf:type sosa:FeatureOfInterest ;
  sosa:hasProperty <window/104#state> .

<window/104#state> rdf:type sosa:ActuatableProperty ;
  sosa:isActedOnBy <actuation/188> .


# WindowCloser #987 made actuation #188
# SSN allows to explicitly say that <windowCloser/987> is designed to automatically open and close window #104.

<windowCloser/987> rdf:type sosa:Actuator ;
  sosa:madeActuation <actuation/188> ;
  sosa:forProperty <window/104#state> .


# Actuation #188 acted on the state of window #104 and returned 'true'.

<actuation/188> rdf:type sosa:Actuation ;
  sosa:actsOnProperty  <window/104#state> ;
  sosa:actuationMadeBy <windowCloser/987> ; 
  sosa:hasSimpleResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_29_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex10.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:observedProperty  <apartment/134/electricConsumption> ;
  sosa:madeBySensor <sensor/926> ; 
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:numericValue "22.4"^^xsd:double ;
     qudt:hasUnit unit:KiloW-HR ] ;
  sosa:phenomenonTime [
    rdf:type time:Interval ;
    time:hasBeginning [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
    time:hasEnd [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .


# Sensor #926 observes the electric consumption of apartment #134, and we know that 
# it made some observations.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <apartment/134/electricConsumption> ;
  sosa:madeObservation <Observation/235714>, <Observation/235715>, <Observation/235716> .

# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. 

<tempSensor/23> rdf:type sosa:Sensor ;
  sosa:observes  <tempSensor/23#temperature> ;
  sosa:madeObservation <tempSensor/23/4572>, <tempSensor/23/4573>, <tempSensor/23/4574> .


# Sensor #926 observes the electric consumption of apartment #134

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <apartment/134/electricConsumption> .

# This is equivalent to saying that the electric consumption of apartment #134 is 
# observed by Sensor #926

<apartment/134/electricConsumption> rdf:type sosa:ObservableProperty ;
  sosa:isObservedBy <sensor/926>  .


# Sensor #926 made observations identified by <Observation/235714> and <Observation/235715>.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:madeObservation <Observation/235714>, <Observation/235715> .

# This is equivalent to saying that these observations have been made by sensor #926.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .

<Observation/235754> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .


# the window opening state is an ActuatableProperty.
# SSN allows to explicitly say that <window/104#state> is a property of <window>

<window> rdf:type sosa:FeatureOfInterest ;
  sosa:hasProperty <window/104#state> .

<window/104#state> rdf:type sosa:ActuatableProperty ;
  sosa:isActedOnBy <actuation/188> .


# WindowCloser #987 made actuation #188
# SSN allows to explicitly say that <windowCloser/987> is designed to automatically open and close window #104.

<windowCloser/987> rdf:type sosa:Actuator ;
  sosa:madeActuation <actuation/188> ;
  sosa:forProperty <window/104#state> .


# Actuation #188 acted on the state of window #104 and returned 'true'.

<actuation/188> rdf:type sosa:Actuation ;
  sosa:actsOnProperty  <window/104#state> ;
  sosa:actuationMadeBy <windowCloser/987> ; 
  sosa:hasSimplResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_30_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex5.ttl



```turtle
ex:Temperature a owl:Class ;
  rdfs:subClassOf sosa:Property .

<office/1> a sosa:FeatureOfInterest;
  sosa:hasProperty <office/1/temperature> . 

<office/1/temperature> a ex:Temperature , sosa:Property .

<Observation/1> a sosa:Observation ;
  sosa:observedProperty <office/1/temperature> ;
  sosa:hasFeatureOfInterest <office/1> .

<office/2> a sosa:FeatureOfInterest;
  sosa:hasProperty <office/2/temperature> . 

<office/2/temperature> a ex:Temperature , sosa:Property .

<Observation/2> a sosa:Observation ;
  sosa:observedProperty <office/2/temperature> ;
  sosa:hasFeatureOfInterest <office/2> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_31_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex19.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
@base <http://example.org/data/> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. 

<http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
  sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .

<iceCore/12> rdf:type sosa:Sample ;
  sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
  sosa:isResultOf <WellDrilling/4578> ;
  sosa:madeBySampler <thermalDrill/2> .

  <WellDrilling/4578> a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult <iceCore/12> ;
    sosa:madeBySampler <thermalDrill/2> ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .

<iceCore/12#observation> a sosa:Observation ;
  sosa:observedProperty <iceCore/12#CO2> ;
  sosa:hasSimpleResult 240 .

# using SSN one can explicitly state that <iceCore/12#CO2> is the property of <iceCore/12> .

<iceCore/12#CO2> sosa:isPropertyOf <iceCore/12> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_32_1.ttl">Open in new window</a>
</blockquote>



## Example spinning-cups-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <http://example.org/data/> .

# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:observes <location/4687#windSpeed> .

# wind sensor #14 made observations #147 and #148.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:madeObservation <observation/147> , <observation/148> .

# the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure.

<observation/147> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^<speed> .

<observation/148> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "43 km/h"^^<speed> .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_33_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex6.ttl



```turtle
ex:TemperatureSensor a sosa:System .

<Observation/1> a sosa:Observation ;
  sosa:madeBySensor ex:TemperatureSensor .

<Observation/2> a sosa:Observation ;
  sosa:madeBySensor ex:TemperatureSensor .

# describing the system capabilities and operating/survival range can be done generically 
# with this modeling choice:

ex:TemperatureSensor ssn-system:hasOperatingRange ex:TemperatureSensorOperatingRange .

ex:TemperatureSensorOperatingRange a ssn-system:OperatingRange ;
  ssn-system:inCondition ex:NormalTemperatureCondition , ex:NormalHumidityCondition .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_34_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex9.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.

@base <http://example.org/data/> .

 <COPR> a sosa:FeatureOfInterest ;
   sosa:hasSample <COPR_SL> ;
   rdfs:comment "Coal Oil Point Reserve: UC Santa Barbara Natural Reserve System"@en ;
   rdfs:label "Coal Oil Point Reserve"@en .

 <COPR_Station_Location> a sosa:Sample ;
   rdfs:comment "."@en ;
   rdfs:label "Air around COPR Station"@en ;
   sosa:isSampleOf <COPR> .
 
 <COPR_Station> a sosa:Platform ;
   rdfs:comment "Station at Coal Oil Point Reserve, CA (see http://www.geog.ucsb.edu/ideas/COPR.html for details)"@en ;
   rdfs:label "Coal Oil Point Reserve Wx Station"@en ;
   rdfs:seeAlso <http://www.geog.ucsb.edu/ideas/COPR.html> ;
   sosa:hosts <COPR-HMP45C-L> .
 
 <COPR-HMP45C-L> a sosa:Platform ;
   rdfs:label "HMP45C-L Temperature and Relative Humidity Probe at Coal Oil Point, UCSB, CA"@en ;
   sosa:hosts <HUMICAP-H> ;
   sosa:isHostedBy <COPR_Station> .

 <HUMICAP-H> a sosa:Sensor ;
   rdfs:label "Vaisala HUMICAP H-chip"@en ;
   sosa:isHostedBy <COPR-HMP45C-L> .

 <RelativeHumidity> a sosa:ObservableProperty ;
   rdfs:comment "Humidity is a measure of the moisture content of air."@en ;
   rdfs:label "Relative Humidity"@en .

 <MeasuringRelativeHumidityA23> a sosa:Procedure ;
   rdfs:comment "... detailed instructions for measuring relative humidity ..."@en ;
   .
  
 <RH_avg_1_COPR_15min_201706020300PM> a sosa:Observation ;
   rdfs:comment "Relative humidity as averaged over 15min at COPR."@en ;
   rdfs:label "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"@en ;
   sosa:madeBySensor <HUMICAP-H> ;
   sosa:hasFeatureOfInterest <COPR_Station_Location> ;
   sosa:hasSimpleResult "92.5 %"^^cdt:ucum ;
   sosa:resultTime "2017-06-02-T03:00:00-7:00"^^xsd:dateTime ;
   sosa:observedProperty <RelativeHumidity> ;
   sosa:usedProcedure <MeasuringRelativeHumidityA23> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_35_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex21.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix ex: <http://example.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .

@prefix rdfp: <https://w3id.org/rdfp/>.

@base <http://example.org/data/> .


<DHT22#Procedure> a sosa:Procedure ;
  sosa:hasOutput <DHT22#output> .

<DHT22#output> a sosa:Output , rdfp:GraphDescription ;
  rdfs:comment "The output is a RDF Graph that describes both the temperature and the humidity. It can be validated by a SHACL shapes graph."@en ;
  rdfp:presentedBy [
    a rdfp:GraphDescription ;
    rdfp:validationRule <shacl_shapes_graph> ;
  ] .


<DHT22/4578> a sosa:System ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> ;
  sosa:hasSubSystem <DHT22/4578#TemperatureSensor>, <DHT22/4578#HumiditySensor> .



<DHT22/4578#TemperatureSensor> a sosa:Sensor , sosa:System ;
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en ;
  ssn-system:hasOperatingRange <DHT22/4578#TemperatureSensorOperatingRange> ; 
  ssn-system:hasSystemCapability <DHT22/4578#TemperatureSensorCapability> ;
  sosa:implements <DHT22#Procedure> .

<DHT22/4578#HumiditySensor> a sosa:Sensor , sosa:System ;
  rdfs:comment "The embedded humidity sensor, a specific instance of humidity sensor."@en ;
  ssn-system:hasOperatingRange <DHT22/4578#HumiditySensorOperatingRange> ;
  sosa:implements <DHT22#Procedure> .



<DHT22/4578#TemperatureSensorOperatingRange> a ssn-system:OperatingRange ;
  rdfs:comment "The conditions in which the DHT22 temperature sensor is expected to operate."@en ;
  ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> .

<DHT22/4578#HumiditySensorOperatingRange> a ssn-system:OperatingRange ;
  rdfs:comment "The conditions in which the DHT22 humidity sensor is expected to operate."@en ;
  ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> .



<NormalOperatingCondition> a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A temperature range of -40 to 80 Celsius."@en ;
  schema:minValue -40.0 ;
  schema:maxValue 80.0 ;
  schema:unitCode unit:DegreeCelsius .

<NormalHumidityCondition> a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A relative humidity range of 5 to 85 %."@en ;
  schema:minValue 5.0 ;
  schema:maxValue 85.0 ;
  schema:unitCode unit:PERCENT .



<DHT22/4578#TemperatureSensorCapability> a sosa:Property , ssn-system:SystemCapability , schema:PropertyValue ;
  rdfs:comment "The capabilities of the temperature sensor in normal temperature and humidity conditions." ;
  ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> ;
  ssn-system:hasSystemProperty <DHT22/4578#TemperatureSensorAccuracy> , <DHT22/4578#TemperatureSensorSensitivity> , <DHT22/4578#TemperatureSensorRepeatability> , <DHT22/4578#TemperatureSensorFrequency> .

<DHT22/4578#TemperatureSensorAccuracy> a sosa:Property , ssn-system:Accuracy , schema:PropertyValue ;
  rdfs:comment "The accuracy of the temperature sensor is +-0.5 °C in normal temperature and humidity conditions."@en ;
  schema:minValue -0.5 ;
  schema:maxValue 0.5 ;
  schema:unitCode unit:DegreeCelsius .

<DHT22/4578#TemperatureSensorSensitivity> a sosa:Property , ssn-system:Sensitivity , ssn-system:Resolution , schema:PropertyValue ;
  rdfs:comment "The sensitivity and resolution of the temperature sensor is 0.1 °C in normal temperature and humidity conditions."@en ;
  schema:value 0.1 ;
  schema:unitCode unit:DegreeCelsius .

<DHT22/4578#TemperatureSensorPrecision> a sosa:Property , ssn-system:Precision , schema:PropertyValue ;
  rdfs:comment "The precision (= repeatability) of the temperature sensor is +-0.2 °C in normal temperature and humidity conditions."@en ;
  schema:minValue 0.2 ;
  schema:maxValue 0.2 ;
  schema:unitCode unit:DegreeCelsius .

<DHT22/4578#TemperatureSensorFrequency> a sosa:Property , ssn-system:Frequency , schema:PropertyValue ;
  rdfs:comment "The smallest possible time between one observation and the next is 2 s on average."@en ;
  schema:value 2 ;
  schema:unitCode unit:Second .


<observation/1087> rdf:type sosa:Observation ;
  sosa:madeBySensor <DHT22/4578#TemperatureSensor> ;
  sosa:usedProcedure <DHT22#Procedure> ;
  ssn-system:qualityOfObservation <observation/1087#quality> .


# one may classify the quality of observation using some class:

<observation/1087#quality> rdf:type ex:FairQuality .


# one may use some other ontology to further qualify this quality.

<observation/1087#quality>
  ex:evaluatedBy <Tom> ;
  ex:confidenceValue "6"^^xsd:integer;
  rdfs:comment """Tom gave a confidence value of 6 out of 10 on this observation."""@en .

# one may use some quantity ontology.

@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

<observation/1087#quality> rdf:type qudt:Quantity ;
  qudt:quantityValue [
    rdf:type qudt:QuantityValue ;
    qudt:numericValue "98.4"^^xsd:double ;
    qudt:hasUnit unit:PERCENT ] .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_36_1.ttl">Open in new window</a>
</blockquote>



## Example 01-observation-collection.ttl



```turtle
# baseURI: file:///C:/dev/W3C/sdw-sosa-ssn/ssn/examples/01-observation-collection.ttl
# imports: http://www.w3.org/ns/sosa-collections/

@prefix eg: <http://example.org/my-feature/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///C:/dev/W3C/sdw-sosa-ssn/ssn/examples/01-observation-collection.ttl>
  a owl:Ontology ;
  owl:imports <http://www.w3.org/ns/sosa-collections/> ;
.
eg:HomoCollection_1
  a sosa:ObservationCollection ;
  rdfs:label "Homogeneous Observation Collection #1" ;
.
eg:a1
  a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
.
eg:c1
  a sosa:ObservationCollection ;
  sosa:hasMember eg:a1 ;
  sosa:observedProperty eg:p1 ;
  sosa:phenomenonTime "2022-05-01T22:33:40Z"^^xsd:dateTime ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
eg:p1
  a skos:Concept ;
  skos:prefLabel "Some Observable Property" ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_37_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex11.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# The electric consumption of apartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:observedProperty  <apartment/134/electricConsumption> ;
  sosa:madeBySensor <sensor/926> ; 
  sosa:hasResult [
     rdf:type qudt-1-1:QuantityValue ;
     qudt:numericValue "22.4"^^xsd:double ;
     qudt:hasUnit unit:KiloW-HR ] ;
  sosa:phenomenonTime [
    rdf:type time:Interval ;
    time:hasBeginning [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
    time:hasEnd [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .


# Sensor #926 observes the electric consumption of apartment #134, and we know that 
# it made some observations.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <apartment/134/electricConsumption> ;
  sosa:madeObservation <Observation/235714>, <Observation/235715>, <Observation/235716> .

# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. 

<tempSensor/23> rdf:type sosa:Sensor ;
  sosa:observes  <tempSensor/23#temperature> ;
  sosa:madeObservation <tempSensor/23/4572>, <tempSensor/23/4573>, <tempSensor/23/4574> .


# Sensor #926 observes the electric consumption of apartment #134

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <apartment/134/electricConsumption> .

# This is equivalent to saying that the electric consumption of apartment #134 is 
# observed by Sensor #926

<apartment/134/electricConsumption> rdf:type sosa:ObservableProperty ;
  sosa:isObservedBy <sensor/926>  .


# Sensor #926 made observations identified by <Observation/235714> and <Observation/235715>.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:madeObservation <Observation/235714>, <Observation/235715> .

# This is equivalent to saying that these observations have been made by sensor #926.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .

<Observation/235754> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .


# the window opening state is an ActuatableProperty.

<window> rdf:type sosa:FeatureOfInterest .

<window/104#state> rdf:type sosa:ActuatableProperty ;
  sosa:isActedOnBy <actuation/188> .


# WindowCloser #987 made actuation #188

<windowCloser/987> rdf:type sosa:Actuator ;
  sosa:madeActuation <actuation/188> .


# Actuation #188 acted on the state of window #104 and returned 'true'.

<actuation/188> rdf:type sosa:Actuation ;
  sosa:actsOnProperty  <window/104#state> ;
  sosa:actuationMadeBy <windowCloser/987> ; 
  sosa:hasSimplResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_38_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex13.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# rangefinder #30 is a laser range finder sensor that was used 
# to observe the height of tree #124 and #125.

<rangefinder/30>        rdf:type           sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .

# rangefinder #30 made observation #1087 of the height of tree #124.

<observation/1087>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest  <tree/124> ;
  sosa:observedProperty  <tree/124/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:hasUnit unit:M ; 
    qudt:numericalValue "15.3"^^xsd:double ] .

<tree/124>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en .

<tree/124#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #124"@en .

# rangefinder #30 made observation #1088 of the height of tree #125.

<observation/1088>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1088"@en ;
  sosa:hasFeatureOfInterest  <tree/125> ;
  sosa:observedProperty  <tree/125/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:numericValue "23.0"^^xsd:double ;
    qudt:hasUnit qunit:M ] .

<tree/125>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #125"@en .

<tree/125#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #125"@en .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_39_1.ttl">Open in new window</a>
</blockquote>



## Example sosa-core_examples.ttl



```turtle
# baseURI: http://www.w3.org/ns/sosa/examples
# imports: http://www.w3.org/ns/sosa

@prefix ex: <http://www.w3.org/ns/sosa/examples#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.w3.org/ns/sosa/examples>
  rdf:type owl:Ontology ;
  owl:imports <http://www.w3.org/ns/sosa> ;
.
<http://www.w3.org/ns/sosa/examples#4830EH_UCSB>
  rdf:type sosa:Sample ;
  rdfs:comment "Instead of measuring temperature at every single office, we select room 4830 Ellison Hall, UCSB as a sample and thereby assume that the temperature observed there is a good proxy for the temperatures in other offices."^^xsd:string ;
  rdfs:label "4830 Ellison Hall"^^xsd:string ;
  sosa:isSampleOf ex:UCSB ;
.
ex:RoomTemperature
  rdf:type sosa:Procedure ;
  rdfs:comment "How is this linked to platform & sensor?--> It s not explicitly linked (see also the comment for ex:TempObservation1) One could add a back-pointing relation to the observation here but in reality one would not do so as this would crate millions of triples as part of each procedure, thereby cluttering a procedure repository. This is/can be handled via UNION queries in SPARQL pr simply an inverse property (path) in your query."^^xsd:string ;
  rdfs:comment "This is a procedure for measuring room temperatures. To ensure a meaningful interpretation of results and interoperability, all room temperature observations need to follow the same procedure. (1) The sensor should be put at least 1m above ground. (2) The sensor should be shielded from direct sun light and circulating air, e.g., via an open window. Other heat sources such as computers should be avoided as well. (3) The sensor should not be moved during observations. (4) Room temperature observations are only comparable if they were taken during comparable outside conditions and with closed windows and doors. (5)...."^^xsd:string ;
.
ex:SamsungGalaxyS4_23
  rdf:type sosa:Platform ;
  rdfs:comment "A Samsung Galaxy S4 smartphone that carries multiple sensors. The S4 remains popular as it contains more sensors than later editions. For example, it can sense temperature."^^xsd:string ;
  rdfs:label "Samsung Galaxy S4"^^xsd:string ;
  sosa:hosts ex:TempSensorS4_23 ;
.
ex:TempObservation1
  rdf:type sosa:Observation ;
  rdfs:comment "A temperature observation created using the SamsungGalaxyS4_23."^^xsd:string ;
  rdfs:comment "Not yet linked through to the platform or sensor. ---> (kj). Yes, this will be 'linked' via SPARQL queries and possible via future axioms outside of SOSA-core. There is no need to habve explicit relations between anything and everything. Also, keep in mind that this is all under the OWA."^^xsd:string ;
  rdfs:label "Temperature observation 1."^^xsd:string ;
  sosa:madeBySensor ex:TempSensorS4_23;
  sosa:hasFeatureOfInterest <http://www.w3.org/ns/sosa/examples#4830EH_UCSB> ;
  sosa:hasResult ex:TempObservationResult1 ;
  sosa:resultTime "2016-08-10T08:30:00"^^xsd:dateTime ;
  sosa:usedProcedure ex:RoomTemperature ;
.
ex:TempSensorS4_23
  rdf:type sosa:Sensor ;
  rdfs:label "The temperature sensor mounted on the S4 platform with the ID 23."^^xsd:string ;
  sosa:hostedBy ex:SamsungGalaxyS4_23 ;
.
ex:TempObservationResult1
  rdf:type sosa:Result ;
  rdfs:comment "The observed temperature for observation 1."^^xsd:string ;
  rdfs:label "Result of temperature observation 1."^^xsd:string ;
  sosa:hasValue "23.8"^^xsd:double ;
.
ex:TempObservation2
  rdf:type sosa:Observation ;
  rdfs:comment "A temperature observation created using the SamsungGalaxyS4_23."^^xsd:string ;
  rdfs:label "Temperature observation 2. We usue this here to demonstrate that all room temperature observations use the same procedure."^^xsd:string ;
  sosa:madeBySensor ex:TempSensorS4_23;
  sosa:hasFeatureOfInterest ex:4830EH_UCSB ;
  sosa:hasResult [ rdf:value 23.8 ] ;
  sosa:resultTime "2016-08-10T09:33:00"^^xsd:dateTime ;
  sosa:usedProcedure ex:RoomTemperature ;
.
ex:TempObservationResult2
  rdf:type sosa:Result ;
  rdfs:comment "The observed temperature for observation 2."^^xsd:string ;
  rdfs:label "Result of temperature observation 2."^^xsd:string ;
  sosa:hasValue "24.3"^^xsd:double ;
.
ex:UCSB
  rdf:type sosa:FeatureOfInterest ;
  sosa:hasSample ex:4830EH_UCSB ;
  rdfs:comment "In our example we would like to study the average room temperature of offices at UCSB. Hence, UCSB is the feature of interest. We will only observe the temperature at some offices that will act as samples."^^xsd:string ;
  rdfs:label "University of California, Santa Barbara"^^xsd:string ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_40_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex17.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@base <http://example.org/data/> .

# movements of spinning cups on wind sensor #14 serves as proxies for the wind speed
# at the location of the wind sensor.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:observes <location/4687#windSpeed> .

# wind sensor #14 detected some movement of spinning cups, from which originated the
# observations #147 and #148.

<windSensor/14> rdf:type sosa:Sensor ;
  sosa:madeObservation <observation/147> , <observation/148> ; 
  sosa:detects <observation/147#spinningCupsMovement> , <observation/148#spinningCupsMovement> .

# observation #147 was originated by the movement of the spinning cups of sensor #14.
# the result of observations #147 and #148 is using some custom datatype that encodes the unit of measure.

<observation/147> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:wasOriginatedBy <observation/147#spinningCupsMovement> ;
  sosa:resultTime "2017-04-12T12:00:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "47 km/h"^^<speed> .

<observation/147#spinningCupsMovement> rdf:type sosa:Stimulus ;
  sosa:isProxyFor <location/4687#windSpeed> .

<observation/148> rdf:type sosa:Observation ;
  sosa:observedProperty <location/4687#windSpeed> ;
  sosa:madeBySensor <windSensor/14> ;
  sosa:wasOriginatedBy <observation/148#spinningCupsMovement> ;
  sosa:resultTime "2017-04-12T12:01:00Z"^^xsd:dateTime ;
  sosa:hasSimpleResult "43 km/h"^^<speed> .

<observation/148#spinningCupsMovement> rdf:type sosa:Stimulus ;
  sosa:isProxyFor <location/4687#windSpeed> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_41_1.ttl">Open in new window</a>
</blockquote>



## Example tree-height.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# rangefinder #30 is a laser range finder sensor that was used 
# to observe the height of tree #124 and #125.

<rangefinder/30>        rdf:type           sosa:Sensor ;
  rdfs:label "rangefinder #30"@en ;
  rdfs:comment "rangefinder #30 is a laser range finder sensor."@en .

# rangefinder #30 made observation #1087 of the height of tree #124.

<observation/1087>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1087"@en ;
  sosa:hasFeatureOfInterest  <tree/124> ;
  sosa:observedProperty  <tree/124/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:hasUnit unit:M ; 
    qudt:numericValue "15.3"^^xsd:double ] .

# using SSN, one can explicitly link a property and its feature of interest.
 
<tree/124>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #124"@en ;
  sosa:hasProperty <tree/124#height> .

<tree/124#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #124"@en ;
  sosa:isPropertyOf <tree/124> .

# rangefinder #30 made observation #1088 of the height of tree #125.

<observation/1088>  rdf:type               sosa:Observation ;
  rdfs:label "observation #1088"@en ;
  sosa:hasFeatureOfInterest  <tree/125> ;
  sosa:observedProperty  <tree/125/height> ;
  sosa:madeBySensor <rangefinder/30> ;
  sosa:hasResult [ 
    qudt:numericValue "23.0"^^xsd:double ;
    qudt:hasUnit unit:M ] .

# using SSN, one can explicitly link a property and its feature of interest.
 
<tree/125>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "tree #125"@en ;
  sosa:hasProperty <tree/125#height> .

<tree/125#height>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the height of tree #125"@en ;
  sosa:isPropertyOf <tree/125> .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_42_1.ttl">Open in new window</a>
</blockquote>



## Example apartment-134-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# The electric consumption of appartment #134 on April 15 2017 was 22.4 kWh as 
# observed by sensor #926. The result was available 12 seconds later.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:observedProperty  <Appartment/134/electricConsumption> ;
  sosa:madeBySensor <sensor/926> ; 
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:numericValue "22.4"^^xsd:double ;
     qudt:hasUnit unit:Kilowatthour ] ;
  sosa:phenomenonTime [
    rdf:type time:Interval ;
    time:hasBeginning [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-15T00:00:00+00:00"^^xsd:dateTimeStamp ] ;
    time:hasEnd [ 
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2017-04-16T00:00:00+00:00"^^xsd:dateTimeStamp ] ] ;
  sosa:resultTime "2017-04-16T00:00:12+00:00"^^xsd:dateTimeStamp .


# Sensor #926 observes the electric consumption of appartment #134, and we know that 
# it made some observations.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <Appartment/134/electricConsumption> ;
  sosa:madeObservation <Observation/235714>, <Observation/235715>, <Observation/235716> .

# mobile sensor tempSensor #23 observes the temperature in its surroundings, and we know 
# that it made some observations. 

<tempSensor/23> rdf:type sosa:Sensor ;
  sosa:observes  <tempSensor/23#temperature> ;
  sosa:madeObservation <tempSensor/23/4572>, <tempSensor/23/4573>, <tempSensor/23/4574> .


# Sensor #926 observes the electric consumption of appartment #134

<sensor/926> rdf:type sosa:Sensor ;
  sosa:observes  <Appartment/134/electricConsumption> .

# This is equivalent to saying that the electric consumption of appartment #134 is 
# observed by Sensor #926

<Appartment/134/electricConsumption> rdf:type sosa:ObservableProperty ;
  sosa:isObservedBy <sensor/926>  .


# Sensor #926 made observations identified by <Observation/235714> and <Observation/235715>.

<sensor/926> rdf:type sosa:Sensor ;
  sosa:madeObservation <Observation/235714>, <Observation/235715> .

# This is equivalent to saying that these observations have been made by sensor #926.

<Observation/235714> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .

<Observation/235754> rdf:type sosa:Observation ;
  sosa:madeBySensor <sensor/926> .


# the window opening state is an ActuatableProperty.

<window> rdf:type sosa:FeatureOfInterest .

<window/104#state> rdf:type sosa:ActuatableProperty ;
  sosa:isActedOnBy <actuation/188> .


# WindowCloser #987 made actuation #188

<windowCloser/987> rdf:type sosa:Actuator ;
  sosa:madeActuation <actuation/188> .


# Actuation #188 acted on the state of window #104 and returned 'true'.

<actuation/188> rdf:type sosa:Actuation ;
  sosa:actsOnProperty  <window/104#state> ;
  sosa:actuationMadeBy <windowCloser/987> ; 
  sosa:hasSimpleResult true ;
  sosa:resultTime "2017-04-18T17:24:00+02:00"^^xsd:dateTimeStamp .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_43_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex3.ttl



```turtle
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .

<Observation/234534> a sosa:Observation ;
   sosa:hasFeatureOfInterest <apartment/134> ;
   sosa:hasSimpleResult "-29.9 Cel"^^cdt:ucum .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_44_1.ttl">Open in new window</a>
</blockquote>



## Example iphone_barometer-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@base <http://example.org/data/> .

# The barometric readings from a Bosch Sensortec BMP282 sensor in an Apple IPhone 7 observed on June 6 2017
# using only the SOSA core.

<earthAtmosphere> rdf:type sosa:FeatureOfInterest ;
  rdfs:label "Atmosphere of Earth"@en .


# An iPhone 7 as the Platform that hosts several sensors, among others the Bosch Sensortec BMP282 atmospheric pressure sensor.

<iphone7/35-207306-844818-0> a sosa:Platform ;
  rdfs:label "IPhone 7 - IMEI 35-207306-844818-0"@en ;
  rdfs:comment "IPhone 7 - IMEI 35-207306-844818-0 - John Doe"@en ;
  sosa:hosts <sensor/35-207306-844818-0/BMP282> .

<sensor/35-207306-844818-0/BMP282> rdf:type sosa:Sensor ;
  rdfs:label "Bosch Sensortec BMP282"@en ;
  sosa:observes <sensor/35-207306-844818-0/BMP282/atmosphericPressure> .


# An observation made by the Bosch Sensortec BMP282 atmospheric pressure sensor.

<Observation/346344> rdf:type sosa:Observation ;
  sosa:observedProperty <sensor/35-207306-844818-0/BMP282/atmosphericPressure> ;
  sosa:hasFeatureOfInterest <earthAtmosphere> ;
  sosa:madeBySensor <sensor/35-207306-844818-0/BMP282> ;
  sosa:hasSimpleResult "1021.45 hPa"^^cdt:ucum ;
  sosa:resultTime "2017-06-06T12:36:12Z"^^xsd:dateTime .


# Another observation made a second later by the Bosch Sensortec BMP282 atmospheric pressure sensor
# using the QUDT Ontology for the Units of Measurement and the Time Ontology for the instant.

<Observation/346345> rdf:type sosa:Observation ;
  sosa:observedProperty <sensor/35-207306-844818-0/BMP282/atmosphericPressure> ;
  sosa:hasFeatureOfInterest <earthAtmosphere> ;
  sosa:madeBySensor <sensor/35-207306-844818-0/BMP282> ;
  sosa:hasResult [
    rdf:type qudt:QuantityValue ;
    qudt:numericValue "101936"^^xsd:double ;
    qudt:hasUnit unit:Pascal ] ;
  sosa:resultTime [
    rdf:type time:Instant ;
    time:inXSDDateTimeStamp "2017-06-06T12:36:13+00:00"^^xsd:dateTimeStamp ] .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_45_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex8.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix cdt: <http://w3id.org/lindt/custom_datatypes#> .
@base <http://example.org/data/> .

# The barometric readings from a Bosch Sensortec BMP282 sensor in an Apple IPhone 7
# observed on June 6 2017 using only the SOSA core for modelling.

# the atmosphere is sampled at a specific location
# location coordinates are given using GeoSPARQL

<earthAtmosphere> a sosa:FeatureOfInterest ;
  rdfs:label "Atmosphere of Earth"@en .

<earthAtmosphere_StE> a sosa:Sample ;
  sosa:isSampleOf <earthAtmosphere> ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (4.387611 45.437772)"^^geo:WktLiteral ;
  ] ;
.

<atmosphericPressure> a sosa:ObservableProperty ;
  rdfs:label "Atmospheric pressure"@en .


# An iPhone 7 as the Platform that hosts several sensors,
# among others the Bosch Sensortec BMP282 atmospheric pressure sensor.

<iphone7/35-207306-844818-0> a sosa:Platform ;
  rdfs:label "IPhone 7 - IMEI 35-207306-844818-0"@en ;
  rdfs:comment "IPhone 7 - IMEI 35-207306-844818-0 - John Doe"@en ;
  sosa:hosts <sensor/35-207306-844818-0/BMP282> .

<sensor/35-207306-844818-0/BMP282> a sosa:Sensor ;
  rdfs:label "Bosch Sensortec BMP282"@en ;
  sosa:observes <atmosphericPressure> .


# An observation made by the BMP282 atmospheric pressure sensor
# using the cdt:ucum custom datatype.

<Observation/346344> a sosa:Observation ;
  sosa:observedProperty <atmosphericPressure> ;
  sosa:hasFeatureOfInterest  <earthAtmosphere_StE> ;
  sosa:madeBySensor <sensor/35-207306-844818-0/BMP282> ;
  sosa:hasSimpleResult "1021.45 hPa"^^cdt:ucum ;
  sosa:resultTime "2017-06-06T12:36:12Z"^^xsd:dateTime .


# Another observation made a second later by the BMP282 atmospheric pressure sensor
# using the QUDT Ontology for the Units of Measurement

<Observation/346345> a sosa:Observation ;
  sosa:observedProperty <atmosphericPressure> ;
  sosa:hasFeatureOfInterest  <earthAtmosphere_StE> ;
  sosa:madeBySensor <sensor/35-207306-844818-0/BMP282> ;
  sosa:hasResult [
    a qudt:QuantityValue ;
    qudt:value "101936"^^xsd:decimal ;
    qudt:hasUnit unit:PA ] ;
  sosa:resultTime "2017-06-06T12:36:13Z"^^xsd:dateTime .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_46_1.ttl">Open in new window</a>
</blockquote>



## Example dht22-deployment.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .

@base <http://example.org/data/> .


<Room145> a sosa:FeatureOfInterest ;
  rdfs:label "Room #145"@en ;
  sosa:hasSample <Room145/east> ;
  sosa:hasSample <Room145/south> .

  <Room145/east> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "East wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 1 with DHT22 temperature and humidity sensor #4578."@en ;
    sosa:hosts <PCBBoard1> .

  <Room145/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #145."@en ;
    rdfs:comment "This wall hosts PCB Board 2 with DHT22 temperature and humidity sensor #4579."@en ;
    sosa:hosts <PCBBoard2> .


<Room245> a sosa:FeatureOfInterest ;
  rdfs:label "Room #245"@en ;
  sosa:hasProperty <Room245#temperature> , <Room245#humidity> ;
  sosa:hasSample <Room245/south> .

  <Room245/south> a sosa:Sample , sosa:FeatureOfInterest , sosa:Platform ;
    rdfs:label "South wall of room #245."@en ;
    sosa:hosts <PCBBoard3> .





<PCBBoard1> a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 1"@en ;
  rdfs:comment "PCB Board 1 hosts DHT22 temperature and humidity sensor #4578 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts <DHT22/4578> ;
  sosa:hasSubSystem <DHT22/4578> .

  <DHT22/4578> a sosa:System ;
    rdfs:label "DHT22 sensor #4578"@en ;
    sosa:isHostedBy <PCBBoard1> .


<PCBBoard2> a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 2"@en ;
  rdfs:comment "PCB Board 2 hosts DHT22 temperature and humidity sensor #4579 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts <DHT22/4578> ;
  sosa:hasSubSystem <DHT22/4578> .

  <DHT22/4579> a sosa:System ;
    rdfs:label "DHT22 sensor #4579."@en ;
    sosa:isHostedBy <PCBBoard2> .


<PCBBoard3> a sosa:System , sosa:Platform ;
  rdfs:label "PCB Board 3"@en ;
  rdfs:comment "PCB Board 3 hosts DHT22 temperature and humidity sensor #4580 permanently, one can say it has it as one of its subsystems."@en ;
  sosa:hosts <DHT22/4578> ;
  sosa:hasSubSystem <DHT22/4578> .

  <DHT22/4580> a sosa:System ;
    rdfs:label "DHT22 sensor #4580."@en ;
    sosa:isHostedBy <PCBBoard3> .




<Room245Deployment> a sosa:Deployment ;
  rdfs:comment "Deployment of PCB Board 3 on the south wall of room #245 for the purpose of observing the temperature and humidity of room #245."@en ;
  sosa:deployedOnPlatform <Room245/south> ;
  sosa:deployedSystem <PCBBoard3> ;
  sosa:forProperty <Room245#temperature> , <Room245#humidity> .


<Room145Deployment> a sosa:Deployment ;
  rdfs:comment "Deployment of PCB Board 1 and 2 on the east and south wall of room #145, respectively, for the purpose of observing the temperature and humidity of room #145."@en ;
  sosa:deployedOnPlatform <Room245/east> , <Room245/south> ;
  sosa:deployedSystem <PCBBoard1> , <PCBBoard2> ;
  sosa:forProperty <Room145#temperature> , <Room145#humidity> .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_47_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex1.ttl



```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

<Observation/234534> a sosa:Observation ;
   rdfs:comment "Observation of the difference between the outside temperature and the inside temperature."@en ;
   sosa:hasFeatureOfInterest <apartment/134> ;
   sosa:hasResult [
      a qudt:QuantityValue ;
      qudt:hasUnit unit:DEG_C ;
      qudt:value "-29.9"^^xsd:decimal ] .

<Observation/83985> a sosa:Observation ;
   rdfs:comment "Observation of the temperature inside apartment #134."@en ;
   sosa:hasFeatureOfInterest <apartment/134> ;
   sosa:hasResult [
      a qudt:QuantityValue ;
      qudt:hasUnit unit:DEG_C ;
      qudt:value "22.4"^^xsd:decimal ] .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_48_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex4.ttl



```turtle
ex:Temperature a sosa:Property .

<office/1> a sosa:FeatureOfInterest;
  sosa:hasProperty ex:Temperature . 

<Observation/1> a sosa:Observation ;
  sosa:observedProperty ex:Temperature ;
  sosa:hasFeatureOfInterest <office/1> .

<office/2> a sosa:FeatureOfInterest;
  sosa:hasProperty ex:Temperature . 

<Observation/2> a sosa:Observation ;
  sosa:observedProperty ex:Temperature ;
  sosa:hasFeatureOfInterest <office/2> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_49_1.ttl">Open in new window</a>
</blockquote>



## Example dht22.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix schema: <http://schema.org/>.
@prefix ex: <http://example.org/>.

@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn-system: <http://www.w3.org/ns/ssn/systems/> .

@prefix rdfp: <https://w3id.org/rdfp/>.

@base <http://example.org/data/> .


<DHT22#Procedure> a sosa:Procedure ;
  sosa:hasOutput <DHT22#output> .

<DHT22#output> a sosa:Output , rdfp:GraphDescription ;
  rdfs:comment "The output is a RDF Graph that describes both the temperature and the humidity. It can be validated by a SHACL shapes graph."@en ;
  rdfp:presentedBy [
    a rdfp:GraphDescription ;
    rdfp:validationRule <shacl_shapes_graph> ;
  ] .


<DHT22/4578> a sosa:System ;
  rdfs:comment "DHT22 sensor #4578 contains a humidity and a temperature sensor."@en ;
  rdfs:seeAlso <https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf> ;
  sosa:hasSubSystem <DHT22/4578#TemperatureSensor>, <DHT22/4578#HumiditySensor> .



<DHT22/4578#TemperatureSensor> a sosa:Sensor , sosa:System ;
  rdfs:comment "The embedded temperature sensor, a specific instance of temperature sensor."@en ;
  ssn-system:hasOperatingRange <DHT22/4578#TemperatureSensorOperatingRange> ; 
  ssn-system:hasSystemCapability <DHT22/4578#TemperatureSensorCapability> ;
  sosa:implements <DHT22#Procedure> .

<DHT22/4578#HumiditySensor> a sosa:Sensor , sosa:System ;
  rdfs:comment "The embedded humidity sensor, a specific instance of humidity sensor."@en ;
  ssn-system:hasOperatingRange <DHT22/4578#HumiditySensorOperatingRange> ;
  sosa:implements <DHT22#Procedure> .



<DHT22/4578#TemperatureSensorOperatingRange> a ssn-system:OperatingRange ;
  rdfs:comment "The conditions in which the DHT22 temperature sensor is expected to operate."@en ;
  ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> .

<DHT22/4578#HumiditySensorOperatingRange> a ssn-system:OperatingRange ;
  rdfs:comment "The conditions in which the DHT22 humidity sensor is expected to operate."@en ;
  ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> .



<NormalOperatingCondition> a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A temperature range of -40 to 80 Celsius."@en ;
  schema:minValue -40.0 ;
  schema:maxValue 80.0 ;
  schema:unitCode unit:DegreeCelsius .

<NormalHumidityCondition> a ssn-system:Condition , schema:PropertyValue ;
  rdfs:comment "A relative humidity range of 5 to 85 %."@en ;
  schema:minValue 5.0 ;
  schema:maxValue 85.0 ;
  schema:unitCode unit:PERCENT .



<DHT22/4578#TemperatureSensorCapability> a sosa:Property , ssn-system:SystemCapability , schema:PropertyValue ;
  rdfs:comment "The capabilities of the temperature sensor in normal temperature and humidity conditions." ;
  ssn-system:inCondition <NormalTemperatureCondition> , <NormalHumidityCondition> ;
  ssn-system:hasSystemProperty <DHT22/4578#TemperatureSensorAccuracy> , <DHT22/4578#TemperatureSensorSensitivity> , <DHT22/4578#TemperatureSensorRepeatability> , <DHT22/4578#TemperatureSensorFrequency> .

<DHT22/4578#TemperatureSensorAccuracy> a sosa:Property , ssn-system:Accuracy , schema:PropertyValue ;
  rdfs:comment "The accuracy of the temperature sensor is +-0.5 °C in normal temperature and humidity conditions."@en ;
  schema:minValue -0.5 ;
  schema:maxValue 0.5 ;
  schema:unitCode unit:DegreeCelsius .

<DHT22/4578#TemperatureSensorSensitivity> a sosa:Property , ssn-system:Sensitivity , ssn-system:Resolution , schema:PropertyValue ;
  rdfs:comment "The sensitivity and resolution of the temperature sensor is 0.1 °C in normal temperature and humidity conditions."@en ;
  schema:value 0.1 ;
  schema:unitCode unit:DegreeCelsius .

<DHT22/4578#TemperatureSensorPrecision> a sosa:Property , ssn-system:Precision , schema:PropertyValue ;
  rdfs:comment "The precision (= repeatability) of the temperature sensor is +-0.2 °C in normal temperature and humidity conditions."@en ;
  schema:minValue 0.2 ;
  schema:maxValue 0.2 ;
  schema:unitCode unit:DegreeCelsius .

<DHT22/4578#TemperatureSensorFrequency> a sosa:Property , ssn-system:Frequency , schema:PropertyValue ;
  rdfs:comment "The smallest possible time between one observation and the next is 2 s on average."@en ;
  schema:value 2 ;
  schema:unitCode unit:Second .


<observation/1087> rdf:type sosa:Observation ;
  sosa:madeBySensor <DHT22/4578#TemperatureSensor> ;
  sosa:usedProcedure <DHT22#Procedure> ;
  sosa:resultQuality <observation/1087#quality> ;


# one may classify the quality of observation using some class:

# <observation/1087#quality> rdf:type ex:FairQuality .


# one may use some other ontology to further qualify this quality.

<observation/1087#quality>
  ex:evaluatedBy <Tom> ;
  ex:confidenceValue "6"^^xsd:integer ;
  rdfs:comment """Tom gave a confidence value of 6 out of 10 on this observation."""@en .

# one may use some quantity ontology.

@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .

<observation/1087#quality> rdf:type qudt:Quantity ;
  qudt:quantityValue [
    rdf:type qudt:QuantityValue ;
    qudt:numericValue "98.4"^^xsd:double ;
    qudt:hasUnit unit:PERCENT ] .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_50_1.ttl">Open in new window</a>
</blockquote>



## Example om-20.ttl



```turtle
# baseURI: http://example.org/om-20
# imports: http://example.org/geosparql
# imports: http://qudt.org/2.0/schema/qudt
# imports: http://www.w3.org/2006/time
# imports: http://www.w3.org/ns/prov-o#
# imports: http://www.w3.org/ns/sosa/sampling
# imports: http://www.w3.org/ns/ssn/

@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix examples: <http://example.org/www.w3.org/ns/sosa/examples#> .
@prefix geosparql: <http://www.opengis.net/ont/geosparql#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sampling: <http://www.w3.org/ns/sosa/sampling/> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.org/om-20>
  rdf:type owl:Ontology ;
  dcterms:created "2017-06-06"^^xsd:date ;
  dcterms:creator <http://people.csiro.au/Simon-Cox> ;
  dcterms:modified "2017-06-07" ;
  rdfs:comment "SOSA/SSN examples matching the ones found in Annex C of OMXML 2.0" ;
  rdfs:seeAlso <http://portal.opengeospatial.org/files/?artifact_id=41510> ;
  owl:imports <http://example.org/geosparql> ;
  owl:imports <http://qudt.org/2.0/schema/qudt> ;
  owl:imports <http://www.w3.org/2006/time> ;
  owl:imports <http://www.w3.org/ns/prov-o#> ;
  owl:imports sosa:sampling ;
  owl:imports <http://www.w3.org/ns/ssn/> ;
.
examples:COTest3
  rdf:type sosa:Observation ;
  rdfs:comment "Complex Observation test instance" ;
  sosa:hasFeatureOfInterest <http://www.ga.gov.au/bin/gazd01?rec=293604> ;
  sosa:hasResult examples:a1 ;
  sosa:observedProperty <http://sweetontology.net/phenAtmo/Weather> ;
  sosa:phenomenonTime examples:ot1t-3 ;
  sosa:resultTime "2005-01-11T17:22:25.00+10:00"^^xsd:dateTime ;
  sosa:usedProcedure <http://www.example.org/register/process/weatherStation3> ;
.
examples:CV123476
  rdf:type sosa:Result ;
  rdfs:comment "Result details not provided - need an RDF element for a 1-D coverage" ;
.
examples:CV12415
  rdf:type sosa:Result ;
  rdfs:comment "Result details not provided - need an RDF element for a 1-D coverage" ;
.
examples:DA1412412
  rdf:type sosa:Result ;
  rdfs:comment "Result details not provided - need an RDF element for a 1-D coverage" ;
.
examples:DA3464
  rdf:type sosa:Result ;
  rdfs:comment "Result details not provided - need an RDF element for an array and headers" ;
.
examples:DC756254
  rdf:type sosa:Result ;
  rdfs:comment "Result details not provided - need an RDF element for a set of geometry-value pairs" ;
.
examples:O35235
  rdf:type sosa:Observation ;
  rdfs:label "Weather Data" ;
  sosa:hasFeatureOfInterest <http://www.ga.gov.au/bin/gazd01?rec=293604> ;
  sosa:hasResult examples:DA3464 ;
  sosa:observedProperty <http://example.org/weather1.xml> ;
  sosa:phenomenonTime examples:TP2523 ;
  sosa:resultTime "2007-04-01T03:40:00.000-06:00"^^xsd:dateTime ;
  sosa:usedProcedure <urn:vast:sensor:weatherStation> ;
.
examples:OPTest1
  rdf:type sosa:Observation ;
  rdfs:comment "Observation instance with remote result" ;
  rdfs:label "Observation Pointer 1" ;
  skos:editorialNote "Procedure/sensor unknown so omitted in RDF representation" ;
  sosa:hasFeatureOfInterest <http://my.example.org/wfs%26request=getFeature%26;featureid=789002> ;
  sosa:hasResult <http://my.example.org/results%3f798002%26property=RH> ;
  sosa:observedProperty <urn:example:RelativeHumidity> ;
  sosa:phenomenonTime examples:op1t ;
  sosa:resultTime "2005-01-11T18:22:25.00+10:00"^^xsd:dateTime ;
.
examples:T13411414
  rdf:type time:Instant ;
  time:inXSDDateTimeStamp "2007-06-06T14:20:30.00+08:00"^^xsd:dateTimeStamp ;
.
examples:T3247149
  rdf:type time:Instant ;
  time:inXSDDateTimeStamp "2007-06-06T17:20:30.00+08:00"^^xsd:dateTimeStamp ;
.
examples:T9897
  rdf:type time:Instant ;
  time:inXSDDateTimeStamp "2007-06-06T14:20:30.00+08:00"^^xsd:dateTimeStamp ;
.
examples:TP2523
  rdf:type time:ProperInterval ;
  time:hasBeginning [
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2007-04-01T00:00:00.000-06:00"^^xsd:dateTimeStamp ;
    ] ;
  time:hasEnd [
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2007-04-01T03:40:00.000-06:00"^^xsd:dateTimeStamp ;
    ] ;
.
examples:a1
  rdf:type sosa:Result ;
  rdfs:comment "Result details not provided - need an RDF element for an array" ;
.
examples:b1
  rdf:type sosa:Sample ;
  geosparql:hasGeometry examples:pr1_ls1 ;
  geosparql:hasGeometry [
      rdf:type sf:Polygon ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Polygon(-30.711 134.196 , -30.711 134.205 , -30.702 134.205 , -30.702 134.196 )"^^geosparql:wktLiteral ;
    ] ;
  rdfs:comment "Geology borehole Encoded as a SamplingCurve With three logs encoded as the results of relatedObservations" ;
  rdfs:label "b1" ;
  skos:editorialNote "Bounding box encoded as Polygon" ;
  skos:editorialNote "relatedObservation encoded using sosa:isFeatureOfInterestOf" ;
  sosa:isFeatureOfInterestOf examples:b1_lith1 ;
  sosa:isFeatureOfInterestOf examples:b1_ms1 ;
  sosa:isFeatureOfInterestOf examples:b1_p1 ;
  sosa:isSampleOf <http://my.geology.custodian.org/unit/g345> ;
.
examples:b1_lith1
  rdf:type sosa:Observation ;
  rdfs:comment "Lithology log Result is encoded using OGC Discrete Coverage/interleaved pattern" ;
  skos:editorialNote "No result shown - requires a 1-D coverage encoding" ;
  sosa:hasFeatureOfInterest examples:b1 ;
  sosa:hasResult examples:CV12415 ;
  sosa:madeBySensor <http://www.csiro.au/people/ps205.html> ;
  sosa:observedProperty <urn:ogc:def:phenomenon:CGI:2007:lithology> ;
  sosa:phenomenonTime examples:T3247149 ;
  sosa:resultTime "2007-06-06T17:20:30.00+08:00"^^xsd:dateTime ;
.
examples:b1_ms1
  rdf:type sosa:Observation ;
  rdfs:comment "Magnetic susceptibility log Result is encoded using SWE Common \"DataArray\" element, which embeds values in a text string" ;
  sosa:hasFeatureOfInterest examples:b1 ;
  sosa:hasResult examples:DA1412412 ;
  sosa:observedProperty <urn:ogc:def:phenomenon:CGI:2007:MagneticSusceptibility> ;
  sosa:phenomenonTime examples:T13411414 ;
  sosa:usedProcedure <http://www.geophysics.org/MS34> ;
.
examples:b1_p1
  rdf:type sosa:Observation ;
  rdfs:comment "Porosity log Result is encoded using OGC Discrete Point Coverage/interleaved pattern" ;
  sosa:hasFeatureOfInterest examples:b1 ;
  sosa:hasResult examples:CV123476 ;
  sosa:observedProperty <http://sweetontology.net/propFraction/Porosity> ;
  sosa:phenomenonTime examples:T9897 ;
  sosa:resultTime "2007-06-06T14:20:30.00+08:00"^^xsd:dateTime ;
  sosa:usedProcedure <http://www.geophysics.org/PO34> ;
.
examples:foi
  rdf:type owl:Thing ;
  geosparql:hasGeometry [
      rdf:type sf:Polygon ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.3:62836405> Polygon(-90 -180 , -90 180 , 90 180 , 90 -180 )"^^geosparql:wktLiteral ;
    ] ;
  rdfs:comment "This collection contains a sampling curve plus some associated stations" ;
  rdfs:member examples:ot2s ;
  rdfs:member examples:st1 ;
  rdfs:member examples:st2 ;
  rdfs:member examples:st3 ;
  rdfs:member examples:st4 ;
  skos:editorialNote "Bounding box encoded as Polygon" ;
  skos:editorialNote "Collection encoded as a owl:Thing" ;
.
examples:obsTest1
  rdf:type sosa:Observation ;
  rdfs:comment "Observation test instance: fruit mass" ;
  rdfs:label "Observation test 1" ;
  skos:editorialNote "Contextual information (ambient temperature) not shown - no RDF available" ;
  sosa:hasFeatureOfInterest <http://wfs.example.org?request=getFeature&amp;featureid=fruit37f> ;
  sosa:hasResult [
      rdf:type qudt:QuantityValue ;
      rdf:type sosa:Result ;
      qudt:numericValue "0.28"^^<http://www.linkedmodel.org/schema/dtype#numericUnion> ;
      qudt:hasUnit <http://qudt.org/vocab/unit/Kilogram> ;
      skos:editorialNote "Use qudt:QuantityValue for sosa:Result" ;
    ] ;
  sosa:madeBySensor <http://www.example.org/register/process/scales34.xml> ;
  sosa:observedProperty <http://sweetontology.net/propMass/Mass> ;
  sosa:phenomenonTime examples:ot1t ;
  sosa:resultTime "2005-01-11T16:22:25.00+10:00"^^xsd:dateTimeStamp ;
.
examples:obsTest1s
  rdf:type sosa:Observation ;
  rdfs:comment "Spatial observation test instance: water level" ;
  rdfs:label "Spatial observation test 1" ;
.
examples:obsTest2
  rdf:type sosa:Observation ;
  rdfs:comment "Observation test instance: fruit identification" ;
  rdfs:label "Observation test 2" ;
  sosa:hasFeatureOfInterest <http://wfs.example.org?request=getFeature&amp;featureid=fruit37f> ;
  sosa:hasResult <http://en.wikipedia.org/wiki/List_of_fruits#Banana> ;
  sosa:madeBySensor <http://www.example.org/party/individual/abc123> ;
  sosa:observedProperty <http://sweetontology.net/matrBiomass/Species> ;
  sosa:phenomenonTime examples:ot2t ;
  sosa:resultTime "2005-01-11T17:22:25.00+10:00"^^xsd:dateTime ;
  sosa:usedProcedure <http://www.example.org/party/role/field_worker> ;
.
examples:obsTest4
  rdf:type sosa:Observation ;
  rdfs:comment "Observation test instance - multi-element featureOfInterest" ;
  rdfs:label "Multi-element 1" ;
  sosa:hasFeatureOfInterest <http://wfs.example.org?request=getFeature&#38;featureid=stc1> ;
  sosa:hasResult examples:DC756254 ;
  sosa:madeBySensor <urn:ogc:object:feature:Sensor:NASA:xyz345> ;
  sosa:observedProperty <http://sweetontology.net/propEnergyFlux/Radiance> ;
  sosa:phenomenonTime examples:ots1t ;
  sosa:resultTime "2005-06-17"^^xsd:date ;
.
examples:op1t
  rdf:type time:ProperInterval ;
  time:hasBeginning [
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2005-01-11T17:22:25.00+10:00"^^xsd:dateTimeStamp ;
    ] ;
  time:hasEnd [
      rdf:type time:Instant ;
      time:inXSDDateTimeStamp "2005-01-11T18:22:25.00+10:00"^^xsd:dateTimeStamp ;
    ] ;
.
examples:ot1t
  rdf:type time:Instant ;
  time:inXSDDateTimeStamp "2005-01-11T16:22:25.00+10:00"^^xsd:dateTimeStamp ;
.
examples:ot1t-3
  rdf:type time:Instant ;
  time:inXSDDateTimeStamp "2005-01-11T17:22:25.00+10:00"^^xsd:dateTimeStamp ;
.
examples:ot2s
  rdf:type sosa:Sample ;
  geosparql:hasGeometry examples:pr1_ls1 ;
  rdfs:label "8903" ;
  sosa:isSampleOf <http://wfs.flakey.org?request=getFeature&amp;featureid=tract470> ;
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship <urn:example:station> ;
      sampling:relatedSample examples:st1 ;
    ] ;
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship <urn:example:station> ;
      sampling:relatedSample examples:st2 ;
    ] ;
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship <urn:example:station> ;
      sampling:relatedSample examples:st3 ;
    ] ;
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship <urn:example:station> ;
      sampling:relatedSample examples:st4 ;
    ] ;
.
examples:ot2t
  rdf:type time:Instant ;
  time:inXSDDateTimeStamp "2005-01-11T17:22:25.00+10:00"^^xsd:dateTimeStamp ;
.
examples:ots1t
  rdf:type time:Instant ;
  time:inXSDDate "2005-06-17"^^xsd:date ;
.
examples:pr1
  rdf:type sosa:Sample ;
  geosparql:hasGeometry examples:pr1_ls1 ;
  geosparql:hasGeometry [
      rdf:type sf:Polygon ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Polygon(-30.711 134.196 , -30.711 134.205 , -30.702 134.205 , -30.702 134.196 )"^^geosparql:wktLiteral ;
    ] ;
  rdfs:comment "Geology traverse" ;
  rdfs:comment """elevation and position obtained using
					http://my.geology.example.org/procedures/survey/position/GPS4""" ;
  rdfs:label "pr1" ;
  skos:editorialNote "Bounding box encoded as Polygon" ;
  skos:editorialNote "Positional accuracy not encoded" ;
  sosa:isSampleOf <http://my.geology.example.org/unit/g345> ;
.
examples:pr1_ls1
  rdf:type sf:LineString ;
  geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4347> LineString(-30.711 134.205 321. , -30.710 134.204 315. , -30.709 134.203 303. , -30.708 134.201 296. , -30.706 134.196 272. , -30.703 134.197 271. , -30.702 134.199 280.  )"^^geosparql:wktLiteral ;
.
examples:pr1_s2
  rdf:type sosa:Sample ;
  <http://schema.org/material> <http://www.opengis.net/def/material/OGC-OM/2.0/rock> ;
  geosparql:hasGeometry [
      rdf:type sf:Point ;
      geosparql:asWKT "<http://www.opengis.net/def/crs/EPSG/0/4347> Point(-30.706 134.196 272.)"^^geosparql:wktLiteral ;
    ] ;
  rdfs:comment "Rock sample collected on traverse" ;
  rdfs:label "pr1_s2" ;
  prov:generatedAtTime "2007-01-29T12:19:55.00+09:00"^^xsd:dateTime ;
  sosa:isSampleOf <http://my.geology.example.org/unit/g345> ;
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship <http://www/example/org/sampling/parentSpecimen> ;
      sampling:relatedSample <http://my.geology.example.org/projects/2007/pr1_s1> ;
    ] ;
  sosa:usedProcedure <http://geochemistry.example.org/splits/biased/density/greaterThan/2.9> ;
.
examples:st1
  rdf:type sosa:Sample ;
  geosparql:hasGeometry [
      rdf:type sf:Point ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Point(-30.702 134.199 299.)"^^geosparql:wktLiteral ;
    ] ;
  sosa:isSampleOf <http://wfs.flakey.org?request=getFeature&amp;featureid=tract470> ;
.
examples:st2
  rdf:type sosa:Sample ;
  geosparql:hasGeometry [
      rdf:type sf:Point ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Point(-30.710 134.204 315.)"^^geosparql:wktLiteral ;
    ] ;
  sosa:isSampleOf <http://wfs.flakey.org?request=getFeature&amp;featureid=tract470> ;
.
examples:st2-h
  rdf:type sosa:Sample ;
  geosparql:hasGeometry [
      rdf:type sf:Point ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Point(-30.711 134.205)"^^geosparql:wktLiteral ;
    ] ;
  rdfs:comment "Hydrology sampling station" ;
  rdfs:label "st2" ;
  rdfs:seeAlso <http://my.hydrology.example.org/chemistry/2007/rtg78n> ;
  skos:editorialNote "Use rdfs:seeAlso for relatedObservation " ;
  sosa:isSampleOf <http://my.hydrology.example.org/catchments/Potamos> ;
  sampling:hasSampleRelationship [
      rdf:type sampling:SampleRelationship ;
      sampling:natureOfRelationship <http://www.example.org/complex/member> ;
      sampling:relatedSample <http://my.example.org/wfs?request=getFeature;featureid=coll32> ;
    ] ;
.
examples:st3
  rdf:type sosa:Sample ;
  geosparql:hasGeometry [
      rdf:type sf:Point ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Point(-30.709 134.203 303.)"^^geosparql:wktLiteral ;
    ] ;
  sosa:isSampleOf <http://wfs.flakey.org?request=getFeature&amp;featureid=tract470> ;
.
examples:st4
  rdf:type sosa:Sample ;
  geosparql:hasGeometry [
      rdf:type sf:Point ;
      geosparql:asWKT "<urn:ogc:def:crs:EPSG:6.8:4283> Point(-30.708 134.201 296.)"^^geosparql:wktLiteral ;
    ] ;
  sosa:isSampleOf <http://wfs.flakey.org?request=getFeature&amp;featureid=tract470> ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_51_1.ttl">Open in new window</a>
</blockquote>



## Example 2017ex2.ttl



```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .

<Observation/234534> a sosa:Observation ;
   rdfs:comment "Observation of the difference between the outside temperature and the inside temperature."@en ;
   sosa:hasFeatureOfInterest <apartment/134> ;
   sosa:hasResult [
      a om:Measure ;
      om:hasUnit om:degreeCelsius ;
      om:hasNumericalValue "-29.9"^^xsd:decimal ] .

<Observation/83985> a sosa:Observation ;
   rdfs:comment "Observation of the temperature inside apartment #134."@en ;
   sosa:hasFeatureOfInterest <apartment/134> ;
   sosa:hasResult [
      a om:Point ;
      om:hasScale om:CelsiusScale ;
      om:hasNumericalValue "22.4"^^xsd:decimal ] .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_52_1.ttl">Open in new window</a>
</blockquote>



## Example seismograph-sosa.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@base <http://example.org/data/> .

# Observation #358 of seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca) measured
# a earth displacement speed of 0.000500 cm/sec at 8:23 am on April 18, 2017, Pacific
# Daylight Time.

<earth>  rdf:type    sosa:FeatureOfInterest ;
  rdfs:label "earth"@en .

<VCAB-DP1-BP-40> rdf:type sosa:Sensor ;
  rdfs:label "seismograph VCAB DP1 BP 40 (Vineyard Canyon, Parkfield, Ca)"@en ;
  rdfs:seeAlso <https://earthquake.usgs.gov/monitoring/seismograms/153> ;
  sosa:observes <VCAB-DP1-BP-40#groundDisplacementSpeed> .

<VCAB-DP1-BP-40#location> rdf:type sosa:FeatureOfInterest ;
  rdfs:label "location of VCAB-DP1-BP-40"@en ;
  geo:lat 35.8648067 ;
  geo:long -120.6195831 ;
  geo:alt 12.75 ;
  sosa:isSampleOf <earth> .

<VCAB-DP1-BP-40#groundDisplacementSpeed>  rdf:type    sosa:ObservableProperty , sosa:Property ;
  rdfs:label "the ground displacement speed at location of VCAB-DP1-BP-40"@en ;
  sosa:isObservedBy <VCAB-DP1-BP-40> .

<VCAB-DP1-BP-40?t=2017-04-18T08%3A23%3A00-07%3A00> rdf:type sosa:Observation ;
  sosa:madeBySensor <VCAB-DP1-BP-40> ; 
  sosa:hasFeatureOfInterest  <VCAB-DP1-BP-40#location> ;
  sosa:observedProperty  <VCAB-DP1-BP-40#groundDisplacementSpeed> ;
  sosa:hasResult [
     rdf:type qudt:QuantityValue ;
     qudt:numericValue "5e-4"^^xsd:double ;
     qudt:hasUnit unit:CentiM-PER-SEC ] ;
  sosa:resultTime "2017-04-18T08:23:00-07:00"^^xsd:dateTimeStamp .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_53_1.ttl">Open in new window</a>
</blockquote>



## Example IDEAS.ttl



```turtle
 @prefix owl: <http://www.w3.org/2002/07/owl#> .
 @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
 @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
 @prefix sosa: <http://www.w3.org/ns/sosa#> .
 @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
 @prefix cdt: <http://w3id.org/lindt/custom_datatypes#>.

@base <http://example.org/data/> .

<IDEA> a owl:Ontology ;
   owl:imports <http://www.w3.org/ns/sosa> .
 
 <COPR> a sosa:FeatureOfInterest ;
   sosa:hasSample <COPR_SL> ;
   rdfs:comment "Coal Oil Point Reserve: UC Santa Barbara Natural Reserve System"@en ;
   rdfs:label "Coal Oil Point Reserve"@en .

 <COPR_Station_Location> a sosa:Sample ;
   rdfs:comment "."@en ;
   rdfs:label "Air around COPR Station"@en ;
   sosa:isSampleOf <COPR> .
 
 <COPR_Station> a sosa:Platform ;
   rdfs:comment "Station at Coal Oil Point Reserve, CA (see http://www.geog.ucsb.edu/ideas/COPR.html for details)"@en ;
   rdfs:label "Coal Oil Point Reserve Wx Station"@en ;
   rdfs:seeAlso <http://www.geog.ucsb.edu/ideas/COPR.html> ;
   sosa:hosts <COPR-HMP45C-L> .
 
 <COPR-HMP45C-L> a sosa:Platform ;
   rdfs:label "HMP45C-L Temperature and Relative Humidity Probe at Coal Oil Point, UCSB, CA"@en ;
   sosa:hosts <HUMICAP-H> ;
   sosa:isHostedBy <COPR_Station> .

 <HUMICAP-H> a sosa:Sensor ;
   rdfs:label "Vaisala HUMICAP H-chip"@en ;
   sosa:isHostedBy <COPR-HMP45C-L> .

 <RelativeHumidity> a sosa:ObservableProperty ;
   rdfs:comment "Humidity is a measure of the moisture content of air."@en ;
   rdfs:label "Relative Humidity"@en .

 <MeasuringRelativeHumidity> a sosa:Procedure ;
   rdfs:comment "Instructions for measuring relative humidity"@en .
  
 <RH_avg_1_COPR_15min_201706020300PM> a sosa:Observation ;
   rdfs:comment "Relative humidity as averaged over 15min at COPR."@en ;
   rdfs:label "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"@en ;
   sosa:madeBySensor <HUMICAP-H> ;
   sosa:hasFeatureOfInterest <COPR_Station_Location> ;
   sosa:hasSimpleResult "92.5 %"^^cdt:ucum ;
   sosa:resultTime "2017-06-02T03:00:00-07:00"^^xsd:dateTime ;
   sosa:observedProperty <RelativeHumidity> ;
   sosa:usedProcedure <MeasuringRelativeHumidity> .

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_54_1.ttl">Open in new window</a>
</blockquote>



## Example 2023ex1.ttl



```turtle
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .

<earthAtmosphere_StE> a sosa:Sample ;
  sosa:isSampleOf <earthAtmosphere> ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (4.387611 45.437772)"^^geo:WktLiteral ;
  ] ;
.

```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/ogcapi-sosa/build/tests/sosa/properties/spec-examples/example_55_1.ttl">Open in new window</a>
</blockquote>


# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/properties/spec-examples" target="_blank">_sources/properties/spec-examples</a></code>

