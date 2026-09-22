from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

from gov360_brain.contracts import (
    NormalizationContext,
    NormalizationResult,
    ProbeResult,
    SourceInventory,
)

from .base import QuarantinedSourceError, ValidatingAdapter, neutralize_untrusted_text, unit


class _VisibleHtmlParser(HTMLParser):
    BLOCK_TAGS = {
        "article",
        "blockquote",
        "br",
        "div",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "li",
        "main",
        "p",
        "section",
        "table",
        "td",
        "th",
        "tr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "template", "noscript"}:
            self._ignored_depth += 1
        elif not self._ignored_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "template", "noscript"} and self._ignored_depth:
            self._ignored_depth -= 1
        elif not self._ignored_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._ignored_depth:
            self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts)
        lines = [re.sub(r"\s+", " ", line).strip() for line in raw.splitlines()]
        return "\n".join(line for line in lines if line)


def _decode_text(path: Path) -> tuple[str, str, list[str]]:
    raw = path.read_bytes()
    if b"\x00" in raw[:8192] and not raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        raise QuarantinedSourceError("binary data found in a text source")
    warnings: list[str] = []
    for encoding in ("utf-8-sig", "utf-16"):
        try:
            return raw.decode(encoding), encoding, warnings
        except UnicodeDecodeError:
            pass
    try:
        from charset_normalizer import from_bytes

        match = from_bytes(raw).best()
        if match is not None:
            encoding = match.encoding or "utf-8"
            if match.chaos > 0.20:
                warnings.append("encoding detection has low confidence")
            return str(match), encoding, warnings
    except ImportError:
        warnings.append("charset-normalizer is unavailable; used Windows-1252 fallback")
    return raw.decode("windows-1252"), "windows-1252", warnings


class TextDocumentAdapter(ValidatingAdapter):
    adapter_id = "text"
    supported_extensions = {".html", ".htm", ".md", ".txt"}

    def probe(self, path: Path) -> ProbeResult | None:
        suffix = path.suffix.lower()
        if suffix not in self.supported_extensions:
            return None
        with path.open("rb") as stream:
            head = stream.read(4096)
        if b"\x00" in head and not head.startswith((b"\xff\xfe", b"\xfe\xff")):
            return None
        source_format = "html" if suffix in {".html", ".htm"} else suffix.lstrip(".")
        mime = "text/html" if source_format == "html" else "text/plain"
        return ProbeResult(self.adapter_id, source_format, mime, 0.85)

    def _content(self, path: Path) -> tuple[str, str, str, list[str]]:
        text, encoding, warnings = _decode_text(path)
        source_format = "html" if path.suffix.lower() in {".html", ".htm"} else path.suffix.lower().lstrip(".")
        if source_format == "html":
            parser = _VisibleHtmlParser()
            parser.feed(text)
            text = parser.text()
        return text, encoding, source_format, warnings

    def inventory(self, path: Path, context: NormalizationContext | None = None) -> SourceInventory:
        text, encoding, source_format, warnings = self._content(path)
        return SourceInventory(
            source_format=source_format,
            source_kind="document",
            unit_count=max(1, len(text.splitlines())),
            metadata={"encoding": encoding, "line_count": len(text.splitlines())},
            warnings=tuple(warnings),
        )

    def normalize(self, path: Path, context: NormalizationContext) -> NormalizationResult:
        text, encoding, source_format, warnings = self._content(path)
        lines = text.splitlines() or [""]
        chunks: list[tuple[int, int, str]] = []
        start = 1
        current: list[str] = []
        current_chars = 0
        for line_number, line in enumerate(lines, 1):
            projected = current_chars + len(line) + 1
            if current and projected > context.max_markdown_chars:
                chunks.append((start, line_number - 1, "\n".join(current)))
                start = line_number
                current = []
                current_chars = 0
            if len(line) > context.max_markdown_chars:
                if current:
                    chunks.append((start, line_number - 1, "\n".join(current)))
                    current = []
                    current_chars = 0
                for offset in range(0, len(line), context.max_markdown_chars):
                    segment = line[offset : offset + context.max_markdown_chars]
                    chunks.append((line_number, line_number, segment))
                start = line_number + 1
                continue
            current.append(line)
            current_chars += len(line) + 1
        if current:
            chunks.append((start, len(lines), "\n".join(current)))

        units = []
        for number, (first, last, content) in enumerate(chunks, 1):
            locator = f"Line {first}" if first == last else f"Lines {first}-{last}"
            units.append(
                unit(
                    locator_kind="line_range",
                    locator=locator,
                    filename=f"lines-{first:06d}-{last:06d}-{number:04d}.md",
                    body=f"## {locator}\n\n{neutralize_untrusted_text(content)}",
                    metadata={"encoding": encoding, "source_line_start": first, "source_line_end": last},
                )
            )
        inventory = SourceInventory(
            source_format=source_format,
            source_kind="document",
            unit_count=len(lines),
            metadata={"encoding": encoding, "line_count": len(lines)},
            warnings=tuple(warnings),
        )
        return NormalizationResult(
            adapter_id=self.adapter_id,
            adapter_version=self.adapter_version,
            source_format=source_format,
            source_kind="document",
            inventory=inventory,
            units=units,
            overview_sections={"encoding": encoding, "line_count": len(lines)},
            warnings=warnings,
            metrics={"line_count": len(lines), "unit_count": len(units)},
        )
