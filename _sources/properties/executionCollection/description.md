## SOSA ExecutionCollection Properties

This building block describes the properties common to any `sosa:ExecutionCollection` - the abstract collection of Executions.

`sosa:ExecutionCollection` generalizes `ActuationCollection`, `ObservationCollection`, and `SamplingCollection`. It is considered abstract, and shares the same properties as [Execution Properties](../execution/) - collections do not declare their own member type here, since member item types differ per concrete collection.

These properties are independent of the feature model implementation, and are inherited by more specific building blocks (such as [ObservationCollection Properties](../observationCollection/)) rather than used directly.
