## SOSA Sample Properties

A Sample is "a feature which is intended to be representative of a `FeatureOfInterest` on which Observations may be made." It is typically the result of a [Sampling](../sampling/), linked back via `isResultOf`.

`sosa:MaterialSample`, `sosa:SpatialSample`, and `sosa:StatisticalSample` are bare subclasses of Sample with no additional properties - represent them via `featureType`/`@type` rather than as separate building blocks.
