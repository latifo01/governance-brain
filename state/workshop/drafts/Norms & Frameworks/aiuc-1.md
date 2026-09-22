---
id: aiuc-1
title: AIUC-1
type: knowledge
domains:
- RISK
status: draft
aliases:
- AIUC-1
tags: []
evidence_sources: []
---

AIUC-1 is a framework and third-party certification standard designed specifically to assess the security, reliability, and governance of enterprise AI agents. 

Often described in the industry as the "[[SOC 2]] for AI agents," it was developed by the Artificial Intelligence Underwriting Company ([[AIUC]]) to provide assurance to security, legal, and procurement teams during the deployment of autonomous agents. 

# What is its objective? 

Unlike traditional security standards (such as [[SOC 2]] or [[iso-27001]]) that govern general information systems, AIUC-1 targets risks specific to the behaviors of generative models and autonomous agents: 
* **[[prompt-injection]]**; 
* **unsafe or [[unauthorized tool/API calls]]**; 
* **[[hallucinations]]** and **[[toxic-or-biased-outputs]]**; 
* **confidential [[data leaks]]** via model contexts. 
The assessment relies on continuous testing and quarterly re-evaluation to keep pace with the rapid evolution of models and cyber threats.
# 6 core risks pillars

**AIUC-1** evaluates enterprise AI systems across **six core risk pillars**:
### 1. Data & Privacy (Domain A)
Focuses on protecting sensitive enterprise and personal data from exposure during model training, retrieval, or execution.
**Key Controls:** 
* Guarding against Personally Identifiable Information (PII) leakage, 
* enforcing cross-customer/tenant data isolation, 
* preventing IP/trade secret infringement, and 
* restricting unauthorized training on user inputs.
### 2. Security (Domain B)
Protects the AI deployment environment and agent execution paths from adversarial manipulation and unauthorized operations.
**Key Controls:** 
- Defending against direct/indirect [[prompt-injection]], 
- mitigating jailbreak vectors, 
- enforcing role-based user access controls, 
- protecting runtime environments, and 
- blocking non-sanctioned agent executions.
### 3. Safety (Domain C)
Ensures the agent’s generated outputs do not cause reputational, legal, or operational harm.
**Key Controls:** 
- Preventing harmful, offensive, or out-of-scope outputs, 
- conducting pre-deployment red-teaming/safety testing, 
- defining risk taxonomies, and 
- establishing human-in-the-loop escalation paths for sensitive tasks.
### 4. Reliability (Domain D)

Validates that the agent operates predictably, accurately, and within strict system boundaries.
**Key Controls:** 
- Mitigating hallucinations, 
- restricting unsafe tool calls or unvalidated Model Context Protocol (MCP) interactions, 
- enforcing rate limits, and 
- monitoring execution accuracy across complex multi-step workflows.
### 5. Accountability (Domain E)
Provides governance, traceability, and operational auditing mechanisms for agentic decisions.
**Key Controls:**
- Comprehensive runtime activity logging (who initiated the agent, what tools were called, and actions taken), 
- maintaining AI incident response plans, 
- vendor due diligence, and 
- transparent AI usage disclosure.
### 6. Society (Domain F)
Addresses macro-level risks and high-consequence misuse vectors enabled by agentic automation.
**Key Controls:** 
- Safeguards against AI-enabled cyber attack automation, 
- preventing chemical, biological, radiological, or nuclear (CBRN) risk amplification, and 
- aligning agent behaviors with broader regulatory mandates (e.g., [[eu-ai-act]]).
## Resources

* [Official AIUC-1 website](https://www.aiuc-1.com/)
* AIUC-1 uses the AI risks on [[mitre-atlas]] to define its framework
