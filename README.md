# OGC Building Blocks for SOSA 


The SOSA ([Sensor, Observation, Sample, and Actuator](https://www.w3.org/TR/vocab-ssn/)) ontology  is a realisation of the 
 Observations, Measurements and Sampling (OMS) Conceptual model. This repository defines:
 *  JSON schema encoding for each feature type (class) defined by SOSA, compatible with the OGC API Features using the FG-JSON extension to GeoJSON
 * JSON-LD contexts for each class to link schema elements to relevant class and properties defined by SOSA
 * examples that can be used in documentation
 * validation resources  for this schema and the JSON-LD RDF binding

 This encoding is defined using the [OGC Building Blocks](https://opengeospatial.github.io/bblocks) template, and hence can be combined with other Building Blocks to implement more complete domain models with interoperable encodings and extensible APIs.

## Status and Compatibility

This building block is __under construction__ and is undertaken in the context of the update of SOSA to align with OMS V3.

It is assumed that this will be _backwards compatible_ with the last published SOSA version https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/. Any changes to this status will be noted in this section.

## Documentation

This building block self-documents using the build process described below.  For each component building block in this repository the
deployed documentation is built on commit and can be found here: 

https://opengeospatial.github.io/ogcapi-sosa/



## General Building block repository structure


The `build/` directory contains the **_reusable assets_** for implementing this building block, in full or part, and the rest of the repository contain *sources* to build these assets.  *Sources* minimise redundant information and preserve original forms of inputs, such as externally published schemas etc.  This allow these to be updated safely, and also allows for alternative forms of original source material to be used whilst preserving uniformity of the reusable assets.

Note that the these components will be consistently structured for a given type of building block, and the editable components may vary according to the source material used to derive the building block, and therefore cannot be directly referenced.

### Editable components

- `features/`: schemas for the feature types defined by this bb (which is a "super-bb" containing at least oneOf these defined features)
- `datatypes/`: reusable schemas for (potentially complex) datatypes defined by this bb
- `aspects/`: groups of properties that may be included in feature types (equivalent to attribute groups in XML schema)
- `assets/`: Documentation assets (e.g. images) directory. See [Assets](#assets) below.

[More information on design and usage](https://github.com/opengeospatial/bblock-template/blob/master/USAGE.md)
