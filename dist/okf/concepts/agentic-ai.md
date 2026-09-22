---
aliases:
- Agentic AI
- AI agents
- Autonomous agents
brain_id: agentic-ai
brain_sha256: c2f4f1e8d0623368c1b24c92c732dcac58e0c1a4814edd6d9ab1a21b7fc10325
domains:
- AI
evidence_sources:
- AI_ACT
- AI_NICE_TO_KNOW
id: agentic-ai
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0015
  evidence_ref: concepts-lin4-src-0015-p0002
  id: brain-61ee49210533ae45
  locator: Page 2
  resource: /references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md
  unit_file_sha256: 4b3cb2f09237d94235b43f279b2a0324c8db92942ba37c5e8a1db43332ffdd67
  unit_path: ingest/SRC-0015/units/p0002.md
  unit_sha256: 575b58f8668932284d90c1d814c9a577111e3e49fe47f756039261e473f3cc10
- authority: GUIDANCE
  brain_source_id: SRC-0027
  evidence_ref: concepts-lin4-src-0027-p0011
  id: brain-83b419a404a703af
  locator: Page 11
  resource: /references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md
  unit_file_sha256: 62af7b9b2d37dd3b5410c093ef81c904113d9cc25eb787ea347dc001a80e72bb
  unit_path: ingest/SRC-0027/units/p0011.md
  unit_sha256: 9dad2c1b3933450b0cb3b6a515f0adaa3650d598a533927bb59f631f3a84dcaf
- authority: GUIDANCE
  brain_source_id: SRC-0015
  evidence_ref: concepts-lin4-src-0015-p0006
  id: brain-ff18e304376b6232
  locator: Page 6
  resource: /references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md
  unit_file_sha256: 4b82ed2513ab44e38dc5b74eed90fe94311aaba9a436eaa7a49ec16ee194b3c8
  unit_path: ingest/SRC-0015/units/p0006.md
  unit_sha256: 3a7fc23218b5935b643787e37ffac8fd4c946050d39ce61d789c6b0fccca915b
status: stable
tags:
- ai-concepts
- fundamentals
- agentic-security
title: Agentic AI
type: knowledge
---


# Agentic AI

## Summary

Agentic AI designates AI systems that perform sequences of actions across interconnected tools and data sources to achieve goals, with reduced or minimal human involvement in the intermediate steps. The term has no legal definition in the EU AI Act: the legislature chose a functional, technology-neutral definition in Article 3(1) and regulates AI systems, not architectural patterns. An AI agent nonetheless satisfies every element of that definition and is characterized, per the EDPS and European Commission descriptions, as a system acting autonomously with limited human interaction to fulfil goals rather than isolated tasks, capable of reasoning, planning and coordinating actions in changing environments.

The distinguishing functional characteristics are: (i) planning and task decomposition — breaking a high-level goal into sub-tasks and determining execution order; (ii) external tool invocation via APIs, databases, code interpreters, web browsers or other software, which is the critical differentiator from a standalone large language model; (iii) autonomous execution of intermediate steps without human approval for each one, with the degree of autonomy ranging from per-action confirmation to fully autonomous operation.

The governance consequence is that identical agent architectures produce radically different regulatory profiles depending on deployment: an agent screening CVs triggers high-risk classification under the AI Act, while an agent summarizing meeting notes triggers only transparency obligations. The technology is identical; the regulatory consequence diverges completely.

Section evidence: [^brain-61ee49210533ae45] [^brain-ff18e304376b6232]

## Applicability

This concept frames LLM-based agents, copilots with tool access, multi-agent systems and orchestration layers. Risk increases with the breadth of tool and data access, the autonomy level of intermediate steps, and the materiality of the actions the agent can influence.

Agent-specific security concerns are documented in the OWASP Top 10 for Agentic Applications 2026: goal hijacking through manipulated natural-language inputs or poisoned external data, persistent memory and inter-agent channels as propagation paths, and the need to treat all natural-language inputs as untrusted before they can influence goal selection, planning or tool calls.

Section evidence: [^brain-61ee49210533ae45] [^brain-83b419a404a703af] [^brain-ff18e304376b6232]

## Governance Considerations

- Inventory agents by autonomy level and by action blast radius, not only by model; the same architecture yields different obligations across deployment contexts.
- Enforce least privilege on agent tools and require human approval for high-impact or goal-changing actions; lock system prompts so that goals and permitted actions are explicit and auditable.
- Validate both user intent and agent intent before executing goal-changing actions; pause, surface and record unexpected goal shifts.
- Sanitize every connected data source (RAG inputs, emails, calendar invites, uploaded files, external APIs, browsing output, peer-agent messages) before it can influence agent goals or actions.
- Maintain behavioral baselines and monitoring of goal state and tool-use patterns.

Section evidence: [^brain-61ee49210533ae45] [^brain-83b419a404a703af] [^brain-ff18e304376b6232]

## Limits

The definition and characteristics are drawn from an EU-law working paper that cites EDPS and European Commission characterizations, and from a security framework; neither is a binding definition of "AI agent". The prior CDO draft's marketing-style framing ("AI that answers" vs "AI that acts", example product goals) is not asserted. Autonomy is a spectrum: per-action human confirmation still qualifies as agentic.

Section evidence: [^brain-61ee49210533ae45]

## Related Concepts

- [generative-ai](/concepts/generative-ai.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [human-oversight](/concepts/human-oversight.md)
- [genai-guardrails](/concepts/genai-guardrails.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)

## Source References

- SRC-0015, AI Agents under EU Law working paper (April 2026), page 2 (absence of legal definition in the AI Act; EDPS/Commission characterization; functional characteristics: planning and task decomposition, external tool invocation, autonomous execution; autonomy spectrum; Article 3(1) definition satisfied) and page 6 (deployment-dependent regulatory profiles: CV screening vs meeting summarization).
- SRC-0027, OWASP Top 10 for Agentic Applications 2026, page 11 (goal hijacking, untrusted natural-language inputs, least privilege, human approval for goal-changing actions, system-prompt locking, data-source sanitation, monitoring of goal state and tool use).


[^brain-61ee49210533ae45]: [SRC-0015](/references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md); locator: Page 2.
[^brain-83b419a404a703af]: [SRC-0027](/references/src-0027-0e0f67fb3c832104d9eff10ea61976ad69d8ce57bba1b38e6cbe7cc35c941fed.md); locator: Page 11.
[^brain-ff18e304376b6232]: [SRC-0015](/references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md); locator: Page 6.
