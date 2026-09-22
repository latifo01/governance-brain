---
id: aiuc-1
title: AIUC-1
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - AIUC-1
  - Agentic AI security controls crosswalk
tags:
  - norms-frameworks
  - agentic-security
  - controls
evidence_sources: [AI_NICE_TO_KNOW]
---

# AIUC-1

## Summary

AIUC-1 is a security, safety and reliability standard for AI agents, organized across six principles: Data & Privacy, Security, Safety, Reliability, Accountability, and Society. The local corpus documents it through a bidirectional crosswalk (AIUC-1 Crosswalks) mapping AIUC-1 to the OWASP Top 10 for Agentic Applications (2026), including a gap analysis identifying eight gaps and mapping appendices.

The mapping methodology distinguishes Primary and Secondary mappings with eight rationale codes such as PREV (preventive), DETECT (detective) and GOVERN (governance).

## Applicability

This note applies to organizations selecting and justifying controls for agentic AI systems: the crosswalk connects a principle-based standard with a practitioner risk taxonomy, enabling control coverage arguments for [[agentic-ai]] deployments.

## Governance Considerations

- Use the six principles as the control objectives for agent governance; use the crosswalk to check coverage against the OWASP agentic Top 10.
- Track the eight identified gaps as accepted risk items: areas where neither framework provides a mapped control.
- Record mapping rationale codes (PREV/DETECT/GOVERN) in control matrices so reviewers can distinguish preventive, detective and governance intent.

## Limits

The corpus contains the crosswalk document, not the full AIUC-1 standard text; the principles are evidenced, the full control clauses are not locally reproduced. The crosswalk edition reflects the 2026 OWASP agentic list and ages with it.

## Related Concepts

- [[agentic-ai]] is the system class the controls address.
- [[genai-guardrails]] operationalizes preventive/detective controls around model inputs and outputs.
- [[mitre-atlas]] supplies the attacker-side techniques these controls must resist.
- [[prompt-injection]] is the dominant agentic risk the crosswalk maps.

## Source References

- SRC-0023, AIUC-1 Crosswalks OWASP Top 10 for Agentic Applications, page 5 (AIUC-1 defined as a security, safety and reliability standard for AI agents with six principles: Data & Privacy, Security, Safety, Reliability, Accountability, Society; bidirectional crosswalk with OWASP agentic Top 10 2026; eight identified gaps), page 6 (mapping methodology: Primary/Secondary mappings, eight rationale codes including PREV, DETECT, GOVERN).
