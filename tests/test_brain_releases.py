import json
from pathlib import Path

import pytest

from gov360_brain.brain.common import digest
from gov360_brain.workshop import init_release, integrate, metadata, render
from test_brain_evidence import make_receipt, put


def proposal(root, *, index=False, schema_version=3):
    created = init_release(root, ['GENERAL'], 'GENERAL', 'synthetic-release',
                          author_identity='release-author', schema_version=schema_version)
    p = root / created['path']
    manifest = json.loads((p / 'manifest.json').read_text())
    if index:
        note_path = 'indexes/synthetic-index.md'
        note = put(p, 'future-vault/' + note_path, render(metadata('synthetic-index', 'Synthetic index', kind='index', status='active'), '# Navigation\n'))
        identity = 'synthetic-index'
    else:
        receipt, data, original = make_receipt(root)
        note_path = 'controls/synthetic-control.md'
        note = put(p, 'future-vault/' + note_path, original.read_text())
        identity = 'synthetic-control'
        # Existing identical note is an UPDATE rather than overwriting an ADD.
        put(p, 'evidence-lock.json', {'schema_version': 2, 'evidence_refs': ['synthetic-evidence'],
            'library_receipts': [{'path': receipt.relative_to(root).as_posix(), 'sha256': digest(receipt.read_bytes())}]})
    manifest.update(status='HUMAN_REVIEW', files=[note_path], changes={'ADD': [identity] if index else [], 'UPDATE': [] if index else [identity], 'SUPERSEDE': [], 'NOOP': []})
    put(p, 'manifest.json', manifest)
    return p, manifest


def approve(root, p, manifest, *, reviewer='independent-reviewer'):
    preview = integrate(root, ['GENERAL'], [p])
    candidate = preview['candidate_sha256']
    put(p, 'review/release-review.json', {'schema_version': 1, 'verdict': 'READY_FOR_HUMAN_APPROVAL',
        'candidate_sha256': candidate, 'reviewer_identity': reviewer, 'reviewed_at': '2026-09-16T00:00:00Z', 'findings': []})
    put(p, 'review/approval.md', f'''# Approval
Status: APPROVED
- Approver identity: Test operator
- Decision: APPROVED
- Scope: synthetic-release
- Rationale: Synthetic test approval
- Decision date: 2026-09-16
- Candidate SHA-256: {candidate}
''')
    manifest['status'] = 'APPROVED'; put(p, 'manifest.json', manifest)
    return candidate


def test_v3_independent_review_exact_approval_and_noop(tmp_path):
    (tmp_path / 'brain wiki').mkdir()
    p, manifest = proposal(tmp_path, index=True)
    with pytest.raises(ValueError, match='independent review'): integrate(tmp_path, ['GENERAL'], [p], apply=True)
    approve(tmp_path, p, manifest, reviewer='release-author')
    assert not integrate(tmp_path, ['GENERAL'], [p])['reviewed']
    approve(tmp_path, p, manifest)
    assert integrate(tmp_path, ['GENERAL'], [p], apply=True)['written'] == 1
    assert integrate(tmp_path, ['GENERAL'], [p], apply=True)['written'] == 0
    approval = p / 'review/approval.md'; approval.write_text(approval.read_text().replace('Candidate SHA-256:', 'Other hash:'))
    with pytest.raises(ValueError, match='must be APPROVED'): integrate(tmp_path, ['GENERAL'], [p], apply=True)


def test_v3_refuses_empty_unresolved_or_changed_evidence(tmp_path):
    p, manifest = proposal(tmp_path)
    assert integrate(tmp_path, ['GENERAL'], [p])['valid']
    library = tmp_path / 'state/workshop/evidence-library/synthetic-receipt.json'
    library.write_text(library.read_text() + '\n')
    with pytest.raises(ValueError, match='receipt changed'): integrate(tmp_path, ['GENERAL'], [p])
    put(p, 'evidence-lock.json', {'schema_version': 2, 'evidence_refs': [], 'library_receipts': []})
    with pytest.raises(ValueError, match='empty evidence'): integrate(tmp_path, ['GENERAL'], [p])


def test_v3_promotes_declared_fast_strict_and_binds_author(tmp_path):
    (tmp_path / 'brain wiki').mkdir()
    p, manifest = proposal(tmp_path, index=True)
    manifest['contract_changes'] = True; put(p, 'manifest.json', manifest)
    preview = integrate(tmp_path, ['GENERAL'], [p])
    assert preview['risk_tiers'] == ['strict']
    manifest['author_identity'] = 'different-author'; put(p, 'manifest.json', manifest)
    assert integrate(tmp_path, ['GENERAL'], [p])['candidate_sha256'] != preview['candidate_sha256']


def test_v3_rolls_back_note_when_derived_build_fails(tmp_path, monkeypatch):
    (tmp_path / 'brain wiki').mkdir()
    p, manifest = proposal(tmp_path, index=True); approve(tmp_path, p, manifest)
    def fail(root): raise OSError('synthetic derived failure')
    monkeypatch.setattr('gov360_brain.derived.build_derived', fail)
    with pytest.raises(OSError): integrate(tmp_path, ['GENERAL'], [p], apply=True)
    assert not (tmp_path / 'brain wiki/indexes/synthetic-index.md').exists()


def test_v2_preview_preserved_but_new_publication_blocked(tmp_path):
    (tmp_path / 'brain wiki').mkdir()
    p, manifest = proposal(tmp_path, index=True, schema_version=2)
    manifest['schema_version'] = 2; put(p, 'manifest.json', manifest)
    assert integrate(tmp_path, ['GENERAL'], [p])['valid']
    # Historical v2 releases remain readable; new CLI-created candidates use
    # v3. Applying an unreviewed historical candidate still requires its
    # existing independent review gate.
    with pytest.raises(ValueError, match='independent review'):
        integrate(tmp_path, ['GENERAL'], [p], apply=True)
