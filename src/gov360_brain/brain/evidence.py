"""Hash-bound evidence library. Existing prose/status never grants review."""
from __future__ import annotations

from datetime import date
from pathlib import Path

import jsonschema

from .common import canonical, digest, parse_markdown, read_json, read_jsonl, safe_path


LIBRARY = 'state/workshop/evidence-library'
VALID_SOURCE_STATES = {'READY_FOR_LLM'}


def receipt_hash(receipt: dict) -> str:
    return digest(canonical({k: v for k, v in receipt.items() if k != 'review'}))


def _schema(root: Path) -> dict:
    path = root / 'config/schemas/brain-evidence.schema.json'
    if not path.exists():
        path = Path(__file__).resolve().parents[3] / 'config/schemas/brain-evidence.schema.json'
    return read_json(path)


def unit_check(root: Path, evidence: dict, manifests: dict) -> tuple[bool, str]:
    """Revalidate file, body, unit metadata, document and current source record."""
    source = manifests.get(evidence['source_id'])
    if not source or source.get('status') not in VALID_SOURCE_STATES:
        return False, 'SOURCE_UNAVAILABLE'
    if source.get('source_sha256') != evidence['source_sha256']:
        return False, 'SOURCE_HASH_CHANGED'
    unit = safe_path(root, evidence['unit_path'], area='ingest/' + evidence['source_id'])
    document_path = safe_path(root, 'ingest/' + evidence['source_id'] + '/document.json')
    document = read_json(document_path, {})
    if (document.get('validation', {}).get('valid') is not True
            or document.get('source_sha256') != evidence['source_sha256']):
        return False, 'DOCUMENT_UNVALIDATED'
    if not unit.is_file() or digest(unit.read_bytes()) != evidence['unit_file_sha256']:
        return False, 'UNIT_FILE_HASH_CHANGED'
    meta, body = parse_markdown(unit.read_text(encoding='utf-8'))
    if (meta.get('source_id') != evidence['source_id']
            or meta.get('source_sha256') != evidence['source_sha256']
            or meta.get('locator') != evidence['locator']
            or meta.get('content_sha256') != evidence['unit_sha256']
            or digest(body.rstrip() + '\n') != evidence['unit_sha256']):
        return False, 'UNIT_CONTENT_HASH_CHANGED'
    matches = [u for u in document.get('units', [])
               if u.get('filename') == unit.relative_to(document_path.parent).as_posix()]
    if len(matches) != 1 or any(matches[0].get(k) != v for k, v in {
        'locator': evidence['locator'], 'file_sha256': evidence['unit_file_sha256'],
        'content_sha256': evidence['unit_sha256']}.items()):
        return False, 'UNIT_LINEAGE_MISMATCH'
    return True, 'PASS'


