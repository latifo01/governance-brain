---
id: ai-model-transparency
title: AI model transparency
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - AI model transparency
  - Model transparency
tags:
  - ai-risk-mitigations
  - transparency
  - disclosure
evidence_sources: [AI_NICE_TO_KNOW, AI_ACT]
---

# AI model transparency

## Summary

AI model transparency has two evidenced senses that governance must keep distinct.

**Practice transparency (documentation and disclosure of model behavior).** The Microsoft Responsible AI Transparency Report documents how a major AI provider publishes its responsible AI program: mapping of released generative models, measurement of harmful content across modalities, red-teaming coverage, and safety systems deployed in production. Transparency here means producing and publishing evidence about how models are built, evaluated and guarded.

**Operational transparency (AI Act Article 50 obligations).** The Commission's Article 50 guidelines document disclosure duties for deployers of certain AI systems: informing users that they are interacting with an AI system unless obvious, marking synthetic audio, image, video or text content in machine-readable form (including deepfakes and, in defined cases, publication contexts), and notifying people exposed to emotion-recognition or biometric-categorisation systems. The guidelines state the objective of the Article 50(2) transparency obligation and interpret its scope for affected systems.

## Applicability

The first sense applies to model providers and system builders producing evaluation evidence (connects to [[ai-model-documentation]] and [[ai-model-validation]]). The second applies to deployers of AI systems within Article 50's scope; it is a legal expectation for the covered systems, not a voluntary practice.

## Governance Considerations

- Separate transparency duties by role: provider disclosure (documentation, evaluations) versus deployer disclosure (user notification, content marking).
- For systems covered by Article 50, identify which obligation applies (AI-interaction disclosure, synthetic content marking, emotion-recognition notification) and implement it in the product surface, not only in policy documents.
- Publish or retain evaluation evidence at the depth your role requires; measurement without disclosure is not transparency for providers.
- Machine-readable marking of synthetic content is an engineering requirement, not a disclaimer.

## Limits

The Article 50 obligations as described here cover the general shapes documented in the guidelines; system-specific determinations route through the AI Act Knowledge Bank. Vendor transparency practice is documented as one provider's practice, not a norm for all providers.

## Related Concepts

- [[ai-model-documentation]] carries the evidence artifacts that practice transparency discloses.
- [[toxic-or-biased-outputs]] describes what measurement must cover for transparency claims to be meaningful.
- [[eu-ai-act]] is the legal framework behind Article 50.

## Source References

- SRC-0009, Microsoft Responsible AI Transparency Report, page 10 (measurement pipelines, evaluator annotation, harmful-content metrics) and page 16 (red teaming across modalities), documenting published transparency practice.
- SRC-0018, Guidelines on transparency obligations under Article 50 of the AI Act, page 24 (Article 50(2) transparency objective and interpretation) and page 50 (scope of the obligations and market surveillance context).
