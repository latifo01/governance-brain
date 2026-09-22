import json
from pathlib import Path

import pytest

from gov360_brain.derived import CANVAS_PATH, REGISTRY_PATH, build_derived, canvas_document
from gov360_brain.workshop import init_release, integrate, inventory, metadata, render, validate

def test_inventory_preserves_cdo_and_routes_mitigations(tmp_path):
    cdo = tmp_path / 'cdo'; (cdo / 'mitigations').mkdir(parents=True)
    original = '# Control\n\nSee [[Other]].\n'
    (cdo / 'mitigations/Control.md').write_text(original)
    (cdo / 'Other.md').write_text('---\naliases: []\n---\n')
    result = inventory(tmp_path, cdo)
    assert result == {'notes': 2, 'drafts': 1, 'empty_backlog': 1}
    assert (cdo / 'mitigations/Control.md').read_text() == original
    target = tmp_path / 'state/workshop/drafts/AI Risk Mitigations/control.md'
    assert '[[other]]' in target.read_text()

def test_validator_rejects_broken_links_and_drafts(tmp_path):
    meta = metadata('a', 'A', status='active')
    (tmp_path / 'a.md').write_text(render(meta, '# A\n\n[[missing]]'))
    assert not validate(tmp_path, ['GENERAL'])['valid']
    (tmp_path / 'a.md').write_text(render(meta, '# A\n\nUseful navigation.'))
    assert validate(tmp_path, ['GENERAL'])['valid']
    meta['status'] = 'draft'
    (tmp_path / 'a.md').write_text(render(meta, '# A\n\nContent.'))
    assert not validate(tmp_path, ['GENERAL'])['valid']

def test_validator_applies_proposal_as_path_overlay(tmp_path):
    vault = tmp_path / 'brain wiki'
    overlay = tmp_path / 'proposal'
    (vault / 'questions').mkdir(parents=True)
    (overlay / 'questions').mkdir(parents=True)
    first = metadata('q-001', 'Question one', kind='question', status='active')
    first.update(topic='first-topic', priority='high', applies_to='AI',
                 answer_type='boolean', depends_on=None,
                 question_fr='Première question ?', question_en='First question?')
    second = metadata('q-002', 'Question two', kind='question', status='active')
    second.update(topic='second-topic', priority='medium', applies_to='AI',
                  answer_type='boolean',
                  depends_on={'question_id': 'q-001', 'equals': True},
                  question_fr='Deuxième question ?', question_en='Second question?')
    (vault / 'questions/q-001.md').write_text(render(first, '# Question one'))
    (overlay / 'questions/q-002.md').write_text(render(second, '# Question two'))
    assert validate(vault, ['GENERAL'], overlay)['valid']

    second['depends_on']['question_id'] = 'q-999'
    (overlay / 'questions/q-002.md').write_text(render(second, '# Question two'))
    assert not validate(vault, ['GENERAL'], overlay)['valid']

def test_validator_combines_proposal_overlays_and_rejects_path_conflicts(tmp_path):
    vault = tmp_path / 'brain wiki'
    first_overlay = tmp_path / 'proposal-one'
    second_overlay = tmp_path / 'proposal-two'
    (vault / 'knowledge').mkdir(parents=True)
    (first_overlay / 'indexes').mkdir(parents=True)
    (second_overlay / 'questions').mkdir(parents=True)

    knowledge = metadata('concept', 'Concept', status='active')
    index = metadata('combined-index', 'Combined index', kind='index', status='active')
    question = metadata('q-001', 'Question', kind='question', status='active')
    question.update(topic='combined-question', priority='high', applies_to='AI',
                    answer_type='boolean', depends_on=None,
                    question_fr='Question ?', question_en='Question?')

    (vault / 'knowledge/concept.md').write_text(render(knowledge, '# Concept'))
    (first_overlay / 'indexes/combined-index.md').write_text(
        render(index, '# Combined index\n\n[[concept]]\n[[q-001]]'))
    (second_overlay / 'questions/q-001.md').write_text(render(question, '# Question'))

    result = validate(vault, ['GENERAL'], [first_overlay, second_overlay])
    assert result['valid']
    assert result['notes'] == 3
    assert result['overlays'] == ['proposal-one', 'proposal-two']

    conflicting = second_overlay / 'indexes/combined-index.md'
    conflicting.parent.mkdir(parents=True)
    conflicting.write_text(render(index, '# Conflicting index'))
    result = validate(vault, ['GENERAL'], [first_overlay, second_overlay])
    assert not result['valid']
    assert any(error['error'] == 'conflicting proposal paths' for error in result['errors'])

