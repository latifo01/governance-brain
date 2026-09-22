from __future__ import annotations

from pathlib import Path

from gov360_brain.contracts import (
    NormalizationContext,
    NormalizationResult,
    ProbeResult,
    SourceInventory,
)

from .base import DependencyUnavailableError, QuarantinedSourceError, ValidatingAdapter, unit


IMAGE_SIGNATURES = (
    (b"\x89PNG\r\n\x1a\n", "png", "image/png"),
    (b"\xff\xd8\xff", "jpeg", "image/jpeg"),
    (b"II*\x00", "tiff", "image/tiff"),
    (b"MM\x00*", "tiff", "image/tiff"),
)


class RasterImageAdapter(ValidatingAdapter):
    adapter_id = "raster-image"

    def probe(self, path: Path) -> ProbeResult | None:
        with path.open("rb") as stream:
            head = stream.read(16)
        for signature, source_format, mime in IMAGE_SIGNATURES:
            if head.startswith(signature):
                expected = {"jpeg": {".jpg", ".jpeg"}, "png": {".png"}, "tiff": {".tif", ".tiff"}}[
                    source_format
                ]
                warnings = () if path.suffix.lower() in expected else ("extension does not match image signature",)
                return ProbeResult(self.adapter_id, source_format, mime, 1.0, warnings)
        return None

    def _metadata(self, path: Path) -> tuple[dict[str, object], str]:
        try:
            from PIL import Image, UnidentifiedImageError
        except ImportError as exc:
            raise DependencyUnavailableError("Pillow is required for raster image normalization") from exc
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                source_format = (image.format or "image").lower()
                metadata: dict[str, object] = {
                    "width": image.width,
                    "height": image.height,
                    "mode": image.mode,
                    "frame_count": int(getattr(image, "n_frames", 1)),
                    "animated": bool(getattr(image, "is_animated", False)),
                    "has_exif": bool(image.getexif()),
                    "info_fields": sorted(str(key) for key in image.info.keys()),
                }
                return metadata, source_format
        except (UnidentifiedImageError, OSError, ValueError) as exc:
            raise QuarantinedSourceError("raster image cannot be decoded safely") from exc

    def inventory(self, path: Path, context: NormalizationContext | None = None) -> SourceInventory:
        metadata, source_format = self._metadata(path)
        return SourceInventory(
            source_format=source_format,
            source_kind="image",
            unit_count=int(metadata["frame_count"]),
            metadata=metadata,
            warnings=("image content requires local OCR or human visual review",),
        )

    def normalize(self, path: Path, context: NormalizationContext) -> NormalizationResult:
        metadata, source_format = self._metadata(path)
        body = (
            "## Image 1\n\n"
            "> Raster source retained as an immutable original. No text was inferred.\n\n"
            "### Technical metadata\n\n"
            f"- Width: {metadata['width']} pixels\n"
            f"- Height: {metadata['height']} pixels\n"
            f"- Color mode: {metadata['mode']}\n"
            f"- Frames: {metadata['frame_count']}"
        )
        normalized = unit(
            locator_kind="image_region",
            locator="Image 1",
            filename="image-0001.md",
            body=body,
            visual_review="REVIEW_REQUIRED",
            metadata={**metadata, "ocr_used": False, "extraction_mode": "native"},
            warnings=["local OCR or human visual review is required before evidentiary use"],
        )
        inventory = SourceInventory(
            source_format=source_format,
            source_kind="image",
            unit_count=int(metadata["frame_count"]),
            metadata=metadata,
            warnings=("image content requires local OCR or human visual review",),
        )
        return NormalizationResult(
            adapter_id=self.adapter_id,
            adapter_version=self.adapter_version,
            source_format=source_format,
            source_kind="image",
            inventory=inventory,
            units=[normalized],
            overview_sections=metadata,
            data_artifacts=[
                {
                    "artifact_type": "visual_candidate",
                    "locator": "Image 1",
                    "metadata": {**metadata, "review_status": "REVIEW_REQUIRED"},
                }
            ],
            warnings=["image content requires local OCR or human visual review"],
            metrics={"frame_count": metadata["frame_count"], "unit_count": 1},
        )
