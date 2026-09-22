---
id: nist-ai-rmf
title: NIST AI Risk Management Framework
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - NIST AI RMF
  - AI RMF
  - NIST AI 100-1
tags:
  - norms-frameworks
  - risk-management
  - trustworthiness
evidence_sources: [AI_NICE_TO_KNOW]
---

# NIST AI Risk Management Framework

## Summary

The NIST AI Risk Management Framework (AI RMF 1.0, NIST AI 100-1) presents AI risk management as a key component of responsible AI development and a path to trustworthy AI. Its Core defines four high-level functions — GOVERN, MAP, MEASURE, MANAGE — broken into categories and subcategories, with governance as a cross-cutting function applied throughout.

The framework enumerates the characteristics of trustworthy AI: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed.

## Applicability

This note applies to any organization seeking a function-based taxonomy for AI risk: GOVERN (policies, roles, risk tolerance), MAP (context and risk identification), MEASURE (analysis and metrics), MANAGE (prioritized response). The companion Playbook (SRC-0040) provides suggested actions per category, including impact assessment policies (see [[ai-impact-assessment-aiia]]).

## Governance Considerations

- Use the four functions as the process spine; map existing controls onto categories rather than duplicating them.
- Treat trustworthiness characteristics as measurable targets; several correspond to Brain risk notes ([[toxic-or-biased-outputs]], [[data-leakage]], [[hallucinations]]).
- GOVERN is cross-cutting: decision rights and accountability (see [[human-oversight]]) precede measurement.

## Limits

The framework is voluntary guidance, not law; it does not create obligations. Adoption does not substitute for the regulatory requirements routed through the AI Act Knowledge Bank.

## Related Concepts

- [[iso-23894]] and [[iso-42001]] are the ISO counterparts for risk guidance and management systems.
- [[ai-impact-assessment-aiia]] is a MEASURE/GOVERN mechanism recommended by the companion Playbook.
- [[mitre-atlas]] covers the adversarial threat landscape the MEASURE function can draw on.

## Source References

- SRC-0039, NIST AI RMF 1.0 (NIST AI 100-1), page 6 (executive summary: AI risk management as key component of responsible development), page 17 (trustworthy AI characteristics), pages 25-26 (Core: four functions, governance cross-cutting), page 29 (MAP), page 33 (MEASURE), page 36 (MANAGE).
- SRC-0040, NIST AI RMF Playbook, pages 26-27 (GOVERN 4: impact assessment policies and suggested actions).
