from __future__ import annotations

import hashlib
from collections import Counter
from pathlib import Path
from typing import Any

from gov360_brain.contracts import (
    NormalizationContext,
    NormalizationResult,
    ProbeResult,
    SourceInventory,
    ValidationReport,
)

from .base import (
    DependencyUnavailableError,
    QuarantinedSourceError,
    ValidatingAdapter,
    neutralize_untrusted_text,
    unit,
)


class PdfAdapter(ValidatingAdapter):
    adapter_id = "pdf"
    adapter_version = "1.2.0"
    capabilities = {"air_gap": True, "native_text": True, "rendering": True, "ocr": "optional-local", "tables": "review", "charts": "review"}

    def probe(self, path: Path) -> ProbeResult | None:
        with path.open("rb") as stream:
            head = stream.read(1024)
        offset = head.find(b"%PDF-")
        if offset < 0:
            return None
        warnings = () if path.suffix.lower() == ".pdf" else ("extension does not match PDF signature",)
        return ProbeResult(self.adapter_id, "pdf", "application/pdf", 1.0, warnings)

    def _reader(self, path: Path):
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise DependencyUnavailableError("pypdf is required for PDF normalization") from exc
        try:
            reader = PdfReader(path, strict=False)
            if reader.is_encrypted and reader.decrypt("") == 0:
                raise QuarantinedSourceError("password-protected PDF cannot be normalized")
            _ = len(reader.pages)
            return reader
        except QuarantinedSourceError:
            raise
        except Exception as exc:
            raise QuarantinedSourceError("PDF structure cannot be read") from exc

    @staticmethod
    def _image_fingerprints(page: Any) -> tuple[list[str], int]:
        fingerprints: list[str] = []
        errors = 0
        try:
            resources = page.get("/Resources") or {}
            resources = resources.get_object() if hasattr(resources, "get_object") else resources
            xobjects = resources.get("/XObject") or {}
            xobjects = xobjects.get_object() if hasattr(xobjects, "get_object") else xobjects
            for reference in xobjects.values():
                try:
                    obj = reference.get_object() if hasattr(reference, "get_object") else reference
                    if str(obj.get("/Subtype")) != "/Image":
                        continue
                    payload = obj.get_data()
                    fingerprints.append(hashlib.sha256(payload).hexdigest())
                except Exception:
                    errors += 1
        except Exception:
            errors += 1
        return fingerprints, errors

    def inventory(self, path: Path, context: NormalizationContext | None = None) -> SourceInventory:
        reader = self._reader(path)
        metadata = reader.metadata or {}
        return SourceInventory(
            source_format="pdf",
            source_kind="document",
            unit_count=len(reader.pages),
            metadata={
                "page_count": len(reader.pages),
                "encrypted": bool(reader.is_encrypted),
                "title_present": bool(metadata.get("/Title")),
                "author_present": bool(metadata.get("/Author")),
            },
        )

    def normalize(self, path: Path, context: NormalizationContext) -> NormalizationResult:
        reader = self._reader(path)
        extracted: list[tuple[str, list[str], int, list[str]]] = []
        fingerprint_counts: Counter[str] = Counter()
        warnings: list[str] = []
        for page_number, page in enumerate(reader.pages, 1):
            page_warnings: list[str] = []
            try:
                text = page.extract_text() or ""
            except Exception:
                text = ""
                page_warnings.append("native text extraction failed")
            fingerprints, image_errors = self._image_fingerprints(page)
            fingerprint_counts.update(set(fingerprints))
            if image_errors:
                page_warnings.append("one or more image objects could not be inspected")
            extracted.append((text, fingerprints, image_errors, page_warnings))

        units = []
        visual_candidates = 0
        ocr_candidates = 0
        total_pages = len(extracted)
        for page_number, (text, fingerprints, _, page_warnings) in enumerate(extracted, 1):
            unique_visuals = [digest for digest in fingerprints if fingerprint_counts[digest] < max(2, total_pages // 2)]
            repeated_visuals = [digest for digest in fingerprints if digest not in unique_visuals]
            text_chars = len(text.strip())
            if unique_visuals or (fingerprints and text_chars < 80):
                visual_state = "REVIEW_REQUIRED"
                visual_candidates += 1
            elif fingerprints:
                visual_state = "DECORATIVE"
            else:
                visual_state = "NONE"
            if text_chars < 20 and fingerprints:
                page_warnings.append("native text is sparse; local OCR or human review is required")
                ocr_candidates += 1
                visual_state = "REVIEW_REQUIRED"
            locator = f"Page {page_number}"
            units.append(
                unit(
                    locator_kind="page",
                    locator=locator,
                    filename=f"p{page_number:04d}.md",
                    body=f"## {locator}\n\n{neutralize_untrusted_text(text)}",
                    visual_review=visual_state,
                    metadata={
                        "page_number": page_number,
                        "native_text_chars": text_chars,
                        "image_object_count": len(fingerprints),
                        "unique_visual_count": len(unique_visuals),
                        "repeated_visual_count": len(repeated_visuals),
                        "image_fingerprints": fingerprints,
                        "extraction_mode": "native",
                        "ocr_used": False,
                    },
                    warnings=page_warnings,
                )
            )
            warnings.extend(f"{locator}: {warning}" for warning in page_warnings)

        inventory = SourceInventory(
            source_format="pdf",
            source_kind="document",
            unit_count=total_pages,
            metadata={"page_count": total_pages, "encrypted": bool(reader.is_encrypted)},
            warnings=tuple(warnings),
        )
        return NormalizationResult(
            adapter_id=self.adapter_id,
            adapter_version=self.adapter_version,
            source_format="pdf",
            source_kind="document",
            inventory=inventory,
            units=units,
            overview_sections={
                "page_count": total_pages,
                "visual_candidate_pages": visual_candidates,
                "ocr_candidate_pages": ocr_candidates,
            },
            data_artifacts=[
                {
                    "artifact_type": "visual_inventory",
                    "locator": "Document",
                    "metadata": {
                        "candidate_pages": visual_candidates,
                        "ocr_candidate_pages": ocr_candidates,
                    },
                }
            ],
            warnings=warnings,
            metrics={"page_count": total_pages, "unit_count": len(units)},
        )

    def validate(
        self, result: NormalizationResult, context: NormalizationContext
    ) -> ValidationReport:
        report = super().validate(result, context)
        errors = list(report.errors)
        if result.inventory.unit_count != len(result.units):
            errors.append("PDF page coverage does not match the page inventory")
        return ValidationReport(
            valid=not errors,
            errors=tuple(errors),
            warnings=report.warnings,
            metrics=report.metrics,
        )
