"""Compile the active Markdown contract without trusting note status as evidence."""
from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
from collections import Counter
from pathlib import Path

import jsonschema

from .common import canonical, digest, parse_markdown, prose_without_code, read_json, read_jsonl, safe_path, sections
from .evidence import resolve_library


def read_notes(root: Path) -> list[dict]:
    notes = []
    for path in sorted((root / 'brain wiki').rglob('*.md')):
        if any(part.startswith('.') for part in path.relative_to(root / 'brain wiki').parts):
            continue
        safe_path(root, path.relative_to(root).as_posix(), area='brain wiki')
        text = path.read_text(encoding='utf-8')
        meta, body = parse_markdown(text)
        notes.append({**meta, 'metadata': meta, 'path': path.relative_to(root).as_posix(),
                      'body': body, 'sha256': digest(path.read_bytes())})
    return notes


def publication_inventory(root: Path) -> tuple[list[dict], dict[str, str]]:
    """Preserve historical formats, report missing links instead of guessing."""
    releases, published = [], {}
    for path in sorted((root / 'state/workshop/proposals').glob('*/manifest.json')):
        manifest = read_json(path, {})
        report = read_json(path.parent / 'review/integration-report.json', {})
        files = report.get('files', [])
        lock = read_json(path.parent / 'evidence-lock.json', {})
        facts = {'proposal_id': path.parent.name, 'status': manifest.get('status'),
                 'schema_version': manifest.get('schema_version', 1),
                 'candidate_sha256': report.get('candidate_sha256'),
                 'files': len(files), 'evidence_refs': len(lock.get('evidence_refs', [])),
                 'publication_verified': False, 'findings': []}
        if manifest.get('status') == 'INTEGRATED':
            # Preview recomputes the candidate using the historical algorithm;
            # it does not rewrite receipts or perform an LLM/source read.
            def _replay(historical):
                from ..workshop import integrate
                proposal_ids = report.get('proposal_ids') or [path.parent.name]
                proposal_paths = [Path('state/workshop/proposals') / p for p in proposal_ids]
                preview = integrate(root, read_json(root / 'config/brain-domains.json', []),
                                    proposal_paths, historical=historical)
                return bool(preview['approved'] and preview['reviewed']
                            and preview['candidate_sha256'] == report.get('candidate_sha256'))
            try:
                facts['publication_verified'] = _replay(False)
            except (ValueError, KeyError, TypeError, OSError):
                facts['publication_verified'] = False
            if not facts['publication_verified']:
                # A receipt can remain sound while later approved releases
                # changed the same paths; recompute the candidate from the
                # proposal set alone before reporting the receipt unresolved.
                try:
                    facts['publication_verified'] = _replay(True)
                except (ValueError, KeyError, TypeError, OSError):
                    facts['publication_verified'] = False
                facts['findings'].append('PUBLICATION_RECEIPT_HISTORICAL_ONLY'
                                        if facts['publication_verified']
                                        else 'PUBLICATION_RECEIPT_UNRESOLVED')
            if facts['publication_verified']:
                for item in files:
                    active = safe_path(root, 'brain wiki/' + item['path'], area='brain wiki')
                    if active.is_file() and digest(active.read_bytes()) == item['sha256']:
                        published['brain wiki/' + item['path']] = item['sha256']
                    else:
                        facts['findings'].append('ACTIVE_NOTE_DIFFERS_FROM_RECEIPT')
            if manifest.get('schema_version', 1) >= 2 and not lock.get('evidence_refs'):
                facts['findings'].append('EMPTY_EVIDENCE_LOCK')
        releases.append(facts)
    return releases, published


