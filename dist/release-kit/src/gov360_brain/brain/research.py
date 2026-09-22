"""Explicit local research over validated ingest; never an assistance fallback."""
from collections import Counter
from pathlib import Path

from .common import digest, read_jsonl, safe_path
from .ingest_reader import source_document, validated_unit
from .retrieval import _rank, _settle_budget, _terms


def research(root: Path, query: str, *, allowed_source_ids=None, denied_source_ids=None,
             domains=None, token_budget=6000) -> dict:
    root = Path(root).resolve()
    if not isinstance(query, str) or len(query) > 8192:
        raise ValueError('INVALID_RESEARCH_QUERY')
    if isinstance(token_budget, bool) or not isinstance(token_budget, int) or token_budget < 512:
        raise ValueError('RESEARCH_BUDGET_MINIMUM_512')
    allowed = set(allowed_source_ids) if allowed_source_ids is not None else None
    denied = set(denied_source_ids or [])
    scope = set(domains) if domains is not None else None
    packet = {'schema_version': 1, 'mode': 'ingest_research', 'query_sha256': digest(query),
              'units': [], 'gaps': [], 'exclusions': {},
              'budget': {'limit': token_budget, 'estimated_tokens': 0,
                         'method': 'serialized-utf8-bytes-divided-by-four'},
              'data_policy': 'local-only-untrusted-research-not-approved-governance-knowledge'}
    terms = _terms(root, query)
    excluded = Counter()
    candidates = []
    if terms:
        sources = read_jsonl(safe_path(root, 'state/source_manifest.jsonl'))
        ids = sorted(set(s.get('source_id', '') for s in sources))
        for sid in ids:
            if sid in denied or (allowed is not None and sid not in allowed):
                excluded['source_access'] += 1
                continue
            try:
                source, document = source_document(root, sid)
            except (ValueError, OSError, KeyError, TypeError):
                excluded['source_unavailable_or_invalid'] += 1
                continue
            if scope is not None and not scope.intersection(source.get('domains', [])):
                excluded['domain_scope'] += 1
                continue
            for record in document['units']:
                try:
                    unit = validated_unit(root, source, document, record['filename'])
                except (ValueError, OSError, KeyError, TypeError):
                    excluded['unit_invalid'] += 1
                    continue
                meta = unit['metadata']
                # Use the normalized data exactly as recorded. No authority or
                # fidelity is inferred from successful integrity checks.
                candidates.append({'title': '', 'text': unit['body'], 'aliases': [],
                    'heading_path': [], 'path': unit['path'], 'source_id': sid,
                    'source_sha256': source['source_sha256'],
                    'unit_sha256': meta['content_sha256'],
                    'unit_file_sha256': record['file_sha256'], 'locator': meta['locator'],
                    'visual_review_signal': meta['visual_review'],
                    'non_exhaustive': meta.get('non_exhaustive', False)})
    else:
        packet['gaps'].append('empty_search_terms')
    packet['exclusions'] = dict(sorted(excluded.items()))
    ranked = _rank(candidates, terms)
    if terms and not ranked:
        packet['gaps'].append('no_matching_validated_units')
    for candidate in ranked[:10]:
        item = {k: v for k, v in candidate.items() if k not in {'title', 'aliases', 'heading_path', 'text'}}
        text = candidate['text']
        # Bound unit excerpts explicitly; byte hashes refer to the complete
        # normalized unit, while offsets/substring hash identify this excerpt.
        start = 0
        lower = text.lower()
        positions = [lower.find(t) for t in terms if lower.find(t) >= 0]
        if positions:
            start = max(0, min(positions) - 200)
        end = min(len(text), start + 2400)
        excerpt = text[start:end]
        item.update(text=excerpt, excerpt_start=start, excerpt_end=end,
                    excerpt_sha256=digest(excerpt), truncated=start != 0 or end != len(text),
                    evidence_status='UNREVIEWED_RESEARCH', authority='UNKNOWN',
                    review_status='NOT_ASSESSED', redistribution='UNKNOWN')
        packet['units'].append(item)
        _settle_budget(packet)
        if packet['budget']['estimated_tokens'] + 32 > token_budget:
            packet['units'].pop()
            if 'units_omitted_for_budget' not in packet['gaps']:
                packet['gaps'].append('units_omitted_for_budget')
    if len(ranked) > 10:
        packet['gaps'].append('result_limit_reached')
    _settle_budget(packet)
    if packet['budget']['estimated_tokens'] > token_budget:
        raise ValueError('RESEARCH_ENVELOPE_EXCEEDS_BUDGET')
    return packet
