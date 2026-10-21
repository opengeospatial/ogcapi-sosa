# bblocks python transform: SOSA/SSN Turtle -> JSON-LD conforming to a target SOSA bblock.
#
# Installed by the spec-examples-jsonld skill. Referenced from transforms.yaml of each
# _sources/spec-examples/<group>/ block; runs inside bblocks-postprocess (rdflib + pyld).
#
# metadata (transforms.yaml):
#   target: bblock id         the output profile; its published JSON-LD context is referenced
#                             by the output's @context
#   rootClasses: [IRI, ...]   classes whose instances become the root object
#   containerClasses: [IRI]   classes whose SOSA links embed a root candidate (default rootClasses)
#   suppressTerms: [term]     target context terms not to use when compacting (e.g. the GeoJSON
#                             alias 'features' for sosa:hasMember, so the schema's 'hasMember' is used)
# per example (examples.yaml):
#   x-root: IRI               pick this resource as the root (multi-root examples)
#   snippet shacl-closure     (from the transform context) closures that may put the example's
#                             resources in collections: the root takes a property it lacks from
#                             the nearest containing collection with a single value for it; a
#                             closure may also give an example resource such a value directly
#
# Output: the root resource framed and compacted with the target bblock's JSON-LD context, with
#   "@context": [<target context URL>, {<only what the target context does not define>}]
# The local part holds the example's own prefixes and typed-literal coercions for its non-SOSA
# properties; it never redefines a target term. Times are plain xsd:dateTime strings: a
# phenomenonTime time:Instant with a single date-time position becomes a string, anything more
# complex (e.g. a time:Interval) stays an object using the target's time terms.
import json
import re
from pathlib import Path
from urllib.parse import urljoin

from pyld import jsonld
from rdflib import BNode, Graph, Literal, Namespace, RDF, URIRef

