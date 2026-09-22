---
name: knowledge-synthesis
description: Propose evidence-backed knowledge notes, relations, and domain changes from audited ingest evidence. Use after evidence verification; do not use to normalize sources or publish changes.
---

# Knowledge synthesis

Read the repository `AGENTS.md` and the `knowledge_architect` role prompt. Work
only from evidence with a current audit verdict; do not reuse a legacy
`VERIFIED` label without re-examination.

- Reuse stable knowledge notes where intent matches; emit proposed Markdown and
  a change manifest rather than editing shared notes.
- Preserve scope, authority, exceptions, dates, uncertainty, and disagreements.
- Follow `brain wiki/SCHEMA.md` and `config/schemas/brain-note.schema.json`.
- Attach exact evidence references to every claim and list all affected domains.
- Route domain overlap through taxonomy proposals instead of silently changing the taxonomy.

Read [materialization rules](references/materialization.md) when deciding whether evidence supports a new concept, rule, or domain relation.

Reuse audits only for matching source/unit hashes, scope and current review
validity. Associate proposed sections and individual claims with reviewed
evidence in the assigned sidecar contract; do not infer eligibility from active
legacy notes. Build questions with knowledge where evidence is shared.
