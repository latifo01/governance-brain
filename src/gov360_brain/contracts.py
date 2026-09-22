from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol, runtime_checkable


@dataclass(frozen=True, slots=True)
class ProbeResult:
    adapter_id: str
    source_format: str
    mime_type: str
    confidence: float
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class SourceInventory:
    source_format: str
    source_kind: str
    unit_count: int
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class NormalizationContext:
    project_root: Path
    source_id: str
    source_sha256: str
    relative_source_path: str
    domain_slugs: tuple[str, ...]
    output_dir: Path
    max_markdown_chars: int = 40_000
    max_records_per_unit: int = 250
    full_markdown_max_rows: int = 50_000
    full_markdown_max_bytes: int = 25 * 1024 * 1024
    profile: str = "strict-local"


@dataclass(slots=True)
class NormalizedUnit:
    locator_kind: str
    locator: str
    filename: str
    markdown_body: str
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class NormalizationResult:
    adapter_id: str
    adapter_version: str
    source_format: str
    source_kind: str
    inventory: SourceInventory
    units: list[NormalizedUnit] = field(default_factory=list)
    overview_sections: dict[str, Any] = field(default_factory=dict)
    data_artifacts: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ValidationReport:
    valid: bool
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    metrics: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class SourceAdapter(Protocol):
    adapter_id: str
    adapter_version: str

    def probe(self, path: Path) -> ProbeResult | None: ...

    def inventory(self, path: Path, context: NormalizationContext | None = None) -> SourceInventory: ...

    def normalize(
        self, path: Path, context: NormalizationContext
    ) -> NormalizationResult: ...

    def validate(
        self, result: NormalizationResult, context: NormalizationContext
    ) -> ValidationReport: ...
