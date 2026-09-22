---
id: core-004-system-boundary
title: AI system boundary
type: question
domains: [AI, PROCESS, GOVERNANCE_ACCOUNTABILITY]
status: active
aliases: [AI system scope]
tags: [questionnaire, common-core, inventory]
evidence_sources: [AI_NICE_TO_KNOW]
topic: system-boundary
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: "yes"
question_fr: "Le périmètre documenté du système identifie-t-il ses modèles, données, interfaces, dépendances, outils, environnements, sorties et processus humains ?"
question_en: "Does the documented system boundary identify its models, data, interfaces, dependencies, tools, environments, outputs and human processes?"
---

# AI system boundary

## Purpose

Define the object governed by later risk, legal, security and assurance checks.

## Guidance

Answer yes only when internal and third-party components, data flows, users,
downstream uses, deployment context and relevant human decisions are visible.

## Related knowledge

- [[ai-system]]
- [[ai-model-documentation]]
- [[nist-ai-rmf]]

## Source references

- SRC-0039, pages 29-31, for mapping context, components, users, impacts and requirements.
- SRC-0039, pages 40-46, for AI actors, lifecycle roles and human-AI configurations.
