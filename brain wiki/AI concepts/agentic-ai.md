---
id: agentic-ai
title: Agentic AI
type: knowledge
domains: [AI]
status: active
aliases:
  - Agentic AI
  - AI agents
  - Autonomous agents
tags:
  - ai-concepts
  - fundamentals
  - agentic-security
evidence_sources: [AI_ACT, AI_NICE_TO_KNOW]
---

# Agentic AI

## Summary

Agentic AI designates AI systems that perform sequences of actions across interconnected tools and data sources to achieve goals, with reduced or minimal human involvement in the intermediate steps. The term has no legal definition in the EU AI Act: the legislature chose a functional, technology-neutral definition in Article 3(1) and regulates AI systems, not architectural patterns. An AI agent nonetheless satisfies every element of that definition and is characterized, per the EDPS and European Commission descriptions, as a system acting autonomously with limited human interaction to fulfil goals rather than isolated tasks, capable of reasoning, planning and coordinating actions in changing environments.

The distinguishing functional characteristics are: (i) planning and task decomposition — breaking a high-level goal into sub-tasks and determining execution order; (ii) external tool invocation via APIs, databases, code interpreters, web browsers or other software, which is the critical differentiator from a standalone large language model; (iii) autonomous execution of intermediate steps without human approval for each one, with the degree of autonomy ranging from per-action confirmation to fully autonomous operation.

The governance consequence is that identical agent architectures produce radically different regulatory profiles depending on deployment: an agent screening CVs triggers high-risk classification under the AI Act, while an agent summarizing meeting notes triggers only transparency obligations. The technology is identical; the regulatory consequence diverges completely.

## Applicability

This concept frames LLM-based agents, copilots with tool access, multi-agent systems and orchestration layers. Risk increases with the breadth of tool and data access, the autonomy level of intermediate steps, and the materiality of the actions the agent can influence.

Agent-specific security concerns are documented in the OWASP Top 10 for Agentic Applications 2026: goal hijacking through manipulated natural-language inputs or poisoned external data, persistent memory and inter-agent channels as propagation paths, and the need to treat all natural-language inputs as untrusted before they can influence goal selection, planning or tool calls.

## Governance Considerations

- Inventory agents by autonomy level and by action blast radius, not only by model; the same architecture yields different obligations across deployment contexts.
- Enforce least privilege on agent tools and require human approval for high-impact or goal-changing actions; lock system prompts so that goals and permitted actions are explicit and auditable.
- Validate both user intent and agent intent before executing goal-changing actions; pause, surface and record unexpected goal shifts.
- Sanitize every connected data source (RAG inputs, emails, calendar invites, uploaded files, external APIs, browsing output, peer-agent messages) before it can influence agent goals or actions.
- Maintain behavioral baselines and monitoring of goal state and tool-use patterns.

## Limits

The definition and characteristics are drawn from an EU-law working paper that cites EDPS and European Commission characterizations, and from a security framework; neither is a binding definition of "AI agent". The prior CDO draft's marketing-style framing ("AI that answers" vs "AI that acts", example product goals) is not asserted. Autonomy is a spectrum: per-action human confirmation still qualifies as agentic.

## Related Concepts

- [[generative-ai]]
- [[prompt-injection]]
- [[human-oversight]]
- [[genai-guardrails]]
- [[ai-model-monitoring]]

## Source References

- SRC-0015, AI Agents under EU Law working paper (April 2026), page 2 (absence of legal definition in the AI Act; EDPS/Commission characterization; functional characteristics: planning and task decomposition, external tool invocation, autonomous execution; autonomy spectrum; Article 3(1) definition satisfied) and page 6 (deployment-dependent regulatory profiles: CV screening vs meeting summarization).
- SRC-0027, OWASP Top 10 for Agentic Applications 2026, page 11 (goal hijacking, untrusted natural-language inputs, least privilege, human approval for goal-changing actions, system-prompt locking, data-source sanitation, monitoring of goal state and tool use).