def compile_brain(root: Path) -> dict:
    root = root.resolve()
    from ..workshop import validate
    domains = read_json(root / 'config/brain-domains.json', [])
    validation = validate(root / 'brain wiki', domains)
    if not validation['valid']:
        raise ValueError('Active Markdown validation failed; run workshop validate')
    notes = read_notes(root)
    library = resolve_library(root)
    releases, published = publication_inventory(root)
    records = {r['evidence_ref']: r for r in library['records']}
    binding_map = {}
    for item in library['bindings']:
        binding_map.setdefault(item['section_id'], []).append(item)
    note_ids = {note['id'] for note in notes}
    all_sections, edges, findings = [], [], list(library['findings'])
    for note in notes:
        for target in re.findall(r'\[\[([^\]|#]+)', prose_without_code(note['body'])):
            if target in note_ids:
                edges.append({'source': note['id'], 'target': target, 'kind': 'link'})
        if note.get('depends_on'):
            edges.append({'source': note['id'], 'target': note['depends_on']['question_id'], 'kind': 'depends_on'})
        publication_valid = published.get(note['path']) == note['sha256']
        note['publication_verified'] = publication_valid
        for section in sections(note['id'], note['body']):
            candidates = [b for b in binding_map.get(section['section_id'], [])
                          if b['note_id'] == note['id'] and b['note_sha256'] == note['sha256']
                          and b['section_sha256'] == section['sha256'] and b['evidence_status'] == 'REVIEWED']
            # Conflicting reviewed mappings are visible, not silently merged.
            qualification_fields = ['evidence_refs', 'modality', 'applicability',
                                    'conflicts', 'limits', 'access_restrictions']
            unique = {canonical({k: b.get(k) for k in qualification_fields}) for b in candidates}
            binding = candidates[0] if len(unique) == 1 else None
            citations = [records[r] for r in binding['evidence_refs'] if r in records] if binding else []
            eligible = (publication_valid and bool(citations)
                        and all(c['evidence_status'] == 'REVIEWED' for c in citations))
            all_sections.append({**section, 'note_id': note['id'], 'path': note['path'],
                                 'note_sha256': note['sha256'], 'title': note['title'],
                                 'type': note['type'], 'domains': note['domains'], 'tags': note['tags'],
                                 'aliases': note['aliases'], 'status': note['status'],
                                 'evidence_status': 'REVIEWED' if eligible else 'UNRESOLVED',
                                 'modality': binding['modality'] if binding else None,
                                 **{k: binding.get(k) if binding else None
                                    for k in qualification_fields[2:]},
                                 'citations': citations, 'derived_from': [c['evidence_ref'] for c in citations]})
        if not publication_valid and note['type'] != 'index':
            findings.append({'severity': 'WARNING', 'code': 'PUBLICATION_LINEAGE_UNRESOLVED', 'id': note['id'], 'artifact': note['path']})
    edges = sorted({canonical(e): e for e in edges}.values(), key=lambda e: (e['source'], e['target'], e['kind']))
    incoming = Counter(e['target'] for e in edges)
    orphans = sorted(n['id'] for n in notes if n['type'] == 'knowledge' and not incoming[n['id']])
    for identity in orphans:
        findings.append({'severity': 'WARNING', 'code': 'NO_INCOMING_LINK', 'id': identity})
    source_rows = read_jsonl(root / 'state/source_manifest.jsonl')
    sources = [{k: s.get(k) for k in ['source_id', 'source_sha256', 'relative_paths', 'source_format', 'adapter_id', 'adapter_version', 'status', 'normativity', 'unit_count', 'domains']} for s in source_rows]
    content = {'schema_version': 1, 'notes': notes, 'sections': all_sections, 'edges': edges,
               'sources': sources, 'evidence': library, 'releases': releases,
               'findings': findings, 'orphans': orphans}
    content['catalogue_sha256'] = digest(canonical(content))
    return content


def coverage_matrix(root: Path, catalogue: dict) -> dict:
    original = read_json(root / 'state/workshop/coverage/coverage-register.json', {})
    criteria = original.get('definition_of_done', [])
    cells = []
    for pillar in original.get('pillars', []):
        scope = set(pillar['domains'])
        notes = [n for n in catalogue['notes'] if scope & set(n['domains']) and n['type'] == 'knowledge']
        questions = [n['id'] for n in catalogue['notes'] if scope & set(n['domains']) and n['type'] == 'question']
        sources = [s['source_id'] for s in catalogue['sources'] if scope & set(s.get('domains') or [])]
        for criterion in criteria:
            # Domain overlap is only a candidate search. It never proves a
            # criterion (or an obligation) complete.
            cells.append({'cell_id': f"{pillar['id']}::{criterion}", 'pillar_id': pillar['id'], 'criterion': criterion, 'status': 'UNASSESSED',
                          'candidate_note_ids': [n['id'] for n in notes],
                          'candidate_question_ids': questions, 'candidate_source_ids': sources,
                          'next_action': 'REVIEW_CRITERION_EVIDENCE' if sources else 'SEARCH_EXISTING_CORPUS_AND_RECORD_GAP',
                          'recorded_pillar_status': pillar['status']})
    base = {'schema_version': 1, 'catalogue_sha256': catalogue['catalogue_sha256'],
            'cells': cells, 'criteria': criteria, 'pillars': len(original.get('pillars', [])),
            'completion_policy': 'Candidate matches are not evidence of criterion completion; reviewed decisions require a release.'}
    try:
        from .coverage import project_coverage
        return project_coverage(root, catalogue, base)
    except (ImportError, OSError, TypeError, ValueError) as exc:
        # A missing/invalid decision contract is diagnostic only; the base
        # routing matrix remains visible and all statuses remain UNASSESSED.
        return {**base, 'diagnostics': [{'code': 'COVERAGE_PROJECTION_FAILED',
                                        'error_type': type(exc).__name__}]}


