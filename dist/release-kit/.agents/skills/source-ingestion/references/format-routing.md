# Format routing

## Document and presentation formats

- PDF: extract native text page by page first; escalate only suspect pages to local layout/OCR processing.
- DOCX/ODT: preserve headings, tables, lists, notes, hyperlinks, and section or page locators when reliable.
- PPTX/ODP: preserve slide order, notes, tables, links, alt text, groups, and chart metadata; render locally when layout matters.
- Legacy DOC/PPT: require an available local Office or LibreOffice bridge. Never execute macros or update links.

## Tabular and structured formats

- CSV/TSV: stream physical records, retain raw strings, repeat headers, and record decoding or dialect uncertainty.
- XLSX/ODS: retain sheet order and visibility, formulas separately from values, tables, names, comments, charts, and external-dependency warnings.
- Legacy XLS: use a controlled local conversion copy; the original stays untouched.
- JSON/JSONL/XML: use record or path locators. Quarantine malformed regions that cannot be isolated safely.

If row count exceeds 50,000 or source size exceeds 25 MiB, create local columnar partitions and Markdown schema/quality/profile artifacts. Mark samples non-exhaustive; derive aggregates only through recorded, reproducible local queries.

## Images and visuals

Use object type, caption cues, occupied area, extraction quality, hash, position, and repetition together. Repeated branding can be `DECORATIVE`; unique diagrams or charts require review. Prefer native chart data over image interpretation. OCR uses only locally installed artifacts.

