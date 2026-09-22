# ATLAS complementarity matrix

This audit compares the reviewed ATLAS export with active Brain notes. ATLAS
is treated as security guidance and threat taxonomy, not as binding authority.
Only validated units and existing active notes were considered.

| Stable element | Decision | Target note | Justification | Evidence / locator |
|---|---|---|---|---|
| `AML.M0024` AI Telemetry Logging | ENRICH | `ai-model-monitoring` | Adds an ATLAS-specific mapping from agent tool calls and suspicious AI-service requests to monitoring evidence. The note already covers governance memory and monitoring, so no new concept is needed. | `SRC-0044`, `sheet-002-techniques addressed-002.md`, rows 251-254 |
| `AML.M0025` Maintain AI Dataset Provenance | ENRICH | `retrieval-augmented-generation` | Strengthens the existing provenance and poisoning discussion with an explicit mitigation relationship. | `SRC-0044`, `sheet-002-techniques addressed-002.md`, rows 255-259 |
| `AML.M0026` Privileged AI Agent Permissions Configuration | ENRICH | `genai-guardrails` | The active note already describes tool authorization and least privilege; ATLAS supplies stable mitigation and technique references. | `SRC-0044`, `sheet-002-techniques addressed-002.md`, rows 260-266 |
| `AML.M0028` AI Agent Tools Permissions Configuration | ENRICH | `genai-guardrails` | Complements the existing external policy gate and scoped-credential guidance with a dedicated tool-permission crosswalk. | `SRC-0044`, `sheet-002-techniques addressed-002.md`, rows 337-346 |
| `AML.M0033` Input and Output Validation for AI Agent Components | ENRICH | `genai-guardrails` | Provides a precise ATLAS mitigation anchor for the existing input, output and tool validation controls. | `SRC-0044`, `sheet-002-techniques addressed-002.md`, rows 294-299 |
| `AML.M0036` AI Agent Authority Expansion Controls | CREATE | — | A distinct reusable subject: limiting runtime acquisition of new authority, credentials, targets and delegated scope is not represented by a dedicated active concept note. Create only after a bounded knowledge proposal and review. | `SRC-0046`, `key-0003.md`, object `AML.M0036` |
| `AML.M0038` AI Agent Scope Violation Controls | CREATE | — | A distinct reusable subject concerning runtime drift beyond approved objectives and resources. Existing agent and guardrail notes mention boundaries but do not define this mitigation as a standalone concept. Create only after evidence review. | `SRC-0044`, `sheet-001-mitigations-001.md`, rows 299-304 |
| `AML.M0029` Human In-the-Loop for AI Agent Actions | NOOP | `human-in-the-loop-for-ai-agent-actions` | Already published with audited primary ATLAS evidence and linked to human oversight and guardrails. | `SRC-0044`, `sheet-001-mitigations-001.md`, row 31; `sheet-002-techniques addressed-002.md`, rows 279-281 |
| `AML.T0053`, `AML.T0086`, `AML.T0101` agent tool invocation, exfiltration and destruction | ENRICH | `agentic-ai`, `data-leakage`, `genai-guardrails` | Existing concepts cover the risks; the ATLAS relationships can improve threat-model and control crosswalk precision without importing a bulk technique catalogue. | `SRC-0044`, `sheet-002-techniques addressed-002.md`, rows 279-281 |
| `SRC-0026` OWASP LLM guidance | NOOP | `genai-guardrails`, `prompt-injection` | Already visibly cited and used for the current guardrail and prompt-injection reasoning; no ATLAS-specific gap demonstrated by this audit. | Validated `SRC-0026` units; existing note references pages 10-12 and 30 |
| `SRC-0027` OWASP Agentic guidance | NOOP | `agentic-ai`, `genai-guardrails` | Already covers least privilege, human approval, intent validation and source sanitation; ATLAS adds identifiers and relationships rather than an absent concept. | Validated `SRC-0027` units; existing note references pages 11, 33 and 38 |

The two CREATE decisions are recommendations for a subsequent bounded
proposal; this matrix does not publish notes or alter the active vault.
