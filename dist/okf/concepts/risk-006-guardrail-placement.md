---
aliases:
- Guardrail architecture
answer_type: boolean
applies_to: AI
brain_id: risk-006-guardrail-placement
brain_sha256: c08a2b57878070bc9ce53a2f18116e3acaf0a6f18c3164b27bb50c41315436e7
depends_on: null
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: risk-006-guardrail-placement
priority: high
question_en: Are guardrails placed at the relevant control points, including before
  the model, after retrieval, before tool calls, after model output and before downstream
  propagation?
question_fr: Les garde-fous sont-ils placés aux points de contrôle pertinents, notamment
  avant le modèle, après la récupération, avant les appels d’outils, après la sortie
  du modèle et avant toute propagation aval ?
sources:
- authority: UNCLASSIFIED
  brain_source_id: SRC-0039
  evidence_ref: provenance-repair-20260920-src-0039-p0036
  id: brain-2e4b4525d4d1a1c6
  locator: Page 36
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 1f9fd40ed70351959e58dd61c3bfa534684fd68063b8588f38999a16226bcf47
  unit_path: ingest/SRC-0039/units/p0036.md
  unit_sha256: 222e2f94f1578d073561d97026ec51ac4934f8c01be272fddc639e398726a545
- authority: UNCLASSIFIED
  brain_source_id: SRC-0027
  evidence_ref: provenance-repair-20260920-src-0027-p0038
  id: brain-53f655908153bee3
  locator: Page 38
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: e5c424785ae6f7506c33f80078326c620ce3fb7e17db212706a1789c495a1ab6
  unit_path: ingest/SRC-0027/units/p0038.md
  unit_sha256: 390515da16b1932836298c26ad0c515ee062459a9cd484366cb68cf40486ba14
- authority: UNCLASSIFIED
  brain_source_id: SRC-0039
  evidence_ref: provenance-repair-20260920-src-0039-p0038
  id: brain-71ccd7d25286c13a
  locator: Page 38
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: ff1de0e3693819bc5f7068ef4a1481d154d2891deacc1b5ab16e03374914b60f
  unit_path: ingest/SRC-0039/units/p0038.md
  unit_sha256: d3f4eff907102e22e34b18552cff5f1a2cc62a4631a6a9361cff58129a950c2a
- authority: UNCLASSIFIED
  brain_source_id: SRC-0027
  evidence_ref: provenance-repair-20260920-src-0027-p0033
  id: brain-8b4ef3c61a359e98
  locator: Page 33
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 054d918a5b79cb9e264043f31974db49387db3cf85b4cf85722c1b303e90cfd6
  unit_path: ingest/SRC-0027/units/p0033.md
  unit_sha256: e9573b439fb81438f806fd0b6eaf24be71c66ed4a8a59e95b1ab2760f082c6f5
- authority: UNCLASSIFIED
  brain_source_id: SRC-0039
  evidence_ref: provenance-repair-20260920-src-0039-p0037
  id: brain-a9b376e5a0e20630
  locator: Page 37
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 882a5e7f9abe541347758055c17d6c3bc5ff0a03852038df9058f7538db9a681
  unit_path: ingest/SRC-0039/units/p0037.md
  unit_sha256: 70995f881cc7f2563d8f541900ec5d39c94f5d24c14e43d6fb5669d1593101d6
- authority: UNCLASSIFIED
  brain_source_id: SRC-0027
  evidence_ref: provenance-repair-20260920-src-0027-p0011
  id: brain-ae89d977c026b1b1
  locator: Page 11
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 62af7b9b2d37dd3b5410c093ef81c904113d9cc25eb787ea347dc001a80e72bb
  unit_path: ingest/SRC-0027/units/p0011.md
  unit_sha256: 9dad2c1b3933450b0cb3b6a515f0adaa3650d598a533927bb59f631f3a84dcaf
- authority: UNCLASSIFIED
  brain_source_id: SRC-0039
  evidence_ref: provenance-repair-20260920-src-0039-p0035
  id: brain-ba993b3441a2ab14
  locator: Page 35
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 9c378153e475afecb6438fda22c12e7a4d0af0fafe7055b4619a1934f41f2add
  unit_path: ingest/SRC-0039/units/p0035.md
  unit_sha256: 7c2df886cf5671889f4e54cfd1e5097145ed938a3c5ac78ed1e4c151c06ebcef
- authority: UNCLASSIFIED
  brain_source_id: SRC-0039
  evidence_ref: provenance-repair-20260920-src-0039-p0032
  id: brain-fca7e5263d97bd67
  locator: Page 32
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 3fb08605b67176fe71e367f627b72a5b557a50e19ed8d048a64271e490d3b54d
  unit_path: ingest/SRC-0039/units/p0032.md
  unit_sha256: 4d6d21a07d29ce58c5e16dd5acd6c0cbe08e8a08e43f18b968eabfe92132bb57
status: stable
tags:
- questionnaire
- guardrails
title: Guardrail placement
topic: guardrail-placement
type: question
---


# Guardrail placement

## Purpose

This question assesses whether guardrails are embedded in the system architecture rather than treated as a single model-level instruction.

Section evidence: [^brain-2e4b4525d4d1a1c6] [^brain-53f655908153bee3] [^brain-71ccd7d25286c13a] [^brain-8b4ef3c61a359e98] [^brain-a9b376e5a0e20630] [^brain-ae89d977c026b1b1] [^brain-ba993b3441a2ab14] [^brain-fca7e5263d97bd67]

## Guidance

Answer "yes" only when the architecture shows where controls operate, which risks each control addresses, who owns exceptions, and how failures are monitored and remediated.

Section evidence: [^brain-2e4b4525d4d1a1c6] [^brain-53f655908153bee3] [^brain-71ccd7d25286c13a] [^brain-8b4ef3c61a359e98] [^brain-a9b376e5a0e20630] [^brain-ae89d977c026b1b1] [^brain-ba993b3441a2ab14] [^brain-fca7e5263d97bd67]

## Related Knowledge

- [genai-guardrails](/concepts/genai-guardrails.md)
- [prompt-injection](/concepts/prompt-injection.md)

## Source References

- SRC-0027, pages 11, 33 and 38, for input safeguards, human approval, policy gates, output validation, blast-radius controls and monitoring.
- SRC-0039, pages 32 and 35-38, for documented controls, measurement and risk treatment.



[^brain-2e4b4525d4d1a1c6]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 36.
[^brain-53f655908153bee3]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 38.
[^brain-71ccd7d25286c13a]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 38.
[^brain-8b4ef3c61a359e98]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 33.
[^brain-a9b376e5a0e20630]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 37.
[^brain-ae89d977c026b1b1]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 11.
[^brain-ba993b3441a2ab14]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 35.
[^brain-fca7e5263d97bd67]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 32.
