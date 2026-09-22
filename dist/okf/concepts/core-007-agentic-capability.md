---
aliases:
- AI agent capability
answer_type: boolean
applies_to: AI
brain_id: core-007-agentic-capability
brain_sha256: b42d03745833ab6925ca5bb367d09f7bc88c73c5f6a7b1b25638977348db87b7
depends_on:
  equals: 'yes'
  question_id: core-003-ai-system-determination
domains:
- AI
- AI_SECURITY
- RISK
evidence_sources:
- AI_ACT
- AI_NICE_TO_KNOW
id: core-007-agentic-capability
priority: high
question_en: Does the system plan or execute actions through tools, external data,
  memory or other agents with autonomy over intermediate steps?
question_fr: Le système planifie-t-il ou exécute-t-il des actions au moyen d’outils,
  de données externes, de mémoire ou d’autres agents de manière autonome lors des
  étapes intermédiaires ?
status: stable
tags:
- questionnaire
- common-core
- capability
- agentic-ai
title: Agentic capability
topic: agentic-capability
type: question
---


# Agentic capability

## Purpose

Route systems to controls for goals, tool privileges, action impact, memory,
prompt manipulation and human approval.

## Guidance

Describe planning, tool calls, connected data, memory, peer agents, autonomy
level and the most consequential action the system can execute or influence.

## Related knowledge

- [agentic-ai](/concepts/agentic-ai.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [human-oversight](/concepts/human-oversight.md)

## Source references

- SRC-0015, pages 2 and 6, for planning, tool invocation, autonomous intermediate steps and deployment-dependent impact.
- SRC-0027, pages 10-11, for goal hijacking, connected data, tool use, least privilege and human approval.
