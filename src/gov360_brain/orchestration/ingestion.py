from __future__ import annotations

import json
import os
import shutil
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from ..contracts import NormalizationContext, NormalizationResult
from ..domains import DomainPack
from ..project import ProjectPaths
from ..utils import atomic_write_json, atomic_write_text, canonical_json, frontmatter, sha256_file, sha256_text
from .state import RunJournal, SourceCatalog, _safe_error


class IngestionOrchestrator:
    def __init__(self, paths: ProjectPaths, registry: Any, *, light_workers: int = 2):
        self.paths = paths
        self.registry = registry
        self.light_workers = max(1, light_workers)
        self._heavy = threading.Semaphore(1)

    def inventory(self, pack: DomainPack, journal: RunJournal | None = None) -> list[dict[str, Any]]:
        records = SourceCatalog(self.paths).discover(pack, self.registry)
        if journal:
            journal.event("inventory_completed", source_count=len(records))
        return records

    def ingest(
        self,
        pack: DomainPack,
        records: list[dict[str, Any]],
        *,
        profile: str,
        journal: RunJournal | None = None,
        changed_only: bool = True,
    ) -> list[dict[str, Any]]:
        eligible = [row for row in records if row.get("status") not in {"QUARANTINED", "RETIRED", "SUPERSEDED"}]
        results: list[dict[str, Any]] = []
        manifest_updates: dict[str, dict[str, Any]] = {}
        with ThreadPoolExecutor(max_workers=self.light_workers, thread_name_prefix="gov360-ingest") as pool:
            futures = {
                pool.submit(self._normalize_one, pack, row, profile, changed_only): row
                for row in eligible
            }
            for future in as_completed(futures):
                row = futures[future]
                try:
                    receipt = future.result()
                except Exception as exc:
                    receipt = {
                        "source_id": row["source_id"],
                        "stage": "normalize",
                        "status": "FAILED",
                        "error": _safe_error(exc),
                    }
                    manifest_updates[str(row["source_id"])] = {"status": "FAILED", "error": receipt["error"]}
                else:
                    update = receipt.pop("_manifest_update", None)
                    if update:
                        manifest_updates[str(row["source_id"])] = update
                results.append(receipt)
                if journal:
                    journal.receipt(
                        f"normalize-{row['source_id'].lower()}",
                        {
                            "idempotency_key": sha256_text(
                                f"NORMALIZE:{row['source_id']}:{row['source_sha256']}"
                            ),
                            "stage": "NORMALIZE",
                            "status": "FAILED" if receipt["status"] == "FAILED" else "SUCCEEDED",
                            "source_id": row["source_id"],
                            "input_sha256": row["source_sha256"],
                            "output_sha256": sha256_text(canonical_json(receipt)),
                            "result": receipt,
                            "warnings": [],
                        },
                    )
                    journal.event("source_normalized", source_id=row["source_id"], status=receipt["status"])
        if manifest_updates:
            SourceCatalog(self.paths).apply_updates(manifest_updates)
        return sorted(results, key=lambda item: str(item.get("source_id")))

    def _normalize_one(
        self,
        pack: DomainPack,
        row: dict[str, Any],
        profile: str,
        changed_only: bool,
    ) -> dict[str, Any]:
        source_id = str(row["source_id"])
        digest = str(row["source_sha256"])
        relative_paths = [str(item) for item in row.get("relative_paths", [])]
        if not relative_paths:
            raise ValueError("Manifest record has no source path")
        source_path = self.paths.root / relative_paths[0]
        final_dir = self.paths.ingest / source_id
        existing = self._read_document(final_dir)
        adapter = self.registry.select(source_path)
        adapter_version = str(getattr(adapter, "adapter_version", "unknown"))
        if (
            changed_only
            and existing
            and existing.get("source_sha256") == digest
            and existing.get("adapter_id") == getattr(adapter, "adapter_id", None)
            and existing.get("adapter_version") == adapter_version
            and existing.get("validation", {}).get("valid") is True
        ):
            return {"source_id": source_id, "stage": "normalize", "status": "NOOP", "unit_count": len(existing.get("units", []))}

        temp_dir = Path(tempfile.mkdtemp(prefix=f".{source_id}-", dir=self.paths.ingest))
        context = NormalizationContext(
            project_root=self.paths.root,
            source_id=source_id,
            source_sha256=digest,
            relative_source_path=relative_paths[0],
            domain_slugs=tuple(sorted({pack.slug})),
            output_dir=temp_dir,
            profile=profile,
        )
        try:
            lock = self._heavy if bool(getattr(adapter, "heavy", False)) else _NullContext()
            with lock:
                result = adapter.normalize(source_path, context)
            if sha256_file(source_path) != digest:
                raise RuntimeError("immutable source changed during normalization")
            report = adapter.validate(result, context)
            if not report.valid:
                raise ValueError("Adapter validation failed: " + "; ".join(report.errors[:5]))
            document = self._write_result(temp_dir, row, context, result, report)
            self._validate_directory(temp_dir, document)
            self._replace_directory(temp_dir, final_dir)
        except BaseException:
            shutil.rmtree(temp_dir, ignore_errors=True)
            raise
        return {
            "source_id": source_id,
            "stage": "normalize",
            "status": "NORMALIZED",
            "unit_count": len(result.units),
            "_manifest_update": {
                "status": "READY_FOR_LLM",
                "adapter_id": result.adapter_id,
                "adapter_version": result.adapter_version,
                "source_format": result.source_format,
                "unit_count": len(result.units),
                "error": None,
            },
        }

    def _write_result(self, output: Path, row: dict[str, Any], context: NormalizationContext, result: NormalizationResult, report: Any) -> dict[str, Any]:
        units_dir = output / "units"
        units_dir.mkdir(parents=True, exist_ok=True)
        unit_records: list[dict[str, Any]] = []
        for index, unit in enumerate(result.units, start=1):
            body = unit.markdown_body.rstrip() + "\n"
            content_digest = sha256_text(body)
            fields = {
                "type": "ingested_unit",
                "schema_version": 1,
                "source_id": context.source_id,
                "source_sha256": context.source_sha256,
                "source_format": result.source_format,
                "adapter_id": result.adapter_id,
                "adapter_version": result.adapter_version,
                "locator_kind": unit.locator_kind,
                "locator": unit.locator,
                "content_sha256": content_digest,
                "extraction_mode": unit.metadata.get("extraction_mode", "native"),
                "visual_review": unit.metadata.get("visual_review", "NONE"),
                "warnings": unit.warnings,
            }
            for optional in ("record_count", "non_exhaustive", "query_sha256"):
                if optional in unit.metadata:
                    fields[optional] = unit.metadata[optional]
            filename = Path(unit.filename).name
            if not filename.lower().endswith(".md"):
                filename += ".md"
            path = units_dir / filename
            if path.exists():
                raise ValueError(f"Duplicate normalized unit filename: {filename}")
            atomic_write_text(path, frontmatter(fields) + body)
            unit_record = {
                "index": index,
                "filename": f"units/{filename}",
                "locator_kind": unit.locator_kind,
                "locator": unit.locator,
                "content_sha256": content_digest,
                "file_sha256": sha256_file(path),
                "visual_review": fields["visual_review"],
                "warnings": list(unit.warnings),
            }
            for optional in ("record_count", "non_exhaustive", "query_sha256"):
                if optional in unit.metadata:
                    unit_record[optional] = unit.metadata[optional]
            unit_records.append(unit_record)

        overview = [
            f"# {context.source_id}",
            "",
            f"- Format: `{result.source_format}`",
            f"- Adapter: `{result.adapter_id}@{result.adapter_version}`",
            f"- Units: {len(unit_records)}",
            f"- Validation: `VALID`",
            "",
            "## Unit index",
            "",
        ]
        overview.extend(f"- [{item['locator']}]({item['filename']})" for item in unit_records)
        atomic_write_text(output / "overview.md", "\n".join(overview) + "\n")
        document = {
            "schema_version": 1,
            "source_id": context.source_id,
            "source_sha256": context.source_sha256,
            "relative_source_paths": sorted(str(item) for item in row.get("relative_paths", [])),
            "domains": sorted(str(item) for item in row.get("domains", [])),
            "source_format": result.source_format,
            "source_kind": result.source_kind,
            "adapter_id": result.adapter_id,
            "adapter_version": result.adapter_version,
            "inventory": {
                "unit_count": len(unit_records),
                "native_unit_count": result.inventory.unit_count,
                "normalized_unit_count": len(unit_records),
                "metadata": result.inventory.metadata,
                "warnings": list(result.inventory.warnings),
            },
            "units": unit_records,
            "data_artifacts": [
                *result.data_artifacts,
                *self._inventory_data(output / "data"),
            ],
            "metrics": result.metrics,
            "warnings": list(result.warnings),
            "validation": {
                "valid": True,
                "warnings": list(report.warnings),
                "metrics": report.metrics,
            },
        }
        atomic_write_json(output / "document.json", document)
        return document

    @staticmethod
    def _inventory_data(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [
            {"filename": item.relative_to(path.parent).as_posix(), "sha256": sha256_file(item), "size": item.stat().st_size}
            for item in sorted(path.rglob("*")) if item.is_file()
        ]

    @staticmethod
    def _read_document(directory: Path) -> dict[str, Any] | None:
        path = directory / "document.json"
        if not path.exists():
            return None
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            return value if isinstance(value, dict) else None
        except (OSError, json.JSONDecodeError):
            return None

    @staticmethod
    def _validate_directory(directory: Path, document: dict[str, Any]) -> None:
        if document.get("validation", {}).get("valid") is not True:
            raise ValueError("Normalized document is not valid")
        units = document.get("units", [])
        if len(units) != document.get("inventory", {}).get("normalized_unit_count"):
            raise ValueError("Normalized unit count does not match inventory")
        for unit in units:
            path = directory / unit["filename"]
            if not path.is_file() or sha256_file(path) != unit["file_sha256"]:
                raise ValueError(f"Normalized unit checksum mismatch: {unit.get('filename')}")

    def validate_existing(self, source_ids: set[str] | None = None) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for directory in sorted(self.paths.ingest.glob("SRC-*")):
            if source_ids and directory.name not in source_ids:
                continue
            try:
                document = self._read_document(directory)
                if document is None:
                    raise ValueError("Missing or invalid document.json")
                self._validate_directory(directory, document)
                results.append({"source_id": directory.name, "valid": True, "unit_count": len(document.get("units", []))})
            except Exception as exc:
                results.append({"source_id": directory.name, "valid": False, "error": _safe_error(exc)})
        return results

    @staticmethod
    def _replace_directory(source: Path, destination: Path) -> None:
        backup = destination.with_name(f".{destination.name}.previous")
        if backup.exists():
            shutil.rmtree(backup)
        if destination.exists():
            os.replace(destination, backup)
        try:
            os.replace(source, destination)
        except BaseException:
            if backup.exists() and not destination.exists():
                os.replace(backup, destination)
            raise
        shutil.rmtree(backup, ignore_errors=True)


class _NullContext:
    def __enter__(self) -> None:
        return None

    def __exit__(self, *args: Any) -> None:
        return None
