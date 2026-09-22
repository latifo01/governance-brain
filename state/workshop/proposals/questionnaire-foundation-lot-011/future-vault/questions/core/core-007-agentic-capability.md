---
id: core-007-agentic-capability
title: Agentic capability
type: question
domains: [AI, AI_SECURITY, RISK]
status: active
aliases: [AI agent capability]
tags: [questionnaire, common-core, capability, agentic-ai]
evidence_sources: [AI_ACT, AI_NICE_TO_KNOW]
topic: agentic-capability
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: "yes"
question_fr: "Le système planifie-t-il ou exécute-t-il des actions au moyen d’outils, de données externes, de mémoire ou d’autres agents de manière autonome lors des étapes intermédiaires ?"
question_en: "Does the system plan or execute actions through tools, external data, memory or other agents with autonomy over intermediate steps?"
---

# Agentic capability

## Purpose

Route systems to controls for goals, tool privileges, action impact, memory,
prompt manipulation and human approval.

## Guidance

Describe planning, tool calls, connected data, memory, peer agents, autonomy
level and the most consequential action the system can execute or influence.

## Related knowledge

- [[agentic-ai]]
- [[prompt-injection]]
- [[human-oversight]]

## Source references

- SRC-0015, pages 2 and 6, for planning, tool invocation, autonomous intermediate steps and deployment-dependent impact.
- SRC-0027, pages 10-11, for goal hijacking, connected data, tool use, least privilege and human approval.
