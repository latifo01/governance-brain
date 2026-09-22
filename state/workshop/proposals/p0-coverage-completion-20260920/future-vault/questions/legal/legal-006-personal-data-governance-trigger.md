---
id: legal-006-personal-data-governance-trigger
title: Personal data governance applicability
type: question
domains:
- DATA_PROTECTION
- LEGAL
- AI
status: active
aliases: []
tags:
- personal-data
- conditional
- gdpr
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
topic: personal-data-governance-trigger
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-009-personal-data-involvement
  equals: true
question_fr: Le projet a-t-il établi que les contrôles de gouvernance des données
  personnelles sont applicables et identifié le traitement concerné ?
question_en: Has the project established that personal-data governance controls apply
  and identified the relevant processing?
---
# Personal data governance applicability

## Purpose

Déclencher les modules conditionnels sans appliquer le GDPR aux jeux de données non personnels.

## Guidance

Identifier les données personnelles, les finalités, les rôles, les traitements, les risques et les déclencheurs DPIA pertinents ; ne pas conclure à la conformité par la seule réponse.

## Related knowledge

- [[data-governance-quality-roles-decisions]]
- [[data-governance-quality-evidence-artifacts]]
- [[data-protection-impact-assessments-dpia]]

## Source references

- Evidence refs: p0cov-src-0010-p0016, p0cov-src-0010-p0049, p0cov-src-0010-p0050, p0cov-src-0010-p0053
