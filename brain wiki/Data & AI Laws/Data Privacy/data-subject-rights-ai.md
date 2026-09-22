---
id: data-subject-rights-ai
title: Data subject rights in AI processing
type: knowledge
domains: [DATA_PROTECTION, LEGAL, AI, PROCESS]
status: active
aliases:
  - AI data subject rights
  - Data subject rights in AI systems
  - Droits des personnes dans les traitements IA
tags:
  - data-protection
  - data-subject-rights
  - ai-governance
  - automated-decision-making
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
---

# Data subject rights in AI processing

## Summary

The GDPR rights framework applies to personal-data processing performed with
AI systems. It includes access to personal data and processing information,
rectification, erasure, restriction, portability, objection and safeguards for
solely automated decisions that produce legal or similarly significant effects.
The applicable right depends on the processing, legal basis, decision context
and the facts of the request; the presence of an AI component does not by
itself determine the answer (SRC-0010, pages 43-46).

## Applicability

Use this note when an AI system processes personal data at any lifecycle stage,
including input, retrieval, output, evaluation or monitoring. Route the
assessment to [[data-protection-impact-assessments-dpia]] where the processing
risk may require a DPIA, and to [[gdpr-article-22-automated-decision-making]]
when an individual outcome may be based solely on automated processing.

## Rights map

- Article 15 covers confirmation of processing, access and information about
  purposes, categories, recipients, retention, other rights, complaints, data
  source and automated decision-making; it also covers a copy of the data and
  information about safeguards for third-country transfers.
- Articles 16-18 cover rectification, erasure and restriction, with conditions
  and exceptions that must be assessed against the processing context.
- Article 19 addresses notification to recipients of rectification, erasure or
  restriction where applicable.
- Article 20 covers portability for qualifying automated processing based on
  consent or contract, subject to its conditions and limits.
- Article 21 covers objection, including specific rules for direct marketing.
- Article 22 addresses solely automated decisions with legal or similarly
  significant effects and requires the applicable safeguards to be identified
  where an exception is relied on.

These provisions are the operative GDPR text and their applicability must be
checked individually; this list is a routing map rather than a conclusion about
any particular system (SRC-0010, pages 43-46).

## Governance considerations

Maintain a rights-handling record that identifies the processing operations,
systems and suppliers in scope, the controller or controllers, applicable
legal bases, response owner, escalation route, relevant recipients and any
automated decision-making path. Connect the record to the [[data-subject-access-requests]]
process and to [[data-protection-officer-dpo]] advice where relevant.

For AI systems, the record should show how requests and objections are routed
across the data stores and processing stages in scope. Where Article 22 may
apply, record the decision process, the Article 22 condition relied upon and
the measures supporting human intervention, the person's point of view and
contestation (SRC-0010, pages 43-46).

## Limits and uncertainties

This note states the rights and conditions visible in the reviewed GDPR units.
It does not determine whether a particular model memorises personal data,
which national restrictions apply, how competing rights should be balanced,
or whether a particular request must be granted. Those questions require a
fact-specific review and, where appropriate, DPO or legal advice. The reviewed
units do not establish current supervisory interpretations or implementation
dates beyond the text captured in the source.

## Related concepts

- [[data-subject-access-requests]]
- [[gdpr-article-22-automated-decision-making]]
- [[data-protection-impact-assessments-dpia]]
- [[fundamental-right-impact-assessment-fria]]
- [[data-protection-officer-dpo]]

## Source references

- SRC-0010, page 43, for Article 15 access and information rights, transfer safeguards and copies.
- SRC-0010, pages 43-44, for rectification, erasure and restriction.
- SRC-0010, page 45, for notification, portability and objection.
- SRC-0010, page 46, for automated decision-making safeguards and restrictions.
