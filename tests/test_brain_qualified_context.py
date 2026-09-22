"""Behavioral extension tests; the 45-case reference benchmark stays unchanged."""
from copy import deepcopy
import json
from pathlib import Path

import jsonschema
import pytest

from gov360_brain.brain.retrieval import build_context
from test_brain_retrieval import context, section
from test_brain_evidence import make_receipt
from gov360_brain.brain.evidence import receipt_hash
from gov360_brain.brain.common import digest
from gov360_brain.brain import catalogue as cat


def test_qualified_binding_survives_end_to_end(tmp_path, monkeypatch):
    path, data, note = make_receipt(tmp_path)
    data['schema_version'] = 2
    data['bindings'][0].update(applicability=['Synthetic scope'], conflicts=['Synthetic conflict'],
                               limits=['Synthetic limitation'], access_restrictions=['Local only'])
    data['evidence'][0].update(document_date='2020-01-01', applicable_from='2020-02-01',
                               applicable_until='2099-01-01', review_expires_at='2099-01-01')
    data['review']['candidate_sha256'] = receipt_hash(data)
    path.write_text(json.dumps(data))
    monkeypatch.setattr(cat, 'publication_inventory', lambda root: ([], {
        'brain wiki/controls/synthetic-control.md': digest(note.read_bytes())}))
    result = build_context(tmp_path, 'synthetic', as_of='2026-09-22')
    retained = result['sections'][0]
    assert retained['modality'] == 'recommendation'
    assert retained['applicability'] == ['Synthetic scope']
    assert retained['conflicts'] == ['Synthetic conflict']
    assert retained['access_restrictions'] == ['Local only']
    assert retained['citations'][0]['reviewed_at'] == data['review']['reviewed_at']
    assert retained['citations'][0]['valid_from'] is None
    assert 'unknown_validity' in result['gaps']
    assert not build_context(tmp_path, 'synthetic', require_known_validity=True)['sections']
    schema = json.loads((Path(__file__).resolve().parents[1] / 'config/schemas/brain-context.schema.json').read_text())
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(result)


@pytest.mark.parametrize('field,value,reason', [
    ('valid_from', '2020-01-01invalid', 'invalid_validity'),
    ('applicable_from', '2099-01-01', 'applicability_scope'),
    ('applicable_until', '2000-01-01', 'applicability_scope'),
    ('review_expires_at', '2000-01-01', 'review_expired'),
    ('reviewed_at', '2020-01-01garbage', 'invalid_validity'),
    ('reviewed_at', '2020-01-01T00:00:00', 'invalid_validity'),
    ('superseded_by', 'other-evidence', 'superseded_evidence'),
    ('hash_status', 'CHANGED', 'hash_changed'),
])
def test_temporal_and_lineage_blockers_are_not_silently_dropped(tmp_path, field, value, reason):
    item = section()
    item['citations'][0][field] = value
    result = context(tmp_path, [item], as_of='2026-09-22')
    assert not result['sections']
    assert result['exclusions'][reason] == 1


def test_binding_modality_requires_binding_review_and_missing_modality_excluded(tmp_path):
    item = section(modality='obligation')
    assert not context(tmp_path, [item])['sections']
    item['citations'][0]['authority'] = 'BINDING'
    assert context(tmp_path, [item])['sections']
    item['citations'][0]['evidence_status'] = 'UNRESOLVED'
    assert not context(tmp_path, [item])['sections']
    assert not context(tmp_path, [section(modality=None)])['sections']


def test_unknown_gap_only_describes_returned_context(tmp_path):
    known = section()
    known['citations'][0].update(valid_from='2020-01-01', valid_until='2099-01-01',
                                 reviewed_at='2020-01-01T00:00:00Z', review_expires_at='2099-01-01')
    other = section('unrelated', text='Unrelated', title='Unrelated', aliases=[], heading_path=['Unrelated'])
    result = context(tmp_path, [known, other], as_of='2026-09-22')
    assert [s['note_id'] for s in result['sections']] == ['synthetic-note']
    assert 'unknown_validity' not in result['gaps']
    assert context(tmp_path, [known], require_known_validity=True)['sections']
