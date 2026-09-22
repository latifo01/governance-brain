# Fidelity checks — CDO backlog closure lot 010

Method: corpus-backed claims traced to validated ingest units (all cited pages verified present and content-checked); one note is web-sourced under operator authorization with provenance recorded below.

## Corpus-backed notes

- ai-model-transparency: SRC-0018 p0024 verified (Article 50(2) transparency obligation objective) and p0050 (scope/market surveillance); SRC-0009 p0010/p0016 (transparency report practice; pages OCR-verdict MATCH, coverage >= 0.969).
- ai-model-fairness-and-bias-avoidance: SRC-0009 p0010 verified (harmful-content measurement, hate and unfairness metrics), p0022-p0023 verified (multimodal hate and unfairness evaluation across text and imagery, severity levels, Azure AI Content Safety categories). Pages carry VISUAL_REVIEW flags; automated OCR verdicts MATCH (coverage >= 0.969) in state/workshop/fidelity-review.json.
- traceability: SRC-0035 p0006 verified (model signing: authenticity, integrity, provenance; risks of unsigned artifacts) and p0007; SRC-0038 p0021 and pp.13-15 (documentation and monitoring records); SRC-0036 p0013 (inventory). SRC-0035 pages are clean in extraction-quality.json.
- data-subject-access-requests: SRC-0010 p0043 verified (Article 15 text: confirmation duty; enumerated information including recipients, retention, source, automated decision-making with logic). Page clean.
- iso-27001: SRC-0004 p0003 verified (clause list 6.1.2/6.1.3/8.2/8.3), p0010 verified (risk treatment and Statement of Applicability), p0014 (clauses 8.2-8.3). Pages clean.
- ai-board: SRC-0011 p0296 verified (Article 65: creation and structure) and p0297 verified (one representative per Member State, EDPS participation, three-year terms, rules of procedure). Pages clean.

## Web-backed note (operator-authorized deviation)

- mit-ai-risk-initiative: sourced from the official MIT AI Risk Initiative site (https://airisk.mit.edu/), accessed 2026-09-12. Facts captured: mission statement; datasets (AI Risk Repository 1,700+ risks / 65 frameworks, Version 4 December 2025; AI Incident Tracker; AI Governance dataset; 272-expert priorities survey; AI Risk Navigator; AI Risk Mitigation Database with 13 frameworks); MIT FutureTech attribution; CC BY 4.0 licensing; institutional users listed on the site. Fetches of atlas.mitre.org mitigation pages (for AML.M0029) returned 404 to non-browser clients; recorded in unresolved-identifiers.md.
- This note is explicitly marked as web-sourced in its Limits section; it does not carry SRC locators because no ingest source covers it.

## Already-covered backlog drafts

- general-purpose-ai-gpai -> covered by gpai-model (alias addition proposed).
- ai-model-documentation / ai-model-monitoring / ai-model-validation -> integrated in lots 001-002; byte-identical pattern confirmed during lot 001-003 approval.
