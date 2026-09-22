---
aliases:
  - guardrails
tags:
  - GenAI
  - mitigation
type: Mitigation
MITRE ATLAS ID: AML.M0020
---
Guardrails are safety controls placed between users, tools, and generative AI models to evaluate prompts, retrieved context, model outputs, and agent actions before they are accepted, executed, or shown to a user. They can help block, modify, or route unwanted content such as malicious code, malicious instructions, sensitive data, unsupported claims, policy-violating responses, or unsafe tool requests.

Guardrails can be implemented using rule-based controls such as filters, allowlists, blocklists, regular expressions, schema validation, policy rules, and permission checks, or using AI-based techniques such as classifiers, LLM reviewers/judges, named entity recognition, groundedness checks, and task-adherence checks. They may be applied at multiple stages of a generative AI workflow, including input handling, prompt construction, retrieval, tool execution, model output review, and post-deployment monitoring.

Examples of specific guardrail implementations include:[[owasp-llm-top10]]  [[datadog-llm-guardrails]] [[azure-ai-content-safety]] [[nvidia-nemo-guardrails]]
- Input moderation: Screen user prompts for harmful content, prompt injection attempts, jailbreak attempts, sensitive data, off-topic requests, or inputs that exceed expected length or format.
- Output moderation: Scan model responses before sending them to users for harmful content, PII, secrets, policy violations, unsupported claims, or unsafe code using classical scanners, classifiers, or a dedicated reviewer model .
- System prompt and policy enforcement: Enforce system instructions, user roles, domain boundaries, response formats, and refusal policies before the model responds (See [Generative AI Guidelines](/mitigations/AML.M0021)).
- Tool and action guardrails: Validate tool calls, tool arguments, permissions, and tool outputs before execution or before results are returned to the model. Require human approval for high-impact, irreversible, privileged, or externally visible actions (See [Human In-the-Loop for AI Agent Actions](/mitigations/AML.M0029), [Input and Output Validation for AI Agent Components](/mitigations/AML.M0033)).
- Retrieval guardrails: Filter and validate retrieved documents before they are added to model context, including checks for untrusted sources, malicious instructions, irrelevant context, or sensitive data.
- Groundedness and factuality checks: Compare model responses against trusted source material or approved knowledge bases to detect unsupported or hallucinated claims.
- Sensitive data and secret protection: Detect, redact, or block personal information, credentials, tokens, proprietary data, system prompts, and other confidential information in prompts, retrieved context, tool outputs, and model responses.
- Structured output validation: Enforce schemas, type checks, allowed values, and safe formats before model outputs are consumed by downstream systems

Guardrails should be continuously evaluated, red-teamed, and updated as adversarial techniques evolve. Guardrail decisions should be logged (See [AI Telemetry Logging](/mitigations/AML.M0021)) and observed failures should be systematically incorporated into updated policies, evaluation datasets, detection logic, prompts, and [Generative AI Model Alignment](/mitigations/AML.M0022).
