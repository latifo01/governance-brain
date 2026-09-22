# Local release dossier — 2026-09-16

Prepared by: `git_helper` role (research/preparation only)
Readiness: **READY_FOR_OPERATOR_REVIEW** (with blockers listed below)

## Scope

This dossier covers the sanitized LOCAL release kit at `dist/release-kit/` and
this report only. It is preparation work: nothing was staged, committed,
tagged, pushed or published. Human knowledge approval and remote Git
publication remain separate, outstanding operator decisions.

Commands executed (local, read-only or build-verification):

- `.venv/bin/python -m pytest tests/ -q`
- `.venv/bin/gov360 brain status`
- `.venv/bin/gov360 brain validate`
- SHA-256 computation via `.venv/bin/python -c "import hashlib; ..."`
- `git status --porcelain` (read-only; nothing added, staged or committed)

## Kit verification (`dist/release-kit/`)

Built by the deterministic allowlist builder `gov360 brain release-kit`.

| Check | Result |
|---|---|
| `sources/` directory present in kit | No — absent |
| `ingest/` directory present in kit | No — absent |
| `.git` history present in kit | No — absent |
| Kit file count | 146 files |
| `KIT.md` present and consistent | Yes — states no source corpus, extracted text, prior Git history or publication approvals; documents bootstrap steps |
| `config/source-seed.json` loads as JSON | Yes — `schema_version: 1`, 46 sources |
| Secrets in kit configuration | None found — profiles (`strict-local.yaml`, `no-llm.yaml`) reference environment variable names only (`GOV360_LLM_BASE_URL`, `GOV360_LLM_API_KEY`, `GOV360_LLM_MODEL`, `GOV360_VISION_MODEL`); no key values |
| Redistribution policy | `config/redistribution-policy.json`: `schema_version: 1`, `default: deny`, `original_code_license: Apache-2.0`, 141 allowlisted original files, 0 content grants; notice confirms no wildcard, source, ingest, historical receipt, local settings or third-party note is eligible |

Kit contents are limited to: original Apache-2.0 code (`src/`), synthetic tests
(`tests/`), contracts (`config/schemas/`), profiles without secrets, reviewed
documentation (`README.md`, `AGENTS.md`, `WORKSHOP.md`, `ROADMAP.md`, `KIT.md`,
`manue.md`, `plan.md`, `docs/okf-mapping.md`), Domain Pack routing (`domain_packs/`),
provider-independent prompts (`prompts/roles/`), agent/command/skill wrappers
without model pins, `LICENSE`, `THIRD_PARTY_NOTICES.md`, and the generated
manifest, source seed and redistribution policy.

## Source seed summary

- `dist/release-kit/config/source-seed.json`: `schema_version: 1`, 46 sources,
  hash-bound (each entry identifies expected files by SHA-256 for local
  reconstruction by the corpus holder).
- Matches the 46 sources reported by `gov360 brain status`.
- SHA-256 of the seed file: `ec90f913f42e9cae7414effb3bd4a7551bf0c94f3b1833db608ed995b0a89b4f`

## Test results

- Command: `.venv/bin/python -m pytest tests/ -q` (repository root)
- Result: **111 passed, 0 failed, 0 errors** (exit code 0)

## Brain status and validation

From `.venv/bin/gov360 brain status` and `.venv/bin/gov360 brain validate`
(both report the same catalogue):

| Metric | Value |
|---|---|
| `valid` | `true` |
| `notes` | 108 |
| Note types | 73 knowledge, 27 question, 8 index |
| `sources` | 46 |
| `sections` | 578 |
| `reviewed_sections` | 9 |
| `orphan_knowledge` | 25 |
| `publication_verified_notes` | 29 |
| `evidence_findings` | 59 |
| `llm_calls` | 0 |
| `llm_cost` | `null` (not `0`) |
| Validation errors | 0 |
| Validation warnings | 156 |
| `catalogue_sha256` | `8d29171262fdd695d9cac3cdf22c1cdd122c0138928b0aa0f7e44e215bef4683` |
| `schema_version` | 1 |

Validator note (verbatim meaning): technical validity does not establish full
evidence coverage. `llm_calls=0` confirms all checks were deterministic with
no LLM invocation.

## OKF export summary (`dist/okf/`)

- Format: OKF v0.2, specification revision
  `0b87c52c6ef999286c745e19998fdfcd03d5dbee`
  (spec SHA-256 `26aa5da029278939f914e578107242d9607d4f2dc5fe153272b82f9ed1030101`).
- `public: false` — local, non-public export; derived view, not an editable vault.
- 108 mapped concepts (108 concept files, 1 reference file, 111 manifest file
  entries).
- Gaps: 107 entries, all code `SOURCE_PROVENANCE_UNRESOLVED` — source
  provenance is not resolved for the exported notes; missing verification
  metadata remains missing.
