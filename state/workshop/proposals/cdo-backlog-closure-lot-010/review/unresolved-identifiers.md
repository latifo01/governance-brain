# Unresolved identifiers — CDO backlog closure lot 010

## AML.M0029

- CDO draft: `mitigations/AML.M0029.md` (empty body; EMPTY_BACKLOG in cdo-inventory.json).
- The identifier follows the MITRE ATLAS mitigation ID convention (AML.M#### — the corpus's `mitre-atlas` note documents ATLAS techniques; mitigations use the M-series).
- Resolution attempts (2026-09-12):
  - Ingest corpus: no occurrence of "M0029" anywhere in `ingest/` (verified by search).
  - Live ATLAS site (atlas.mitre.org): JavaScript-rendered; mitigation pages return 404 to non-browser clients, including for known-valid IDs.
  - ATLAS source repositories (mitre/advmlthreatmatrix, mitre/atlas-navigator): the matrix era predates M-numbered mitigation IDs; no mitigation data files.
  - Wikipedia, Wayback Machine: no archived snapshot of the mitigation page.
- Assistant knowledge: the specific title and description of AML.M0029 are NOT known with confidence; fabricating them would insert an unverified claim into the vault. The operator (who has the CDO taxonomy context) will verify the identifier and supply the title/description.
- Status: UNRESOLVED_IDENTIFIER — remains in the workshop. **Operator decision (2026-09-12): "pour l'AML nous allons revenir" — resolution deferred by the operator to a later session.** The lot 010 integration proceeds without this note; when the operator provides the verified content, the note will follow the normal review path in a dedicated lot.
- Verification path for the operator: open `https://atlas.mitre.org/#/mitigations` in a browser, locate AML.M0029 in the mitigations list, and provide the title and summary; or consult the CDO's internal taxonomy that produced the draft filename.

## Closed without new notes (already covered in the vault)

- `general-purpose-ai-gpai` (EMPTY_BACKLOG): semantically covered by the integrated note [[gpai-model]] (AI concepts). Proposed follow-up: add the alias "General-Purpose AI (GPAI)" to `gpai-model` upon lot approval to close the CDO entry.
- `ai-model-documentation`, `ai-model-monitoring`, `ai-model-validation` (EMPTY_BACKLOG): covered by the integrated notes of the same IDs (lots 001-002).
