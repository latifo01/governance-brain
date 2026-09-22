---
aliases:
- AI system scope
answer_type: boolean
applies_to: AI
brain_id: core-004-system-boundary
brain_sha256: 78a5f95d15e9239911226383e2b76ffd90ae7b9f1630584a2e52a3c782e42330
depends_on:
  equals: 'yes'
  question_id: core-003-ai-system-determination
domains:
- AI
- PROCESS
- GOVERNANCE_ACCOUNTABILITY
evidence_sources:
- AI_NICE_TO_KNOW
id: core-004-system-boundary
priority: high
question_en: Does the documented system boundary identify its models, data, interfaces,
  dependencies, tools, environments, outputs and human processes?
question_fr: Le périmètre documenté du système identifie-t-il ses modèles, données,
  interfaces, dépendances, outils, environnements, sorties et processus humains ?
status: stable
tags:
- questionnaire
- common-core
- inventory
title: AI system boundary
topic: system-boundary
type: question
---


# AI system boundary

## Purpose

Define the object governed by later risk, legal, security and assurance checks.

## Guidance

Answer yes only when internal and third-party components, data flows, users,
downstream uses, deployment context and relevant human decisions are visible.

## Related knowledge

- [ai-system](/concepts/ai-system.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)
- [nist-ai-rmf](/concepts/nist-ai-rmf.md)

## Source references

- SRC-0039, pages 29-31, for mapping context, components, users, impacts and requirements.
- SRC-0039, pages 40-46, for AI actors, lifecycle roles and human-AI configurations.
