"""Synthetic normalized data: no real source text or originals needed."""
import json
from pathlib import Path

import pytest
import yaml

from gov360_brain.adapters.base import fenced_json_data
from gov360_brain.brain.common import digest
from gov360_brain.brain.ingest_reader import IngestReadError, source_document, structured_json, validated_unit
from gov360_brain.derived import atlas_catalog, build_atlas_catalog


def normalized_fixture(root, objects=None):
    if objects is None:
        objects = [{'id': 'attack-pattern--synthetic', 'type': 'attack-pattern',
                    'name': 'Synthetic', 'description': 'Path C:\\fixture <tool> &amp;',
                    'external_references': [{'source_name': 'mitre-atlas', 'external_id': 'AML.TEST'}]}]
    source = {'source_id': 'SRC-0046', 'source_sha256': 'a' * 64, 'status': 'READY_FOR_LLM'}
    body = '## JSON pointer `/objects`\n\n' + fenced_json_data(objects) + '\n'
    meta = dict(type='ingested_unit', schema_version=1, source_id=source['source_id'],
                source_sha256=source['source_sha256'], source_format='json', adapter_id='structured',
                adapter_version='1', locator_kind='json_path', locator='/objects',
                content_sha256=digest(body), extraction_mode='native', visual_review='NONE', warnings=[])
    path = root / 'ingest/SRC-0046/units/objects.md'
    path.parent.mkdir(parents=True)
    path.write_text('---\n' + yaml.safe_dump(meta) + '---\n' + body, encoding='utf-8')
    doc = {**source, 'validation': {'valid': True}, 'relative_source_paths': ['sources/missing.json'],
           'units': [{'filename': 'units/objects.md', 'locator': '/objects',
                      'file_sha256': digest(path.read_bytes()), 'content_sha256': digest(body)}]}
    (path.parent.parent / 'document.json').write_text(json.dumps(doc))
    (root / 'state').mkdir()
    (root / 'state/source_manifest.jsonl').write_text(json.dumps(source) + '\n')
    return path, source, doc, objects


def test_atlas_uses_validated_ingest_with_absent_original(tmp_path):
    path, source, doc, objects = normalized_fixture(tmp_path)
    source, doc = source_document(tmp_path, 'SRC-0046')
    decoded = structured_json(validated_unit(tmp_path, source, doc, 'units/objects.md'))
    assert decoded == objects
    rows, manifest = atlas_catalog(tmp_path)
    assert rows[0]['external_id'] == 'AML.TEST'
    assert rows[0]['description'] == objects[0]['description']
    assert manifest['unit_locator'] == '/objects'
    assert not (tmp_path / 'sources').exists()


@pytest.mark.parametrize('fault', ['tamper', 'document', 'quarantine', 'duplicate', 'symlink'])
def test_ingest_rejects_invalid_inputs(tmp_path, fault):
    path, source, doc, _ = normalized_fixture(tmp_path)
    if fault == 'tamper':
        path.write_text(path.read_text() + 'tampered')
    elif fault == 'document':
        doc['validation']['valid'] = False
        (path.parent.parent / 'document.json').write_text(json.dumps(doc))
    elif fault == 'quarantine':
        source['status'] = 'QUARANTINED'
        (tmp_path / 'state/source_manifest.jsonl').write_text(json.dumps(source) + '\n')
    elif fault == 'duplicate':
        (tmp_path / 'state/source_manifest.jsonl').write_text((json.dumps(source) + '\n') * 2)
    else:
        target = tmp_path / 'outside.md'
        path.rename(target)
        path.symlink_to(target)
    with pytest.raises(ValueError):
        atlas_catalog(tmp_path)


def test_body_hash_cannot_be_bypassed_by_updating_file_hash(tmp_path):
    path, source, doc, _ = normalized_fixture(tmp_path)
    path.write_text(path.read_text().replace('Synthetic', 'Changed'))
    doc['units'][0]['file_sha256'] = digest(path.read_bytes())
    (path.parent.parent / 'document.json').write_text(json.dumps(doc))
    with pytest.raises(IngestReadError, match='UNIT_CONTENT_OR_LINEAGE_CHANGED'):
        atlas_catalog(tmp_path)


def test_non_exhaustive_objects_refused(tmp_path):
    path, source, doc, _ = normalized_fixture(tmp_path)
    path.write_text(path.read_text().replace('schema_version: 1', 'non_exhaustive: true\nschema_version: 1'))
    doc['units'][0]['file_sha256'] = digest(path.read_bytes())
    (path.parent.parent / 'document.json').write_text(json.dumps(doc))
    with pytest.raises(ValueError, match='non-exhaustive'):
        atlas_catalog(tmp_path)


def test_atlas_preview_is_read_only_and_rebuild_is_noop(tmp_path):
    normalized_fixture(tmp_path)
    preview = build_atlas_catalog(tmp_path, write=False)
    assert preview['written'] == 0 and not preview['current']
    assert not (tmp_path / 'state/derived').exists()
    assert build_atlas_catalog(tmp_path)['written'] == 2
    assert build_atlas_catalog(tmp_path)['written'] == 0
    assert build_atlas_catalog(tmp_path, write=False)['current']
