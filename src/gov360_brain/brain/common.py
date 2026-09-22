"""Small shared primitives; no source discovery or network side effects."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml


def digest(value: bytes | str) -> str:
    return hashlib.sha256(value.encode('utf-8') if isinstance(value, str) else value).hexdigest()


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def read_json(path: Path, default=None):
    if not path.is_file():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()] if path.is_file() else []


def safe_path(root: Path, relative: str, *, area: str | None = None) -> Path:
    root = root.resolve()
    raw = Path(relative)
    if raw.is_absolute() or '..' in raw.parts or '\\' in relative:
        raise ValueError('Unsafe repository-relative path')
    path = root / raw
    if any((root / Path(*raw.parts[:i])).is_symlink() for i in range(1, len(raw.parts) + 1)):
        raise ValueError('Symbolic links are not accepted for Brain inputs')
    if not path.resolve().is_relative_to(root):
        raise ValueError('Path escapes repository')
    if area and not path.resolve().is_relative_to((root / area).resolve()):
        raise ValueError('Path outside expected input area')
    return path


def parse_markdown(text: str) -> tuple[dict, str]:
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    meta = yaml.safe_load(match.group(1))
    if not isinstance(meta, dict):
        raise ValueError('Frontmatter must be an object')
    return meta, text[match.end():]


def sections(note_id: str, body: str) -> list[dict]:
    """Stable heading paths, including repeated headings; ignore fenced code."""
    result, stack, lines = [], [], []
    counts: dict[str, int] = {}
    fence = None

    def flush():
        text = ''.join(lines).strip()
        if not text:
            return
        path = [title for _, title in stack] or ['Preamble']
        label = '/'.join(path)
        counts[label] = counts.get(label, 0) + 1
        key = label + (f'/{counts[label]}' if counts[label] > 1 else '')
        result.append({'section_id': note_id + ':' + digest(key)[:16], 'heading': path[-1],
                       'heading_path': path, 'text': text, 'sha256': digest(text)})

    for line in body.splitlines(keepends=True):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append(line)
            continue
        heading = re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', line) if fence is None else None
        if heading:
            flush(); lines.clear()
            level = len(heading.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, heading.group(2)))
        else:
            lines.append(line)
    flush()
    return result


def prose_without_code(body: str) -> str:
    return re.sub(r'(?m)^\s{0,3}(`{3,}|~{3,})[^\n]*\n[\s\S]*?^\s{0,3}\1\s*$', '', body)
