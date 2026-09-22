---
name: vault-audit
description: Audit a Governance Brain vault for schema, provenance, link, authority, questionnaire, and approval defects. Use before publication or for repository health review; report findings without granting approval.
---

# Vault audit

Read the repository `AGENTS.md`, `brain wiki/SCHEMA.md`, and the
`vault_reviewer` role prompt. Run the active workshop validator before
qualitative review.

- Report findings with severity, artifact, stable identifier, and remediation.
- Distinguish generated review readiness from recorded human approval.
- Fail publication for unsupported claims, missing reviewed evidence, invalid
  authority, broken links, duplicate question intent, dependency cycles, or
  missing affected-domain approval.
- Keep reports free of raw source text and sensitive values.

Read [audit checks](references/audit-checks.md) for a full publication gate. For a focused repair, load only the relevant section.

Use `gov360 brain validate` to examine evidence eligibility alongside workshop
schema validation. Resolve source/unit hashes, locators, review identities and
the exact candidate approval chain. Distinguish an existing active note from
reviewed assistance-eligible content; report unresolved history without rewriting
old receipts. Check author/reviewer independence and per-claim authority.
