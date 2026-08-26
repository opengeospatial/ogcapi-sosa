# Transform: flatten-observations
#
# Flattens a (possibly nested) SOSA ObservationCollection GeoJSON document into a
# plain GeoJSON FeatureCollection of Observation Features. Each output Feature's
# `properties` merges in every property inherited from its containing
# ObservationCollection(s) - the nearest collection wins on conflicting keys. If a
# Feature has no geometry of its own, one is taken from the `geometry` of its own
# `hasFeatureOfInterest`, or - failing that - from the nearest ancestor collection's
# `hasFeatureOfInterest` that carries a geometry.
#
# Executed as a bblocks `python` transform: receives `input_data` (the source JSON
# text) and must assign the result to `output_data`.

import json

_MISSING = object()

_COLLECTION_MARKERS = ("ObservationCollection",)


def _has_collection_marker(node):
    for key in ("featureType", "@type", "type"):
        value = node.get(key)
        if isinstance(value, str) and any(m in value for m in _COLLECTION_MARKERS):
            return True
        if isinstance(value, list) and any(
            isinstance(v, str) and any(m in v for m in _COLLECTION_MARKERS)
            for v in value
        ):
            return True
    return False


def _node_kind(node):
    if isinstance(node, str):
        return "ref"
    if isinstance(node, dict):
        if "properties" in node or node.get("type") in ("Feature", "FeatureCollection"):
            return "wrapped"
        return "raw"
    return "unknown"


def _own_id(node):
    return node.get("@id", node.get("id"))


def _decompose(node):
    """
    Break a member down into (own_id, own_geometry, own_properties, sub_members,
    is_collection). `own_geometry` is `_MISSING` when the node carries no
    `geometry` key at all (as opposed to an explicit `null`).
    """
    kind = _node_kind(node)

    if kind == "ref":
        # A bare IRI/CURIE reference - no embedded data, only inherited properties apply.
        return node, _MISSING, {}, [], False

    if kind == "wrapped":
        # A GeoJSON Feature (or FeatureCollection): SOSA properties live under `properties`,
        # members under `features` and/or `properties.hasMember`.
        props = node.get("properties") or {}
        sub_members = list(node.get("features") or []) + list(props.get("hasMember") or [])
        own_properties = {k: v for k, v in props.items() if k != "hasMember"}
        own_geometry = node["geometry"] if "geometry" in node else _MISSING
        is_collection = bool(sub_members) or _has_collection_marker(node)
        return _own_id(node), own_geometry, own_properties, sub_members, is_collection

    if kind == "raw":
        # A bare SOSA property object (no GeoJSON wrapper), as found inside `hasMember`.
        sub_members = list(node.get("hasMember") or [])
        own_properties = {k: v for k, v in node.items() if k not in ("hasMember", "@id", "id")}
        is_collection = bool(sub_members) or _has_collection_marker(node)
        return _own_id(node), _MISSING, own_properties, sub_members, is_collection

    return None, _MISSING, {}, [], False


def _geometry_from_foi_chain(foi_chain):
    """First non-null geometry carried by a featureOfInterest object, nearest first."""
    for foi in foi_chain:
        if isinstance(foi, dict):
            geometry = foi.get("geometry")
            if geometry is not None:
                return geometry
    return None


def _flatten(node, inherited_properties, foi_chain, output_features):
    own_id, own_geometry, own_properties, sub_members, is_collection = _decompose(node)

    effective_properties = dict(inherited_properties)
    effective_properties.update(own_properties)

    own_foi = own_properties.get("hasFeatureOfInterest")
    current_foi_chain = ([own_foi] if own_foi is not None else []) + foi_chain

    if is_collection:
        for member in sub_members:
            _flatten(member, effective_properties, current_foi_chain, output_features)
        return

    geometry = own_geometry
    if geometry is _MISSING or geometry is None:
        geometry = _geometry_from_foi_chain(current_foi_chain)

    feature = {"type": "Feature"}
    if own_id is not None:
        feature["@id"] = own_id
    feature["geometry"] = geometry
    feature["properties"] = effective_properties
    output_features.append(feature)


_data = json.loads(input_data)

_flattened_features = []
_flatten(_data, {}, [], _flattened_features)

_result = {
    "type": "FeatureCollection",
    "features": _flattened_features,
}

output_data = json.dumps(_result, indent=2, ensure_ascii=False)
