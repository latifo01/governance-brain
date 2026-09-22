---
aliases:
- Air Canada chatbot case
- Chatbot liability case
brain_id: 2022-air-canada-chatbot
brain_sha256: ccb882c8234cd24a76c366046c15aaaf49d7616147d10ff6f133947c33a519d4
domains:
- AI
- RISK
- LEGAL
evidence_sources:
- AI_NICE_TO_KNOW
- AI_LEGAL_GUIDANCE
id: 2022-air-canada-chatbot
status: stable
tags:
- famous-ai-incidents
- liability
- conversational-ai
title: Air Canada chatbot case (2022)
type: knowledge
---


# Air Canada chatbot case (2022)

## Summary

A documented case reported by CoSAI: in 2022, a passenger asked an airline's website chatbot about bereavement fares and was given information that contradicted the airline's actual bereavement policy. The airline refused to honor the chatbot's claim; the passenger sued. A Canadian court held the airline responsible for the chatbot's representation and ordered payment of CAD 812.02 in damages.

The corpus's reference list identifies the case as the Air Canada chatbot case; the body text anonymizes the airline.

## Applicability

This incident is governance evidence that an organization can be held liable for representations made by its customer-facing chatbot: a chatbot is treated as the organization's agent, not as a disclaimable information service.

## Governance Considerations

- Treat chatbot outputs as organizational representations; contract terms attempting to disclaim them may fail.
- Control the gap between chatbot answers and actual policy: grounding, retrieval from authoritative sources, and human escalation for material claims (see [genai-guardrails](/concepts/genai-guardrails.md), [human-oversight](/concepts/human-oversight.md)).
- Include conversational channels in incident response and claims handling; record chatbot transcripts as evidence.
- This connects to [hallucinations](/concepts/hallucinations.md): the failure mode was a confident, wrong answer on a material term.

## Limits

The corpus documents the case anonymously in the body text with the airline named only in the reference list; details commonly reported elsewhere (passenger name, tribunal instance, 2024 ruling date, appeal) are not in the local corpus and are not asserted here. The case rests on a single documented source; treat it as an illustrative incident, not a body of case law.

## Related Concepts

- [2023-chevrolet-of-watsonville](/concepts/2023-chevrolet-of-watsonville.md) is the companion commercial-chatbot incident in the same source.
- [hallucinations](/concepts/hallucinations.md) covers the underlying failure mode.
- [human-oversight](/concepts/human-oversight.md) and [genai-guardrails](/concepts/genai-guardrails.md) are the mitigating controls.

## Source References

- SRC-0029, CoSAI AI Shared Responsibility Framework, page 6 (national carrier sued after failing to honor a chatbot claim contradicting its bereavement policy; court held the airline responsible; CAD 812.02), page 33 (reference identifying the Air Canada chatbot case).
