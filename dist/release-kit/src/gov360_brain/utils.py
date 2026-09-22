from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Iterable


TEMP_SUFFIXES = {".tmp", ".part", ".crdownload", ".download", ".lock"}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def atomic_write_bytes(path: Path, content: bytes) -> None:
    """Atomically replace a generated binary artifact on the same volume."""

    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = canonical_json(value) + "\n"
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(line)
        stream.flush()
        os.fsync(stream.fileno())


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as stream:
        for number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{number}: {exc}") from exc
            if not isinstance(item, dict):
                raise ValueError(f"JSONL object expected at {path}:{number}")
            rows.append(item)
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    ordered = "".join(canonical_json(row) + "\n" for row in rows)
    atomic_write_text(path, ordered)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "item"


def safe_filename(value: str, suffix: str = "") -> str:
    name = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", "-", value).strip(" .")
    name = re.sub(r"\s+", " ", name)
    return (name[:180] or "untitled") + suffix


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def frontmatter(fields: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, (list, tuple)):
            if value:
                lines.append(f"{key}:")
                lines.extend(f"  - {yaml_scalar(item)}" for item in value)
            else:
                lines.append(f"{key}: []")
        elif isinstance(value, dict):
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False, sort_keys=True)}")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def escape_markdown_cell(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")
    if text.startswith(("=", "+", "-", "@")):
        text = "`" + text.replace("`", "\\`") + "`"
    return text


def ensure_within(root: Path, candidate: Path) -> Path:
    resolved_root = root.resolve()
    resolved_candidate = candidate.resolve()
    if resolved_candidate != resolved_root and resolved_root not in resolved_candidate.parents:
        raise ValueError(f"Path escapes project root: {candidate}")
    return resolved_candidate
