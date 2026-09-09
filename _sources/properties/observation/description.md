## SOSA Observation Properties

This building block describes the canonical set of properties for an Observation object.

These properties are independent of the feature model implementation - for example may be included in the "properties" component of a GeoJSON object, or used in any other schema.

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."

Observation is a specialisation of the abstract SOSA `Execution` class, alongside `Actuation` and
`Sampling`. It inherits its common properties (`resultTime`, `phenomenonTime`, `hasFeatureOfInterest`,
`usedProcedure`, `hasResult`/`hasSimpleResult`) from [Execution Properties](../execution/) via
[Observation Properties (SOSA OWA)](../observation-owa/), adding `observedProperty` and
`madeBySensor` as properties specific to Observation.

