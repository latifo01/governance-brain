# CDO plan — ATLAS complementarity lot 015

## Objective

Identify only the MITRE ATLAS information that materially complements the
active Brain Wiki or closes a documented coverage gap.

## Decision rule

- `NOOP`: existing notes already cover the intent adequately.
- `ENRICH`: add a bounded ATLAS relation, scenario or control to an existing
  concept note.
- `CREATE`: create a new concept only when the ATLAS material represents a
  distinct, reusable subject absent from the vault.

## Evidence boundary

Use only validated Markdown units under `ingest/` and their audited source
metadata. ATLAS is security guidance and threat taxonomy, not binding law.
No bulk technique import is authorised by this lot.

## Gate

This lot produces a complementarity matrix first. Any note or question changes
require a subsequent bounded proposal, independent review and human approval.
