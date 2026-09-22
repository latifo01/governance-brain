import json

import pytest

from gov360_brain.brain import catalogue as mod
from gov360_brain.brain.common import sections, digest
from gov360_brain.brain.retrieval import build_context
from gov360_brain.workshop import init_release, integrate, render, metadata
from test_brain_evidence import make_receipt, put


def test_active_vault_loaded_without_promoting_active_to_reviewed(tmp_path):
    make_receipt(tmp_path)
    result = mod.compile_brain(tmp_path)
    assert len(result['notes']) == 1 and result['notes'][0]['type'] == 'knowledge'
    assert result['sections'][0]['evidence_status'] == 'UNRESOLVED'
    assert not build_context(tmp_path, 'synthetic')['sections']
    research = build_context(tmp_path, 'synthetic', mode='research')
    assert research['sections'] and 'research_contains_unreviewed_material' in research['gaps']


def test_current_publication_and_evidence_enable_only_bound_section(tmp_path, monkeypatch):
    _, _, note = make_receipt(tmp_path)
    monkeypatch.setattr(mod, 'publication_inventory', lambda root: ([], {'brain wiki/controls/synthetic-control.md': digest(note.read_bytes())}))
    result = mod.compile_brain(tmp_path)
    assert result['sections'][0]['evidence_status'] == 'REVIEWED'
    note.write_text(note.read_text() + '\nAdditional unreviewed statement.\n')
    assert mod.compile_brain(tmp_path)['sections'][0]['evidence_status'] == 'UNRESOLVED'


def test_section_headings_ignore_fences_and_distinguish_duplicates():
    result = sections('test', '# One\n\n## Repeated\n\nfirst\n```md\n# Code heading\n```\n## Repeated\n\nsecond\n')
    assert len(result) == 2
    assert len({r['section_id'] for r in result}) == 2
    assert all('Code heading' not in r['heading_path'] for r in result)


def test_build_deterministic_coverage_is_not_automatic_completion(tmp_path):
    make_receipt(tmp_path)
    put(tmp_path, 'state/workshop/coverage/coverage-register.json', {
        'definition_of_done': ['definition', 'accountability'],
        'pillars': [{'id': 'risk', 'domains': ['GENERAL'], 'status': 'EVIDENCE_READY'}]})
    first = mod.build(tmp_path)
    second = mod.build(tmp_path)
    assert first['written'] == 7 and second['written'] == 0 and second['current']
    matrix = json.loads((tmp_path / 'state/derived/brain/coverage-matrix.json').read_text())
    assert len(matrix['cells']) == 2
    assert all(c['status'] == 'UNASSESSED' for c in matrix['cells'])


def test_superseded_receipt_verifies_per_file_without_guessing(tmp_path):
    """A receipt whose files were later changed by other approved releases
    remains verifiable per file; superseded files are reported, not merged."""
    put(tmp_path, 'config/brain-domains.json', ['GENERAL'])
    (tmp_path / 'brain wiki/controls').mkdir(parents=True)
    kept = tmp_path / 'brain wiki/controls/kept-control.md'
    moved = tmp_path / 'brain wiki/controls/moved-control.md'
    kept.write_text(render(metadata('kept-control', 'Kept', status='active'), '# Kept\n\nOriginal.'))
    original = render(metadata('moved-control', 'Moved', status='active'), '# Moved\n\nOriginal.')
    moved.write_text(original)

    created = init_release(tmp_path, ['GENERAL'], 'GENERAL', 'superseded-release',
                           author_identity='release-author')
    proposal = tmp_path / created['path']
    (proposal / 'future-vault/controls').mkdir(parents=True)
    (proposal / 'future-vault/controls/kept-control.md').write_text(kept.read_text())
    (proposal / 'future-vault/controls/moved-control.md').write_text(original)
    manifest_path = proposal / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest.update(status='HUMAN_REVIEW',
                    files=['controls/kept-control.md', 'controls/moved-control.md'],
                    requires_proposals=[],
                    changes={'ADD': ['kept-control', 'moved-control'],
                             'UPDATE': [], 'SUPERSEDE': [], 'NOOP': []})
    manifest_path.write_text(json.dumps(manifest))

    preview = integrate(tmp_path, ['GENERAL'], [proposal])
    candidate = preview['candidate_sha256']
    (proposal / 'review/release-review.json').write_text(json.dumps({
        'schema_version': 1, 'verdict': 'READY_FOR_HUMAN_APPROVAL',
        'candidate_sha256': candidate, 'reviewer_identity': 'independent-reviewer',
        'reviewed_at': '2026-09-17', 'findings': []}))
    manifest['status'] = 'APPROVED'
    manifest_path.write_text(json.dumps(manifest))
    (proposal / 'review/approval.md').write_text(
        '# Human approval\n\nStatus: APPROVED\n\n'
        '- Approver identity: Test approver\n- Decision: APPROVED\n'
        '- Scope: superseded-release\n- Rationale: Reviewed candidate\n'
        f'- Decision date: 2026-09-17\n- Candidate SHA-256: {candidate}\n')
    assert integrate(tmp_path, ['GENERAL'], [proposal], apply=True)['applied']

    # A later approved release legitimately changed one published file.
    moved.write_text(original.replace('Original.', 'Updated by a later release.'))

    releases, published = mod.publication_inventory(tmp_path)
    assert releases[0]['proposal_id'] == 'superseded-release'
    assert releases[0]['publication_verified'] is True
    assert 'PUBLICATION_RECEIPT_HISTORICAL_ONLY' in releases[0]['findings']
    assert 'ACTIVE_NOTE_DIFFERS_FROM_RECEIPT' in releases[0]['findings']
    assert published == {'brain wiki/controls/kept-control.md': digest(kept.read_bytes())}

    # A receipt whose candidate no longer reproduces stays unresolved.
    (proposal / 'future-vault/controls/moved-control.md').write_text(
        original.replace('Original.', 'Tampered overlay.'))
    releases, published = mod.publication_inventory(tmp_path)
    assert releases[0]['publication_verified'] is False
    assert 'PUBLICATION_RECEIPT_UNRESOLVED' in releases[0]['findings']
    assert published == {}


def test_failed_build_restores_previous_generation(tmp_path, monkeypatch):
    _, _, note = make_receipt(tmp_path)
    mod.build(tmp_path)
    previous = (tmp_path / 'state/derived/brain/catalogue.json').read_bytes()
    note.write_text(note.read_text() + '\nSynthetic new paragraph.\n')
    real_replace = mod.os.replace
    def fail(source, target):
        if str(source).split('/')[-1].startswith('.brain-build-'):
            raise OSError('synthetic failure')
        return real_replace(source, target)
    monkeypatch.setattr(mod.os, 'replace', fail)
    with pytest.raises(OSError): mod.build(tmp_path)
    assert (tmp_path / 'state/derived/brain/catalogue.json').read_bytes() == previous