SOSA_SSN = ('http://www.w3.org/ns/sosa/', 'http://www.w3.org/ns/ssn/')
SOSA = Namespace('http://www.w3.org/ns/sosa/')
TIME = Namespace('http://www.w3.org/2006/time#')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
TZ = re.compile(r'(Z|[+-]\d{2}:\d{2})$')
PLAIN = (None, XSD.string, URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'))


def _get(obj, key, default=None):
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


meta = transform_metadata.metadata
tctx = transform_metadata.context
working_dir = Path(_get(tctx, 'working_dir') or '.')
root_classes = [URIRef(c) for c in _get(meta, 'rootClasses', [])]
container_classes = [URIRef(c) for c in (_get(meta, 'containerClasses') or [])] or root_classes
example = _get(tctx, 'example') or {}
wanted_root = _get(example, 'x-root')

# --- target JSON-LD context: local file (to compact with) and published URL (to reference) --
own_ctx = _get(tctx, 'jsonld_context_path')
if not own_ctx or not (working_dir / own_ctx).is_file():
    raise FileNotFoundError(f'JSON-LD context for this block not found ({own_ctx})')
target = _get(meta, 'target')
target_ctx = own_ctx  # the block $refs the target schema, so its context is the target's
if target:
    # annotated/<register subdirs>/<own subdirs>/context.jsonld -> .../<target subdirs>/...
    id_prefix = _get(tctx, 'id_prefix') or ''
    own_parts = _get(tctx, 'bblock_id')[len(id_prefix):].split('.')
    target_parts = target[len(id_prefix):].split('.') if target.startswith(id_prefix) else None
    ctx_parts = Path(own_ctx).parts
    if target_parts and tuple(ctx_parts[-1 - len(own_parts):-1]) == tuple(own_parts):
        candidate = Path(*ctx_parts[:-1 - len(own_parts)], *target_parts, ctx_parts[-1])
        if (working_dir / candidate).is_file():
            target_ctx = str(candidate.as_posix())
target_context = json.loads((working_dir / target_ctx).read_text(encoding='utf-8'))['@context']
base_url = _get(tctx, 'base_url')
target_ctx_ref = urljoin(base_url, Path(target_ctx).as_posix()) if base_url else Path(target_ctx).as_posix()


def _context_iris(ctx, prefixes=None):
    """IRIs of all terms defined in a context, including property-scoped ones."""
    if isinstance(ctx, list):
        return set().union(*[_context_iris(c, prefixes) for c in ctx]) if ctx else set()
    if not isinstance(ctx, dict):
        return set()
    prefixes = dict(prefixes or {})
    prefixes.update({k: v for k, v in ctx.items() if isinstance(v, str) and v.endswith(('/', '#'))})

    def expand(v):
        if isinstance(v, str) and ':' in v and v.split(':', 1)[0] in prefixes:
            return prefixes[v.split(':', 1)[0]] + v.split(':', 1)[1]
        return v
    iris = set()
    for k, v in ctx.items():
        if k.startswith('@'):
            continue
        iris.add(expand(v.get('@id', k) if isinstance(v, dict) else v))
        if isinstance(v, dict) and '@context' in v:
            iris |= _context_iris(v['@context'], prefixes)
    return iris


target_terms = set(target_context) if isinstance(target_context, dict) else set()
target_iris = _context_iris(target_context)

# --- parse --------------------------------------------------------------------------------
src = transform_metadata.source_mime_type or 'text/turtle'
try:
    g = Graph(bind_namespaces='none')
except TypeError:  # rdflib < 7
    g = Graph()
# relative IRIs resolve against the example's URL, as in Turtle validation
snippet_ref = _get(_get(tctx, 'snippet'), 'ref')
g.parse(data=input_data, format='json-ld' if 'json' in src else 'turtle',
        publicID=snippet_ref if isinstance(snippet_ref, str) and re.match(r'^https?://', snippet_ref) else None)
prefixes = {p: str(ns) for p, ns in g.namespaces()
            if p and not str(ns).startswith(SOSA_SSN) and p not in ('sosa', 'ssn', 'ssn-system')}
for p, ns in (_get(meta, '_prefixes') or {}).items():
    prefixes.setdefault(p, ns)
# never redefine a target term
prefixes = {p: ns for p, ns in prefixes.items() if p not in target_terms}


# --- root selection -----------------------------------------------------------------------
def _instances(classes):
    return {s for c in classes for s in g.subjects(RDF.type, c)}


def _roots():
    inst = _instances(root_classes)
    containers = _instances(container_classes)
    nested = set()
    for s, p, o in g:
        if o not in inst or s == o or p == RDF.type:
            continue
        if isinstance(o, BNode) or not str(p).startswith(SOSA_SSN) or s in containers:
            nested.add(o)
    return sorted(inst - nested, key=str)


if wanted_root:
    root = URIRef(wanted_root)
    if (root, None, None) not in g:
        raise ValueError(f'x-root {wanted_root} has no statements in the example')
else:
    roots = _roots()
    if not roots:
        raise ValueError('no root resource of class ' + ', '.join(root_classes) + ' found')
    root = roots[0]


# --- values inherited from containing collections (SOSA collection rule 2) ------------------
# The snippet's SHACL closures (passed in the transform context) may put the example's resources
# in collections. A property the root lacks takes the value of the nearest containing collection
# (in the example or a closure) that has it, if that collection has a single value - as the SHACL
# rules do - so the output is complete on its own.
def _closure_graph():
    cg = Graph()
    files_path = _get(tctx, 'bblock_files_path') or '.'
    for ref in _get(_get(tctx, 'snippet'), 'shacl-closure') or []:
        if re.match(r'^https?://', ref):
            cg.parse(ref)
            continue
        for candidate in (working_dir / files_path / ref, working_dir / ref):
            if candidate.is_file():
                cg.parse(candidate, format='turtle' if candidate.suffix == '.ttl' else None)
                break
        else:
            raise FileNotFoundError(f'SHACL closure {ref} not found')
    return cg


GEOJSON_FEATURES = URIRef('https://purl.org/geojson/vocab#features')
INHERITED = [SOSA[p] for p in (
    'resultTime', 'phenomenonTime', 'startTime', 'endTime', 'hasFeatureOfInterest',
    'hasUltimateFeatureOfInterest', 'observedProperty', 'actsOnProperty', 'usedProcedure',
    'madeBySensor', 'madeByActuator', 'madeBySampler', 'madeBySystem')]


def _containers(u, node):
    return set(u.subjects(SOSA.hasMember, node)) | set(u.subjects(GEOJSON_FEATURES, node)) \
        | set(u.objects(node, SOSA.memberOf))


def _copy(u, node):
    """Copy a blank node value's description from u into g."""
    if isinstance(node, BNode):
        for p, o in u.predicate_objects(node):
            if (node, p, o) not in g:
                g.add((node, p, o))
                _copy(u, o)


def _inherit(u, node):
    for p in INHERITED:
        if (node, p, None) in g:
            continue
        seen, level = {node}, _containers(u, node)
        while level:
            values = {v for c in level for v in u.objects(c, p)}
            if values:
                if len(values) == 1:
                    value = values.pop()
                    g.add((node, p, value))
                    _copy(u, value)
                break
            seen |= level
            level = {c for n in level for c in _containers(u, n)} - seen


closure = _closure_graph()
if len(closure):
    # values a closure gives the example's own resources directly
    direct = [(s, p, o) for s, p, o in closure
              if p in INHERITED and (s, None, None) in g and (s, p, None) not in g]
    for s, p, o in direct:
        g.add((s, p, o))
        _copy(closure, o)
    u = g + closure
    # the root, and the example's resources that are members of closure-only collections (the
    # output may embed them); members of the example's own collections inherit from those
    in_closure = {m for p in (SOSA.hasMember, GEOJSON_FEATURES)
                  for c, m in closure.subject_objects(p) if (c, None, None) not in g} \
        | {m for m, c in closure.subject_objects(SOSA.memberOf) if (c, None, None) not in g}
    for node in sorted(n for n in in_closure if (n, None, None) in g and n != root) + [root]:
        _inherit(u, node)


# --- times: plain xsd:dateTime strings where the value is a single date-time ----------------
def _retype(p, wanted, accept):
    for s, o in list(g.subject_objects(p)):
        if isinstance(o, Literal) and o.datatype in accept and o.datatype != wanted:
            if wanted == XSD.dateTimeStamp and not TZ.search(str(o)):
                continue
            g.remove((s, p, o))
            g.add((s, p, Literal(str(o), datatype=wanted)))


DATETIMES = (XSD.dateTime, XSD.dateTimeStamp)
for p in (SOSA.resultTime, SOSA.phenomenonTime, SOSA.startTime, SOSA.endTime, TIME.inXSDDateTime):
    _retype(p, XSD.dateTime, DATETIMES)
_retype(TIME.inXSDDateTimeStamp, XSD.dateTimeStamp, DATETIMES)

for s, inst in list(g.subject_objects(SOSA.phenomenonTime)):
    if not isinstance(inst, BNode) or len(list(g.subject_predicates(inst))) != 1:
        continue
    po = list(g.predicate_objects(inst))
    types = {o for p, o in po if p == RDF.type}
    values = [(p, o) for p, o in po if p != RDF.type]
    if (types <= {TIME.Instant} and len(values) == 1
            and values[0][0] in (TIME.inXSDDateTime, TIME.inXSDDateTimeStamp)
            and isinstance(values[0][1], Literal) and values[0][1].datatype in DATETIMES):
        g.remove((inst, None, None))
        g.remove((s, SOSA.phenomenonTime, inst))
        g.add((s, SOSA.phenomenonTime, Literal(str(values[0][1]), datatype=XSD.dateTime)))

# --- typed literals of the example's own properties: coerce in the local context -----------
# (integers, doubles and booleans are serialized as native JSON values and need none)
NATIVE = (XSD.integer, XSD.double, XSD.boolean)
coercions = {}
for p in set(g.predicates()):
    if str(p) in target_iris or str(p).startswith(SOSA_SSN):
        continue
    dts = {o.datatype if isinstance(o, Literal) else 'node' for o in g.objects(None, p)}
    if len(dts) == 1 and (dt := dts.pop()) not in PLAIN + NATIVE and dt != 'node':
        coercions[p] = dt


def _curie(iri):
    for pfx, ns in sorted(prefixes.items(), key=lambda kv: -len(kv[1])):
        if iri.startswith(ns) and re.fullmatch(r'[A-Za-z_][\w.-]*', iri[len(ns):] or '-'):
            return f'{pfx}:{iri[len(ns):]}'
    return None


local_context = dict(prefixes)
for p, dt in coercions.items():
    term = _curie(str(p))
    if term and term not in target_terms:
        dt = str(dt)
        local_context[term] = {'@type': 'xsd:' + dt[len(str(XSD)):] if dt.startswith(str(XSD))
                               and 'xsd' not in target_terms else _curie(dt) or dt}


# Blank-node roots cannot be addressed by @id in a frame: skolemize just that node.
if isinstance(root, BNode):
    skolem = URIRef(f'urn:x-bnode:{root}')
    for p, o in list(g.predicate_objects(root)):
        g.remove((root, p, o)); g.add((skolem, p, o))
    for s, p in list(g.subject_predicates(root)):
        g.remove((s, p, root)); g.add((s, p, skolem))
    root = skolem

# --- frame + compact ----------------------------------------------------------------------
expanded = json.loads(g.serialize(format='json-ld', use_native_types=True))
# A term coercing to a datatype (e.g. phenomenonTime -> xsd:dateTime) is not selected for an
# object value (e.g. a time:Interval), so compact with those coercions removed and turn the
# matching value objects back into plain strings afterwards (_plain): same JSON, same RDF.
coerced = {t: d['@type'] for t, d in target_context.items()
           if isinstance(d, dict) and d.get('@type') not in (None, '@id', '@vocab', '@json')} \
    if isinstance(target_context, dict) else {}
compact_target = {t: ({k: v for k, v in d.items() if k != '@type'} if t in coerced else d)
                  for t, d in target_context.items()} if coerced else target_context
frame_context = dict(local_context, **{t: None for t in (_get(meta, 'suppressTerms') or [])})
context = [compact_target, frame_context] if frame_context else compact_target
framed = jsonld.frame(expanded, {'@context': context, '@id': str(root)},
                      {'embed': '@once', 'omitGraph': True})
framed.pop('@context', None)
if '@graph' in framed:  # defensive: omitGraph should have collapsed a single match
    framed = framed['@graph'][0]
if str(framed.get('id', '')).startswith('urn:x-bnode:'):
    framed.pop('id')


def _tidy(node):
    """Value objects keep the @type keyword rather than the 'featureType' alias of the target."""
    if isinstance(node, list):
        return [_tidy(v) for v in node]
    if not isinstance(node, dict):
        return node
    node = {k: _tidy(v) for k, v in node.items()}
    if '@value' in node:
        node = {('@type' if k in ('featureType', 'type') else k): v for k, v in node.items()}
    return node


def _expand_type(t):
    if isinstance(t, str) and ':' in t and t.split(':', 1)[0] in local_context:
        return local_context[t.split(':', 1)[0]] + t.split(':', 1)[1]
    return t


def _plain(node):
    """Values of datatype-coerced target terms as plain strings (see compact_target)."""
    if isinstance(node, list):
        return [_plain(v) for v in node]
    if not isinstance(node, dict):
        return node
    out = {}
    for k, v in node.items():
        if k in coerced:
            vs = [{'@value': x['@value']} if isinstance(x, dict) and set(x) == {'@value', '@type'}
                  and _expand_type(x['@type']) == coerced[k] else x for x in (v if isinstance(v, list) else [v])]
            vs = [x['@value'] if isinstance(x, dict) and set(x) == {'@value'} else _plain(x) for x in vs]
            out[k] = vs if isinstance(v, list) else vs[0]
        else:
            out[k] = _plain(v)
    return out


framed = _plain(_tidy(framed))


def _usage(node, prefixes_used, keys_used):
    if isinstance(node, dict):
        for k, v in node.items():
            keys_used.add(k)
            _usage(k, prefixes_used, keys_used); _usage(v, prefixes_used, keys_used)
    elif isinstance(node, list):
        for v in node:
            _usage(v, prefixes_used, keys_used)
    elif isinstance(node, str) and ':' in node:
        prefixes_used.add(node.split(':', 1)[0])


used_prefixes, used_keys = set(), set()
_usage(framed, used_prefixes, used_keys)
local_context = {k: v for k, v in local_context.items()
                 if (k in used_prefixes if isinstance(v, str) else k in used_keys)}
for k, v in list(local_context.items()):
    if isinstance(v, dict):  # a used coercion needs its own prefixes
        for c in (k, v['@type']):
            pfx = c.split(':', 1)[0] if ':' in c else None
            if pfx in prefixes:
                local_context.setdefault(pfx, prefixes[pfx])
            elif pfx == 'xsd':
                local_context.setdefault('xsd', str(XSD))
out = {'@context': [target_ctx_ref, local_context] if local_context else target_ctx_ref, **framed}
output_data = json.dumps(out, indent=2, ensure_ascii=False)
