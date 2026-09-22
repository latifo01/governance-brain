from __future__ import annotations

import json
import re
from abc import ABC
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

from gov360_brain.contracts import (
    NormalizationContext,
    NormalizationResult,
    NormalizedUnit,
    ValidationReport,
)
from gov360_brain.utils import escape_markdown_cell, slugify


VISUAL_REVIEW_STATES = {
    "NONE",
    "DECORATIVE",
    "REVIEW_REQUIRED",
    "REVIEWED",
    "UNREADABLE",
}
LOCATOR_KINDS = {
    "page",
    "section",
    "slide",
    "sheet_range",
    "row_range",
    "json_path",
    "xml_path",
    "line_range",
    "image_region",
}
EXTRACTION_MODES = {"native", "rendered", "ocr", "hybrid", "aggregate"}


class AdapterError(RuntimeError):
    """Base error whose message is safe to include in a sanitized run receipt."""

    error_code = "ADAPTER_ERROR"

    def __init__(self, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.details = details or {}


class UnsupportedSourceError(AdapterError):
    error_code = "UNSUPPORTED_SOURCE"


class UnsafeSourceError(AdapterError):
    error_code = "UNSAFE_SOURCE"


class DependencyUnavailableError(AdapterError):
    error_code = "DEPENDENCY_UNAVAILABLE"


class QuarantinedSourceError(AdapterError):
    error_code = "SOURCE_QUARANTINED"


def neutralize_untrusted_text(value: Any) -> str:
    """Represent source-controlled text as a Markdown quotation, never as markup."""

    text = "" if value is None else str(value)
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    if not text:
        return ">"
    escaped: list[str] = []
    for line in text.split("\n"):
        # Quoting establishes a clear data boundary. Escaping backslashes and HTML
        # delimiters also keeps source strings from becoming active Markdown/HTML.
        line = line.replace("\\", "\\\\").replace("<", "&lt;").replace(">", "&gt;")
        escaped.append(f"> {line}")
    return "\n".join(escaped)


def fenced_json_data(value: Any) -> str:
    """Render structured source data without allowing embedded Markdown fences."""

    return neutralize_untrusted_text(json.dumps(value, ensure_ascii=False, indent=2))


def markdown_table(headers: Sequence[Any], rows: Iterable[Sequence[Any]]) -> str:
    safe_headers = [escape_markdown_cell(item) or f"Column {index}" for index, item in enumerate(headers, 1)]
    materialized = [list(row) for row in rows]
    if not safe_headers:
        return ""
    if len(safe_headers) <= 20:
        lines = [
            "| " + " | ".join(safe_headers) + " |",
            "| " + " | ".join("---" for _ in safe_headers) + " |",
        ]
        for row in materialized:
            padded = list(row[: len(safe_headers)]) + [""] * max(0, len(safe_headers) - len(row))
            lines.append("| " + " | ".join(escape_markdown_cell(item) for item in padded) + " |")
        return "\n".join(lines)

    # Very wide records are easier for a model to consume as explicit fields.
    blocks: list[str] = []
    for row_number, row in enumerate(materialized, 1):
        blocks.append(f"### Record {row_number}")
        padded = list(row[: len(safe_headers)]) + [""] * max(0, len(safe_headers) - len(row))
        for header, value in zip(safe_headers, padded, strict=True):
            blocks.append(f"- **{header}:** {escape_markdown_cell(value)}")
    return "\n".join(blocks)


def normalized_filename(prefix: str, number: int, locator: str) -> str:
    label = slugify(locator)[:60]
    return f"{prefix}-{number:04d}-{label}.md"


def safe_xml_tag(tag: str) -> str:
    return re.sub(r"^\{[^}]+\}", "", tag)


class ValidatingAdapter(ABC):
    adapter_id: str
    adapter_version = "1.1.0"
    heavy = False
    capabilities: dict[str, Any] = {
        "air_gap": True,
        "native_text": True,
        "rendering": False,
        "ocr": False,
        "tables": False,
        "charts": False,
    }

    def validate(
        self, result: NormalizationResult, context: NormalizationContext
    ) -> ValidationReport:
        errors: list[str] = []
        warnings = list(result.warnings)
        if result.adapter_id != self.adapter_id:
            errors.append("adapter_id does not match the validating adapter")
        if not result.source_format:
            errors.append("source_format is missing")
        if result.inventory.source_format != result.source_format:
            errors.append("inventory source_format does not match the normalization result")
        if not result.units:
            errors.append("normalization produced no units")

        filenames: set[str] = set()
        locators: set[tuple[str, str]] = set()
        total_chars = 0
        for unit in result.units:
            if not unit.filename or Path(unit.filename).name != unit.filename:
                errors.append("unit filename must be a plain relative filename")
            elif unit.filename in filenames:
                errors.append(f"duplicate unit filename: {unit.filename}")
            filenames.add(unit.filename)

            key = (unit.locator_kind, unit.locator)
            if not unit.locator_kind or not unit.locator:
                errors.append(f"unit {unit.filename or '<unnamed>'} has no stable locator")
            elif unit.locator_kind not in LOCATOR_KINDS:
                errors.append(f"unit {unit.filename} has an unsupported locator_kind")
            elif key in locators:
                errors.append(f"duplicate unit locator: {unit.locator}")
            locators.add(key)

            if "\x00" in unit.markdown_body:
                errors.append(f"unit {unit.filename} contains a NUL byte")
            if not unit.markdown_body.strip():
                errors.append(f"unit {unit.filename} has an empty Markdown body")
            total_chars += len(unit.markdown_body)

            visual_state = unit.metadata.get("visual_review", "NONE")
            if visual_state not in VISUAL_REVIEW_STATES:
                errors.append(f"unit {unit.filename} has an invalid visual_review state")
            extraction_mode = unit.metadata.get("extraction_mode", "native")
            if extraction_mode not in EXTRACTION_MODES:
                errors.append(f"unit {unit.filename} has an invalid extraction_mode")
            if len(unit.markdown_body) > context.max_markdown_chars:
                warnings.append(
                    f"{unit.filename} exceeds max_markdown_chars because its native unit was not split"
                )

        if any(not isinstance(item, dict) for item in result.data_artifacts):
            errors.append("data_artifacts must contain JSON-serializable descriptor objects")
        else:
            try:
                json.dumps(result.data_artifacts, ensure_ascii=False, sort_keys=True)
            except (TypeError, ValueError):
                errors.append("data_artifacts contains a non-JSON-serializable value")

        return ValidationReport(
            valid=not errors,
            errors=tuple(errors),
            warnings=tuple(dict.fromkeys(warnings)),
            metrics={
                "normalized_unit_count": len(result.units),
                "native_unit_count": result.inventory.unit_count,
                "markdown_chars": total_chars,
            },
        )


def unit(
    *,
    locator_kind: str,
    locator: str,
    filename: str,
    body: str,
    visual_review: str = "NONE",
    metadata: dict[str, Any] | None = None,
    warnings: list[str] | None = None,
) -> NormalizedUnit:
    values = dict(metadata or {})
    values["visual_review"] = visual_review
    return NormalizedUnit(
        locator_kind=locator_kind,
        locator=locator,
        filename=filename,
        markdown_body=body.rstrip() + "\n",
        metadata=values,
        warnings=list(warnings or []),
    )
