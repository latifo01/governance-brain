---
id: brain-schema
title: Governance Brain schema
type: index
domains: [GENERAL]
status: active
aliases: []
tags: []
evidence_sources: []
---

# Governance Brain schema

This document and `config/schemas/brain-note.schema.json` define the active
Markdown contract. The older `vault-frontmatter.schema.json` and
`questionnaire.schema.json` support historical v1 tooling and must not validate
or publish this vault.

## Common fields

Every Markdown file begins with YAML. Required fields: `id` (unique lowercase kebab-case), `title` (nonempty string), `type` (knowledge, question, index), `domains` (nonempty list from the domain registry), `status` (active or deprecated in this vault), `aliases` and `tags` (string lists), `evidence_sources` (list of registered Knowledge Bank aliases, possibly empty). Drafts remain outside the vault. Filenames match IDs except these two entry documents, README.md and SCHEMA.md.

## Knowledge

Use Summary, Applicability, Governance considerations, Related concepts and Source references as appropriate. Omit empty sections. Include document names and precise page or section references; record hash-bound review evidence in the workshop. Explain uncertainties and separate interpretation from documentary facts.

## Questions

In addition to common fields, require `topic` (nonempty controlled intent label), `priority` (high, medium, low), `applies_to` (AI or ALL), `answer_type` (boolean, text, choice), `depends_on`, `question_fr` and `question_en` (nonempty equivalent wording). Choice questions require at least two options, each with a stable `value`, `label_fr` and `label_en`.

`topic` is a stable intent label using the current kebab-case convention and is shared by questions that ask for the
same underlying information. `depends_on` is null or an object containing
exactly `question_id` and `equals`. The referenced question must exist. Cycles
are invalid. Explain more complex relationships in prose. Do not encode waves or
a rules engine. Intentional shared topics must be explained in the review
record. Use `domains`, `tags`, and `depends_on` to publish a common core and
conditional modules. Answers and assessment scores are outside this repository.

Question bodies explain Purpose, Guidance and Related knowledge. Each question assesses one intent.

## Indexes

Indexes use common fields and meaningful links for navigation only. They introduce no independent regulatory conclusions.

## Domains and routing

The registry preserves the macro domains AI, LEGAL, DATA_PROTECTION,
INTERNAL_REGULATION, RISK, PROCESS, and GENERAL. It also contains the active
Domain Pack IDs AI_SECURITY, AUDIT_ASSURANCE, DATA_PRIVACY,
GOVERNANCE_ACCOUNTABILITY, HUMAN_OVERSIGHT_RESPONSIBLE_AI, LEGAL_REGULATORY,
MODEL_RISK, OPERATIONAL_RESILIENCE_INCIDENTS, THIRD_PARTIES_SUPPLY_CHAIN, and
TRANSPARENCY_DISCLOSURE. Folder names never determine business logic. New IDs
require a reviewed taxonomy proposal before activation.

Allowed bank aliases: AI_ACT, AI_LEGAL_GUIDANCE, AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL, DATA_AI_CLASSIFICATION. These route future verification; they do not assert that verification has occurred.

Markdown question notes are canonical. Obsidian Canvas files are derived
navigation or editorial references and do not establish evidence or approval.
The active `Risk analysis questionnaire.canvas` and the offline
`state/derived/question-registry.jsonl` are regenerated from active question
frontmatter. They must never become an independent source of question content.