- `undated_publication_receipts`: none.
- The OKF publication receipt history (`dist/okf/log.md`) records 8 prior
  hash-bound lot approvals (2026-09-13 to 2026-09-15); these are historical
  vault-integration approvals and do not constitute approval of this release
  dossier or authorization to publish.

## File hashes (SHA-256)

| File | SHA-256 |
|---|---|
| `dist/release-kit/brain-release.json` | `0184c675479e0f07e6ccec416cf4dabb31a96f11d569dbc930c33ff53fd77c6a` |
| `dist/release-kit/config/source-seed.json` | `ec90f913f42e9cae7414effb3bd4a7551bf0c94f3b1833db608ed995b0a89b4f` |

## Git working-tree summary (read-only inspection)

`git status --porcelain` (no content staged, added or committed):

- **49 modified** tracked files.
- **89 untracked** entries (files and directories).
- Total: 138 entries.

Notable categories:

- Modified: skills (`.agents/skills/`), agent wrappers (`.opencode/agents/`,
  `.codex/config.toml`), canonical docs (`AGENTS.md`, `README.md`,
  `WORKSHOP.md`), vault notes and `brain wiki/SCHEMA.md`, Obsidian settings,
  `config/brain-domains.json`, setup docs, 3 canonical role prompts, 4 source
  modules under `src/gov360_brain/`, 2 state manifests (`state/*.jsonl`), and
  5 existing test files.
- Untracked (new): brain module `src/gov360_brain/brain/` and
  `src/gov360_brain/derived.py`; new vault notes (AI Risk Mitigations, Data &
  AI Laws, 18 Famous AI incidents notes, `brain wiki/indexes/`,
  `brain wiki/questions/core/`, questionnaire Canvas); new schemas
  (`brain-note`, `brain-evidence`, `brain-context`, `workshop-release`,
  `workshop-release-v3`); new config (`brain-evaluation.json`,
  `brain-vocabulary.json`, `redistribution-policy.json`); new role prompts
  (5) and agent wrappers (Codex TOML + OpenCode Markdown, commands);
  `LICENSE`, `ROADMAP.md`, `THIRD_PARTY_NOTICES.md`, `manue.md`, `plan.md`,
  `docs/okf-mapping.md`; new brain tests (5); `state/derived/`;
  `state/workshop/` subdirectories (coverage, drafts, evidence-library,
  proposals, questionnaire-canvas, brain-upgrade, cdo-reference);
  `ingest/SRC-0043/`, `ingest/SRC-0044/`, `ingest/SRC-0046/`; `sources/`;
  `.vscode/`.

Safety note for any future commit list: `sources/` and `ingest/` appear as
untracked paths. Per repository invariants, source originals and ingest text
must never be committed or published; any operator-authorized commit list must
exclude them explicitly.

## Blockers and outstanding decisions

1. **Human content approval outstanding.** No hash-bound human approval has
   been recorded for this release dossier. Successful extraction, validation,
   and test execution never imply approval.
2. **Remote publication not authorized.** No push, tag, or remote release may
   occur. Pushing/publishing requires a separate, explicit operator
   authorization; this preparation is not permission.
3. **Corpus evidence coverage is partial.** Only 1 evidence-library receipt
   exists under `state/workshop/evidence-library/`
   (`gdpr-article22-reconciliation-001.json`); `reviewed_sections` is 9 of 578
   sections. The OKF export reports 107 `SOURCE_PROVENANCE_UNRESOLVED` gaps.
   No completeness percentage may be inferred from note counts alone.
4. **Validation warnings.** 156 warnings remain from `gov360 brain validate`
   (0 errors); warnings should be reviewed before any approval decision.
5. **Orphan knowledge.** 25 knowledge notes are not linked into the graph;
   link repair is a candidate follow-up before publication claims.

## Authorization statement

This dossier is local preparation only. Pushing, tagging, or publishing any
part of this repository or kit requires a separate, explicit operator
authorization, distinct from any human knowledge content approval. Nothing in
this report grants, implies, or records either decision.

## Operator decision — 2026-09-17

- Approver identity: abdelatif (repository operator)
- Decision: APPROVED — local release dossier only
- Dossier SHA-256 at approval: `60f846e78ccdcfc890162e34d3a14029f2bdf47b1f0ef4adc643d1de892c5aef`
- Scope: this dossier and the sanitized local kit at `dist/release-kit/` as
  prepared (`brain-release.json` SHA-256
  `0184c675479e0f07e6ccec416cf4dabb31a96f11d569dbc930c33ff53fd77c6a`,
  `source-seed.json` SHA-256
  `ec90f913f42e9cae7414effb3bd4a7551bf0c94f3b1833db608ed995b0a89b4f`).
- Explicitly NOT authorized by this decision: any push, tag, remote release or
  publication; those remain separate future decisions.
- Accepted limits at approval: partial evidence coverage (29/586 reviewed
  sections at dossier time), 156 validation warnings, remaining lineage debt.
  Lineage and evidence reconciliation continues as the active technical-debt
  programme.
