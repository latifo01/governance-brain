from __future__ import annotations

import importlib.metadata
import zipfile
from collections.abc import Iterable
from pathlib import Path

from gov360_brain.contracts import ProbeResult, SourceAdapter

from .base import (
    AdapterError,
    QuarantinedSourceError,
    UnsafeSourceError,
    UnsupportedSourceError,
)


EXECUTABLE_EXTENSIONS = {
    ".bat",
    ".cmd",
    ".com",
    ".dll",
    ".exe",
    ".js",
    ".msi",
    ".ps1",
    ".scr",
    ".sh",
    ".vbs",
}
ARCHIVE_EXTENSIONS = {".7z", ".gz", ".rar", ".tar", ".tgz", ".zip"}
EXECUTABLE_MAGICS = (b"MZ", b"\x7fELF", b"\xfe\xed\xfa", b"\xcf\xfa\xed\xfe")
ARCHIVE_MAGICS = (b"Rar!\x1a\x07", b"7z\xbc\xaf\x27\x1c", b"\x1f\x8b")


def _validate_candidate(path: Path) -> None:
    if not path.exists() or not path.is_file():
        raise UnsupportedSourceError("source is not a regular file")
    if path.is_symlink():
        raise UnsafeSourceError("symbolic-link sources are not accepted")
    suffix = path.suffix.lower()
    if suffix in EXECUTABLE_EXTENSIONS:
        raise UnsafeSourceError("executable or script sources are not accepted")
    with path.open("rb") as stream:
        head = stream.read(16)
    if head.startswith(EXECUTABLE_MAGICS):
        raise UnsafeSourceError("executable signature detected")
    if suffix in ARCHIVE_EXTENSIONS or head.startswith(ARCHIVE_MAGICS):
        raise UnsafeSourceError("standalone archives are not opened automatically")


def validate_safe_zip(path: Path) -> None:
    """Apply conservative zip-bomb checks to OOXML/ODF packages."""

    try:
        with zipfile.ZipFile(path) as package:
            entries = package.infolist()
            if len(entries) > 25_000:
                raise QuarantinedSourceError("document package contains too many entries")
            total_compressed = sum(max(item.compress_size, 1) for item in entries)
            total_uncompressed = sum(item.file_size for item in entries)
            if total_uncompressed > 2 * 1024 * 1024 * 1024:
                raise QuarantinedSourceError("document package expands beyond the safety limit")
            if total_uncompressed > 100 * 1024 * 1024 and total_uncompressed / total_compressed > 200:
                raise QuarantinedSourceError("suspicious document package compression ratio")
            for item in entries:
                normalized = item.filename.replace("\\", "/")
                parts = normalized.split("/")
                if normalized.startswith("/") or ".." in parts:
                    raise QuarantinedSourceError("document package contains an unsafe path")
    except zipfile.BadZipFile as exc:
        raise QuarantinedSourceError("invalid document package") from exc


class AdapterRegistry:
    def __init__(self, adapters: Iterable[SourceAdapter] = ()) -> None:
        self._adapters: list[SourceAdapter] = []
        for adapter in adapters:
            self.register(adapter)

    @property
    def adapters(self) -> tuple[SourceAdapter, ...]:
        return tuple(self._adapters)

    def register(self, adapter: SourceAdapter) -> None:
        if any(item.adapter_id == adapter.adapter_id for item in self._adapters):
            raise ValueError(f"adapter already registered: {adapter.adapter_id}")
        self._adapters.append(adapter)

    def discover_entry_points(self, group: str = "gov360_brain.adapters") -> None:
        """Load explicit local extensions without coupling them to the orchestrator."""

        for entry_point in importlib.metadata.entry_points().select(group=group):
            loaded = entry_point.load()
            adapter = loaded() if isinstance(loaded, type) else loaded
            self.register(adapter)

    def probe(self, path: Path) -> tuple[SourceAdapter, ProbeResult]:
        path = Path(path)
        _validate_candidate(path)
        matches: list[tuple[float, int, SourceAdapter, ProbeResult]] = []
        failures: list[AdapterError] = []
        for position, adapter in enumerate(self._adapters):
            try:
                result = adapter.probe(path)
            except AdapterError as exc:
                failures.append(exc)
                continue
            if result is not None:
                matches.append((result.confidence, -position, adapter, result))
        if not matches:
            if failures:
                raise failures[0]
            raise UnsupportedSourceError("no adapter recognized the source signature")
        _, _, adapter, result = max(matches, key=lambda item: (item[0], item[1]))
        return adapter, result

    def select(self, path: Path) -> SourceAdapter:
        return self.probe(path)[0]


def get_default_registry() -> AdapterRegistry:
    # Imports remain local so optional document libraries are only needed when
    # their formats are actually normalized.
    from .image import RasterImageAdapter
    from .office import (
        LegacyOfficeAdapter,
        OpenDocumentAdapter,
        PresentationAdapter,
        SpreadsheetAdapter,
        WordProcessingAdapter,
    )
    from .pdf import PdfAdapter
    from .structured import StructuredDataAdapter
    from .tabular import DelimitedTextAdapter
    from .text import TextDocumentAdapter

    registry = AdapterRegistry(
        [
            PdfAdapter(),
            WordProcessingAdapter(),
            PresentationAdapter(),
            SpreadsheetAdapter(),
            OpenDocumentAdapter(),
            LegacyOfficeAdapter(),
            RasterImageAdapter(),
            StructuredDataAdapter(),
            DelimitedTextAdapter(),
            TextDocumentAdapter(),
        ]
    )
    registry.discover_entry_points()
    return registry
