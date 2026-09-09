## SOSA Asset Feature

This building block defines a GeoJSON feature wrapping the properties common to any `sosa:Asset` - a physical or virtual entity that can be hosted on, or host, other Assets.

Even though `Asset` is abstract, feature-level building blocks such as [System Feature](../system/) and [Platform Feature](../platform/) explicitly declare conformance to this block rather than only to [Asset Properties](../../properties/asset/) at the properties level, so the relationship is discoverable directly from the register.
