## SOSA System Feature

This building block defines a GeoJSON feature wrapping the properties common to any `sosa:System` - an Asset that implements a Procedure and carries out Executions.

Even though `System` is abstract, feature-level building blocks such as [Sensor Feature](../sensor/) explicitly declare conformance to this block rather than only to [System Properties](../../properties/system/) at the properties level, so the relationship is discoverable directly from the register.
