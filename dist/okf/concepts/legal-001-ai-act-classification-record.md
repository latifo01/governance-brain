---
aliases:
- AI Act high-risk classification question
answer_type: boolean
applies_to: AI
brain_id: legal-001-ai-act-classification-record
brain_sha256: fe95e6c956e134ac986a5a789771d9cafbeca930d49bb8e9aed96f5a471204c4
depends_on:
  equals: no-prohibited-practice-identified
  question_id: core-011-prohibited-practice-screening
domains:
- AI
- LEGAL
- RISK
- PROCESS
evidence_sources:
- AI_ACT
- AI_LEGAL_GUIDANCE
id: legal-001-ai-act-classification-record
priority: high
question_en: Does the project have a documented AI Act classification record covering
  intended purpose, organisational role, relevant Annex I or Annex III categories,
  any profiling and any claimed derogation?
question_fr: Le projet dispose-t-il d’un enregistrement documenté de la classification
  AI Act, incluant la finalité prévue, le rôle de l’organisation, les catégories Annex
  I ou Annex III pertinentes, le profilage éventuel et toute dérogation revendiquée
  ?
status: stable
tags:
- questionnaire
- ai-act
title: AI Act classification record
topic: ai-act-classification-record
type: question
---


# AI Act classification record

## Purpose

This question checks whether AI Act classification is governed as a formal decision rather than inferred informally from the project label.

## Guidance

Answer "yes" only when the record is specific to the system and use case, identifies the evidence used and has an accountable reviewer.

## Related knowledge

- [eu-ai-act](/concepts/eu-ai-act.md)
- [high-risk-ai-system-classification](/concepts/high-risk-ai-system-classification.md)
- [fundamental-right-impact-assessment-fria](/concepts/fundamental-right-impact-assessment-fria.md)

## Source references

- SRC-0011, pages 179-181, for Article 6 classification and derogation documentation.
- SRC-0043, pages 18 and 35, for the 2026-amended classification clarifications and the route-specific application dates.
- SRC-0022, pages 95-97, for training-based explanation of product safety and Annex III high-risk routing.
