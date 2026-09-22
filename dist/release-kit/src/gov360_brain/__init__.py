"""Governance Brain ingestion and knowledge pipeline."""

from .contracts import (
    NormalizationContext,
    NormalizationResult,
    NormalizedUnit,
    ProbeResult,
    SourceAdapter,
    SourceInventory,
    ValidationReport,
)

__all__ = [
    "NormalizationContext",
    "NormalizationResult",
    "NormalizedUnit",
    "ProbeResult",
    "SourceAdapter",
    "SourceInventory",
    "ValidationReport",
]

__version__ = "0.1.0"

