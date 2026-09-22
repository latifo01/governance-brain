"""Read validated normalized units without opening immutable originals.

Integrity is checked here; authority, fidelity and approval are not granted.
Exceptions contain fixed codes only, never source-controlled values.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import jsonschema

from .common import digest, parse_markdown, read_json, read_jsonl, safe_path


class IngestReadError(ValueError):
    pass


def source_document(root: Path, source_id: str) -> tuple[dict, dict]:
    if not re.fullmatch(r'SRC-[0-9]{4,}', source_id):
        raise IngestReadError('INVALID_SOURCE_ID')
    rows = read_jsonl(safe_path(root, 'state/source_manifest.jsonl'))
    matches = [r for r in rows if r.get('source_id') == source_id]
    if len(matches) != 1 or matches[0].get('status') != 'READY_FOR_LLM':
        raise IngestReadError('SOURCE_UNAVAILABLE_OR_AMBIGUOUS')
    source = matches[0]
    document = read_json(safe_path(root, f'ingest/{source_id}/document.json'), {})
    if (document.get('source_id') != source_id
            or document.get('source_sha256') != source.get('source_sha256')
            or document.get('validation', {}).get('valid') is not True):
        raise IngestReadError('DOCUMENT_UNVALIDATED')
    if not re.fullmatch(r'[a-f0-9]{64}', str(source.get('source_sha256', ''))):
        raise IngestReadError('INVALID_SOURCE_HASH')
    units = document.get('units')
    if not isinstance(units, list) or any(not isinstance(u, dict) for u in units):
        raise IngestReadError('INVALID_UNIT_INVENTORY')
    names = [u.get('filename') for u in units]
    if any(not isinstance(n, str) for n in names) or len(names) != len(set(names)):
        raise IngestReadError('AMBIGUOUS_UNIT_INVENTORY')
    return source, document


def validated_unit(root: Path, source: dict, document: dict, filename: str) -> dict:
    """Inputs source/document must come from source_document in the same operation."""
    source_id = source['source_id']
    try:
        unit_path = safe_path(root, f'ingest/{source_id}/{filename}', area=f'ingest/{source_id}/units')
        matches = [u for u in document['units'] if u.get('filename') == filename]
        if len(matches) != 1:
            raise IngestReadError('UNIT_LINEAGE_MISMATCH')
        record = matches[0]
        raw = unit_path.read_bytes()
        if digest(raw) != record.get('file_sha256'):
            raise IngestReadError('UNIT_FILE_HASH_CHANGED')
        meta, body = parse_markdown(raw.decode('utf-8'))
        schema_path = root / 'config/schemas/ingested-unit.schema.json'
        if not schema_path.is_file():
            schema_path = Path(__file__).resolve().parents[3] / 'config/schemas/ingested-unit.schema.json'
        jsonschema.Draft202012Validator(read_json(schema_path)).validate(meta)
        if (meta['source_id'] != source_id or meta['source_sha256'] != source['source_sha256']
                or meta['content_sha256'] != record.get('content_sha256')
                or digest(body.rstrip() + '\n') != meta['content_sha256']
                or meta['locator'] != record.get('locator')):
            raise IngestReadError('UNIT_CONTENT_OR_LINEAGE_CHANGED')
        return {'metadata': meta, 'body': body, 'record': record,
                'path': unit_path.relative_to(root.resolve()).as_posix()}
    except IngestReadError:
        raise
    except (ValueError, OSError, KeyError, TypeError, jsonschema.ValidationError):
        raise IngestReadError('INVALID_NORMALIZED_UNIT') from None


def structured_json(unit: dict):
    """Reverse StructuredDataAdapter's quoted JSON encoding; never execute it."""
    quoted = [line[2:] if line.startswith('> ') else ''
              for line in unit['body'].splitlines() if line.startswith('>')]
    if not quoted:
        raise IngestReadError('NORMALIZED_JSON_MISSING')
    # Reverse backslash doubling and HTML escaping in the inverse order.
    text = '\n'.join(quoted).replace('\\\\', '\\')
    # Only the two entities produced by neutralize_untrusted_text are decoded.
    # html.unescape would corrupt original strings such as &amp; or &#65;.
    text = text.replace('&lt;', '<').replace('&gt;', '>')
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        raise IngestReadError('INVALID_NORMALIZED_JSON') from None
