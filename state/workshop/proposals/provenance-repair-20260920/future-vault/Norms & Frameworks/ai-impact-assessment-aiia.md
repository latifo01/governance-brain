---
id: ai-impact-assessment-aiia
title: AI impact assessment (AIIA)
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - AIIA
  - AI impact assessment
  - Algorithmic impact assessment
tags:
  - norms-frameworks
  - impact-assessment
  - governance-gates
evidence_sources: [AI_NICE_TO_KNOW, AI_ACT]
---

# AI impact assessment (AIIA)

## Summary

An AI impact assessment (AIIA) is a structured assessment of the risks and effects of an algorithm or AI deployment, used to frame risks, support go/no-go decisions and drive responsible development practices. The NIST AI RMF Playbook presents impact assessments as an approach that may be iterative and multi-stakeholder, and recommends establishing impact assessment policies aligned with legal requirements.

A documented implementation is the Canadian Algorithmic Impact Assessment Tool: a raw impact score built from six indicators (Project, System, Algorithm, Decision, Impact, Data), combined with a mitigation score. The local corpus also documents a typology of impact assessments distinguishing human rights impact assessments, the AI Act's fundamental rights impact assessment (FRIA), and the GDPR's data protection impact assessment (DPIA).

## Applicability

This note applies to any organization instituting pre-deployment assessment gates for AI systems. AIIA is the general mechanism; FRIA and DPIA are its legal specializations for high-risk AI systems and personal-data processing respectively.

## Governance Considerations

- Establish a policy-level requirement for impact assessments (NIST GOVERN 4) rather than ad-hoc assessments per project.
- Score-based tools (raw impact + mitigation) make the gate auditable; record both scores and the go/no-go decision.
- Map each AI deployment to the applicable specialized assessment: FRIA where the AI Act requires it, DPIA where GDPR requires it (see [[fundamental-right-impact-assessment-fria]] and [[data-protection-impact-assessments-dpia]]); do not treat one as substituting for the other.

## Limits

AIIA as a general practice is voluntary; the binding triggers belong to the specialized assessments and remain governed by the AI Act and privacy Knowledge Banks. The Canadian tool is documented as an implementation example, not a requirement.

## Related Concepts

- [[fundamental-right-impact-assessment-fria]] is the AI Act specialization.
- [[data-protection-impact-assessments-dpia]] is the GDPR specialization.
- [[nist-ai-rmf]] recommends AIIA policies under GOVERN.
- [[human-oversight]] governs who decides at the gate.

## Source References

- SRC-0040, NIST AI RMF Playbook, pages 26-27 (GOVERN 4.2: impact assessments as an approach for responsible technology development; iterative, multi-stakeholder, go/no-go support; suggested actions to establish assessment policies aligned with legal requirements).
- SRC-0012, FRIA academic article (Computer Law & Security Review), pages 12-16 (impact-assessment methodology; the Canadian Algorithmic Impact Assessment Tool with six indicators and a mitigation score).
- SRC-0022, SPE training on AI and data protection, page 183 (typology of impact assessments: HRIA, FRIA under AI Act Article 27, DPIA under GDPR Article 35).
