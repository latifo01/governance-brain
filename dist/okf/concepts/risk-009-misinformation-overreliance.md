---
aliases:
- Controls against misinformation and overreliance
answer_type: boolean
applies_to: AI
brain_id: risk-009-misinformation-overreliance
brain_sha256: 8e9022f77223ab664b0c31220232c59371a61ef4835ff4617ab51813cf438911
depends_on: null
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: risk-009-misinformation-overreliance
priority: high
question_en: Does the system identify the decisions, workflows and agent actions influenced
  by unverified model outputs, and apply controls (validation, source verification
  or human review) before they execute?
question_fr: Le système identifie-t-il les décisions, flux de travail et actions d’agents
  influencés par des sorties de modèle non vérifiées, et applique-t-il des contrôles
  (validation, vérification des sources ou revue humaine) avant leur exécution ?
sources:
- authority: UNCLASSIFIED
  brain_source_id: SRC-0028
  evidence_ref: provenance-repair-20260920-src-0028-p0013
  id: brain-0d57fb2dd737c4b4
  locator: Page 13
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: 8913b0f8583a0586545a0305d4c743322405d03187394517d36b6a36f5ec8594
  unit_path: ingest/SRC-0028/units/p0013.md
  unit_sha256: e9d93f7e5bc79986760f38bd587c948ea6764949c3848637299c8f15f86b7904
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0043
  id: brain-2126cff5e8afc508
  locator: Page 43
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 88e28d2175d3b1930ce678de0c337536e6e0eadc2be4e497362f66304326e004
  unit_path: ingest/SRC-0026/units/p0043.md
  unit_sha256: 06db05750519a9ac0eba31a934321f1608592b38a838de9c681e291734fd3d36
- authority: UNCLASSIFIED
  brain_source_id: SRC-0026
  evidence_ref: provenance-repair-20260920-src-0026-p0044
  id: brain-ec903f664b7714dd
  locator: Page 44
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 34b75ff97d135bb6d8ec2e4a4706f08238c43ae9671defdaefaa0d6e069e8cbb
  unit_path: ingest/SRC-0026/units/p0044.md
  unit_sha256: 139ba0594ce862fa9463fb9b7ff84f829ddd743a3ae64ccc4a84410bdefe689c
status: stable
tags:
- questionnaire
- hallucinations
title: Misinformation and overreliance controls
topic: misinformation-overreliance-controls
type: question
---


# Misinformation and overreliance controls

## Purpose

This question checks whether the organization treats model-generated misinformation and overreliance on fluent output as a system-level risk rather than only a model-quality issue.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-ec903f664b7714dd]

## Guidance

Answer "yes" only when material decisions, workflow triggers, code execution or agent actions derived from model output are inventoried, and at least one verification control (grounding checks, source verification, human gate) is enforced before execution.

Section evidence: [^brain-0d57fb2dd737c4b4] [^brain-2126cff5e8afc508] [^brain-ec903f664b7714dd]

## Related Knowledge

- [hallucinations](/concepts/hallucinations.md)

## Source References

- SRC-0026, OWASP Top 10 for LLM Applications 2026, pages 43-44, for misinformation root causes, overreliance and the requirement to reference prompt injection, poisoning or supply-chain compromise separately.
- SRC-0028, CoSAI AI Incident Response Framework V1.0, page 13, for inspecting model outputs including hallucinations before downstream use.


[^brain-0d57fb2dd737c4b4]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 13.
[^brain-2126cff5e8afc508]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 43.
[^brain-ec903f664b7714dd]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 44.
