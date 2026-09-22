from __future__ import annotations

import hashlib
import re
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable

from ..domains import DomainPack
from ..project import ProjectPaths
from ..utils import TEMP_SUFFIXES, append_jsonl, atomic_write_json, canonical_json, read_jsonl, sha256_file, write_jsonl


_SOURCE_ID = re.compile(r"^SRC-(\d{4,})$")
_NORMATIVITY = {"BINDING", "GUIDANCE", "STANDARD", "FRAMEWORK", "DATASET", "RESEARCH", "UNCLASSIFIED"}


def _source_kind(source_format: str) -> str:
    if source_format in {"csv", "tsv", "json", "jsonl"}:
        return "dataset"
    if source_format in {"xlsx", "xlsm", "xls", "ods"}:
        return "mixed"
    if source_format in {"png", "jpeg", "jpg", "tiff"}:
        return "image"
    if source_format in {"ppt", "pptx", "pptm", "odp"}:
        return "presentation"
    return "document"


def _utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _safe_error(exc: BaseException) -> dict[str, str]:
    """Return an operational error without source text or values."""
    # Exception messages from parsers often embed cell contents or document text.
    # Only the exception class crosses the operational logging boundary.
    return {"type": type(exc).__name__, "code": "OPERATION_FAILED"}


class SourceCatalog:
    def __init__(self, paths: ProjectPaths):
        self.paths = paths
        self.path = paths.state / "source_manifest.jsonl"

    def read(self) -> list[dict[str, Any]]:
        return read_jsonl(self.path)

    def discover(self, pack: DomainPack, registry: Any) -> list[dict[str, Any]]:
        existing = self.read()
        by_hash = {str(row.get("source_sha256")): row for row in existing if row.get("source_sha256")}
        path_to_row: dict[str, dict[str, Any]] = {}
        for row in existing:
            for rel in row.get("relative_paths", []):
                path_to_row[str(rel)] = row

        found: list[tuple[str, Path, str]] = []
        for root_value in (*pack.source_roots, "sources/_shared"):
            source_root = (self.paths.root / root_value).resolve()
            if not source_root.exists():
                continue
            if self.paths.sources.resolve() not in (source_root, *source_root.parents):
                raise ValueError(f"Source root escapes immutable sources tree: {root_value}")
            for path in sorted(source_root.rglob("*")):
                if not path.is_file() or path.is_symlink():
                    continue
                if (
                    path.name == ".ready"
                    or path.name.startswith("~$")
                    or path.name.endswith(":Zone.Identifier")
                    or path.suffix.lower() in TEMP_SUFFIXES
                ):
                    continue
                relative = path.relative_to(self.paths.root).as_posix()
                found.append((relative, path, sha256_file(path)))

        next_number = max(
            (int(match.group(1)) for row in existing if (match := _SOURCE_ID.fullmatch(str(row.get("source_id", ""))))),
            default=0,
        ) + 1
        touched: set[str] = set()
        for relative, path, digest in sorted(found):
            row = by_hash.get(digest)
            if row is None:
                probe = None
                error = None
                try:
                    adapter = registry.select(path)
                    probe = adapter.probe(path)
                except Exception as exc:  # adapter discovery must quarantine, not abort inventory
                    adapter = None
                    error = _safe_error(exc)
                row = {
                    "schema_version": 1,
                    "source_id": f"SRC-{next_number:04d}",
                    "source_sha256": digest,
                    "relative_paths": [relative],
                    "domains": [pack.domain_id],
                    "primary_domain": pack.domain_id,
                    "status": "DISCOVERED" if adapter is not None else "QUARANTINED",
                    "source_format": getattr(probe, "source_format", path.suffix.lower().lstrip(".")),
                    "source_kind": _source_kind(getattr(probe, "source_format", path.suffix.lower().lstrip("."))),
                    "adapter_id": getattr(adapter, "adapter_id", None),
                    "discovered_at": _utc_now(),
                    "warnings": list(getattr(probe, "warnings", ()) if probe else ()),
                }
                if error:
                    row["error"] = error
                existing.append(row)
                by_hash[digest] = row
                next_number += 1
            else:
                paths = set(str(item) for item in row.get("relative_paths", []))
                paths.add(relative)
                row["relative_paths"] = sorted(paths)
                domains = set(str(item) for item in row.get("domains", []))
                domains.add(pack.domain_id)
                row["domains"] = sorted(domains)
            previous = path_to_row.get(relative)
            if previous and previous.get("source_sha256") != digest and previous.get("status") != "RETIRED":
                previous["status"] = "SUPERSEDED"
                previous["superseded_by"] = row["source_id"]
                row["supersedes"] = previous["source_id"]
            touched.add(str(row["source_id"]))

        rows = sorted(existing, key=lambda item: str(item.get("source_id", "")))
        write_jsonl(self.path, rows)
        return [row for row in rows if row.get("source_id") in touched]

    def update(self, source_id: str, **changes: Any) -> dict[str, Any]:
        rows = self.read()
        for row in rows:
            if row.get("source_id") == source_id:
                row.update(changes)
                write_jsonl(self.path, sorted(rows, key=lambda item: str(item.get("source_id", ""))))
                return row
        raise KeyError(source_id)

    def classify(self, source_id: str, *, normativity: str, reviewer: str) -> dict[str, Any]:
        """Record an explicit CDO/source-authority classification.

        Classification changes the manifest view only; it never edits the
        immutable original or upgrades evidence status by itself.  A compact
        event is kept separately so the reviewer and decision remain auditable.
        """

        authority = str(normativity).upper().strip()
        reviewer = str(reviewer).strip()
        if authority not in _NORMATIVITY:
            raise ValueError(f"Unsupported source normativity: {authority}")
        if not reviewer:
            raise ValueError("A reviewer is required for source classification")
        rows = self.read()
        for row in rows:
            if str(row.get("source_id")) != str(source_id):
                continue
            if row.get("relative_paths"):
                path = self.paths.root / str(row["relative_paths"][0])
                if path.exists() and sha256_file(path) != row.get("source_sha256"):
                    raise ValueError("Cannot classify a source whose immutable hash changed")
            old = str(row.get("normativity", "UNCLASSIFIED"))
            row["normativity"] = authority
            write_jsonl(self.path, sorted(rows, key=lambda item: str(item.get("source_id", ""))))
            event = {
                "schema_version": 1,
                "event_id": "CLS-" + hashlib.sha256(f"{source_id}:{row.get('source_sha256')}:{authority}:{reviewer}".encode("utf-8")).hexdigest()[:20].upper(),
                "event": "SOURCE_CLASSIFIED",
                "source_id": str(source_id),
                "source_sha256": str(row.get("source_sha256")),
                "previous_normativity": old,
                "normativity": authority,
                "reviewer": reviewer,
                "at": _utc_now(),
            }
            event_path = self.paths.state / "source_classification_events.jsonl"
            if not any(item.get("event_id") == event["event_id"] for item in read_jsonl(event_path)):
                append_jsonl(event_path, event)
            return {**row, "classification_event_id": event["event_id"]}
        raise KeyError(source_id)

    def apply_updates(self, updates: dict[str, dict[str, Any]]) -> None:
        """Apply one main-thread batch so concurrent workers cannot lose rows."""
        rows = self.read()
        remaining = set(updates)
        for row in rows:
            source_id = str(row.get("source_id", ""))
            if source_id in updates:
                row.update(updates[source_id])
                remaining.discard(source_id)
        if remaining:
            raise KeyError(f"Unknown source IDs in manifest update: {', '.join(sorted(remaining))}")
        write_jsonl(self.path, sorted(rows, key=lambda item: str(item.get("source_id", ""))))


