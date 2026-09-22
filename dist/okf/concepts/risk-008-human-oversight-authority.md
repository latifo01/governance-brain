---
aliases:
- Oversight authority
answer_type: boolean
applies_to: AI
brain_id: risk-008-human-oversight-authority
brain_sha256: 7a360e5e6af749641ee6b828941e519b4ffae490bbb30f7189b7728af96c7839
depends_on: null
domains:
- AI
- RISK
- LEGAL
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: risk-008-human-oversight-authority
priority: high
question_en: Do the people responsible for human oversight have the information, training,
  time and authority needed to interpret, challenge, interrupt or reject the system
  output?
question_fr: Les personnes chargées de la supervision humaine disposent-elles de l’information,
  de la formation, du temps et de l’autorité nécessaires pour interpréter, contester,
  interrompre ou rejeter le résultat du système ?
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: be036-src-0026-p0012-ec-008
  id: brain-1523744993ed9f3d
  locator: Page 12
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 1cfba4e0154a048c96ae27e2d0743a858fcdeccc7cdfce4658758a4810b266df
  unit_path: ingest/SRC-0026/units/p0012.md
  unit_sha256: 436d3b986575a0f607a14600038e62cef6853d18e2042e570ec91350dd18ffbb
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be036-src-0039-p0045-ec-015
  id: brain-3a2861a95a3ee288
  locator: Page 45
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 6c471013c7e708e3795cf6420ba5df75cc32dabad343f437d4c55cf5be8f6ab7
  unit_path: ingest/SRC-0039/units/p0045.md
  unit_sha256: 297d8959055aa6adddf8a80417c9068d7a9b2958d098417e20ff798b8e56f1a0
- authority: GUIDANCE
  brain_source_id: SRC-0027
  evidence_ref: be036-src-0027-p0033-ec-012
  id: brain-8b340b40e1245a51
  locator: Page 33
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 054d918a5b79cb9e264043f31974db49387db3cf85b4cf85722c1b303e90cfd6
  unit_path: ingest/SRC-0027/units/p0033.md
  unit_sha256: e9573b439fb81438f806fd0b6eaf24be71c66ed4a8a59e95b1ab2760f082c6f5
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be036-src-0039-p0032-ec-013
  id: brain-b07aa31f608be7a0
  locator: Page 32
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 3fb08605b67176fe71e367f627b72a5b557a50e19ed8d048a64271e490d3b54d
  unit_path: ingest/SRC-0039/units/p0032.md
  unit_sha256: 4d6d21a07d29ce58c5e16dd5acd6c0cbe08e8a08e43f18b968eabfe92132bb57
- authority: GUIDANCE
  brain_source_id: SRC-0027
  evidence_ref: be036-src-0027-p0011-ec-010
  id: brain-db63174bab64260c
  locator: Page 11
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 62af7b9b2d37dd3b5410c093ef81c904113d9cc25eb787ea347dc001a80e72bb
  unit_path: ingest/SRC-0027/units/p0011.md
  unit_sha256: 9dad2c1b3933450b0cb3b6a515f0adaa3650d598a533927bb59f631f3a84dcaf
status: stable
tags:
- questionnaire
- human-oversight
title: Human oversight authority
topic: human-oversight-authority
type: question
---


# Human oversight authority

## Purpose

This question checks whether human oversight is operationally meaningful and whether the assigned people have defined roles, usable information and practical authority to intervene.

Section evidence: [^brain-3a2861a95a3ee288] [^brain-b07aa31f608be7a0]

## Guidance

Answer "yes" only when the oversight process defines responsibilities, competence or training, access to relevant context and uncertainty, time to review, escalation routes and authority to challenge, defer, reject, interrupt or stop an output where the risk context requires it.

For agentic or high-impact workflows, verify whether human approval gates and output validation are placed before consequential actions or downstream propagation. NIST and OWASP support this as contextual governance and control guidance; they do not create a universal legal rule.

Section evidence: [^brain-1523744993ed9f3d] [^brain-3a2861a95a3ee288] [^brain-8b340b40e1245a51] [^brain-b07aa31f608be7a0] [^brain-db63174bab64260c]

## Related Knowledge

- [human-oversight](/concepts/human-oversight.md)
- [genai-guardrails](/concepts/genai-guardrails.md)

## Source References

- SRC-0039, pages 32 and 45, for documented oversight processes, human roles and contextual human-AI configurations.
- SRC-0027, pages 11 and 33, for human approval, intent validation and gates before high-impact or high-risk propagation.
- SRC-0026, pages 10-12, for the security and privilege context in which human intervention may be relevant.


[^brain-1523744993ed9f3d]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 12.
[^brain-3a2861a95a3ee288]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 45.
[^brain-8b340b40e1245a51]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 33.
[^brain-b07aa31f608be7a0]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 32.
[^brain-db63174bab64260c]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 11.
