## SOSA System Properties

This building block describes the properties common to any `sosa:System` - an Asset (such as a device, sensor, or software agent) that implements a Procedure and carries out Executions.

`sosa:System` generalizes `Sensor`, `Actuator`, and `Sampler`, and is itself a specialisation of [Asset Properties](../asset/). It is considered abstract: individual systems SHOULD be typed with one of these concrete sub-classes rather than with `sosa:System` itself.

These properties are independent of the feature model implementation, and are inherited by more specific building blocks (such as [Sensor Properties](../sensor/)) rather than used directly.
