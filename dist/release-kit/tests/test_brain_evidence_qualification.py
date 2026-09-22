"""Versioned qualification travels through reviewed evidence, never invented."""
import json

import pytest

from gov360_brain.brain.evidence import receipt_hash, resolve_library
from test_brain_evidence import make_receipt, put


@pytest.mark.parametrize('fields,code', [
    ({'review_expires_at': '2000-01-01'}, 'EVIDENCE_REVIEW_EXPIRED'),
    ({'revoked': True}, 'EVIDENCE_REVOKED_OR_SUPERSEDED'),
    ({'superseded_by': 'synthetic-successor'}, 'EVIDENCE_REVOKED_OR_SUPERSEDED'),
])
def test_v2_qualification_invalidates_bindings(tmp_path, fields, code):
    path, data, _ = make_receipt(tmp_path)
    data['schema_version'] = 2
    data['evidence'][0].update(fields)
    data['review']['candidate_sha256'] = receipt_hash(data)
    path.write_text(json.dumps(data))
    result = resolve_library(tmp_path)
    assert result['records'][0]['evidence_status'] == 'UNRESOLVED'
    assert result['bindings'][0]['evidence_status'] == 'UNRESOLVED'
    assert code in {f['code'] for f in result['findings']}


def test_qualification_requires_new_version_and_review(tmp_path):
    path, data, _ = make_receipt(tmp_path)
    data['evidence'][0]['document_date'] = '2025-01-01'
    path.write_text(json.dumps(data))
    assert not resolve_library(tmp_path)['records']
    data['schema_version'] = 2
    path.write_text(json.dumps(data))
    assert resolve_library(tmp_path)['records'][0]['evidence_status'] == 'UNRESOLVED'
    data['review']['candidate_sha256'] = receipt_hash(data)
    path.write_text(json.dumps(data))
    assert resolve_library(tmp_path)['records'][0]['evidence_status'] == 'REVIEWED'


def test_duplicate_source_identity_fails_closed(tmp_path):
    make_receipt(tmp_path)
    path = tmp_path / 'state/source_manifest.jsonl'
    path.write_text(path.read_text() * 2)
    assert resolve_library(tmp_path)['records'][0]['evidence_status'] == 'UNRESOLVED'