def test_v3_integration_requires_human_gate_and_is_idempotent(tmp_path):
    """Two ordered index releases: ordering, review gate, approval gate, NOOP."""
    (tmp_path / 'brain wiki/knowledge').mkdir(parents=True)
    (tmp_path / 'brain wiki/knowledge/base.md').write_text(
        render(metadata('base', 'Base', status='active'), '# Base\n\nOriginal.'))

    first_created = init_release(tmp_path, ['GENERAL'], 'GENERAL', 'first-release',
                                 author_identity='release-author')
    second_created = init_release(tmp_path, ['GENERAL'], 'GENERAL', 'second-release',
                                  author_identity='release-author')
    first = tmp_path / first_created['path']
    second = tmp_path / second_created['path']
    (first / 'future-vault/indexes').mkdir()
    (second / 'future-vault/indexes').mkdir()
    (first / 'future-vault/indexes/first-index.md').write_text(
        render(metadata('first-index', 'First index', kind='index', status='active'),
               '# First index\n\n[[base]]'))
    (second / 'future-vault/indexes/second-index.md').write_text(
        render(metadata('second-index', 'Second index', kind='index', status='active'),
               '# Second index\n\n[[base]] and [[first-index]].'))
    for proposal, identity, path, requires in (
        (first, 'first-index', 'indexes/first-index.md', []),
        (second, 'second-index', 'indexes/second-index.md', ['first-release']),
    ):
        manifest_path = proposal / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        manifest.update(status='HUMAN_REVIEW', files=[path], requires_proposals=requires,
                       changes={'ADD': [identity], 'UPDATE': [], 'SUPERSEDE': [], 'NOOP': []})
        manifest_path.write_text(json.dumps(manifest))

    with pytest.raises(ValueError, match='Required proposal must appear earlier'):
        integrate(tmp_path, ['GENERAL'], [second])
    requested = [first, second]
    preview = integrate(tmp_path, ['GENERAL'], requested)
    assert preview['valid'] and not preview['reviewed'] and not preview['approved']
    assert preview['would_write'] == 2
    with pytest.raises(ValueError, match='independent review'):
        integrate(tmp_path, ['GENERAL'], requested, apply=True)

    candidate = preview['candidate_sha256']
    for proposal in (first, second):
        (proposal / 'review/release-review.json').write_text(json.dumps({
            'schema_version': 1,
            'verdict': 'READY_FOR_HUMAN_APPROVAL',
            'candidate_sha256': candidate,
            'reviewer_identity': 'independent-reviewer',
            'reviewed_at': '2026-09-16',
            'findings': [],
        }))
    with pytest.raises(ValueError, match='must be APPROVED'):
        integrate(tmp_path, ['GENERAL'], requested, apply=True)

    approval = f'''# Human approval

Status: APPROVED

- Approver identity: Test approver
- Decision: APPROVED
- Scope: Both ordered releases
- Rationale: Reviewed candidate
- Decision date: 2026-09-16
- Candidate SHA-256: {candidate}
'''
    for proposal in (first, second):
        manifest_path = proposal / 'manifest.json'
        manifest = json.loads(manifest_path.read_text())
        manifest['status'] = 'APPROVED'
        manifest_path.write_text(json.dumps(manifest))
        (proposal / 'review/approval.md').write_text(approval)

    applied = integrate(tmp_path, ['GENERAL'], requested, apply=True)
    assert applied['reviewed'] and applied['approved'] and applied['applied']
    assert applied['written'] == 2
    vault = tmp_path / 'brain wiki'
    assert (vault / 'indexes/first-index.md').is_file()
    assert (vault / 'indexes/second-index.md').is_file()
    report_path = first / 'review/integration-report.json'
    first_report = report_path.read_text()

    repeated = integrate(tmp_path, ['GENERAL'], requested, apply=True)
    assert repeated['applied'] and repeated['written'] == 0
    assert report_path.read_text() == first_report


