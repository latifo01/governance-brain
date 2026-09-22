---
name: pdf-evidence-extraction
description: Extract and verify page-addressable Markdown from PDF sources with selective local OCR and visual triage. Use for PDF ingest or PDF-specific evidence failures; do not use for general knowledge synthesis.
---

# PDF evidence extraction

Read the repository `AGENTS.md` first, then use the generic source-ingestion contract.

- Preflight every page for native text, extraction errors, object inventory, and visual signals.
- Prefer native text. Escalate only missing, damaged, tabular, or layout-dependent pages to local processing.
- Keep page number, source hash, extraction mode, OCR status, and warnings in every unit.
- Compare extracted coverage with the PDF page count before validation.
- Never infer unreadable content or discard a unique visual automatically.

Read [visual triage](references/visual-triage.md) only when the document contains candidate images, scans, diagrams, charts, or image-only tables.

