## SOSA Asset Properties

This building block describes the properties common to any `sosa:Asset` - a physical or virtual entity that can be hosted on, or host, other Assets, and be the subject of a Deployment.

`sosa:Asset` generalizes `System` and `Platform`. It is considered abstract: individual assets SHOULD be typed with one of these concrete sub-classes rather than with `sosa:Asset` itself.

These properties are independent of the feature model implementation, and are inherited by more specific building blocks (such as [System Properties](../system/) and [Platform Properties](../platform/)) rather than used directly.
