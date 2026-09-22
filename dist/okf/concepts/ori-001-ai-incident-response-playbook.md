---
aliases:
- AI incident response preparedness
answer_type: boolean
applies_to: AI
brain_id: ori-001-ai-incident-response-playbook
brain_sha256: 56ee80ce9f75c6b658e0ade41c7408db1f6841bc396e56817fbf8df0925e9aa7
depends_on:
  equals: true
  question_id: core-003-ai-system-determination
domains:
- OPERATIONAL_RESILIENCE_INCIDENTS
- AI_SECURITY
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: ori-001-ai-incident-response-playbook
priority: high
question_en: Does the AI system have an incident response plan defining roles, escalation,
  detection, containment, recovery and communications playbooks?
question_fr: Le système d'IA dispose-t-il d'un plan de réponse aux incidents qui définit
  les rôles, l'escalade, les playbooks de détection, de confinement, de récupération
  et les communications ?
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0028
  evidence_ref: ops28-src-0028-p0021
  id: brain-00f23962e4385710
  locator: Page 21
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: 8f61d45a6539090406946c86d9153de45f80fe306459651ee3caef4657ec81c7
  unit_path: ingest/SRC-0028/units/p0021.md
  unit_sha256: 6057f0d4419819b8f01f103cff22ffb1f653b624f64b0abed8faeab2415f4c15
- authority: FRAMEWORK
  brain_source_id: SRC-0028
  evidence_ref: ops28-src-0028-p0006
  id: brain-1d4431386d951879
  locator: Page 6
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: 78710ff012046644651f338a27820616d2770b611638961bea396de18cac4ddb
  unit_path: ingest/SRC-0028/units/p0006.md
  unit_sha256: 8f33558bcd218cf0fc15b401c3104634e328aced18e2cef61398d56f48e00ba2
- authority: FRAMEWORK
  brain_source_id: SRC-0028
  evidence_ref: ops28-src-0028-p0007
  id: brain-4a9b9ee5be9e69a9
  locator: Page 7
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: 8c0400d24afea4d42a1644213e3eb837e88de0ba24b8777192391949cd9020c3
  unit_path: ingest/SRC-0028/units/p0007.md
  unit_sha256: f61eeb7f324f4e39b8ec0f2b2105ff7ecf99379d17bb6b9a4358c032c693f422
- authority: FRAMEWORK
  brain_source_id: SRC-0028
  evidence_ref: ops28-src-0028-p0023
  id: brain-640cd196defea38e
  locator: Page 23
  resource: /references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md
  unit_file_sha256: fee6e45dd39335192837ce6ae2a1cb54dbe036f2217edb6b567a24a86639b8da
  unit_path: ingest/SRC-0028/units/p0023.md
  unit_sha256: 4cbd7b564d5e465a99d613c36f0454b4eb4d906559124960da4eefbd186a2a19
status: stable
tags:
- questionnaire
- incidents
- resilience
- playbooks
title: AI incident response playbook
topic: ai-incident-response-playbook
type: question
---


# AI incident response playbook

## Purpose

Establish whether the organisation can coordinate an AI-specific incident from
detection through recovery and improvement.

Section evidence: [^brain-1d4431386d951879] [^brain-640cd196defea38e]

## Guidance

Answer "yes" only when the plan covers AI-specific incident types, named roles,
severity and escalation criteria, evidence preservation, containment,
recovery validation, communications and post-incident learning. It should cover
the model, data, prompts, tools, dependencies and operating environment.

Section evidence: [^brain-00f23962e4385710] [^brain-4a9b9ee5be9e69a9] [^brain-640cd196defea38e]

## Related knowledge

- [ai-incident-response-resilience](/concepts/ai-incident-response-resilience.md)
- [ai-governance-accountability](/concepts/ai-governance-accountability.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)

## Source references

- SRC-0028, pages 6-7 and 21-24, for the AI incident lifecycle, roles, playbooks and communications.


[^brain-00f23962e4385710]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 21.
[^brain-1d4431386d951879]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 6.
[^brain-4a9b9ee5be9e69a9]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 7.
[^brain-640cd196defea38e]: [SRC-0028](/references/src-0028-5722b7682ae060d9373666f4804a3f6d165199bbb4035053adedd46df1730654.md); locator: Page 23.
