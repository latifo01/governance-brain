---
aliases:
- Threat model for prompt injection
answer_type: boolean
applies_to: AI
brain_id: risk-005-prompt-injection-threat-model
brain_sha256: 5167005d4492cef98603d9013da395d5d7d2bc9b79bdc2bf90318c7f1d67d210
depends_on: null
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
id: risk-005-prompt-injection-threat-model
priority: high
question_en: Does the system identify the surfaces through which direct or indirect
  prompt injection can influence the model, memory, retrieval, planning or tool calls?
question_fr: Le système identifie-t-il les surfaces par lesquelles une injection de
  prompt directe ou indirecte peut influencer le modèle, la mémoire, la récupération
  documentaire, la planification ou les appels d’outils ?
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: be036-src-0026-p0010-ec-005
  id: brain-87877bbabc25c47d
  locator: Page 10
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: d1be278acb738a07bc9c1e9b40bf34996aa983b63d9c5227d69a4b36df286c6c
  unit_path: ingest/SRC-0026/units/p0010.md
  unit_sha256: 1e079b84e0c06cb6adea796baf5670389e5347c345fc5f90af0272fb5090936e
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: be036-src-0026-p0010-ec-006
  id: brain-8b21a9b83de61fab
  locator: Page 10
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: d1be278acb738a07bc9c1e9b40bf34996aa983b63d9c5227d69a4b36df286c6c
  unit_path: ingest/SRC-0026/units/p0010.md
  unit_sha256: 1e079b84e0c06cb6adea796baf5670389e5347c345fc5f90af0272fb5090936e
- authority: GUIDANCE
  brain_source_id: SRC-0027
  evidence_ref: be036-src-0027-p0033-ec-012
  id: brain-8b340b40e1245a51
  locator: Page 33
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 054d918a5b79cb9e264043f31974db49387db3cf85b4cf85722c1b303e90cfd6
  unit_path: ingest/SRC-0027/units/p0033.md
  unit_sha256: e9573b439fb81438f806fd0b6eaf24be71c66ed4a8a59e95b1ab2760f082c6f5
- authority: GUIDANCE
  brain_source_id: SRC-0027
  evidence_ref: be036-src-0027-p0011-ec-011
  id: brain-96f4e0cc80381b72
  locator: Page 11
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 62af7b9b2d37dd3b5410c093ef81c904113d9cc25eb787ea347dc001a80e72bb
  unit_path: ingest/SRC-0027/units/p0011.md
  unit_sha256: 9dad2c1b3933450b0cb3b6a515f0adaa3650d598a533927bb59f631f3a84dcaf
- authority: GUIDANCE
  brain_source_id: SRC-0027
  evidence_ref: be036-src-0027-p0010-ec-009
  id: brain-9f266cb0abe5b7e3
  locator: Page 10
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 3d103366f2e5b82835826f96e87c7fd530df1114abfc5af2e1d530ba5adab8c1
  unit_path: ingest/SRC-0027/units/p0010.md
  unit_sha256: 5d43e8b7084a31babde002d2a45bf3c4dcacf0c7df6cf7c52c801c936a115bcd
- authority: GUIDANCE
  brain_source_id: SRC-0026
  evidence_ref: be036-src-0026-p0011-ec-007
  id: brain-b8b9fc824a0a38ac
  locator: Page 11
  resource: /references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md
  unit_file_sha256: 4c999333e6d421b9c504f9189e54a7b69131f9dbd000038868328c5701c731d9
  unit_path: ingest/SRC-0026/units/p0011.md
  unit_sha256: 66c2b463e56b8e23a41fb97fba09c5445f366c2e0bc97abf28da1132ce66d31a
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
- prompt-injection
title: Prompt injection threat model
topic: prompt-injection-threat-model
type: question
---


# Prompt injection threat model

## Purpose

This question checks whether prompt injection has been treated as a concrete threat model covering direct and indirect inputs, propagation, context, memory and agent execution surfaces.

Section evidence: [^brain-87877bbabc25c47d] [^brain-8b21a9b83de61fab] [^brain-9f266cb0abe5b7e3] [^brain-b8b9fc824a0a38ac]

## Guidance

Answer "yes" only when the assessment identifies the relevant user, document, retrieval, tool-output, memory and external-data paths, considers how an injected instruction could propagate, and records the privileges or actions reachable through the model or agent.

The assessment should also consider validation, least privilege, human gates and monitoring as control points where applicable. OWASP examples describe threat surfaces and control guidance; they do not establish that every system is vulnerable or that one control is universally required.

Section evidence: [^brain-8b340b40e1245a51] [^brain-96f4e0cc80381b72] [^brain-db63174bab64260c]

## Related Knowledge

- [prompt-injection](/concepts/prompt-injection.md)
- [genai-guardrails](/concepts/genai-guardrails.md)

## Source References

- SRC-0026, pages 10-12, for direct and indirect prompt injection surfaces, threat-model dimensions and possible impact paths.
- SRC-0027, pages 10-11, for agent goal hijack, untrusted inputs and agentic propagation.


[^brain-87877bbabc25c47d]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 10.
[^brain-8b21a9b83de61fab]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 10.
[^brain-8b340b40e1245a51]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 33.
[^brain-96f4e0cc80381b72]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 11.
[^brain-9f266cb0abe5b7e3]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 10.
[^brain-b8b9fc824a0a38ac]: [SRC-0026](/references/src-0026-ef87993a4e50ae9d83b41ff7a3d3e6320a82dfa8d4ec6bf98d0ce264b2e6108e.md); locator: Page 11.
[^brain-db63174bab64260c]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 11.
