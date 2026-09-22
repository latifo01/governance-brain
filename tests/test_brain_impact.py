from gov360_brain.brain.impact import impact


def test_impact_keeps_unresolved_dependencies_and_question_links(tmp_path):
    catalogue = {'catalogue_sha256': 'a' * 64,
        'evidence': {'records': [{'source_id': 'SRC-9001', 'evidence_ref': 'synthetic',
                                  'receipt_id': 'receipt', 'evidence_status': 'UNRESOLVED'}],
                     'bindings': [{'evidence_refs': ['synthetic'], 'note_id': 'question',
                                   'section_id': 'question:en'}]},
        'notes': [{'id': 'question', 'type': 'question', 'path': 'brain wiki/question.md'},
                  {'id': 'child', 'type': 'question', 'path': 'brain wiki/child.md',
                   'depends_on': {'question_id': 'question'}}]}
    result = impact(tmp_path, source_id='SRC-9001', catalogue=catalogue)
    assert result['section_ids'] == ['question:en']
    assert result['question_ids'] == ['question']
    assert result['direct_dependent_question_ids'] == ['child']
    assert result['unresolved_evidence_refs'] == ['synthetic']
    assert result['rebuild_required']
    missing = impact(tmp_path, source_id='SRC-9002', catalogue=catalogue)
    assert not missing['matched'] and not missing['rebuild_required']
