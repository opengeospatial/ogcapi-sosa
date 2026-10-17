#!/usr/bin/env python3
"""
Classify SOSA spec examples by the SOSA/SSN class of their root resources, and
assign each to a target building block for JSON-LD conversion + output profile
validation.

The candidate set is the document's examples (via check_spec_examples.doc_examples)
plus the examples already in the bblocks, so nothing is dropped.

Usage:
  python classify_examples.py [--repo .] [--spec-dir PATH] [--out plan.yaml]

Writes a grouping plan (YAML) consumed by sync_spec_example_blocks.py.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from urllib.request import urlopen

import yaml
from rdflib import BNode, Graph, RDF, URIRef, Namespace

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'spec-examples-check' / 'scripts'))
from check_spec_examples import doc_examples, bblock_examples, RAW_BASE, PUBLISHED_BASE  # noqa: E402

SOSA = Namespace('http://www.w3.org/ns/sosa/')

# Target groups in priority order: the first group whose root class has an
# instance that is not nested inside another instance (see roots()) wins.
# group -> (target bblock, root classes)
GROUPS = {
    'observation-collections': ('ogc.sosa.properties.observationCollection', [SOSA.ObservationCollection]),
    'sample-collections': ('ogc.sosa.properties.sampleCollection', [SOSA.SampleCollection]),
    'observations': ('ogc.sosa.properties.observation', [SOSA.Observation]),
    'samplings': ('ogc.sosa.properties.sampling', [SOSA.Sampling]),
    'actuations': ('ogc.sosa.properties.actuation', [SOSA.Actuation]),
    'deployments': ('ogc.sosa.properties.deployment', [SOSA.Deployment]),
    'samples': ('ogc.sosa.properties.sample', [SOSA.Sample, SOSA.MaterialSample]),
    'platforms': ('ogc.sosa.properties.platform', [SOSA.Platform]),
    'systems': ('ogc.sosa.properties.system',
                [SOSA.Sensor, SOSA.Actuator, SOSA.Sampler, SOSA.System]),
}
OTHER = 'other'
SOSA_SSN = ('http://www.w3.org/ns/sosa/', 'http://www.w3.org/ns/ssn/')


def load(url: str, spec_dir: Path | None) -> tuple[Graph, str]:
    text = None
    if spec_dir and url.startswith(PUBLISHED_BASE):
        local = spec_dir / url[len(PUBLISHED_BASE):]
        if local.is_file():
            text = local.read_text(encoding='utf-8')
    if text is None:
        raw = RAW_BASE + url[len(PUBLISHED_BASE):] if url.startswith(PUBLISHED_BASE) else url
        with urlopen(raw, timeout=30) as r:
            text = r.read().decode('utf-8')
    g = Graph().parse(data=text, format='turtle' if url.endswith('.ttl') else 'json-ld', publicID=url)
    return g, text


SUBCLASSES = {SOSA.MaterialSample: SOSA.Sample}
BAD_SOSA_NS = ('http://www.w3.org/ns/sosa#', 'https://www.w3.org/TR/vocab-ssn/', 'https://www.w3.org/ns/sosa/')


def instances(g: Graph, classes: list[URIRef]) -> set:
    wanted = set(classes) | {sub for sub, sup in SUBCLASSES.items() if sup in classes}
    return {s for c in wanted for s in g.subjects(RDF.type, c)}


def roots(g: Graph, classes: list[URIRef], container_classes: list[URIRef]) -> list:
    """Instances of the classes that would be top-level when framed. An instance is
    embedded (not a root) if it is
      - a blank node referenced from anything else, or
      - referenced through a non-SOSA/SSN predicate (e.g. owl:hasValue in a restriction), or
      - referenced through a SOSA/SSN predicate by another instance of a class of the
        same or higher priority (container_classes), so inverse links from lower-priority
        resources (e.g. a Sample's isResultOf its Sampling) do not hide the root."""
    inst = instances(g, classes)
    targets = instances(g, container_classes)
    nested = set()
    for s, p, o in g.triples((None, None, None)):
        if o not in inst or s == o or p == RDF.type:
            continue
        if isinstance(o, BNode) or not str(p).startswith(SOSA_SSN) or s in targets:
            nested.add(o)
    return sorted(inst - nested, key=str)


def lint(g: Graph, text: str) -> list[str]:
    warnings = []
    for ns in BAD_SOSA_NS:
        if ns in text:
            warnings.append(f'non-standard SOSA namespace <{ns}> (expected <{SOSA}>)')
    return warnings


def classify(g: Graph) -> tuple[str, list, Counter]:
    types = Counter(str(o) for o in g.objects(None, RDF.type) if str(o).startswith(SOSA_SSN))
    seen: list[URIRef] = []
    for group, (_, classes) in GROUPS.items():
        seen += classes
        r = roots(g, classes, seen)
        if r:
            return group, [str(x) for x in r], types
    return OTHER, [], types


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--repo', default='.')
    ap.add_argument('--spec-dir', help='local clone of sdw-sosa-ssn/ssn (faster; must be current)')
    ap.add_argument('--out', default='-', help='plan file (default stdout)')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    spec_dir = Path(args.spec_dir).resolve() if args.spec_dir else None
    source = (str(spec_dir) + '/') if spec_dir else RAW_BASE

    doc = doc_examples(source)
    existing = bblock_examples(repo)
    candidates: dict[str, dict] = {}
    for d in doc:
        candidates[d['url']] = {'url': d['url'], 'in_document': d['kind'], 'chapters': d['chapters']}
    for e in existing:
        candidates.setdefault(e['url'], {'url': e['url'], 'in_document': 'no', 'chapters': []})
    # only examples that are in the doc (included/linked) or already in the bblocks
    candidates = {u: c for u, c in candidates.items()
                  if c['in_document'] in ('included', 'linked') or any(e['url'] == u for e in existing)}

    plan = {'groups': {g: {'target': t, 'rootClasses': [str(c) for c in cs]} for g, (t, cs) in GROUPS.items()},
            'examples': []}
    plan['groups'][OTHER] = {'target': None, 'rootClasses': []}
    for url, c in candidates.items():
        entry = dict(c)
        try:
            g, text = load(url, spec_dir)
            group, rts, types = classify(g)
            entry.update(group=group, roots=rts,
                         types={k.rsplit('/', 1)[-1]: v for k, v in sorted(types.items())})
            if warnings := lint(g, text):
                entry['warnings'] = warnings
        except Exception as exc:  # unparseable examples are still tested as-is
            entry.update(group=OTHER, roots=[], error=f'{type(exc).__name__}: {exc}')
        if url.endswith('.jsonld'):
            entry['group'] = OTHER  # JSON-LD originals are kept alongside the TTL, not re-converted
        plan['examples'].append(entry)
        print(f"{entry['group']:24} {len(entry.get('roots', [])):3} roots  {url.rsplit('/', 1)[-1]}"
              + (f"  ERROR {entry['error']}" if 'error' in entry else '')
              + ''.join(f"  WARNING {w}" for w in entry.get('warnings', [])), file=sys.stderr)

    text = yaml.safe_dump(plan, sort_keys=False, allow_unicode=True, width=120)
    if args.out == '-':
        print(text)
    else:
        Path(args.out).write_text(text, encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
