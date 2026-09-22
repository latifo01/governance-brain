---
id: risk-009-misinformation-overreliance
title: Misinformation and overreliance controls
type: question
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Controls against misinformation and overreliance
tags:
  - questionnaire
  - hallucinations
evidence_sources: [AI_NICE_TO_KNOW]
topic: misinformation-overreliance-controls
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Le système identifie-t-il les décisions, flux de travail et actions d’agents influencés par des sorties de modèle non vérifiées, et applique-t-il des contrôles (validation, vérification des sources ou revue humaine) avant leur exécution ?"
question_en: "Does the system identify the decisions, workflows and agent actions influenced by unverified model outputs, and apply controls (validation, source verification or human review) before they execute?"
---

# Misinformation and overreliance controls

## Purpose

This question checks whether the organization treats model-generated misinformation and overreliance on fluent output as a system-level risk rather than only a model-quality issue.

## Guidance

Answer "yes" only when material decisions, workflow triggers, code execution or agent actions derived from model output are inventoried, and at least one verification control (grounding checks, source verification, human gate) is enforced before execution.

## Related Knowledge

- [[hallucinations]]

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, pages 43-44, for misinformation root causes, overreliance and the requirement to reference prompt injection, poisoning or supply-chain compromise separately.
- SRC-0028, CoSAI AI Incident Response Framework V1.0, page 13, for inspecting model outputs including hallucinations before downstream use.
