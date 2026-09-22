---
aliases:
- AIUC-1
- Agentic AI security controls crosswalk
brain_id: aiuc-1
brain_sha256: 13f18d9cc24b9efdd93343607b405ab7db6eedf66b7b4c7bc4aca63faead60ae
domains:
- AI
- RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: aiuc-1
sources:
- authority: UNCLASSIFIED
  brain_source_id: SRC-0023
  evidence_ref: provenance-repair-20260920-src-0023-p0006
  id: brain-1aff32f3fcd2243e
  locator: Page 6
  resource: /references/src-0023-72fec19e8954c5f548dc12eb1ae74ceb2f7c3877b1a2f0bf6c29f054bcb91d43.md
  unit_file_sha256: 51fa812f60c62bc70feef1928e3fe1edd8e7a6318340e68fe21f44e8cbf12f2c
  unit_path: ingest/SRC-0023/units/p0006.md
  unit_sha256: 258f14023a504bdff3778c0c00051562db5297506489b7feb2a0e2ab06810c5a
- authority: UNCLASSIFIED
  brain_source_id: SRC-0023
  evidence_ref: provenance-repair-20260920-src-0023-p0005
  id: brain-76d60e2b65063d20
  locator: Page 5
  resource: /references/src-0023-72fec19e8954c5f548dc12eb1ae74ceb2f7c3877b1a2f0bf6c29f054bcb91d43.md
  unit_file_sha256: 3db7af74ac5c1bfb22d7bb51c74cc612fab22bdb6fc17ddf3731722ef37b6ae2
  unit_path: ingest/SRC-0023/units/p0005.md
  unit_sha256: 2edadd7725f4d9dc0bb773b3551bef45f95f3f33d5cfdcd38a9fd36f1549b95f
status: stable
tags:
- norms-frameworks
- agentic-security
- controls
title: AIUC-1
type: knowledge
---


# AIUC-1

## Summary

AIUC-1 is a security, safety and reliability standard for AI agents, organized across six principles: Data & Privacy, Security, Safety, Reliability, Accountability, and Society. The local corpus documents it through a bidirectional crosswalk (AIUC-1 Crosswalks) mapping AIUC-1 to the OWASP Top 10 for Agentic Applications (2026), including a gap analysis identifying eight gaps and mapping appendices.

The mapping methodology distinguishes Primary and Secondary mappings with eight rationale codes such as PREV (preventive), DETECT (detective) and GOVERN (governance).

Section evidence: [^brain-1aff32f3fcd2243e] [^brain-76d60e2b65063d20]

## Applicability

This note applies to organizations selecting and justifying controls for agentic AI systems: the crosswalk connects a principle-based standard with a practitioner risk taxonomy, enabling control coverage arguments for [agentic-ai](/concepts/agentic-ai.md) deployments.

Section evidence: [^brain-1aff32f3fcd2243e] [^brain-76d60e2b65063d20]

## Governance Considerations

- Use the six principles as the control objectives for agent governance; use the crosswalk to check coverage against the OWASP agentic Top 10.
- Track the eight identified gaps as accepted risk items: areas where neither framework provides a mapped control.
- Record mapping rationale codes (PREV/DETECT/GOVERN) in control matrices so reviewers can distinguish preventive, detective and governance intent.

Section evidence: [^brain-1aff32f3fcd2243e] [^brain-76d60e2b65063d20]

## Limits

The corpus contains the crosswalk document, not the full AIUC-1 standard text; the principles are evidenced, the full control clauses are not locally reproduced. The crosswalk edition reflects the 2026 OWASP agentic list and ages with it.

Section evidence: [^brain-1aff32f3fcd2243e] [^brain-76d60e2b65063d20]

## Related Concepts

- [agentic-ai](/concepts/agentic-ai.md) is the system class the controls address.
- [genai-guardrails](/concepts/genai-guardrails.md) operationalizes preventive/detective controls around model inputs and outputs.
- [mitre-atlas](/concepts/mitre-atlas.md) supplies the attacker-side techniques these controls must resist.
- [prompt-injection](/concepts/prompt-injection.md) is the dominant agentic risk the crosswalk maps.

Section evidence: [^brain-1aff32f3fcd2243e] [^brain-76d60e2b65063d20]

## Source References

- SRC-0023, AIUC-1 Crosswalks OWASP Top 10 for Agentic Applications, page 5 (AIUC-1 defined as a security, safety and reliability standard for AI agents with six principles: Data & Privacy, Security, Safety, Reliability, Accountability, Society; bidirectional crosswalk with OWASP agentic Top 10 2026; eight identified gaps), page 6 (mapping methodology: Primary/Secondary mappings, eight rationale codes including PREV, DETECT, GOVERN).


[^brain-1aff32f3fcd2243e]: [SRC-0023](/references/src-0023-72fec19e8954c5f548dc12eb1ae74ceb2f7c3877b1a2f0bf6c29f054bcb91d43.md); locator: Page 6.
[^brain-76d60e2b65063d20]: [SRC-0023](/references/src-0023-72fec19e8954c5f548dc12eb1ae74ceb2f7c3877b1a2f0bf6c29f054bcb91d43.md); locator: Page 5.
