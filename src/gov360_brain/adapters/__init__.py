"""Read-only source adapters for deterministic Markdown normalization."""

from .base import (
    AdapterError,
    DependencyUnavailableError,
    QuarantinedSourceError,
    UnsafeSourceError,
    UnsupportedSourceError,
)
from .registry import AdapterRegistry, get_default_registry

__all__ = [
    "AdapterError",
    "AdapterRegistry",
    "DependencyUnavailableError",
    "QuarantinedSourceError",
    "UnsafeSourceError",
    "UnsupportedSourceError",
    "get_default_registry",
]