def test_derived_registry_and_canvas_are_complete_and_deterministic(tmp_path):
    questions = tmp_path / 'brain wiki/questions/core'
    questions.mkdir(parents=True)
    first = metadata('core-001', 'First question', kind='question', status='active')
    first.update(topic='first-topic', priority='high', applies_to='AI',
                 answer_type='boolean', depends_on=None,
                 question_fr='Première question ?', question_en='First question?')
    second = metadata('core-002', 'Second question', kind='question', status='active')
    second.update(topic='second-topic', priority='medium', applies_to='AI',
                  answer_type='choice',
                  depends_on={'question_id': 'core-001', 'equals': 'yes'},
                  question_fr='Deuxième question ?', question_en='Second question?',
                  options=[
                      {'value': 'yes', 'label_fr': 'Oui', 'label_en': 'Yes'},
                      {'value': 'no', 'label_fr': 'Non', 'label_en': 'No'},
                  ])
    (questions / 'core-001.md').write_text(render(first, '# First question'))
    (questions / 'core-002.md').write_text(render(second, '# Second question'))

    first_build = build_derived(tmp_path)
    assert first_build['questions'] == 2
    assert first_build['dependencies'] == 1
    assert first_build['written'] == 2
    registry = [json.loads(line) for line in (tmp_path / REGISTRY_PATH).read_text().splitlines()]
    assert [row['question_id'] for row in registry] == ['core-001', 'core-002']
    canvas = json.loads((tmp_path / CANVAS_PATH).read_text())
    files = [node for node in canvas['nodes'] if node['type'] == 'file']
    assert {node['file'] for node in files} == {
        'questions/core/core-001.md', 'questions/core/core-002.md'
    }
    assert len(canvas['edges']) == 1
    assert canvas['edges'][0]['label'] == 'yes'

    registry_bytes = (tmp_path / REGISTRY_PATH).read_bytes()
    canvas_bytes = (tmp_path / CANVAS_PATH).read_bytes()
    repeated = build_derived(tmp_path)
    assert repeated['current'] and repeated['written'] == 0
    assert (tmp_path / REGISTRY_PATH).read_bytes() == registry_bytes
    assert (tmp_path / CANVAS_PATH).read_bytes() == canvas_bytes


def test_canvas_rejects_missing_dependency():
    records = [{
        'question_id': 'q-002', 'module': 'core', 'note_path': 'questions/core/q-002.md',
        'depends_on': {'question_id': 'q-999', 'equals': True},
    }]
    with pytest.raises(ValueError, match='Missing dependency'):
        canvas_document(records)


def test_canvas_rejects_dependency_cycle():
    records = [
        {'question_id': 'q-001', 'module': 'core', 'note_path': 'questions/core/q-001.md',
         'depends_on': {'question_id': 'q-002', 'equals': True}},
        {'question_id': 'q-002', 'module': 'core', 'note_path': 'questions/core/q-002.md',
         'depends_on': {'question_id': 'q-001', 'equals': True}},
    ]
    with pytest.raises(ValueError, match='Dependency cycle'):
        canvas_document(records)


def test_v2_fast_release_with_strict_trigger_is_rejected_at_validation(tmp_path):
    """Historical v2 manifests stay readable, but a declared fast tier with a
    strict-lane trigger is rejected during validation, before any review."""
    (tmp_path / 'brain wiki').mkdir()
    created = init_release(tmp_path, ['GENERAL'], 'GENERAL', 'general-release-002')
    proposal = tmp_path / created['path']
    manifest_path = proposal / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest['schema_version'] = 2
    manifest['contains_binding_claims'] = True
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match='strict-lane triggers'):
        integrate(tmp_path, ['GENERAL'], [proposal])
