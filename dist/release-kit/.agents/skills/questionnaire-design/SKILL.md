---
name: questionnaire-design
description: Design bilingual, evidence-backed governance questions and incremental questionnaire change sets. Use after knowledge review; do not publish questions or invent requirements.
---

# Questionnaire design

Read the repository `AGENTS.md`, `brain wiki/SCHEMA.md`, the
`questionnaire_curator` role prompt, and [the active Brain note schema](../../../config/schemas/brain-note.schema.json).

- Search the global registry for equivalent intent before assigning a new ID.
- Write one assessable intent in equivalent English and French.
- Attach reviewed locator-backed evidence and keep every generated item in a
  proposal outside the active vault.
- Use `UPDATE` for wording that preserves intent and `SUPERSEDE` for changed intent.
- Validate stable topic, response type, bilingual options, domains, tags,
  dependencies, and affected knowledge.
- Build a common core plus conditional modules. Do not collect answers or
  implement scoring in this repository.

Read [question logic](references/question-logic.md) only when a question uses conditional applicability, dependencies, or supersession.
