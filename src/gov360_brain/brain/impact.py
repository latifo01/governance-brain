"""Metadata-only dependency impact for a source, evidence record or receipt."""
from pathlib import Path


def impact(root: Path, *, source_id=None, evidence_ref=None, receipt_id=None, catalogue=None):
    selectors = {k: v for k, v in {'source_id': source_id, 'evidence_ref': evidence_ref,
                                  'receipt_id': receipt_id}.items() if v is not None}
    if len(selectors) != 1:
        raise ValueError('ONE_IMPACT_SELECTOR_REQUIRED')
    if catalogue is None:
        from .catalogue import compile_brain
        catalogue = compile_brain(Path(root))
    key, value = next(iter(selectors.items()))
    records = [r for r in catalogue['evidence']['records'] if r.get(key) == value]
    refs = {r['evidence_ref'] for r in records}
    bindings = [b for b in catalogue['evidence']['bindings'] if refs.intersection(b['evidence_refs'])]
    note_ids = {b['note_id'] for b in bindings}
    notes = [n for n in catalogue['notes'] if n['id'] in note_ids]
    dependent_questions = [n['id'] for n in catalogue['notes'] if n['type'] == 'question'
                          and (n.get('depends_on') or {}).get('question_id') in note_ids]
    return {'schema_version': 1, 'catalogue_sha256': catalogue['catalogue_sha256'],
            'matched': bool(records), 'evidence_refs': sorted(refs),
            'unresolved_evidence_refs': sorted(r['evidence_ref'] for r in records if r['evidence_status'] != 'REVIEWED'),
            'section_ids': sorted({b['section_id'] for b in bindings}),
            'note_ids': sorted(note_ids),
            'question_ids': sorted(n['id'] for n in notes if n['type'] == 'question'),
            'direct_dependent_question_ids': sorted(dependent_questions),
            'affected_note_paths': sorted(n['path'] for n in notes),
            'rebuild_required': ['brain-catalogue', 'brain-context', 'coverage-matrix', 'okf-export'] if records else [],
            'policy': 'dependency-impact-is-not-approval; compilation-rechecks-inputs; no-persistent-retrieval-cache',
            'limits': ['Unresolved or absent historical bindings may leave additional dependencies unknown.',
                       'Dependent-question navigation does not transfer evidential authority.']}
