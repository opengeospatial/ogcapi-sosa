#!/usr/bin/env python3
"""
Check that the spec-examples building blocks are up to date with the examples
included in the SOSA/SSN specification document.

The "document" is the respec source of https://w3c.github.io/sdw-sosa-ssn/ssn/ :
index.html includes chapters via data-include; each chapter includes example
files via <pre class="example ..." data-include="./rdf/...">. Plain links to
example files (<a href="...rdf/examples/x.ttl">) are reported as "linked".

Compared against every examples.yaml under _sources/spec-examples/ (the parent
block plus any grouped child blocks).

Usage:
  python check_spec_examples.py [--repo .] [--spec-dir PATH | --spec-url URL]
                                [--no-network] [--json] [--strict] [--build-dir build]

Exit code: 0 = in sync, 1 = differences found, 2 = error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import yaml

PUBLISHED_BASE = 'https://w3c.github.io/sdw-sosa-ssn/ssn/'
RAW_BASE = 'https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/gh-pages/ssn/'

COMMENT_RE = re.compile(r'<!--.*?-->', re.S)
INCLUDE_RE = re.compile(r'data-include="([^"]+)"')
EXAMPLE_PRE_RE = re.compile(r'<pre\b[^>]*\bclass="[^"]*\bexample\b[^"]*"[^>]*>', re.S)
LINK_RE = re.compile(r'href="([^"]*rdf/examples/[^"#?]+\.(?:ttl|jsonld|json))"')
FOLDER_RE = re.compile(r'href="([^"]*rdf/examples/?)"')
GH_CONTENTS = 'https://api.github.com/repos/w3c/sdw-sosa-ssn/contents/ssn/rdf/examples?ref=gh-pages'
EXAMPLE_EXT = ('.ttl', '.jsonld', '.json')


def _read(source: str, rel: str) -> str:
    if source.startswith(('http://', 'https://')):
        with urlopen(urljoin(source, rel), timeout=30) as r:
            return r.read().decode('utf-8')
    return (Path(source) / rel).read_text(encoding='utf-8')


def _normalise(href: str) -> str | None:
    """Map a chapter-relative or GitHub href to the published spec URL."""
    href = href.strip()
    m = re.search(r'github\.com/w3c/sdw-sosa-ssn/(?:blob|tree)/gh-pages/ssn/(.+)$', href)
    if m:
        return PUBLISHED_BASE + m.group(1)
    if href.startswith(PUBLISHED_BASE):
        return href
    if href.startswith(('http://', 'https://')):
        return None
    return urljoin(PUBLISHED_BASE, href)


def folder_examples(source: str) -> list[str]:
    """Top-level example files in ssn/rdf/examples (the folder the document links to)."""
    if source.startswith(('http://', 'https://')):
        with urlopen(Request(GH_CONTENTS, headers={'Accept': 'application/vnd.github+json'}), timeout=30) as r:
            names = [i['name'] for i in json.load(r) if i['type'] == 'file']
    else:
        names = [f.name for f in (Path(source) / 'rdf' / 'examples').iterdir() if f.is_file()]
    return [PUBLISHED_BASE + 'rdf/examples/' + n for n in sorted(names) if n.endswith(EXAMPLE_EXT)]


def doc_examples(source: str) -> list[dict]:
    """Return examples referenced by the spec document, in document order.

    kind: 'included' (rendered in the document), 'linked' (explicit link to the file),
    'folder' (only reachable via a document link to the examples folder)."""
    index = COMMENT_RE.sub('', _read(source, 'index.html'))
    chapters = [c for c in INCLUDE_RE.findall(index) if c.endswith('.html')]
    found: dict[str, dict] = {}
    folder_linked_from = []
    for chapter in chapters:
        html = COMMENT_RE.sub('', _read(source, chapter.lstrip('./')))
        chapter_name = Path(chapter).stem
        for tag in EXAMPLE_PRE_RE.findall(html):
            inc = INCLUDE_RE.search(tag)
            if not inc or not inc.group(1).endswith(EXAMPLE_EXT):
                continue
            url = _normalise(inc.group(1))
            entry = found.setdefault(url, {'url': url, 'kind': 'included', 'chapters': []})
            entry['kind'] = 'included'
            if chapter_name not in entry['chapters']:
                entry['chapters'].append(chapter_name)
        for href in LINK_RE.findall(html):
            url = _normalise(href)
            if not url:
                continue
            entry = found.setdefault(url, {'url': url, 'kind': 'linked', 'chapters': []})
            if chapter_name not in entry['chapters']:
                entry['chapters'].append(chapter_name)
        if FOLDER_RE.search(html):
            folder_linked_from.append(chapter_name)
    if folder_linked_from:
        for url in folder_examples(source):
            found.setdefault(url, {'url': url, 'kind': 'folder', 'chapters': folder_linked_from})
    return list(found.values())


def bblock_examples(repo: Path) -> list[dict]:
    """Return every snippet ref in _sources/spec-examples/**/examples.yaml."""
    root = repo / '_sources' / 'spec-examples'
    result = []
    for ex_file in sorted(root.rglob('examples.yaml')):
        block_dir = ex_file.parent
        block = '.'.join(('spec-examples', *block_dir.relative_to(root).parts))
        data = yaml.safe_load(ex_file.read_text(encoding='utf-8')) or {}
        for example in data.get('examples') or []:
            for snippet in example.get('snippets') or []:
                ref = snippet.get('ref')
                if not ref:
                    continue
                url = ref if ref.startswith(('http://', 'https://')) else None
                result.append({
                    'url': url or ref,
                    'block': block,
                    'block_dir': str(block_dir.relative_to(repo)).replace('\\', '/'),
                    'title': example.get('title'),
                    'base_output_filename': example.get('base-output-filename'),
                    'language': snippet.get('language'),
                })
    return result


def url_ok(url: str) -> bool:
    try:
        with urlopen(Request(url, method='HEAD'), timeout=20) as r:
            return r.status < 400
    except Exception:
        return False


def build_status(build_dir: Path, entry: dict) -> str:
    """Look for the validation report of a bblock example in build/tests."""
    base = entry.get('base_output_filename')
    if not base:
        return 'unknown (no base-output-filename)'
    tests_dir = build_dir / 'tests' / 'sosa' / Path(*entry['block'].split('.'))
    if (tests_dir / f'{base}.validation_failed.txt').exists():
        return 'failed'
    if (tests_dir / f'{base}.validation_passed.txt').exists():
        return 'passed'
    return 'not built'


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--repo', default='.', help='ogcapi-sosa repository root')
    src = ap.add_mutually_exclusive_group()
    src.add_argument('--spec-dir', help='local clone of sdw-sosa-ssn/ssn (must be up to date with gh-pages)')
    src.add_argument('--spec-url', default=RAW_BASE, help=f'spec source base URL (default {RAW_BASE})')
    ap.add_argument('--strict', action='store_true',
                    help="flag bblock examples that are only in the linked examples folder as extra")
    ap.add_argument('--no-network', action='store_true', help='skip HEAD checks of bblock refs')
    ap.add_argument('--build-dir', default='build', help='build output to read test results from (e.g. build-local)')
    ap.add_argument('--json', action='store_true', help='machine-readable output')
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    source = args.spec_dir if args.spec_dir else args.spec_url
    if args.spec_dir and not source.endswith(('/', '\\')):
        source += '/'

    doc = doc_examples(source)
    required = {d['url']: d for d in doc if d['kind'] in ('included', 'linked')}
    folder = {d['url']: d for d in doc if d['kind'] == 'folder'}
    bb = bblock_examples(repo)
    bb_by_url: dict[str, list[dict]] = {}
    for e in bb:
        bb_by_url.setdefault(e['url'], []).append(e)

    missing = [required[u] for u in required if u not in bb_by_url]
    extra = [dict(url=u, blocks=[e['block'] for e in es], in_folder=u in folder)
             for u, es in bb_by_url.items() if u not in required]
    available = [folder[u] for u in folder if u not in bb_by_url]
    duplicates = [dict(url=u, blocks=[e['block'] for e in es])
                  for u, es in bb_by_url.items() if len({e['block'] for e in es}) > 1]
    broken = [] if args.no_network else [u for u in bb_by_url if u.startswith('http') and not url_ok(u)]
    builds = {u: [dict(block=e['block'], status=build_status(repo / args.build_dir, e)) for e in es]
              for u, es in bb_by_url.items()}
    not_passing = {u: s for u, s in builds.items() if any(x['status'] != 'passed' for x in s)}

    report = dict(source=source, doc_examples=len(doc), required=len(required),
                  bblock_refs=len(bb), missing=missing, extra=extra,
                  folder_not_in_bblocks=available, duplicates=duplicates,
                  broken_refs=broken, build_not_passing=not_passing)
    in_sync = not (missing or [e for e in extra if args.strict or not e['in_folder']] or duplicates or broken)

    if args.json:
        print(json.dumps(dict(report, in_sync=in_sync), indent=2))
    else:
        print(f"Spec source: {source}")
        print(f"Examples in document: {len(required)} included/linked, "
              f"{len(folder)} more in the linked examples folder; bblock snippet refs: {len(bb)}")
        print(f"\nMISSING from bblocks ({len(missing)}):")
        for m in missing:
            print(f"  + {m['url']}   [{', '.join(m['chapters'])}]")
        print(f"\nIN bblocks but NOT included in document ({len(extra)}):")
        for e in extra:
            print(f"  - {e['url']}   ({', '.join(e['blocks'])})"
                  f"{'  [in examples folder]' if e['in_folder'] else '  [STALE: not in spec]'}")
        if available:
            print(f"\nIn examples folder, not in bblocks ({len(available)}) [informational]:")
            for a in available:
                print(f"  ~ {a['url']}")
        if duplicates:
            print(f"\nDUPLICATED across blocks ({len(duplicates)}):")
            for d in duplicates:
                print(f"  * {d['url']}   ({', '.join(d['blocks'])})")
        if not args.no_network:
            print(f"\nBROKEN refs ({len(broken)}):")
            for u in broken:
                print(f"  ! {u}")
        print(f"\nBuild status not 'passed' ({len(not_passing)}):")
        for u, s in not_passing.items():
            print(f"  ? {u.rsplit('/', 1)[-1]}: " + ', '.join(f"{x['block']}={x['status']}" for x in s))
        print('\nRESULT: ' + ('in sync' if in_sync else 'OUT OF DATE'))
    return 0 if in_sync else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:  # noqa
        print(f'ERROR: {type(exc).__name__}: {exc}', file=sys.stderr)
        sys.exit(2)
