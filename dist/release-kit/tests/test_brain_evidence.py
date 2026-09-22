"""Evidence boundaries tested exclusively with invented fixture content."""
import json
from copy import deepcopy
from pathlib import Path

import pytest

from gov360_brain.brain.common import digest, parse_markdown, sections
from gov360_brain.brain.evidence import receipt_hash, resolve_library
from gov360_brain.utils import frontmatter


def put(root, name, value):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value), encoding='utf-8')
    return path


def make_receipt(root, *, authority='GUIDANCE'):
    body = 'An invented test procedure records a synthetic check.\n'
    unit_hash = digest(body)
    source_hash = digest('synthetic source bytes')
    meta = {'type': 'ingested_unit', 'schema_version': 1, 'source_id': 'SRC-9001',
            'source_sha256': source_hash, 'source_format': 'txt', 'adapter_id': 'text',
            'adapter_version': '1', 'locator_kind': 'section', 'locator': 'Section 1',
            'content_sha256': unit_hash, 'extraction_mode': 'native',
            'visual_review': 'NONE', 'warnings': []}
    unit = put(root, 'ingest/SRC-9001/units/one.md', frontmatter(meta) + body)
    content_hash = digest(unit.read_bytes())
    source = {'source_id': 'SRC-9001', 'source_sha256': source_hash, 'status': 'READY_FOR_LLM',
              'relative_paths': ['sources/synthetic.txt'], 'domains': ['GENERAL'], 'normativity': authority}
    put(root, 'state/source_manifest.jsonl', json.dumps(source) + '\n')
    put(root, 'state/source_classification_events.jsonl', json.dumps({'source_id': 'SRC-9001', 'source_sha256': source_hash, 'normativity': authority}) + '\n')
    put(root, 'ingest/SRC-9001/document.json', {'source_id': 'SRC-9001', 'source_sha256': source_hash,
        'validation': {'valid': True}, 'units': [{'filename': 'units/one.md', 'locator': 'Section 1',
        'file_sha256': content_hash, 'content_sha256': unit_hash}]})
    fidelity = put(root, 'state/workshop/synthetic-fidelity.json', {'results': [{'source_id': 'SRC-9001',
        'source_sha256': source_hash, 'locator': 'Section 1', 'unit_file_sha256': content_hash,
        'unit_content_sha256': unit_hash, 'result': 'MATCH'}]})
    note_meta = {'id': 'synthetic-control', 'title': 'Synthetic control', 'type': 'knowledge',
        'domains': ['GENERAL'], 'status': 'active', 'aliases': [], 'tags': [], 'evidence_sources': []}
    note = put(root, 'brain wiki/controls/synthetic-control.md', frontmatter(note_meta) + '# Synthetic control\n\n## Summary\n\nRecord an invented check.\n')
    _, note_body = parse_markdown(note.read_text())
    sec = sections(note_meta['id'], note_body)[0]
    e = {'evidence_ref': 'synthetic-evidence', 'source_id': 'SRC-9001', 'source_sha256': source_hash,
        'unit_path': 'ingest/SRC-9001/units/one.md', 'unit_sha256': unit_hash,
        'unit_file_sha256': content_hash, 'locator': 'Section 1', 'authority': authority,
        'jurisdiction': [], 'valid_from': None, 'valid_until': None,
        'fidelity_inputs': [{'path': 'state/workshop/synthetic-fidelity.json', 'sha256': digest(fidelity.read_bytes())}]}
    data = {'schema_version': 1, 'receipt_id': 'synthetic-receipt', 'author_identity': 'synthetic-author',
        'evidence': [e], 'bindings': [{'note_id': note_meta['id'], 'note_sha256': digest(note.read_bytes()),
        'section_id': sec['section_id'], 'section_sha256': sec['sha256'], 'evidence_refs': ['synthetic-evidence'], 'modality': 'recommendation'}]}
    data['review'] = {'reviewer_identity': 'independent-test-reviewer', 'reviewed_at': '2026-09-15T10:00:00Z',
                     'candidate_sha256': receipt_hash(data), 'verdict': 'EVIDENCE_READY', 'findings': []}
    receipt = put(root, 'state/workshop/evidence-library/synthetic-receipt.json', data)
    put(root, 'config/brain-domains.json', ['GENERAL'])
    return receipt, data, note


def test_independent_current_receipt_resolves_and_changes_invalidate(tmp_path):
    path, data, _ = make_receipt(tmp_path)
    result = resolve_library(tmp_path)
    assert result['records'][0]['evidence_status'] == 'REVIEWED'
    path.write_text(json.dumps({**data, 'author_identity': 'changed-author'}))
    assert resolve_library(tmp_path)['records'][0]['evidence_status'] == 'UNRESOLVED'


@pytest.mark.parametrize('mutation', ['self_review', 'unit', 'source', 'fidelity', 'binding', 'blocking_finding'])
def test_invalid_provenance_does_not_grant_review(tmp_path, mutation):
    path, data, _ = make_receipt(tmp_path)
    if mutation == 'self_review': data['review']['reviewer_identity'] = data['author_identity']
    elif mutation == 'unit': (tmp_path / data['evidence'][0]['unit_path']).write_text('tampered')
    elif mutation == 'source': put(tmp_path, 'state/source_manifest.jsonl', json.dumps({'source_id': 'SRC-9001', 'status': 'SUPERSEDED'}) + '\n')
    elif mutation == 'fidelity': put(tmp_path, 'state/workshop/synthetic-fidelity.json', {'results': []})
    elif mutation == 'binding': data['bindings'][0]['evidence_refs'] = ['unknown-ref']
    else: data['review']['findings'] = [{'severity': 'ERROR', 'code': 'SYNTHETIC_BLOCKER'}]
    path.write_text(json.dumps(data))
    result = resolve_library(tmp_path)
    assert not result['bindings'] or result['bindings'][0]['evidence_status'] == 'UNRESOLVED'


def test_binding_requires_classification_event(tmp_path):
    path, data, _ = make_receipt(tmp_path, authority='BINDING')
    put(tmp_path, 'state/source_classification_events.jsonl', '')
    assert resolve_library(tmp_path)['records'][0]['evidence_status'] == 'UNRESOLVED'


def test_fidelity_scope_must_cover_unit_not_just_an_arbitrary_hash(tmp_path):
    path, data, _ = make_receipt(tmp_path)
    f = put(tmp_path, 'state/workshop/synthetic-fidelity.json', {'results': []})
    data['evidence'][0]['fidelity_inputs'][0]['sha256'] = digest(f.read_bytes())
    data['review']['candidate_sha256'] = receipt_hash(data)
    path.write_text(json.dumps(data))
    result = resolve_library(tmp_path)
    assert result['records'][0]['evidence_status'] == 'UNRESOLVED'
    assert any(f['code'] == 'FIDELITY_SCOPE_UNRESOLVED' for f in result['findings'])


def test_path_escape_is_rejected_without_disclosing_content(tmp_path):
    path, data, _ = make_receipt(tmp_path)
    data['evidence'][0]['unit_path'] = 'ingest/SRC-9001/units/../../outside.md'
    data['review']['candidate_sha256'] = receipt_hash(data)
    path.write_text(json.dumps(data))
    result = resolve_library(tmp_path)
    assert result['records'] == []
    assert result['findings'][0]['code'] == 'INVALID_EVIDENCE_RECEIPT'