@dataclass(slots=True)
class RunJournal:
    paths: ProjectPaths
    run_id: str
    domain_id: str
    profile: str

    @classmethod
    def create(cls, paths: ProjectPaths, *, domain_id: str, profile: str) -> "RunJournal":
        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        run_id = f"{stamp}-{uuid.uuid4().hex[:8]}"
        journal = cls(paths, run_id, domain_id, profile)
        journal.run_dir.mkdir(parents=True, exist_ok=False)
        atomic_write_json(journal.run_dir / "run.json", {
            "schema_version": 1,
            "run_id": run_id,
            "domain_id": domain_id,
            "profile": profile,
            "status": "RUNNING",
            "started_at": _utc_now(),
        })
        journal.event("run_started")
        return journal

    @property
    def run_dir(self) -> Path:
        return self.paths.state / "runs" / self.run_id

    @property
    def receipts_dir(self) -> Path:
        return self.run_dir / "receipts"

    def event(self, event: str, **metadata: Any) -> None:
        safe = {
            key: value
            for key, value in metadata.items()
            if key not in {"content", "text", "prompt", "response", "raw_value"}
        }
        append_jsonl(self.run_dir / "events.jsonl", {
            "schema_version": 1,
            "run_id": self.run_id,
            "event": event,
            "at": _utc_now(),
            **safe,
        })

    def receipt(self, job_id: str, value: dict[str, Any]) -> Path:
        path = self.receipts_dir / f"{job_id}.json"
        payload = {"schema_version": 1, "run_id": self.run_id, "job_id": job_id, **value}
        if path.exists():
            if canonical_json(__import__("json").loads(path.read_text(encoding="utf-8"))) != canonical_json(payload):
                raise FileExistsError(f"Immutable receipt already exists: {job_id}")
            return path
        atomic_write_json(path, payload)
        return path

    def finish(self, status: str, **summary: Any) -> None:
        path = self.run_dir / "run.json"
        value = __import__("json").loads(path.read_text(encoding="utf-8"))
        value.update({"status": status, "finished_at": _utc_now(), **summary})
        atomic_write_json(path, value)
        self.event("run_finished", status=status, **summary)

    @staticmethod
    def latest(paths: ProjectPaths, domain_id: str | None = None) -> dict[str, Any] | None:
        candidates: list[dict[str, Any]] = []
        for path in sorted((paths.state / "runs").glob("*/run.json")):
            try:
                value = __import__("json").loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if domain_id is None or value.get("domain_id") == domain_id:
                candidates.append(value)
        return candidates[-1] if candidates else None


__all__ = ["RunJournal", "SourceCatalog", "_safe_error"]
