---
aliases:
- Human oversight
- Supervision humaine
- Contrôle humain
brain_id: human-oversight
brain_sha256: 670155d1aae9f25e113c1ae1653166c9241e7a60904914fa6227ef0826f322ce
domains:
- AI
- RISK
- LEGAL
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: human-oversight
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be036-src-0039-p0045-ec-015
  id: brain-3a2861a95a3ee288
  locator: Page 45
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 6c471013c7e708e3795cf6420ba5df75cc32dabad343f437d4c55cf5be8f6ab7
  unit_path: ingest/SRC-0039/units/p0045.md
  unit_sha256: 297d8959055aa6adddf8a80417c9068d7a9b2958d098417e20ff798b8e56f1a0
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be036-src-0039-p0032-ec-014
  id: brain-7f7ca0c3c2cde78c
  locator: Page 32
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 3fb08605b67176fe71e367f627b72a5b557a50e19ed8d048a64271e490d3b54d
  unit_path: ingest/SRC-0039/units/p0032.md
  unit_sha256: 4d6d21a07d29ce58c5e16dd5acd6c0cbe08e8a08e43f18b968eabfe92132bb57
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
- human-oversight
- ai-act
- governance
title: Human oversight
type: knowledge
---


# Human oversight

## Summary

Human oversight is a governance process in which human roles, responsibilities and intervention mechanisms are defined, assessed and documented for the relevant AI use. NIST describes human-AI configurations as ranging from autonomous to manual and emphasises that the appropriate arrangement depends on context.

Effective oversight requires more than naming a reviewer. The design should make the reviewer’s information, competence, authority, time, escalation route and ability to challenge or stop an action explicit.

Section evidence: [^brain-3a2861a95a3ee288] [^brain-b07aa31f608be7a0]

## Applicability

Oversight is particularly relevant where an AI system can influence material decisions, change goals, call tools, access sensitive information, modify records or propagate outputs to other systems. The appropriate degree and form of oversight should follow the risk context and the system’s human-AI configuration.

For agentic systems, high-impact or goal-changing actions may warrant a human gate, output validation and scoped access. These are control-design recommendations from security guidance and should be assessed against the system’s actual authority and consequences.

Section evidence: [^brain-3a2861a95a3ee288] [^brain-7f7ca0c3c2cde78c] [^brain-db63174bab64260c]

## Governance Considerations

A reviewable oversight design should:

- define the human roles and responsibilities for decision-making, supervision, escalation and intervention;
- document the information, uncertainty, limitations and context available to the reviewer;
- assess competence, training, time, authority and the ability to interrupt, reject or defer an output;
- apply human approval gates, output validation, isolation and monitoring where downstream impact warrants them;
- record oversight decisions and test whether the workflow creates automation bias or makes rejection impracticable.

The design should be assessed and documented under the organization’s governance process. OWASP recommendations for human approval and NIST expectations for documented oversight are non-binding guidance and framework material.

Section evidence: [^brain-3a2861a95a3ee288] [^brain-7f7ca0c3c2cde78c] [^brain-8b340b40e1245a51] [^brain-b07aa31f608be7a0] [^brain-db63174bab64260c]

## Limits

NIST AI RMF is a voluntary framework and does not itself create legal obligations. OWASP guidance describes security controls rather than a universal oversight pattern. This note deliberately does not generalize the unresolved real-time remote biometric identification pages from SRC-0016; no AI Act obligation or universal two-person rule is asserted here.

Section evidence: [^brain-3a2861a95a3ee288] [^brain-b07aa31f608be7a0]

## Related Concepts

- [genai-guardrails](/concepts/genai-guardrails.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [red-teaming](/concepts/red-teaming.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)

## Source References

- SRC-0039, pages 32 and 45, for documented human oversight processes, differentiated human-AI roles and contextual configurations.
- SRC-0027, pages 11 and 33, for human approval of high-impact or goal-changing actions and human gates before high-risk outputs propagate.
- SRC-0026, pages 10-12, for the agentic and privilege-related attack context that can make human gates relevant.


[^brain-3a2861a95a3ee288]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 45.
[^brain-7f7ca0c3c2cde78c]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 32.
[^brain-8b340b40e1245a51]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 33.
[^brain-b07aa31f608be7a0]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 32.
[^brain-db63174bab64260c]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 11.
