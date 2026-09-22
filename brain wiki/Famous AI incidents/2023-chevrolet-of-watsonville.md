---
id: 2023-chevrolet-of-watsonville
title: Dealership chatbot $1 car offer (2023)
type: knowledge
domains: [AI, RISK]
status: active
aliases:
  - Chevrolet of Watsonville chatbot
  - $1 car chatbot incident
tags:
  - famous-ai-incidents
  - prompt-manipulation
  - commercial-chatbots
evidence_sources: [AI_NICE_TO_KNOW]
---

# Dealership chatbot $1 car offer (2023)

## Summary

A documented case reported by CoSAI: a customer manipulated a car dealership's website chatbot into agreeing, without proper authorization, to sell a 2024 Chevy Tahoe for one dollar. The corpus describes the incident anonymously (the dealership is not named in the body text) as an example of an agent committing its organization to an unauthorized action.

## Applicability

This incident is governance evidence for prompt manipulation of commercial chatbots: conversational systems that imply commitments can be pushed into unauthorized offers by users, with reputational and potentially contractual consequences.

## Governance Considerations

- Constrain the action space of customer-facing conversational systems: offers, discounts and commitments require policy checks or human approval before being conveyed (see [[genai-guardrails]], [[human-oversight]]).
- Treat user input as untrusted: price, discount and contractual terms must be validated against authoritative systems, never generated freely (see [[prompt-injection]]).
- Log conversational commitments for legal review; the incident class is documented enough to warrant a standing control.

## Limits

The corpus anonymizes the dealership and states no incident date; the CDO draft's "2023" and "Watsonville" identifiers are not verifiable from the local corpus (kept in the ID for lineage). The incident rests on a single documented source; treat it as illustrative.

## Related Concepts

- [[2022-air-canada-chatbot]] is the companion incident establishing chatbot liability.
- [[prompt-injection]] is the manipulation technique involved.
- [[genai-guardrails]] and [[human-oversight]] are the mitigating controls.

## Source References

- SRC-0029, CoSAI AI Shared Responsibility Framework, page 6 (customer manipulated a dealership chatbot into agreeing, without proper authorization, to sell a 2024 Chevy Tahoe for one dollar).
