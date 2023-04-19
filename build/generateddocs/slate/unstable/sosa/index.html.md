---
title: Sensor, Observation, Sample, and Actuator (SOSA) (Api)

toc_footers:
  - Version 1.0
  - <a href='#'>Sensor, Observation, Sample, and Actuator (SOSA)</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Sensor, Observation, Sample, and Actuator (SOSA) (Api)
---

# Overview

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

# Description

Sensors are a major source of data available on the Web today. While sensor data may be published as mere values,
searching, reusing, integrating, and interpreting these data requires more than just the observation results. Of equal
importance for the proper interpretation of these values is information about the studied feature of interest, such as a
river, the observed property, such as flow velocity, the utilized sampling strategy, such as the specific locations and
times at which the velocity was measured, and a variety of other information. OGC's Sensor Web Enablement
standards ([Observations and Measurements / O&M](http://www.opengeospatial.org/standards/om),
[SensorML](http://portal.opengeospatial.org/files/55939)) provide a means to annotate sensors and their observations.
However, these standards are not integrated and aligned with W3C Semantic Web technologies and Linked Data in
particular, which are key drivers for creating and maintaining a global and densely interconnected graph of data. With
the rise of the Web of Things and smart cities and homes more generally, actuators and the data they produce also become
first-class citizens of the Web. Given their close relation to sensors, observations, procedures, and features of
interest, it is desirable to provide a common ontology that also includes actuators and actuation. Finally, with the
increasing diversity of data and data providers, definitions such as those for sensors need to be broadened, e.g., to
include social sensing. The following specifications introduce the new Semantic Sensor Network (SSN) and Sensor,
Observation, Sample, and Actuator (SOSA) ontologies that are set out to provide flexible but coherent perspectives for
representing the entities, relations, and activities involved in sensing, sampling, and actuation. SOSA provides a
lightweight core for SSN and aims at broadening the target audience and application areas that can make use of Semantic
Web ontologies. At the same time, SOSA acts as minimal interoperability fall-back level, i.e., it defines those common
classes and properties for which data can be safely exchanged across all uses of SSN, its modules, and SOSA.

# Schema

[schema.yaml](https://raw.githubusercontent.com/opengeospatial/ogcapi-sosa/master/unstable/sosa/_superbblock/schema.yaml)
# Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
