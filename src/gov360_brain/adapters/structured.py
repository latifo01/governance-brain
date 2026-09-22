from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from gov360_brain.contracts import (
    NormalizationContext,
    NormalizationResult,
    ProbeResult,
    SourceInventory,
)

from .base import (
    DependencyUnavailableError,
    QuarantinedSourceError,
    ValidatingAdapter,
    fenced_json_data,
    neutralize_untrusted_text,
    safe_xml_tag,
    unit,
)
from .text import _decode_text
from gov360_brain.utils import atomic_write_bytes


def _json_pointer_segment(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


class StructuredDataAdapter(ValidatingAdapter):
    adapter_id = "structured-data"
    supported_extensions = {".json", ".jsonl", ".ndjson", ".xml"}

    def probe(self, path: Path) -> ProbeResult | None:
        suffix = path.suffix.lower()
        if suffix not in self.supported_extensions:
            return None
        with path.open("rb") as stream:
            head = stream.read(4096).lstrip(b"\xef\xbb\xbf\xff\xfe\x00 \t\r\n")
        source_format = "jsonl" if suffix == ".ndjson" else suffix.lstrip(".")
        if source_format == "xml" and not head.startswith(b"<"):
            return None
        if source_format in {"json", "jsonl"} and not head.startswith((b"{", b"[")):
            return None
        mime = "application/xml" if source_format == "xml" else "application/json"
        return ProbeResult(self.adapter_id, source_format, mime, 0.98)

    def _parse_json(self, path: Path) -> tuple[Any, str, list[str]]:
        text, encoding, warnings = _decode_text(path)
        try:
            return json.loads(text), encoding, warnings
        except json.JSONDecodeError as exc:
            raise QuarantinedSourceError(
                "invalid JSON structure", details={"line": exc.lineno, "column": exc.colno}
            ) from exc

    def _parse_jsonl(self, path: Path) -> tuple[list[Any], str, list[str]]:
        text, encoding, warnings = _decode_text(path)
        values: list[Any] = []
        for line_number, line in enumerate(text.splitlines(), 1):
            if not line.strip():
                continue
            try:
                values.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise QuarantinedSourceError(
                    "invalid JSONL record", details={"record": line_number, "column": exc.colno}
                ) from exc
        if not values:
            raise QuarantinedSourceError("JSONL source contains no records")
        return values, encoding, warnings

    @staticmethod
    def _write_jsonl_parquet(path: Path, records: list[Any]) -> None:
        try:
            import pyarrow as pa
            import pyarrow.parquet as pq
        except ImportError as exc:
            raise DependencyUnavailableError("pyarrow is required for large JSONL partitions") from exc
        encoded = [json.dumps(item, ensure_ascii=False, separators=(",", ":")) for item in records]
        sink = pa.BufferOutputStream()
        pq.write_table(pa.table({"record_json": pa.array(encoded, type=pa.string())}), sink, compression="zstd")
        atomic_write_bytes(path, sink.getvalue().to_pybytes())

    def _parse_xml(self, path: Path) -> tuple[ET.Element, str, list[str]]:
        raw = path.read_bytes()
        probe = raw[:131072].upper()
        if b"<!DOCTYPE" in probe or b"<!ENTITY" in probe:
            raise QuarantinedSourceError("XML declarations with entities or a DOCTYPE are not accepted")
        _, encoding, warnings = _decode_text(path)
        try:
            return ET.fromstring(raw), encoding, warnings
        except ET.ParseError as exc:
            raise QuarantinedSourceError("invalid XML structure") from exc

    def inventory(self, path: Path, context: NormalizationContext | None = None) -> SourceInventory:
        source_format = "jsonl" if path.suffix.lower() == ".ndjson" else path.suffix.lower().lstrip(".")
        if source_format == "json":
            value, encoding, warnings = self._parse_json(path)
            count = len(value) if isinstance(value, (list, dict)) else 1
        elif source_format == "jsonl":
            value, encoding, warnings = self._parse_jsonl(path)
            count = len(value)
        else:
            root, encoding, warnings = self._parse_xml(path)
            count = max(1, len(root))
        return SourceInventory(
            source_format=source_format,
            source_kind="dataset" if source_format in {"json", "jsonl"} else "document",
            unit_count=count,
            metadata={"encoding": encoding},
            warnings=tuple(warnings),
        )

    def normalize(self, path: Path, context: NormalizationContext) -> NormalizationResult:
        source_format = "jsonl" if path.suffix.lower() == ".ndjson" else path.suffix.lower().lstrip(".")
        units = []
        warnings: list[str]
        metadata: dict[str, Any]
        source_kind = "dataset" if source_format in {"json", "jsonl"} else "document"

        if source_format in {"json", "jsonl"}:
            if source_format == "jsonl":
                value, encoding, warnings = self._parse_jsonl(path)
                large_dataset = len(value) > context.full_markdown_max_rows or path.stat().st_size > context.full_markdown_max_bytes
                if large_dataset:
                    data_dir = context.output_dir / "data"
                    data_dir.mkdir(parents=True, exist_ok=True)
                    artifacts: list[dict[str, Any]] = []
                    sample = value[:25]
                    partition_size = 50_000
                    for offset in range(0, len(value), partition_size):
                        records = value[offset : offset + partition_size]
                        filename = f"part-{offset // partition_size + 1:05d}.parquet"
                        self._write_jsonl_parquet(data_dir / filename, records)
                        artifacts.append({"artifact_type": "parquet_partition", "relative_path": f"data/{filename}", "row_start": offset + 1, "row_count": len(records)})
                    units = [
                        unit(locator_kind="row_range", locator="Schema", filename="schema.md", body="## JSONL schema\n\n- Each Parquet record preserves one complete JSON object in `record_json`.\n- No type coercion was performed.", metadata={"extraction_mode": "native"}),
                        unit(locator_kind="row_range", locator="Quality profile", filename="quality.md", body=f"## JSONL quality\n\n- Records scanned: {len(value)}\n- Invalid records: 0\n- Value coercion: disabled", metadata={"extraction_mode": "aggregate"}),
                        unit(locator_kind="row_range", locator="Dataset profile", filename="profile.md", body=f"## JSONL profile\n\n- Physical records: {len(value)}\n- Local partitions: {len(artifacts)}", metadata={"extraction_mode": "aggregate"}),
                        unit(locator_kind="row_range", locator="Sample records 1-25", filename="sample.md", body="## Non-exhaustive sample\n\n> This sample cannot support exhaustive or normative claims.\n\n" + fenced_json_data(sample), metadata={"non_exhaustive": True, "extraction_mode": "native"}),
                    ]
                    warnings.append("large JSONL stored in local Parquet partitions; Markdown sample is non-exhaustive")
                    inventory = SourceInventory("jsonl", "dataset", len(value), {"encoding": encoding, "record_count": len(value), "large_dataset": True}, tuple(warnings))
                    return NormalizationResult(self.adapter_id, self.adapter_version, "jsonl", "dataset", inventory, units, data_artifacts=artifacts, warnings=warnings, metrics={"record_count": len(value), "unit_count": len(units), "partition_count": len(artifacts)})
                partitions = [
                    value[offset : offset + context.max_records_per_unit]
                    for offset in range(0, len(value), context.max_records_per_unit)
                ]
                for index, records in enumerate(partitions, 1):
                    first = (index - 1) * context.max_records_per_unit + 1
                    last = first + len(records) - 1
                    locator = f"Records {first}-{last}"
                    units.append(
                        unit(
                            locator_kind="row_range",
                            locator=locator,
                            filename=f"records-{first:06d}-{last:06d}.md",
                            body=f"## {locator}\n\n{fenced_json_data(records)}",
                            metadata={"record_start": first, "record_end": last, "encoding": encoding},
                        )
                    )
                native_count = len(value)
            else:
                value, encoding, warnings = self._parse_json(path)
                if isinstance(value, list):
                    partitions = [
                        value[offset : offset + context.max_records_per_unit]
                        for offset in range(0, len(value), context.max_records_per_unit)
                    ] or [[]]
                    for index, records in enumerate(partitions, 1):
                        first = (index - 1) * context.max_records_per_unit
                        last = first + len(records) - 1
                        locator = "/" if not records else f"/{first}-/{last}"
                        units.append(
                            unit(
                                locator_kind="json_path",
                                locator=locator,
                                filename=f"items-{first:06d}-{max(last, first):06d}.md",
                                body=f"## JSON items {first}-{last}\n\n{fenced_json_data(records)}",
                                metadata={"item_start": first, "item_end": last, "encoding": encoding},
                            )
                        )
                    native_count = len(value)
                elif isinstance(value, dict):
                    for index, (key, child) in enumerate(value.items(), 1):
                        locator = "/" + _json_pointer_segment(str(key))
                        units.append(
                            unit(
                                locator_kind="json_path",
                                locator=locator,
                                filename=f"key-{index:04d}.md",
                                body=f"## JSON pointer `{locator}`\n\n{fenced_json_data(child)}",
                                metadata={"encoding": encoding},
                            )
                        )
                    if not value:
                        units.append(
                            unit(
                                locator_kind="json_path",
                                locator="/",
                                filename="root-0001.md",
                                body="## JSON root\n\n> {}",
                                metadata={"encoding": encoding},
                            )
                        )
                    native_count = len(value)
                else:
                    units.append(
                        unit(
                            locator_kind="json_path",
                            locator="/",
                            filename="root-0001.md",
                            body=f"## JSON root\n\n{fenced_json_data(value)}",
                            metadata={"encoding": encoding},
                        )
                    )
                    native_count = 1
            metadata = {"encoding": encoding, "record_count": native_count}
        else:
            root, encoding, warnings = self._parse_xml(path)
            root_name = safe_xml_tag(root.tag)
            occurrences: dict[str, int] = {}
            children = list(root)
            if not children:
                children = [root]
            for index, child in enumerate(children, 1):
                name = safe_xml_tag(child.tag)
                occurrences[name] = occurrences.get(name, 0) + 1
                locator = f"/{root_name}" if child is root else f"/{root_name}/{name}[{occurrences[name]}]"
                serialized = ET.tostring(child, encoding="unicode")
                units.append(
                    unit(
                        locator_kind="xml_path",
                        locator=locator,
                        filename=f"xml-{index:04d}.md",
                        body=f"## XML path `{locator}`\n\n{neutralize_untrusted_text(serialized)}",
                        metadata={"encoding": encoding},
                    )
                )
            native_count = len(children)
            metadata = {"encoding": encoding, "root_element": root_name, "child_count": len(children)}

        inventory = SourceInventory(
            source_format=source_format,
            source_kind=source_kind,
            unit_count=native_count,
            metadata=metadata,
            warnings=tuple(warnings),
        )
        return NormalizationResult(
            adapter_id=self.adapter_id,
            adapter_version=self.adapter_version,
            source_format=source_format,
            source_kind=source_kind,
            inventory=inventory,
            units=units,
            overview_sections=metadata,
            data_artifacts=[
                {"artifact_type": "structured_profile", "locator": "/", "metadata": metadata}
            ],
            warnings=warnings,
            metrics={"native_unit_count": native_count, "unit_count": len(units)},
        )
