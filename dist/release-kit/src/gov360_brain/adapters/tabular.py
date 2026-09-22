from __future__ import annotations

import csv
import json
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

from gov360_brain.contracts import NormalizationContext, NormalizationResult, ProbeResult, SourceInventory
from gov360_brain.utils import atomic_write_bytes

from .base import DependencyUnavailableError, QuarantinedSourceError, ValidatingAdapter, markdown_table, unit


class DelimitedTextAdapter(ValidatingAdapter):
    adapter_id = "delimited-text"
    supported_extensions = {".csv", ".tsv"}

    def probe(self, path: Path) -> ProbeResult | None:
        suffix = path.suffix.lower()
        if suffix not in self.supported_extensions:
            return None
        with path.open("rb") as stream:
            head = stream.read(8192)
        if b"\x00" in head and not head.startswith((b"\xff\xfe", b"\xfe\xff")):
            return None
        fmt = suffix.lstrip(".")
        mime = "text/tab-separated-values" if fmt == "tsv" else "text/csv"
        return ProbeResult(self.adapter_id, fmt, mime, 0.95)

    @staticmethod
    def _encoding(path: Path) -> tuple[str, list[str]]:
        with path.open("rb") as stream:
            sample = stream.read(131072)
        if sample.startswith((b"\xff\xfe", b"\xfe\xff")):
            return "utf-16", []
        try:
            sample.decode("utf-8-sig")
            return "utf-8-sig", []
        except UnicodeDecodeError:
            pass
        try:
            from charset_normalizer import from_bytes

            match = from_bytes(sample).best()
            if match is not None and match.encoding:
                warnings = ["encoding detection has low confidence"] if match.chaos > 0.20 else []
                return match.encoding, warnings
        except ImportError:
            pass
        return "windows-1252", ["encoding detection fell back to Windows-1252"]

    @contextmanager
    def _reader(self, path: Path, encoding: str, delimiter: str) -> Iterator[Any]:
        try:
            with path.open("r", encoding=encoding, errors="strict", newline="") as stream:
                yield csv.reader(stream, delimiter=delimiter, strict=True)
        except (UnicodeError, csv.Error) as exc:
            raise QuarantinedSourceError("invalid delimited record structure") from exc

    @staticmethod
    def _dialect(path: Path, encoding: str) -> tuple[str, list[str]]:
        warnings: list[str] = []
        with path.open("r", encoding=encoding, errors="strict", newline="") as stream:
            sample = stream.read(65536)
        if not sample.strip():
            raise QuarantinedSourceError("delimited source is empty")
        default = "\t" if path.suffix.lower() == ".tsv" else ","
        try:
            delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t|").delimiter
        except csv.Error:
            delimiter = default
            warnings.append("delimiter detection failed; used the extension default")
        return delimiter, warnings

    def _scan(self, path: Path) -> tuple[list[str], dict[str, Any], list[str], list[list[str]]]:
        encoding, warnings = self._encoding(path)
        delimiter, dialect_warnings = self._dialect(path, encoding)
        warnings.extend(dialect_warnings)
        record_count = irregular = 0
        samples: list[list[str]] = []
        with self._reader(path, encoding, delimiter) as reader:
            try:
                headers = list(next(reader))
            except StopIteration as exc:
                raise QuarantinedSourceError("delimited source contains no records") from exc
            if not headers:
                raise QuarantinedSourceError("delimited source has no header columns")
            for row in reader:
                record_count += 1
                irregular += int(len(row) != len(headers))
                if len(samples) < 25:
                    samples.append(list(row))
        if irregular:
            warnings.append(f"{irregular} records do not match the header width")
        return headers, {
            "encoding": encoding,
            "delimiter": delimiter,
            "header": headers,
            "column_count": len(headers),
            "record_count": record_count,
            "irregular_record_count": irregular,
        }, warnings, samples

    def inventory(self, path: Path, context: NormalizationContext | None = None) -> SourceInventory:
        _, metadata, warnings, _ = self._scan(path)
        return SourceInventory(path.suffix.lower().lstrip("."), "dataset", int(metadata["record_count"]), metadata, tuple(warnings))

    @staticmethod
    def _normalized_row(row: list[str], width: int) -> list[str]:
        values = row[:width] + [""] * max(0, width - len(row))
        if len(row) > width:
            values[-1] = values[-1] + " [extra fields: " + json.dumps(row[width:], ensure_ascii=False) + "]"
        return values

    @staticmethod
    def _write_parquet(path: Path, headers: list[str], rows: list[list[str]]) -> None:
        try:
            import pyarrow as pa
            import pyarrow.parquet as pq
        except ImportError as exc:
            raise DependencyUnavailableError("pyarrow is required for large dataset partitions") from exc
        names: list[str] = []
        used: set[str] = set()
        for index, header in enumerate(headers, 1):
            candidate = str(header or f"column_{index}")
            base = candidate
            suffix = 2
            while candidate in used:
                candidate = f"{base}_{suffix}"
                suffix += 1
            used.add(candidate)
            names.append(candidate)
        columns = [[row[index] if index < len(row) else "" for row in rows] for index in range(len(names))]
        table = pa.table({name: pa.array(values, type=pa.string()) for name, values in zip(names, columns, strict=True)})
        sink = pa.BufferOutputStream()
        pq.write_table(table, sink, compression="zstd")
        atomic_write_bytes(path, sink.getvalue().to_pybytes())

    @staticmethod
    def _large_units(headers: list[str], metadata: dict[str, Any], samples: list[list[str]]) -> list[Any]:
        schema_rows = [[index, header, "string (preserved, not inferred)"] for index, header in enumerate(headers, 1)]
        return [
            unit(locator_kind="row_range", locator="Schema", filename="schema.md", body="## Dataset schema\n\n" + markdown_table(["Position", "Column", "Ingest type"], schema_rows), metadata={"non_exhaustive": False, "extraction_mode": "native"}),
            unit(locator_kind="row_range", locator="Quality profile", filename="quality.md", body=("## Dataset quality\n\n" f"- Records scanned: {metadata['record_count']}\n" f"- Columns: {metadata['column_count']}\n" f"- Irregular-width records: {metadata['irregular_record_count']}\n" "- Value coercion: disabled"), metadata={"non_exhaustive": False, "extraction_mode": "aggregate"}),
            unit(locator_kind="row_range", locator="Dataset profile", filename="profile.md", body=("## Dataset profile\n\n" f"- Physical records: {metadata['record_count']}\n" f"- Columns: {metadata['column_count']}\n" "- Exact values remain in local Parquet partitions; no aggregate inference was performed."), metadata={"non_exhaustive": False, "extraction_mode": "aggregate"}),
            unit(locator_kind="row_range", locator="Sample rows 2-26", filename="sample.md", body=("## Non-exhaustive sample\n\n> This sample cannot support exhaustive or normative claims.\n\n" + markdown_table(headers, samples)), metadata={"non_exhaustive": True, "extraction_mode": "native"}),
        ]

    def normalize(self, path: Path, context: NormalizationContext) -> NormalizationResult:
        headers, metadata, warnings, samples = self._scan(path)
        source_format = path.suffix.lower().lstrip(".")
        large = int(metadata["record_count"]) > context.full_markdown_max_rows or path.stat().st_size > context.full_markdown_max_bytes
        units: list[Any] = []
        artifacts: list[dict[str, Any]] = []
        encoding = str(metadata["encoding"])
        delimiter = str(metadata["delimiter"])
        if large:
            data_dir = context.output_dir / "data"
            data_dir.mkdir(parents=True, exist_ok=True)
            partition: list[list[str]] = []
            partition_number = 0
            first_record = 1
            with self._reader(path, encoding, delimiter) as reader:
                next(reader)
                for row in reader:
                    partition.append(self._normalized_row(list(row), len(headers)))
                    if len(partition) >= 50_000:
                        partition_number += 1
                        filename = f"part-{partition_number:05d}.parquet"
                        self._write_parquet(data_dir / filename, headers, partition)
                        artifacts.append({"artifact_type": "parquet_partition", "relative_path": f"data/{filename}", "row_start": first_record, "row_count": len(partition)})
                        first_record += len(partition)
                        partition = []
            if partition or partition_number == 0:
                partition_number += 1
                filename = f"part-{partition_number:05d}.parquet"
                self._write_parquet(data_dir / filename, headers, partition)
                artifacts.append({"artifact_type": "parquet_partition", "relative_path": f"data/{filename}", "row_start": first_record, "row_count": len(partition)})
            units = self._large_units(headers, metadata, samples)
            warnings.append("large dataset stored in local Parquet partitions; Markdown rows are explicitly non-exhaustive")
        else:
            batch: list[list[str]] = []
            first = 1
            with self._reader(path, encoding, delimiter) as reader:
                next(reader)
                for logical_record, row in enumerate(reader, 1):
                    batch.append(list(row))
                    if len(batch) >= context.max_records_per_unit:
                        last = logical_record
                        units.append(unit(locator_kind="row_range", locator=f"Rows {first + 1}-{last + 1}", filename=f"rows-{first + 1:06d}-{last + 1:06d}.md", body=f"## Rows {first + 1}-{last + 1}\n\n{markdown_table(headers, batch)}", metadata={"record_count": len(batch), "extraction_mode": "native"}))
                        first, batch = logical_record + 1, []
                if batch or not units:
                    last = first + len(batch) - 1
                    locator = "Header row 1" if not batch else f"Rows {first + 1}-{last + 1}"
                    units.append(unit(locator_kind="row_range", locator=locator, filename="rows-000001-000001.md" if not batch else f"rows-{first + 1:06d}-{last + 1:06d}.md", body=f"## {locator}\n\n{markdown_table(headers, batch)}", metadata={"record_count": len(batch), "extraction_mode": "native"}))
        inventory = SourceInventory(source_format, "dataset", int(metadata["record_count"]), {**metadata, "large_dataset": large}, tuple(warnings))
        return NormalizationResult(self.adapter_id, self.adapter_version, source_format, "dataset", inventory, units, data_artifacts=artifacts, warnings=warnings, metrics={"record_count": metadata["record_count"], "column_count": len(headers), "unit_count": len(units), "partition_count": len(artifacts)})
