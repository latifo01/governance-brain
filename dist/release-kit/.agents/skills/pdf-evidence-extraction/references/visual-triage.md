# PDF visual triage

Render candidate pages locally and classify each as `NONE`, `DECORATIVE`, `REVIEW_REQUIRED`, `REVIEWED`, or `UNREADABLE`.

Flag a page when native text is absent or unusually sparse, parsing failed, a table/picture/layout detector fires, a caption is present, or a unique visual occupies a material area. Use image hashes plus repeated position to identify logos and backgrounds; repetition alone does not justify deletion when text extraction is poor.

Use OCR only for nonblank content with missing or unusable native text. Record languages and extraction mode. Keep render caches outside version control; retain a visual in the vault only when it is required to understand verified evidence.

