"""Resolved-evidence checks for new v3 releases, without rewriting history."""
from __future__ import annotations

import re
from pathlib import Path

from .common import digest, parse_markdown, read_json, safe_path, sections
from .evidence import resolve_library


def resolved_release(root: Path, proposal: Path, overlay: Path, manifest: dict) -> dict:
    lock = read_json(proposal / 'evidence-lock.json', {})
    if lock.get('schema_version') != 2:
        raise ValueError('v3 requires an evidence-lock schema_version 2')
    refs = lock.get('evidence_refs', [])
    if not isinstance(refs, list) or len(refs) != len(set(refs)):
        raise ValueError('Evidence references must be unique')
    receipt_paths = []
    for item in lock.get('library_receipts', []):
        path = safe_path(root, item['path'], area='state/workshop/evidence-library')
        if not path.is_file() or digest(path.read_bytes()) != item['sha256']:
            raise ValueError('Locked evidence library receipt changed')
        receipt_paths.append(path)
    library = resolve_library(root, receipt_paths=receipt_paths)
    if any(f['severity'] in {'ERROR', 'CRITICAL'} for f in library['findings']):
        raise ValueError('Evidence library contains invalid or ambiguous records')
    records = {r['evidence_ref']: r for r in library['records']}
    if any(r not in records or records[r]['evidence_status'] != 'REVIEWED' for r in refs):
        raise ValueError('Every locked evidence reference must currently resolve as REVIEWED')
    reasons, used = set(), set()
    for path in sorted(overlay.rglob('*.md')):
        safe_path(overlay, path.relative_to(overlay).as_posix())
        meta, body = parse_markdown(path.read_text(encoding='utf-8'))
        if meta['type'] == 'index':
            continue
        if not refs:
            raise ValueError('Knowledge/question release cannot use an empty evidence lock')
        note_hash = digest(path.read_bytes())
        for section in sections(meta['id'], body):
            # Citation lists carry locators, not independent prose. Navigation
            # is exempt only when every nonempty line is a bare wikilink.
            navigation = all(re.fullmatch(r'\s*[-*]?\s*\[\[[^\]]+\]\]\s*', line)
                             for line in section['text'].splitlines() if line.strip())
            if section['heading'].casefold() == 'source references' or navigation:
                continue
            matches = [b for b in library['bindings'] if b['note_id'] == meta['id']
                       and b['note_sha256'] == note_hash and b['section_id'] == section['section_id']
                       and b['section_sha256'] == section['sha256'] and b['evidence_status'] == 'REVIEWED']
            if len(matches) != 1 or not set(matches[0]['evidence_refs']) <= set(refs):
                raise ValueError('Each substantive proposed section needs one exact reviewed evidence binding')
            binding = matches[0]
            used.update(binding['evidence_refs'])
            if binding['modality'] in {'obligation', 'prohibition'}:
                reasons.add('binding_claim')
            if re.search(r'\b(must|shall|required|prohibited|obligation|interdit|obligatoire|doit)\b', section['text'], re.I):
                reasons.add('normative_wording_requires_strict_review')
            if any(records[ref]['authority'] == 'BINDING' for ref in binding['evidence_refs']):
                reasons.add('binding_evidence')
    reviewers = sorted({r['reviewer_identity'] for r in library['records'] if r['evidence_ref'] in used})
    if manifest['author_identity'] in reviewers:
        raise ValueError('Release author cannot be its evidence reviewer')
    return {'strict_reasons': sorted(reasons), 'library_reviewers': reviewers,
            'resolved_evidence_refs': sorted(refs), 'author_identity': manifest['author_identity']}
