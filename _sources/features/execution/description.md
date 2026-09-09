## SOSA Execution Feature

This building block defines a GeoJSON feature wrapping the properties common to any
`sosa:Execution` - the abstract act of carrying out a Procedure using a System.

`sosa:Execution` generalizes the `Actuation`, `Observation`, and `Sampling` classes. It is
considered abstract: individual executions SHOULD be typed with one of these concrete
sub-classes rather than with `sosa:Execution` itself.

Even though `Execution` is abstract, feature-level building blocks such as
[Observation Feature](../observation/) explicitly declare conformance to this block rather
than only to [Execution Properties](../../properties/execution/) at the properties level.
Without an explicit feature-level relationship, a client would need to traverse the schema
graph down into the `properties` container to infer that an Observation Feature is also an
Execution Feature - this block makes that conformance discoverable directly from the register.
