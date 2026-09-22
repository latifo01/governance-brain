---
id: fundamental-right-impact-assessment-fria
title: Fundamental rights impact assessment
type: knowledge
domains: [AI, LEGAL, RISK, PROCESS]
status: active
aliases:
  - FRIA
  - Fundamental Rights Impact Assessment
  - Fundamental Right Impact Assessment
  - AI Act fundamental rights impact assessment
tags:
  - impact-assessment
  - fundamental-rights
  - ai-act
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
---

# Fundamental rights impact assessment

## Summary

A fundamental rights impact assessment, or FRIA, is an AI Act impact-assessment mechanism for certain deployers of certain high-risk AI systems. Its governance function is to force a deployer-specific view of how a high-risk AI system will be used, who may be affected, what harms may materialise, what human oversight is implemented and what internal governance or complaint mechanisms are available.

The FRIA is a deployer-side assessment: Article 27 obliges certain deployers of high-risk AI systems to carry it out (SRC-0022, training-based explanation). It is not the same thing as a [[data-protection-impact-assessments-dpia]]: the two overlap considerably, but the DPIA is grounded in the risks of personal-data processing, while the FRIA addresses the impact that the use of a high-risk AI system may produce on fundamental rights (SRC-0022, training-based explanation).

## Applicability

The reviewed AI Act text requires a FRIA before deployment for specified deployers of high-risk AI systems referred to in Article 6(2), except the Article 27 exclusion for Annex III point 2. It applies to deployers that are public-law bodies or private entities providing public services, and to deployers of the specific Annex III point 5(b) and 5(c) high-risk systems concerning creditworthiness/credit scoring and life or health insurance risk assessment and pricing.

This note should therefore trigger a governance question, not an automatic legal conclusion. A project must first establish the AI Act classification through [[eu-ai-act]], then determine the deployer role, Annex III category and sector context.

## Required assessment content

The reviewed official text requires the assessment to include:

- a description of the deployer processes in which the high-risk AI system will be used according to its intended purpose;
- the period and frequency of intended use;
- the categories of natural persons and groups likely to be affected in the specific context;
- the specific risks of harm likely to affect those people or groups, taking account of information supplied by the provider;
- a description of the implementation of human oversight measures;
- measures to be taken if those risks materialise, including internal governance and internal complaint mechanisms.

These elements should be recorded as an operating artifact covering the first use, and updated during use whenever an element changes or is no longer up to date (Article 27(2)). Where personal data are processed, the work done for the [[data-protection-impact-assessments-dpia]] is relevant to the FRIA and the two assessments should be aligned rather than duplicated (SRC-0022, training-based explanation). The human-oversight and complaint-mechanism elements should describe the measures actually implemented, with the provider's information (Articles 27(1)(e) and (f)).

## Governance decisions

A FRIA decision record should answer:

- whether the system is high-risk under Article 6(2) and Annex III;
- whether the deployer falls into an Article 27(1) category;
- whether the planned use follows the provider's intended purpose (Article 27(1)(a));
- which categories of natural persons and groups are likely to be affected in the specific context (Article 27(1)(c));
- whether the [[human-oversight]] measures are implemented according to the instructions for use (Article 27(1)(e));
- whether the internal governance and complaint mechanisms are in place for the risks that may materialise (Article 27(1)(f));
- whether the assessment covers the first use and is updated during use when an element changes or is no longer up to date (Article 27(2)).

## Relationship with DPIA

The AI Act text states that where an Article 27 obligation is already met through a DPIA under GDPR Article 35 or the law-enforcement data protection directive, the FRIA complements that DPIA. This matters operationally: a DPIA can reduce duplication, but it should not be assumed to cover fundamental-rights impacts that sit outside personal-data protection.

## Limits and uncertainties

FRIA methodology varies: there is no single list of elements for human-rights impact assessments, whose methodologies are chosen based on business requirements, while the FRIA's required content is fixed by Article 27 (SRC-0022, training-based explanation). This note records the binding Article 27 content and the training-based explanation only; broader methodological guidance requires a separate reviewed source assignment before stronger claims are made.

## Related concepts

- [[eu-ai-act]]
- [[data-protection-impact-assessments-dpia]]
- [[automatic-decision-making-assessment-adma]]
- [[human-oversight]]
- [[ai-model-documentation]]

## Source references

- SRC-0011, pages 222-224, for Article 27 FRIA scope, required contents, update logic, notification and relationship with DPIA.
- SRC-0022, pages 183-184, for training-based explanation of when FRIA is required and how it relates to other impact assessments.
- SRC-0012, pages 8-10 and 17-18, retained as methodological background requiring deeper review before stronger claims are made.
