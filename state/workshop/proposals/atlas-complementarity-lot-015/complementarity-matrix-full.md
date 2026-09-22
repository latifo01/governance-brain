# ATLAS complementarity audit — SRC-0046

This proposal audits the complete SRC-0046 catalogue: 308 objects, 1,088 relations and 72 case studies. ATLAS is security guidance and threat taxonomy, not binding authority. No active vault, source or ingest file is changed.

## Identifier correction

The verified catalogue establishes `AML.M0036` = **Limit AI Workload Resource Consumption**, `AML.M0037` = **AI Agent Authority Expansion Controls**, and `AML.M0038` = **AI Agent Scope Drift Detection**. The earlier matrix incorrectly assigned authority expansion to M0036; this audit corrects it.

## Mitigation and technique decisions

| Elements | Decision | Target | Rationale |
|---|---|---|---|
| M0024, M0036 | ENRICH | `ai-model-monitoring` | Telemetry and workload consumption add monitoring and resilience crosswalks. |
| M0025 | ENRICH | `retrieval-augmented-generation`, `traceability` | Adds dataset provenance and poisoning control precision. |
| M0026, M0027, M0028, M0030, M0032, M0033 | ENRICH | `genai-guardrails`, `agentic-ai` | Adds permission, untrusted-data, segmentation and validation controls. |
| M0029 | NOOP | `human-in-the-loop-for-ai-agent-actions` | Already published from audited ATLAS evidence. |
| M0034 | NOOP | — | No targeted active-note gap established in this audit scope. |
| M0035 | ENRICH | `red-teaming` | Adds threat-informed ATLAS test linkage. |
| M0037 | CREATE | — | Authority expansion is a distinct concept absent as a dedicated active note. |
| M0038 | CREATE | — | Scope drift detection is a distinct concept absent as a dedicated active note. |
| T0002.002, T0010.005, T0011.002 | ENRICH | `genai-guardrails`, `agentic-ai` | Configuration, tool and poisoned-tool relationships improve threat precision. |
| T0053, T0086, T0102 | ENRICH | `agentic-ai`, `data-leakage`, `genai-guardrails` | Invocation, exfiltration and destruction provide actionable crosswalks. |

Evidence for all rows: `SRC-0046`, validated unit `ingest/SRC-0046/units/key-0003.md`, locator `/objects`, source SHA-256 `6550ac8a7322e2d43d7c6c10234f0f381e74734ac6c734255fb1fc467bf16d7c`, unit SHA-256 `7b18ef3f2ed64ab84d1204bca642c073f03b8264b4a2fe3bb2f19ab84cbd5241`.

## Complete case-study audit

All 72 case studies were compared with active notes. The following 18 high-value cases merit bounded ENRICH proposals; the remaining 54 are explicit NOOP pending a demonstrated active-note gap. They remain available in the derived catalogue and are not silently discarded.

**ENRICH — Hugging Face, supply chain, MCP, exfiltration, infrastructure and agents:** `AML.CS0027`, `AML.CS0028`, `AML.CS0031`, `AML.CS0041`, `AML.CS0045`, `AML.CS0049`, `AML.CS0053`, `AML.CS0054`, `AML.CS0064`, `AML.CS0065`, `AML.CS0068`, `AML.CS0071`, `AML.CS0037`, `AML.CS0059`, `AML.CS0066`, `AML.CS0023`, `AML.CS0024`, `AML.CS0015`.

**NOOP — catalogued, no targeted active-note gap established:** `AML.CS0000`–`AML.CS0022` except `AML.CS0015`; `AML.CS0025`–`AML.CS0026`; `AML.CS0029`–`AML.CS0036` except `AML.CS0037`; `AML.CS0038`–`AML.CS0040`; `AML.CS0042`–`AML.CS0044`; `AML.CS0046`–`AML.CS0048`; `AML.CS0050`–`AML.CS0052`; `AML.CS0055`–`AML.CS0058`; `AML.CS0060`–`AML.CS0063`; `AML.CS0067`; `AML.CS0069`–`AML.CS0070`.

Priority enrichments should cover Hugging Face/model provenance, poisoned dependencies and artifacts, MCP/tool exfiltration, exposed agent infrastructure, and multi-agent compromise. Each future incident note must retain scope, date, affected component, ATLAS mapping, limitations and primary locator; no case study becomes a legal obligation.

## Decision and provenance limits

`ENRICH` means propose a targeted addition to an existing note or incident index; `CREATE` means propose a bounded concept note. Neither is publication approval. Existing notes must be preferred over semantic duplicates. The full catalogue and relations remain deterministic derived data. ATLAS claims must not be used as binding legal requirements.
