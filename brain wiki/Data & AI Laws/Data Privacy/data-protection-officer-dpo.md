---
id: data-protection-officer-dpo
title: Data Protection Officer (DPO)
type: knowledge
domains: [DATA_PROTECTION, LEGAL, PROCESS]
status: active
aliases:
  - DPO
  - Data Protection Officer
  - Délégué à la protection des données
tags:
  - data-protection
  - governance-roles
  - privacy
evidence_sources: [DATA_AI_CLASSIFICATION, AI_LEGAL_GUIDANCE]
---

# Data Protection Officer (DPO)

## Summary

The GDPR (Articles 37-39) requires the designation of a Data Protection Officer where: the processing is carried out by a public authority, or where core activities consist of large-scale regular and systematic monitoring of data subjects, or large-scale processing of special categories. The DPO's position is functionally independent: no instructions are received regarding their tasks, they cannot be dismissed or penalized for performing them, they report directly to the highest management level, they are provided resources and secrecy obligations apply, and conflicts of interest with other roles must be avoided.

The DPO's tasks are to inform and advise, to monitor compliance, to advise on data protection impact assessments, and to cooperate with and act as contact point for the supervisory authority.

## Applicability

This note applies to AI governance organization design: AI systems processing personal data at scale typically trigger DPO involvement — in advising on AI-related DPIAs, lawful bases and automated decision safeguards.

## Governance Considerations

- Check designation criteria early in AI program design; large-scale AI-driven monitoring or special-category processing commonly triggers them.
- Guarantee the independence guarantees in the role charter: reporting line, no dismissal for task performance, resources, conflict-of-interest avoidance (the DPO should not also decide purposes and means of processing).
- Route AI privacy reviews ([[data-protection-impact-assessments-dpia]]) through the DPO for advice, not for signature-only approval.

## Limits

This note reports the GDPR articles; sector-specific DPO regimes and national variations are not locally evidenced. The Digital Omnibus proposal does not change these designation rules in the corpus.

## Related Concepts

- [[gdpr]] is the governing statute.
- [[data-protection-authority-dpa]] is the supervisory counterpart the DPO cooperates with.
- [[data-protection-impact-assessments-dpia]] is the mechanism the DPO advises on.
- [[human-oversight]] is the general counterpart for AI decisions; the DPO advises on privacy, not on every AI gate.

## Source References

- SRC-0010, GDPR, page 55 (Article 37: designation criteria — public authorities, large-scale regular and systematic monitoring, large-scale special-category processing), pages 55-56 (Article 38: independence — no instructions, no dismissal or penalty, direct reporting to highest management, resources, secrecy, conflict-of-interest avoidance), page 56 (Article 39: tasks — inform and advise, monitor compliance, DPIA advice, cooperation with supervisory authorities).
