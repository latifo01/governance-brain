"""Offline Markdown workshop. Never treats extraction integrity as factual approval."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
import jsonschema
import yaml
from .utils import atomic_write_json, atomic_write_text, canonical_json, sha256_file, sha256_text, slugify

DOMAINS = ['AI', 'LEGAL', 'DATA_PROTECTION', 'INTERNAL_REGULATION', 'RISK', 'PROCESS', 'GENERAL']
BANKS = ['AI_ACT', 'AI_LEGAL_GUIDANCE', 'AI_NICE_TO_KNOW', 'AI_REGULATION_INTERNAL', 'DATA_AI_CLASSIFICATION']
CATEGORIES = {'AI concepts': ['AI'], 'AI Risks': ['AI', 'RISK'], 'AI Risk Mitigations': ['AI', 'RISK'], 'Data & AI Laws': ['LEGAL'], 'Famous AI incidents': ['AI', 'RISK'], 'Norms & Frameworks': ['RISK'], 'Organizations': ['GENERAL']}

def parse(text):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    return (yaml.safe_load(match[1]) or {}, text[match.end():]) if match else ({}, text)

def render(meta, body):
    return '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n' + body.strip() + '\n'

def metadata(identity, title, kind='knowledge', domains=None, status='draft'):
    return dict(id=identity, title=title, type=kind, domains=domains or ['GENERAL'], status=status, aliases=[], tags=[], evidence_sources=[])

def inventory(root: Path, cdo: Path):
    """Preserve originals; generate review drafts and a migration manifest."""
    base = root / 'state' / 'workshop'
    files = sorted(cdo.rglob('*.md'))
    files = [p for p in files if not any(x.startswith('.') for x in p.relative_to(cdo).parts)]
    mapping = {p.stem: slugify(p.stem) for p in files}
    ids = list(mapping.values())
    if len(ids) != len(set(ids)) or len(mapping) != len(files):
        raise ValueError('CDO identifier collision requires explicit resolution')
    rows = []
    for path in files:
        rel = path.relative_to(cdo)
        old, body = parse(path.read_text(encoding='utf-8-sig'))
        identity = mapping[path.stem]
        category = 'AI Risk Mitigations' if rel.parts[0] == 'mitigations' else rel.parts[0]
        target = Path(category, *rel.parts[1:-1], identity + '.md') if len(rel.parts) > 1 else Path(identity + '.md')
        domains = ['DATA_PROTECTION', 'LEGAL'] if 'Data Privacy' in rel.parts else CATEGORIES.get(category, ['GENERAL'])
        meta = metadata(identity, path.stem, domains=domains)
        aliases = old.get('aliases', [])
        meta['aliases'] = sorted(set(([aliases] if isinstance(aliases, str) else aliases) + [path.stem]))
        links = re.findall(r'\[\[([^\]]+)\]\]', body)
        unresolved = []
        def rewrite(match):
            raw = match[1]; name = raw.split('|')[0].split('#')[0]
            if name in mapping:
                suffix = raw[len(name):]
                return '[[' + mapping[name] + suffix + ']]'
            unresolved.append(name)
            return match[0]
        body = re.sub(r'\[\[([^\]]+)\]\]', rewrite, body)
        empty = not body.strip()
        rows.append(dict(original_path=rel.as_posix(), source_sha256=sha256_file(path), id=identity, target_path=target.as_posix(), status='EMPTY_BACKLOG' if empty else 'EDITORIAL_REVIEW_REQUIRED', unresolved_links=sorted(set(unresolved)), original_links=links))
        # Exact local reference copies are documentary artifacts, not operational logs.
        atomic_write_text(base / 'cdo-reference' / rel, path.read_text(encoding='utf-8-sig'))
        if not empty:
            atomic_write_text(base / 'drafts' / target, render(meta, body))
    atomic_write_json(base / 'cdo-inventory.json', rows)
    return {'notes': len(rows), 'drafts': sum(r['status'] != 'EMPTY_BACKLOG' for r in rows), 'empty_backlog': sum(r['status'] == 'EMPTY_BACKLOG' for r in rows)}

def quality(root):
    rows = []
    for path in sorted((root / 'ingest').glob('SRC-*/document.json')):
        doc = json.loads(path.read_text(encoding='utf-8'))
        for unit in doc.get('units', []):
            file = (path.parent / unit['filename']).resolve()
            if not file.is_relative_to(path.parent.resolve()):
                raise ValueError('Unit path escapes source directory')
            valid = file.is_file() and sha256_file(file) == unit.get('file_sha256')
            flags = []
            if valid:
                meta, body = parse(file.read_text(encoding='utf-8'))
                if len(body.strip()) < 80: flags.append('SHORT_TEXT')
                if '\ufffd' in body: flags.append('REPLACEMENT_CHARACTER')
                if meta.get('visual_review') in ['REVIEW_REQUIRED', 'UNREADABLE']: flags.append('VISUAL_REVIEW')
                if meta.get('warnings'): flags.append('EXTRACTION_WARNING')
            rows.append(dict(source_id=doc.get('source_id', path.parent.name), filename=unit['filename'], locator=unit.get('locator'), file_sha256=unit.get('file_sha256'), integrity='PASS' if valid else 'FAIL', fidelity='NOT_REVIEWED', flags=flags))
    atomic_write_json(root / 'state/workshop/extraction-quality.json', rows)
    return {'units': len(rows), 'integrity_failures': sum(r['integrity'] == 'FAIL' for r in rows), 'flagged': sum(bool(r['flags']) for r in rows), 'fidelity_reviewed': 0}

def validate(vault, domains, overlay=None):
    errors, notes, dependencies = [], {}, {}
    schema_path = vault.parent / 'config' / 'schemas' / 'brain-note.schema.json'
    if not schema_path.exists():
        schema_path = Path(__file__).resolve().parents[2] / 'config' / 'schemas' / 'brain-note.schema.json'
    schema = json.loads(schema_path.read_text(encoding='utf-8'))
    validator = jsonschema.Draft202012Validator(schema)
    files = {path.relative_to(vault): path for path in vault.rglob('*.md')}
    overlays = [] if overlay is None else ([overlay] if isinstance(overlay, Path) else list(overlay))
    overlay_files = {}
    for directory in overlays:
        for path in directory.rglob('*.md'):
            relative = path.relative_to(directory)
            if relative in overlay_files:
                errors.append({
                    'path': relative.as_posix(),
                    'error': 'conflicting proposal paths',
                    'proposals': [overlay_files[relative].as_posix(), path.as_posix()],
                })
                continue
            overlay_files[relative] = path
    files.update(overlay_files)
    for relative, path in sorted(files.items(), key=lambda item: item[0].as_posix()):
        try:
            meta, body = parse(path.read_text(encoding='utf-8'))
            failures = sorted(validator.iter_errors(meta), key=lambda item: list(item.absolute_path))
            if failures:
                failure = failures[0]
                location = '.'.join(str(part) for part in failure.absolute_path) or 'frontmatter'
                raise ValueError(f'schema: {location}: {failure.message}')
            identity = meta['id']
            if identity in notes: raise ValueError('duplicate id')
            if not isinstance(meta['domains'], list) or not meta['domains'] or set(meta['domains']) - set(domains): raise ValueError('unknown domain')
            if not body.strip() or re.search(r'\bTODO\b|\bPLACEHOLDER\b', body): raise ValueError('empty or placeholder note')
            if path.name not in {'README.md', 'SCHEMA.md'} and path.stem != identity:
                raise ValueError('filename must match id')
            if meta['type'] == 'question':
                dep = meta['depends_on']
                if dep is not None:
                    dependencies[identity] = dep['question_id']
            notes[identity] = (meta, body)
        except (ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
            errors.append({'path': relative.as_posix(), 'error': str(exc)})
    for identity, (meta, body) in notes.items():
        for target in re.findall(r'\[\[([^\]|#]+)', body):
            if target not in notes: errors.append({'id': identity, 'error': 'unresolved link', 'target': target})
    for identity, target in dependencies.items():
        if target not in notes or notes[target][0]['type'] != 'question': errors.append({'id': identity, 'error': 'missing question dependency'})
        seen = {identity}
        while target in dependencies:
            if target in seen:
                errors.append({'id': identity, 'error': 'dependency cycle'}); break
            seen.add(target); target = dependencies[target]
    result = {'notes': len(notes), 'errors': errors, 'valid': not errors}
    if overlays:
        labels = []
        for directory in overlays:
            try:
                labels.append(directory.relative_to(vault.parent).as_posix())
            except ValueError:
                labels.append(directory.name)
        if len(labels) == 1:
            result['overlay'] = labels[0]
        else:
            result['overlays'] = labels
    return result

def resolve_proposals(root: Path, requested: list[Path]):
    proposals_root = (root / 'state' / 'workshop' / 'proposals').resolve()
    resolved = []
    for value in requested:
        proposal = value if value.is_absolute() else root / value
        proposal = proposal.resolve()
        if not proposal.is_relative_to(proposals_root):
            raise ValueError('Proposal must be under state/workshop/proposals')
        overlay = proposal / 'future-vault'
        if not overlay.is_dir():
            raise ValueError('Proposal future-vault directory not found')
        resolved.append((proposal, overlay))
    if not resolved:
        raise ValueError('At least one proposal is required')
    if len({proposal for proposal, _ in resolved}) != len(resolved):
        raise ValueError('A proposal may be supplied only once')
    return resolved


def init_release(root: Path, domains: list[str], domain: str, proposal_id: str,
                 risk_tier: str = 'fast', author_identity: str = 'unassigned',
                 schema_version: int = 2):
    """Create a release scaffold.

    Direct library callers may still create a historical v2 fixture. The CLI
    creates v3 candidates explicitly, as required for new publication.
    """
    if domain not in domains:
        raise ValueError(f'Unknown release domain: {domain}')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', proposal_id):
        raise ValueError('Release ID must use lowercase kebab-case')
    proposal = root / 'state/workshop/proposals' / proposal_id
    if proposal.exists():
        raise ValueError(f'Release already exists: {proposal_id}')
    overlay = proposal / 'future-vault'
    review = proposal / 'review'
    overlay.mkdir(parents=True)
    review.mkdir()
    manifest = {
        'schema_version': schema_version,
        'proposal_id': proposal_id,
        'status': 'DRAFT',
        'published': False,
        'domain': domain,
        'risk_tier': risk_tier,
        'evidence_changes': False,
        'contract_changes': False,
        'contains_binding_claims': False,
        'contains_legal_interpretation': False,
        'shards': [],
        'requires_proposals': [],
        'changes': {'ADD': [], 'UPDATE': [], 'SUPERSEDE': [], 'NOOP': []},
        'files': [],
    }
    if schema_version == 3:
        manifest['author_identity'] = author_identity
    atomic_write_json(proposal / 'manifest.json', manifest)
    atomic_write_json(proposal / 'evidence-lock.json', {'schema_version': 2 if schema_version == 3 else 1, 'evidence_refs': [], **({'library_receipts': []} if schema_version == 3 else {})})
    atomic_write_json(proposal / 'metrics.json', {
        'schema_version': 2, 'llm_calls': None, 'input_tokens': None,
        'output_tokens': None, 'cost': None, 'models': [],
    })
    atomic_write_text(review / 'approval.md', f'''# Human approval — {proposal_id}

Status: PENDING

- Approver identity: PENDING
- Decision: PENDING
- Scope: PENDING
- Rationale: PENDING
- Decision date: PENDING
- Candidate SHA-256: PENDING
''')
    return {'valid': True, 'proposal_id': proposal_id,
            'path': proposal.relative_to(root).as_posix(), 'risk_tier': risk_tier}

def _approval(proposal: Path, expected_sha256: str | None = None):
    path = proposal / 'review' / 'approval.md'
    if not path.is_file():
        return {'approved': False, 'reason': 'approval record missing'}
    text = path.read_text(encoding='utf-8')
    status = re.search(r'^Status:\s*([^\s]+)\s*$', text, re.M)
    fields = {}
    for name in ('Approver identity', 'Decision', 'Scope', 'Rationale', 'Decision date', 'Candidate SHA-256'):
        match = re.search(rf'^- {re.escape(name)}:\s*(.+?)\s*$', text, re.M)
        fields[name] = match.group(1).strip() if match else ''
    required = ('Approver identity', 'Decision', 'Scope', 'Rationale', 'Decision date')
    complete = all(fields[name] and fields[name] != 'PENDING' for name in required)
    hash_matches = expected_sha256 is None or fields['Candidate SHA-256'] == expected_sha256
    approved = bool(status and status.group(1) == 'APPROVED' and fields['Decision'] == 'APPROVED' and complete)
    approved = approved and hash_matches
    reason = None if approved else ('approval candidate hash mismatch' if complete and not hash_matches else 'explicit complete approval required')
    return {'approved': approved, 'reason': reason}


def _validate_release_manifest(root: Path, proposal: Path, overlay: Path,
                               manifest: dict, domains: list[str]):
    """Validate the accelerated v2 release contract and its risk lane."""
    if manifest.get('schema_version') not in {2, 3}:
        return {'risk_tier': 'legacy', 'evidence_lock_sha256': None}
    schema_name = 'workshop-release-v3.schema.json' if manifest['schema_version'] == 3 else 'workshop-release.schema.json'
    schema_path = root / 'config/schemas' / schema_name
    if not schema_path.exists():
        schema_path = Path(__file__).resolve().parents[2] / 'config/schemas' / schema_name
    schema = json.loads(schema_path.read_text(encoding='utf-8'))
    try:
        jsonschema.Draft202012Validator(schema).validate(manifest)
    except jsonschema.ValidationError as exc:
        raise ValueError(f'Invalid release manifest: {exc.message}') from None
    if manifest['domain'] not in domains:
        raise ValueError(f"Unknown release domain: {manifest['domain']}")
    evidence_lock_path = proposal / 'evidence-lock.json'
    if not evidence_lock_path.is_file():
        raise ValueError(f'Evidence lock missing for {proposal.name}')
    evidence_lock = json.loads(evidence_lock_path.read_text(encoding='utf-8'))
    refs = evidence_lock.get('evidence_refs', []) if isinstance(evidence_lock, dict) else None
    if not isinstance(refs, list) or len(refs) > 120:
        raise ValueError('Evidence lock must contain at most 120 evidence_refs')

    counts = {'knowledge': 0, 'question': 0, 'index': 0}
    for path in overlay.rglob('*.md'):
        meta, _ = parse(path.read_text(encoding='utf-8'))
        kind = meta.get('type')
        if kind in counts:
            counts[kind] += 1
    if counts['knowledge'] > 30 or counts['question'] > 50:
        raise ValueError('Release exceeds the fast review limits of 30 knowledge notes or 50 questions')

    strict_reasons = []
    for field in ('evidence_changes', 'contract_changes', 'contains_binding_claims', 'contains_legal_interpretation'):
        if manifest[field]:
            strict_reasons.append(field)
    if manifest['changes'].get('SUPERSEDE'):
        strict_reasons.append('supersession')
    resolved = {}
    if manifest['schema_version'] == 3:
        from .brain.releases import resolved_release
        resolved = resolved_release(root, proposal, overlay, manifest)
        strict_reasons.extend(resolved['strict_reasons'])
    effective_tier = 'strict' if strict_reasons else manifest['risk_tier']
    if manifest['schema_version'] == 2 and manifest['risk_tier'] == 'fast' and strict_reasons:
        raise ValueError('Fast release contains strict-lane triggers: ' + ', '.join(strict_reasons))
    contract = {
        **resolved,
        'risk_tier': effective_tier,
        'evidence_lock_sha256': sha256_file(evidence_lock_path),
        'counts': counts,
    }
    if manifest['schema_version'] == 3:
        # Keep author identity available even for index-only releases where
        # there is no substantive section for resolved_release() to inspect.
        contract['author_identity'] = manifest['author_identity']
    return contract


def _release_review(proposal: Path, expected_sha256: str, contract: dict):
    if contract['risk_tier'] == 'strict':
        evidence_path = proposal / 'review/evidence-review.json'
        if not evidence_path.is_file():
            return {'ready': False, 'reason': 'strict release evidence review missing'}
        try:
            evidence_review = json.loads(evidence_path.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            return {'ready': False, 'reason': 'strict release evidence review invalid'}
        evidence_complete = (isinstance(evidence_review.get('findings'), list)
                             and bool(evidence_review.get('reviewer_identity'))
                             and bool(evidence_review.get('reviewed_at')))
        if (not evidence_complete or evidence_review.get('verdict') != 'EVIDENCE_READY'
                or evidence_review.get('evidence_lock_sha256') != contract['evidence_lock_sha256']):
            return {'ready': False, 'reason': 'evidence review verdict or lock hash mismatch'}
        if contract.get('author_identity') == evidence_review.get('reviewer_identity'):
            return {'ready': False, 'reason': 'evidence reviewer must differ from author'}
        if contract.get('author_identity') and any(f.get('severity') in {'ERROR', 'CRITICAL'} for f in evidence_review.get('findings', [])):
            return {'ready': False, 'reason': 'blocking evidence review findings'}
    path = proposal / 'review/release-review.json'
    if not path.is_file():
        return {'ready': False, 'reason': 'release review missing'}
    try:
        review = json.loads(path.read_text(encoding='utf-8'))
    except (json.JSONDecodeError, OSError):
        return {'ready': False, 'reason': 'release review invalid'}
    complete = (isinstance(review.get('findings'), list)
                and bool(review.get('reviewer_identity'))
                and bool(review.get('reviewed_at')))
    ready = (complete and review.get('verdict') == 'READY_FOR_HUMAN_APPROVAL'
             and review.get('candidate_sha256') == expected_sha256)
    if contract.get('author_identity'):
        ready = ready and review.get('reviewer_identity') != contract['author_identity']
        ready = ready and not any(f.get('severity') in {'ERROR', 'CRITICAL'} for f in review.get('findings', []))
    return {'ready': ready, 'reason': None if ready else 'release review verdict or candidate hash mismatch'}

def integrate(root: Path, domains: list[str], requested: list[Path], *, apply=False,
              historical=False):
    """Validate an ordered proposal set and atomically materialise approved Markdown.

    With ``historical=True`` the candidate is recomputed from the proposal set
    alone: the vault-state application checks (ADD target already present,
    UPDATE/SUPERSEDE target missing) are skipped so a receipt whose files were
    later superseded by other approved releases can still be verified against
    its own recorded candidate. Historical verification never applies.
    """
    if historical and apply:
        raise ValueError('Historical verification cannot apply to the active vault')
    resolved = resolve_proposals(root, requested)
    proposal_ids, manifests, release_contracts = [], [], []
    positions = {}
    for position, (proposal, _) in enumerate(resolved):
        manifest_path = proposal / 'manifest.json'
        if not manifest_path.is_file():
            raise ValueError(f'Manifest missing for {proposal.name}')
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        proposal_id = manifest.get('proposal_id')
        if proposal_id != proposal.name or proposal_id in positions:
            raise ValueError('Proposal ID must be unique and match its directory')
        positions[proposal_id] = position
        proposal_ids.append(proposal_id)
        manifests.append(manifest)
        release_contracts.append(_validate_release_manifest(root, proposal, resolved[position][1], manifest, domains))
    for position, manifest in enumerate(manifests):
        for dependency in manifest.get('requires_proposals', []):
            if dependency not in positions or positions[dependency] >= position:
                raise ValueError(f'Required proposal must appear earlier: {dependency}')

    vault = root / 'brain wiki'
    validation = validate(vault, domains, [overlay for _, overlay in resolved])
    if not validation['valid']:
        raise ValueError('Combined proposal validation failed')

    candidate_files, operations = [], []
    seen_targets = set()
    for (proposal, overlay), manifest in zip(resolved, manifests):
        paths = sorted(overlay.rglob('*.md'))
        relative_paths = [path.relative_to(overlay) for path in paths]
        declared_files = manifest.get('files')
        if declared_files is not None and {path.as_posix() for path in relative_paths} != set(declared_files):
            raise ValueError(f'Manifest file list does not match overlay: {proposal.name}')

        changes = manifest.get('changes')
        id_actions = {}
        if changes is not None:
            for action in ('ADD', 'UPDATE', 'SUPERSEDE'):
                for identity in changes.get(action, []):
                    if identity in id_actions:
                        raise ValueError(f'Duplicate manifest identity: {identity}')
                    id_actions[identity] = action
            proposed_ids = {parse(path.read_text(encoding='utf-8'))[0].get('id') for path in paths}
            if proposed_ids != set(id_actions):
                raise ValueError(f'Manifest change IDs do not match overlay: {proposal.name}')

        for source, relative in zip(paths, relative_paths):
            target = (vault / relative).resolve()
            if not target.is_relative_to(vault.resolve()) or target in seen_targets:
                raise ValueError(f'Unsafe or conflicting integration path: {relative.as_posix()}')
            seen_targets.add(target)
            content = source.read_text(encoding='utf-8')
            meta, _ = parse(content)
            action = id_actions.get(meta.get('id'), manifest.get('change'))
            if not historical and action == 'ADD' and target.exists() and target.read_text(encoding='utf-8') != content:
                raise ValueError(f'ADD target already exists: {relative.as_posix()}')
            if not historical and action in {'UPDATE', 'SUPERSEDE'} and not target.exists():
                raise ValueError(f'{action} target does not exist: {relative.as_posix()}')
            candidate_files.append({
                'proposal_id': proposal.name,
                'path': relative.as_posix(),
                'sha256': sha256_file(source),
            })
            operations.append((source, target, content))

    if any(manifest.get('schema_version') in {2, 3} for manifest in manifests):
        candidate_payload = {
            'files': candidate_files,
            'releases': [{
                'proposal_id': manifest['proposal_id'],
                'domain': manifest.get('domain'),
                'risk_tier': contract['risk_tier'],
                'changes': manifest.get('changes'),
                'shards': manifest.get('shards', []),
                'requires_proposals': manifest.get('requires_proposals', []),
                'strict_flags': {
                    field: manifest.get(field, False)
                    for field in ('evidence_changes', 'contract_changes',
                                  'contains_binding_claims', 'contains_legal_interpretation')
                },
                'evidence_lock_sha256': contract['evidence_lock_sha256'],
                **({'author_identity': manifest['author_identity']} if manifest.get('schema_version') == 3 else {}),
            } for manifest, contract in zip(manifests, release_contracts)],
        }
        candidate_sha256 = sha256_text(canonical_json(candidate_payload))
    else:
        candidate_sha256 = sha256_text(canonical_json(candidate_files))
    approvals = [
        _approval(proposal, candidate_sha256 if manifest.get('schema_version') in {2, 3} else None)
        for (proposal, _), manifest in zip(resolved, manifests)
    ]
    reviews = [
        _release_review(proposal, candidate_sha256, contract) if manifest.get('schema_version') in {2, 3} else {'ready': True, 'reason': None}
        for (proposal, _), manifest, contract in zip(resolved, manifests, release_contracts)
    ]
    changed = [(source, target, content) for source, target, content in operations
               if not target.exists() or target.read_text(encoding='utf-8') != content]
    result = {
        'valid': True,
        'applied': False,
        'approved': all(item['approved'] for item in approvals),
        'reviewed': all(item['ready'] for item in reviews),
        'risk_tiers': [contract['risk_tier'] for contract in release_contracts],
        'evidence_locks': {
            proposal_id: contract['evidence_lock_sha256']
            for proposal_id, contract in zip(proposal_ids, release_contracts)
            if contract['evidence_lock_sha256'] is not None
        },
        'proposal_ids': proposal_ids,
        'candidate_sha256': candidate_sha256,
        'files': len(candidate_files),
        'would_write': len(changed),
        'notes_after_integration': validation['notes'],
    }
    if not apply:
        return result
    if not result['reviewed']:
        raise ValueError('All v2 releases require an independent review bound to the candidate hash')
    if not result['approved'] or any(manifest.get('status') not in {'APPROVED', 'INTEGRATED'} for manifest in manifests):
        raise ValueError('All proposal manifests and approval records must be APPROVED')

    report_paths = [proposal / 'review' / 'integration-report.json' for proposal, _ in resolved]
    from .derived import CANVAS_PATH, REGISTRY_PATH, build_derived

    derived_paths = [root / REGISTRY_PATH, root / CANVAS_PATH]
    state_paths = [proposal / 'manifest.json' for proposal, _ in resolved] + report_paths + derived_paths
    previous = {path: path.read_text(encoding='utf-8') if path.exists() else None
                for path in [target for _, target, _ in changed] + state_paths}
    try:
        for _, target, content in changed:
            atomic_write_text(target, content)
        final_validation = validate(vault, domains)
        if not final_validation['valid']:
            raise ValueError('Active vault validation failed after integration')

        derived = build_derived(root)

        report = {
            'schema_version': 1,
            'proposal_ids': proposal_ids,
            'candidate_sha256': candidate_sha256,
            'files': candidate_files,
            'materialized_files': len(candidate_files),
            'notes': final_validation['notes'],
            'valid': True,
            'derived': {
                'questions': derived['questions'],
                'dependencies': derived['dependencies'],
                'registry_sha256': derived['registry_sha256'],
                'canvas_sha256': derived['canvas_sha256'],
            },
        }
        for (proposal, _), manifest in zip(resolved, manifests):
            manifest['status'] = 'INTEGRATED'
            manifest['published'] = True
            if manifest.get('schema_version') in {2, 3}:
                manifest['candidate_sha256'] = candidate_sha256
            atomic_write_json(proposal / 'manifest.json', manifest)
            atomic_write_json(proposal / 'review' / 'integration-report.json', report)
    except BaseException:
        for target, content in reversed(previous.items()):
            if content is None:
                target.unlink(missing_ok=True)
            else:
                atomic_write_text(target, content)
        raise
    result.update(applied=True, written=len(changed), derived_written=derived['written'])
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('inventory').add_argument('--cdo', required=True, type=Path)
    sub.add_parser('quality')
    check = sub.add_parser('validate')
    check.add_argument('--proposal', type=Path, action='append', default=[])
    assembly = sub.add_parser('integrate')
    assembly.add_argument('--proposal', type=Path, action='append', required=True)
    assembly.add_argument('--apply', action='store_true')
    init = sub.add_parser('domain-add'); init.add_argument('domain')
    release = sub.add_parser('release-init')
    release.add_argument('domain')
    release.add_argument('proposal_id')
    release.add_argument('--risk-tier', choices=['fast', 'strict'], default='fast')
    release.add_argument('--author', default='unassigned')
    sub.add_parser('build-derived')
    sub.add_parser('check-derived')
    sub.add_parser('build-atlas-catalog')
    sub.add_parser('check-atlas-catalog')
    watch = sub.add_parser('watch-derived')
    watch.add_argument('--interval', type=float, default=1.0)
    args = parser.parse_args(); root = args.root.resolve()
    registry = root / 'config/brain-domains.json'
    domains = json.loads(registry.read_text()) if registry.exists() else DOMAINS.copy()
    try:
        if args.command == 'inventory': result = inventory(root, args.cdo)
        elif args.command == 'quality': result = quality(root)
        elif args.command == 'domain-add':
            if not re.fullmatch('[A-Z][A-Z0-9_]*', args.domain): raise ValueError('Domain must be uppercase')
            domains = sorted(set(domains + [args.domain])); atomic_write_json(registry, domains)
            result = {'domains': domains}
        elif args.command == 'release-init':
            result = init_release(root, domains, args.domain, args.proposal_id, args.risk_tier, args.author, schema_version=3)
        elif args.command == 'integrate':
            result = integrate(root, domains, args.proposal, apply=args.apply)
        elif args.command in {'build-derived', 'check-derived'}:
            from .derived import build_derived
            result = build_derived(root, write=args.command == 'build-derived')
        elif args.command in {'build-atlas-catalog', 'check-atlas-catalog'}:
            from .derived import build_atlas_catalog
            result = build_atlas_catalog(root, write=args.command == 'build-atlas-catalog')
        elif args.command == 'watch-derived':
            from .derived import watch_derived
            try:
                watch_derived(root, interval=args.interval)
            except KeyboardInterrupt:
                print(json.dumps({'valid': True, 'stopped': True}, indent=2))
                return
            return
        else:
            resolved = resolve_proposals(root, args.proposal) if args.proposal else []
            result = validate(root / 'brain wiki', domains, [overlay for _, overlay in resolved] or None)
    except ValueError as exc:
        print(json.dumps({'valid': False, 'error': str(exc)}, indent=2))
        raise SystemExit(1) from None
    print(json.dumps(result, indent=2))
    if result.get('valid') is False: raise SystemExit(1)
    if args.command == 'check-derived' and not result.get('current'): raise SystemExit(1)
    if args.command == 'check-atlas-catalog' and not result.get('current'): raise SystemExit(1)

if __name__ == '__main__': main()
