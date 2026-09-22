# Wave 2 AI Act decision-gate lot 012

Status: REVIEWED_PROPOSAL (evidence gate closed 2026-09-14; knowledge
proposal drafted, questionnaire and vault reviews PASS; awaiting human
approval)

## Objective

Create a bounded, evidence-first knowledge lot for three connected decisions:
whether a solution meets the AI Act definition of an AI system, whether an
Article 5 prohibited practice may apply, and whether the system is high-risk
under Article 6 and the relevant annex route. Existing canonical questions keep
their current intent, topic, options and dependencies.

## Why this lot is first

- `ROADMAP.md` places prohibited practices and AI-system classification first
  in Wave 2.
- The integrated common core already routes these decisions through
  `core-003`, `core-010`, `core-011`, `core-013` and `legal-001`.
- The vault has broad `ai-system` and `eu-ai-act` notes but no dedicated note
  for prohibited-practice screening or high-risk classification.
- The selected ingest units have recorded integrity `PASS`; documentary
  fidelity and claim fitness still require review before synthesis.

## Scope

Included:

- the AI-system definition elements supported by reviewed evidence;
- Article 5 categories, conditions and exceptions at decision-gate level;
- Article 6 routes through Annex I and Annex III;
- actor, scope, derogation and documentation boundaries supported by evidence;
- two new knowledge notes, stable-ID updates, question knowledge links and the
  AI Act index.

Excluded:

- downstream high-risk obligations, GPAI, Article 50, monitoring and incidents;
- FRIA and DPIA substance;
- GDPR Article 22 and personal-data routing, reserved for lot 013;
- project answers, scoring or runtime assessment;
- exact application-date claims until reviewed binding evidence resolves the
  current ingest limitation.

## Existing inventory

| ID | Planned disposition | Constraint |
| --- | --- | --- |
| `ai-system` | UPDATE candidate | Preserve ID/path; distinguish binding definition from interpretation |
| `eu-ai-act` | UPDATE candidate | Preserve overview role and link to dedicated concepts |
| `ai-act-prohibited-practices` | ADD candidate | Dedicated Article 5 decision-gate knowledge |
| `high-risk-ai-system-classification` | ADD candidate | Dedicated Article 6 and annex routing knowledge |
| `core-003-ai-system-determination` | link/reference review only | Preserve question semantics |
| `core-010-eu-ai-act-scope` | NOOP expected | Preserve jurisdiction/scope gate |
| `core-011-prohibited-practice-screening` | link update candidate | Preserve options and dependency |
| `core-013-high-risk-ai-classification` | link update candidate | Preserve options and dependency |
| `legal-001-ai-act-classification-record` | link update candidate | Preserve evidence-record intent |
| `ai-act-index` | UPDATE candidate | Add only validated useful links |

No new questionnaire intent is justified at cadrage. The five existing intents
are distinct.

## Evidence routing and authority

| Source | Role in this lot | Candidate locators |
| --- | --- | --- |
| `SRC-0011` | binding base act, combined with the reviewed amendment | Pages 156-165, 172-181, 377-389 |
| `SRC-0043` | binding 2026 modifying act and application dates | Pages 1-41, narrowed by extraction and audit |
| `SRC-0016` | non-binding Commission interpretation | Pages 6-21, narrowed during audit |
| `SRC-0017` | non-binding definition interpretation | Pages 2-3, 5-6, 11-12 |
| `SRC-0022` | non-binding training context | Pages 95-97, only if materially useful |

The foundation review's authority boundary is an input to audit, not permission
to skip source classification, fidelity, currency, scope or locator checks. A
filename never establishes normativity.

## Sequential work and gates

1. Freeze the active inventory and source-specific assignments.
2. Extract atomic candidates into source-specific immutable receipts.
3. Audit every candidate against the same units, including fidelity, authority,
   legal scope, exceptions, currency and conflicts.
4. Draft the two additions and stable-ID knowledge updates from accepted
   evidence only.
5. Perform full-register duplicate analysis and propose only justified question
   link/reference changes and the index update.
6. Validate the overlay, run questionnaire review, then run complete vault
   review.
7. Present the concrete hash-bound candidate for human approval.
8. Integrate only through the deterministic assembler and revalidate.

The evidence gate blocks synthesis unless every claim has an accepted locator
and only `SRC-0011` supports an obligation or prohibition. The knowledge gate
requires distinct scopes, stable IDs, visible references and explicit limits.
The question gate forbids a duplicate intent or an unreviewed semantic change.
The vault and human gates remain mandatory.

## Coverage decision

The `legal-regulatory` pillar remains `EVIDENCE_READY`. This cadrage does not
satisfy the ten completion criteria and therefore does not justify a broader
coverage-state change.

## Evidence-gate result — 2026-09-14

Extraction initially covered 58/58 assigned units and exposed the missing 2026
amendment. The official act was then added as `SRC-0043`; all 41 pages were
normalized and fidelity-checked. Independent audit verified 26 of 30 amendment
candidates, and a second currentness audit resolved 29 of the 30 previously
uncertain base-text candidates while rejecting the superseded machinery entry.
Both legal sources are classified `BINDING`. Lot 012 is now `EVIDENCE_READY`
for knowledge synthesis, subject to the recorded effective dates and the
continued rule that an amending act is not a full consolidated reproduction.
