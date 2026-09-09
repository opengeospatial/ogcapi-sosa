## SOSA Execution Properties

This building block describes the properties common to any `sosa:Execution` - the abstract
act of carrying out a Procedure using a System.

`sosa:Execution` generalizes the `Actuation`, `Observation`, and `Sampling` classes. It is
considered abstract: individual executions SHOULD be typed with one of these concrete
sub-classes rather than with `sosa:Execution` itself.

These properties are independent of the feature model implementation, and are inherited by
more specific building blocks (such as [Observation Properties](../observation-owa/)) rather
than used directly.