def resolve_library(root: Path, *, receipt_paths: list[Path] | None = None) -> dict:
    """Only independent exact-input reviews resolve records; diagnostics stay metadata-only."""
    root = root.resolve()
    source_rows = read_jsonl(safe_path(root, 'state/source_manifest.jsonl'))
    duplicate_sources = {r['source_id'] for r in source_rows
                         if sum(x['source_id'] == r['source_id'] for x in source_rows) > 1}
    manifests = {r['source_id']: r for r in source_rows if r['source_id'] not in duplicate_sources}
    classifications = {r['source_id']: r for r in read_jsonl(root / 'state/source_classification_events.jsonl')}
    records, bindings, findings, receipts = [], [], [], []
    paths = receipt_paths if receipt_paths is not None else sorted((root / LIBRARY).glob('*.json'))
    seen_receipts: set[str] = set()
    for path in paths:
        label = path.relative_to(root).as_posix()
        try:
            safe_path(root, label, area=LIBRARY)
            data = read_json(path)
            jsonschema.Draft202012Validator(_schema(root), format_checker=jsonschema.FormatChecker()).validate(data)
            rid = data['receipt_id']
            if rid in seen_receipts:
                raise ValueError('Duplicate receipt identity')
            seen_receipts.add(rid)
            review = data.get('review', {})
            reviewed = (review.get('verdict') == 'EVIDENCE_READY'
                        and review.get('candidate_sha256') == receipt_hash(data)
                        and review.get('reviewer_identity') != data['author_identity']
                        and bool(review.get('reviewer_identity'))
                        and not any(f.get('severity') in {'ERROR', 'CRITICAL'} for f in review.get('findings', [])))
            refs = {e['evidence_ref'] for e in data['evidence']}
            if len(refs) != len(data['evidence']):
                raise ValueError('Duplicate evidence references')
            statuses = {}
            for evidence in data['evidence']:
                valid, code = unit_check(root, evidence, manifests)
                if evidence.get('revoked') or evidence.get('superseded_by'):
                    valid, code = False, 'EVIDENCE_REVOKED_OR_SUPERSEDED'
                expiry = evidence.get('review_expires_at')
                if expiry and date.fromisoformat(expiry) < date.today():
                    valid, code = False, 'EVIDENCE_REVIEW_EXPIRED'
                authority = evidence['authority']
                event = classifications.get(evidence['source_id'], {})
                # The evidence auditor can qualify non-binding context locally;
                # binding classification requires the explicit source event too.
                if authority == 'BINDING' and (event.get('normativity') != 'BINDING'
                        or event.get('source_sha256') != evidence['source_sha256']):
                    valid, code = False, 'BINDING_CLASSIFICATION_MISSING'
                for item in evidence['fidelity_inputs']:
                    fidelity_path = safe_path(root, item['path'], area='state/workshop')
                    if not fidelity_path.is_file() or digest(fidelity_path.read_bytes()) != item['sha256']:
                        valid, code = False, 'FIDELITY_RECEIPT_CHANGED'
                        continue
                    fidelity = read_json(fidelity_path, {})
                    covered = any(row.get('source_id') == evidence['source_id']
                                  and row.get('source_sha256') == evidence['source_sha256']
                                  and row.get('locator') == evidence['locator']
                                  and row.get('unit_file_sha256') == evidence['unit_file_sha256']
                                  and row.get('unit_content_sha256') == evidence['unit_sha256']
                                  and row.get('result', row.get('verdict')) in {'MATCH', 'REVIEWED'}
                                  for row in fidelity.get('results', []))
                    if not covered:
                        valid, code = False, 'FIDELITY_SCOPE_UNRESOLVED'
                if not evidence['fidelity_inputs']:
                    valid, code = False, 'FIDELITY_RECEIPT_MISSING'
                statuses[evidence['evidence_ref']] = reviewed and valid
                records.append({**evidence, 'receipt_id': rid, 'receipt_path': label,
                                'receipt_sha256': digest(path.read_bytes()),
                                'evidence_status': 'REVIEWED' if reviewed and valid else 'UNRESOLVED',
                                'source_status': manifests.get(evidence['source_id'], {}).get('status'),
                                'reviewer_identity': review.get('reviewer_identity'),
                                'reviewed_at': review.get('reviewed_at')})
                if not reviewed or not valid:
                    findings.append({'severity': 'WARNING', 'code': code if not valid else 'EVIDENCE_REVIEW_REQUIRED',
                                     'artifact': label, 'id': evidence['evidence_ref']})
            for binding in data['bindings']:
                valid_refs = bool(binding['evidence_refs']) and set(binding['evidence_refs']) <= refs
                binding_ready = valid_refs and all(statuses.get(ref, False) for ref in binding['evidence_refs'])
                if binding['modality'] in {'obligation', 'prohibition'}:
                    binding_ready = binding_ready and any(e['authority'] == 'BINDING' and e['evidence_ref'] in binding['evidence_refs'] for e in data['evidence'])
                bindings.append({**binding, 'receipt_id': rid, 'evidence_status': 'REVIEWED' if reviewed and binding_ready else 'UNRESOLVED'})
            receipts.append({'receipt_id': rid, 'path': label, 'candidate_sha256': receipt_hash(data), 'reviewed': reviewed})
        except (ValueError, KeyError, TypeError, OSError, jsonschema.ValidationError):
            findings.append({'severity': 'ERROR', 'code': 'INVALID_EVIDENCE_RECEIPT', 'artifact': label})
    duplicate_refs = {r['evidence_ref'] for r in records if sum(x['evidence_ref'] == r['evidence_ref'] for x in records) > 1}
    for record in records:
        if record['evidence_ref'] in duplicate_refs:
            record['evidence_status'] = 'UNRESOLVED'
    if duplicate_refs:
        findings.append({'severity': 'ERROR', 'code': 'AMBIGUOUS_EVIDENCE_ID', 'ids': sorted(duplicate_refs)})
    return {'schema_version': 1, 'records': records, 'bindings': bindings, 'receipts': receipts, 'findings': findings}
