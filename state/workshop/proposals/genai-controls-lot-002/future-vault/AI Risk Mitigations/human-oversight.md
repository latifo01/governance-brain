---
id: human-oversight
title: Human oversight
type: knowledge
domains: [AI, RISK, LEGAL, PROCESS]
status: active
aliases:
  - Human oversight
  - Supervision humaine
  - Contrôle humain
tags:
  - human-oversight
  - ai-act
  - governance
evidence_sources: [AI_ACT, AI_NICE_TO_KNOW]
---

# Human oversight

## Summary

Human oversight is the governance arrangement that enables natural persons to understand, supervise, challenge, intervene in, approve, override or stop an AI system where the context requires human control. It is not the mere presence of a human in a workflow. Oversight must be designed with competence, authority, information, time, escalation routes and resistance to automation bias.

For high-risk AI systems under the EU AI Act, human oversight has a specific legal role. For broader AI governance, NIST AI RMF frames human oversight as a process to be defined, assessed and documented according to organizational policies and risk context.

## Applicability

Human oversight is most relevant when AI outputs influence material decisions, safety, fundamental rights, legal effects, access to services, operational control, financial movement, employment, law enforcement, healthcare, or other high-consequence domains. Some low-impact AI systems may not require human oversight, while others require strong oversight by law or risk policy.

For agentic AI, oversight becomes especially important where the system can change goals, call tools, spend money, communicate externally, access sensitive information, modify records, or propagate outputs to other systems. In those cases, [[genai-guardrails]] and [[ai-model-monitoring]] should support the human reviewer rather than replace judgment.

## Governance Considerations

A strong human oversight design should specify:

- which decisions or actions require human review, approval or escalation;
- what information the human receives about model purpose, limitations, uncertainty and context;
- what authority the human has to override, stop, defer, restrict or reject system output;
- what training and AI literacy are required;
- how automation bias is mitigated through workflow design, time allocation and incentives;
- how oversight decisions are recorded for audit and learning;
- how human review interacts with incident response, appeals and remediation.

The AI Act guidance on prohibited practices discusses human oversight for high-risk systems and, in a specific real-time remote biometric identification context, refers to Article 14 design requirements and Article 14(5) separate verification by at least two competent, trained and authorized natural persons unless the applicable legal exception applies. That narrow example should not be generalized to every AI system.

NIST AI RMF emphasizes that human-AI configurations vary from fully autonomous to fully manual. AI can make decisions, defer to a human expert, or serve as an additional opinion for a human decision maker. The correct oversight model should follow the risk context, not a slogan such as "human in the loop" by default.

## Limits

Human oversight can be ineffective if the human lacks time, expertise, authority or understandable information. It can also fail if the organization rewards fast approval, hides uncertainty, or structures the workflow so that rejecting the AI output is burdensome. Oversight should therefore be tested as a process, not only documented as a role.

Human review does not automatically make an AI decision acceptable, fair or lawful. It must be connected to the applicable legal basis, risk assessment, impact assessment, technical controls, documentation and appeal or remediation mechanisms.

## Related Concepts

- [[genai-guardrails]] can route high-risk outputs and actions to human review.
- [[prompt-injection]] and agent goal hijack scenarios may require human approval before goal-changing or high-impact actions.
- [[red-teaming]] can test whether human reviewers detect manipulation or overreliance.
- [[ai-model-documentation]] should explain the oversight model and record oversight decisions.

## Source References

- SRC-0016, Guidelines on prohibited AI practices under the AI Act, pages 117 and 125. Used for FRIA/human oversight measures, Article 14 references, competence/training/authority, automation-bias considerations and the specific two-person verification context for certain real-time RBI uses.
- SRC-0039, NIST AI RMF 1.0, pages 32 and 45. Used for human oversight being defined, assessed and documented, and for differentiating human roles and human-AI configurations.
- SRC-0027, OWASP Top 10 for Agentic Applications 2026, pages 11 and 33. Used for human approval of high-impact or goal-changing agent actions and human gates before high-risk outputs propagate downstream.