def status(root: Path, *, catalogue: dict | None = None) -> dict:
    cat = catalogue if catalogue is not None else compile_brain(root)
    return {'valid': True, 'schema_version': 1, 'catalogue_sha256': cat['catalogue_sha256'],
            'notes': len(cat['notes']), 'note_types': dict(Counter(n['type'] for n in cat['notes'])),
            'sections': len(cat['sections']), 'reviewed_sections': sum(s['evidence_status'] == 'REVIEWED' for s in cat['sections']),
            'sources': len(cat['sources']), 'orphan_knowledge': len(cat['orphans']),
            'evidence_findings': len(cat['evidence']['findings']),
            'publication_verified_notes': sum(n['publication_verified'] for n in cat['notes']),
            'llm_calls': 0, 'llm_cost': None}


def build(root: Path, *, write: bool = True) -> dict:
    root = root.resolve()
    cat = compile_brain(root)
    summary = status(root, catalogue=cat)
    baseline = read_json(root / 'state/workshop/brain-upgrade/baseline.json', {})
    baseline_changed = [p for p, h in baseline.get('files', {}).items()
                        if not safe_path(root, p).is_file() or digest(safe_path(root, p).read_bytes()) != h]
    report = ['# Brain diagnostic', '', f"- Notes: {summary['notes']}",
              f"- Sections with current reviewed evidence: {summary['reviewed_sections']}/{summary['sections']}",
              f"- Knowledge notes without incoming links: {summary['orphan_knowledge']}",
              '- Validation checks structure; it does not establish legal correctness.',
              '- Missing historical telemetry is unknown, not zero.', '', '## Releases', '']
    report += [f"- `{r['proposal_id']}`: {r['status']}; evidence refs: {r['evidence_refs']}; findings: {', '.join(r['findings']) or 'None'}" for r in cat['releases']]
    report += ['', '## Findings', ''] + [f"- {f['severity']} `{f['code']}` — `{f.get('id', f.get('artifact', ''))}`" for f in cat['findings']]
    nav = ['# Brain navigation', '', 'Generated from active Markdown. Evidence readiness is reported separately.', '']
    for domain in sorted({d for n in cat['notes'] for d in n['domains']}):
        nav += [f'## {domain}', '']
        nav += [f"- [[{n['id']}|{n['title']}]]" for n in cat['notes'] if domain in n['domains']]
        nav.append('')
    payloads = {
        'catalogue.json': cat,
        'evidence-index.json': cat['evidence'],
        'coverage-matrix.json': coverage_matrix(root, cat),
        'reconciliation.json': {'schema_version': 1, 'releases': cat['releases'], 'baseline_changed_paths': baseline_changed},
        'baseline.json': summary,
    }
    outputs = {name: json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n' for name, value in payloads.items()}
    outputs.update({'report.md': '\n'.join(report) + '\n', 'navigation.md': '\n'.join(nav) + '\n'})
    target = safe_path(root, 'state/derived/brain')
    changed = [name for name, text in outputs.items() if not (target / name).is_file() or (target / name).read_text(encoding='utf-8') != text]
    if write and changed:
        target.parent.mkdir(parents=True, exist_ok=True)
        temp = Path(tempfile.mkdtemp(prefix='.brain-build-', dir=target.parent))
        backup = target.parent / '.brain-previous'
        if backup.exists():
            shutil.rmtree(temp)
            raise ValueError('Previous Brain build requires recovery')
        try:
            for name, text in outputs.items():
                (temp / name).write_text(text, encoding='utf-8')
            if target.exists():
                os.replace(target, backup)
            try:
                os.replace(temp, target)
            except BaseException:
                if backup.exists():
                    os.replace(backup, target)
                raise
            if backup.exists():
                shutil.rmtree(backup)
        finally:
            if temp.exists():
                shutil.rmtree(temp)
    return {**summary, 'current': not changed, 'written': len(changed) if write else 0,
            'changed_paths': ['state/derived/brain/' + name for name in changed],
            'source_baseline_unchanged': not any(p.startswith('sources/') for p in baseline_changed)}
