"""Exercise the watch loop on synthetic approved-question file additions."""
import json
import pytest

from gov360_brain import derived
from gov360_brain.workshop import metadata, render


def test_watcher_addition_rebuilds_canvas_and_then_noops(tmp_path, monkeypatch, capsys):
    directory = tmp_path / 'brain wiki/questions/core'
    directory.mkdir(parents=True)

    def add(number):
        identity = f'core-{number:03}'
        meta = metadata(identity, f'Synthetic {number}', kind='question', status='active')
        meta.update(topic=f'synthetic-{number}', priority='high', applies_to='AI',
                    answer_type='boolean', depends_on=None,
                    question_fr=f'Vérification synthétique {number} ?',
                    question_en=f'Synthetic check {number}?')
        (directory / f'{identity}.md').write_text(render(meta, '# Synthetic'))

    add(1)
    sleeps = 0
    def tick(_):
        nonlocal sleeps
        sleeps += 1
        if sleeps == 1:
            add(2)
        elif sleeps == 3:
            raise KeyboardInterrupt
    monkeypatch.setattr(derived.time, 'sleep', tick)
    with pytest.raises(KeyboardInterrupt):
        derived.watch_derived(tmp_path, interval=0.1)
    events = [json.loads(line) for line in capsys.readouterr().out.splitlines()]
    assert len(events) == 2  # initial build and one addition; idle tick writes nothing
    assert [e['questions'] for e in events] == [1, 2]
    assert all(e['written'] == 2 for e in events)
    canvas = json.loads((tmp_path / derived.CANVAS_PATH).read_text())
    assert {n['file'] for n in canvas['nodes'] if n['type'] == 'file'} == {
        'questions/core/core-001.md', 'questions/core/core-002.md'}
    assert derived.build_derived(tmp_path)['written'] == 0
