## SOSA ExecutionCollection Feature

This building block defines a GeoJSON FeatureCollection wrapping the properties common to any `sosa:ExecutionCollection` - the abstract collection of Executions.

Even though `ExecutionCollection` is abstract, feature-level building blocks such as [ObservationCollection Feature](../observationCollection/) explicitly declare conformance to this block rather than only to [ExecutionCollection Properties](../../properties/executionCollection/) at the properties level, so the relationship is discoverable directly from the register.
