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

In this Brain, FRIA is treated as a deployer-side governance artifact. It complements technical documentation and model validation, but it is not the same thing as a [[data-protection-impact-assessments-dpia]]. The DPIA focuses on personal data processing risks; the FRIA focuses on the impact that the use of a high-risk AI system may produce on fundamental rights.

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

For a CDO, these elements should be translated into an operating artifact with clear owners. Legal should confirm scope and rights analysis. Risk or model governance should challenge severity, likelihood and control design. Business ownership should describe the real process and decision points. Data protection should align DPIA overlaps where personal data are processed.

## Governance decisions

A useful FRIA decision record should answer:

- whether the system is high-risk under Article 6 and Annex III;
- whether the deployer falls into an Article 27 category;
- whether the planned use differs from the provider’s intended purpose;
- which affected groups are exposed to the system in practice;
- whether the [[human-oversight]] model gives trained people authority to intervene, override or stop use;
- whether complaint and escalation mechanisms are operational before deployment;
- whether changes during use require the FRIA to be updated.

## Relationship with DPIA

The AI Act text states that where an Article 27 obligation is already met through a DPIA under GDPR Article 35 or the law-enforcement data protection directive, the FRIA complements that DPIA. This matters operationally: a DPIA can reduce duplication, but it should not be assumed to cover fundamental-rights impacts that sit outside personal-data protection.

## Limits and uncertainties

The academic FRIA source reviewed in the draft folder is useful for critique and methodology, but this lot relies primarily on the official AI Act text and EDPB training material. Methodological claims about best-practice FRIA design should be expanded in a later lot only after reviewing the academic article in more depth.

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
