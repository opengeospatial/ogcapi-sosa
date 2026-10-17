# bblocks python transform: SOSA/SSN Turtle -> JSON-LD conforming to a target SOSA bblock.
#
# Installed by the spec-examples-jsonld skill. Referenced from transforms.yaml of each
# _sources/spec-examples/<group>/ block; runs inside bblocks-postprocess (rdflib + pyld).
#
# metadata (transforms.yaml):
#   rootClasses: [IRI, ...]   classes whose instances become the root object
#   containerClasses: [IRI]   classes whose SOSA links embed a root candidate (default rootClasses)
#   coerce: {term: datatype}  typed-literal coercions added to the output's local @context, for
#                             terms the target schema constrains to plain strings (e.g. resultTime
#                             with format: date-time) but the target context does not coerce
#   suppressTerms: [term]     context terms not to use when compacting (e.g. the GeoJSON alias
#                             'features' for sosa:hasMember, so the schema's 'hasMember' is used)
# per example (examples.yaml):
#   x-root: IRI               pick this resource as the root (multi-root examples)
#
# Output: the root resource framed and compacted with the block's own JSON-LD context
# (which is the target bblock's context, inherited via schema.yaml $ref), with that
# context removed and replaced by a prefix-only @context for any non-SOSA terms. Output
# profile validation re-applies the target block's context, so the JSON Schema, JSON-LD
# context and SHACL shapes of the target are all exercised.
import json
from pathlib import Path

from pyld import jsonld
from rdflib import BNode, Graph, RDF, URIRef

SOSA_SSN = ('http://www.w3.org/ns/sosa/', 'http://www.w3.org/ns/ssn/')


def _get(obj, key, default=None):
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


meta = transform_metadata.metadata
tctx = transform_metadata.context
root_classes = [URIRef(c) for c in _get(meta, 'rootClasses', [])]
container_classes = [URIRef(c) for c in (_get(meta, 'containerClasses') or [])] or root_classes
example = _get(tctx, 'example') or {}
wanted_root = _get(example, 'x-root')

# --- block JSON-LD context (assembled by the postprocessor for this block) ---------------
ctx_path = None
if _get(tctx, 'jsonld_context_path'):
    ctx_path = Path(_get(tctx, 'working_dir') or '.') / _get(tctx, 'jsonld_context_path')
if (ctx_path is None or not ctx_path.is_file()) and _get(meta, 'context'):
    ctx_path = Path(_get(tctx, 'working_dir') or '.') / _get(meta, 'context')
if ctx_path is None or not ctx_path.is_file():
    raise FileNotFoundError(f'JSON-LD context for this block not found ({ctx_path})')
block_context = json.loads(ctx_path.read_text(encoding='utf-8'))['@context']

# --- parse --------------------------------------------------------------------------------
src = transform_metadata.source_mime_type or 'text/turtle'
try:
    g = Graph(bind_namespaces='none')
except TypeError:  # rdflib < 7
    g = Graph()
g.parse(data=input_data, format='json-ld' if 'json' in src else 'turtle')
prefixes = {p: str(ns) for p, ns in g.namespaces()
            if p and not str(ns).startswith(SOSA_SSN) and p not in ('sosa', 'ssn', 'ssn-system')}
for p, ns in (_get(meta, '_prefixes') or {}).items():
    prefixes.setdefault(p, ns)
local_context = dict(prefixes)
for term, datatype in (_get(meta, 'coerce') or {}).items():
    term_def = block_context.get(term) if isinstance(block_context, dict) else None
    term_id = term_def.get('@id') if isinstance(term_def, dict) else term_def
    if term_id:
        local_context[term] = {'@id': term_id, '@type': datatype}
        prefixes.setdefault('xsd', 'http://www.w3.org/2001/XMLSchema#')
        local_context.setdefault('xsd', prefixes['xsd'])


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

# Blank-node roots cannot be addressed by @id in a frame: skolemize just that node.
if isinstance(root, BNode):
    skolem = URIRef(f'urn:x-bnode:{root}')
    for p, o in list(g.predicate_objects(root)):
        g.remove((root, p, o)); g.add((skolem, p, o))
    for s, p in list(g.subject_predicates(root)):
        g.remove((s, p, root)); g.add((s, p, skolem))
    root = skolem

# --- frame + compact ----------------------------------------------------------------------
expanded = json.loads(g.serialize(format='json-ld'))
frame_context = dict(local_context, **{t: None for t in (_get(meta, 'suppressTerms') or [])})
context = [block_context, frame_context] if frame_context else block_context
framed = jsonld.frame(expanded, {'@context': context, '@id': str(root)},
                      {'embed': '@once', 'omitGraph': True})
framed.pop('@context', None)
if '@graph' in framed:  # defensive: omitGraph should have collapsed a single match
    framed = framed['@graph'][0]
if str(framed.get('id', '')).startswith('urn:x-bnode:'):
    framed.pop('id')



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
if any(not isinstance(v, str) for v in local_context.values()):
    local_context['xsd'] = 'http://www.w3.org/2001/XMLSchema#'
out = {'@context': local_context, **framed} if local_context else framed
output_data = json.dumps(out, indent=2, ensure_ascii=False)
