# Governance Brain

Governance Brain transforms immutable governance sources into reviewed,
traceable Markdown knowledge and a bilingual question catalogue for Obsidian.
It separates four responsibilities:

- Obsidian organises human-readable knowledge;
- the local Brain retrieves relevant sections and their evidence;
- the five Governance 360 Knowledge Banks provide official evidence; and
- an LLM reasons only over the selected, cited context.

This repository builds the reviewed vault, question registry, local lexical
retrieval and cited context packages. It exports a derived OKF bundle and a
sanitized reconstruction kit. It does not collect project answers, calculate a
global score or make governance decisions. See `plan.md` for the architecture
programme and `ROADMAP.md` for reviewed business coverage.

## Documentation and collaboration

- [Documentation index](docs/README.md) — setup, architecture and operating guides.
- [Contributing](CONTRIBUTING.md), [Code of Conduct](CODE_OF_CONDUCT.md) and
  [Security policy](SECURITY.md).
- [GitHub Wiki](https://github.com/latifo01/governance-brain/wiki) — navigation
  to the repository documentation.
- [GitHub Releases](https://github.com/latifo01/governance-brain/releases) —
  published versions and release notes.

See [the GitHub guide](docs/github.md) for Wiki synchronization and release
preparation.

## Prerequisites

- Windows 11 with PowerShell 7, Ubuntu/WSL, or another supported Python environment
- Python version declared in `.python-version`
- [uv](https://docs.astral.sh/uv/)
- OpenCode when running the project agents
- Obsidian for human navigation and review

Restore the locked environment and run the local checks:

```sh
uv sync --frozen --extra dev --extra data
uv run python --version
uv run pytest -q
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
```

See `docs/ubuntu-setup.md` for Ubuntu details and
`docs/windows-setup.md` for native Windows. See `docs/opencode-setup.md` for
OpenCode/OpenRouter.

Native Windows quick start:

```powershell
git clone https://github.com/latifo01/governance-brain.git
Set-Location "governance-brain"
uv sync --frozen --extra dev --extra data
PowerShell -ExecutionPolicy Bypass -File .\tools\setup-windows.ps1 -CheckOnly
```

For a complete French explanation of the architecture, agents, evidence gates,
commands and daily workflow, start with [`manuel.md`](manuel.md).

## Active workflow

Read these files in order:

1. `AGENTS.md` — immutable-source, evidence, privacy, and publication rules;
2. `ROADMAP.md` — fifteen-domain completion programme and Definition of Done;
3. `WORKSHOP.md` — proposal, review, approval, and integration workflow;
4. `brain wiki/SCHEMA.md` — active Markdown contract.

The active vault uses only `knowledge`, `question`, and `index` note types.
All notes validate against `config/schemas/brain-note.schema.json`. Stable IDs,
files, links, and frontmatter are part of the public export contract.

Knowledge is written in English. Questions contain equivalent English and French
wording. Markdown questions are canonical; Canvas files provide derived
navigation or editorial input.

## Accelerated release workflow

Work is grouped by domain in v3 releases. The fast lane uses existing reviewed
evidence, one `domain-builder` stage, deterministic checks, one independent
`release-reviewer`, and one human approval bound to the candidate hash. The
strict lane adds source extraction and evidence audit whenever evidence,
binding claims, legal interpretation, contracts, or supersession change.

Create a release scaffold with:

```sh
uv run --offline --no-sync python -m gov360_brain.workshop release-init \
  RISK risk-release-001 --risk-tier fast
```

The deterministic validator prevents a strict trigger from entering the fast
lane. Existing v1/v2 proposal manifests and receipts remain historical and readable;
new publication candidates use v3 and resolved evidence review links.

## Source-to-knowledge boundary

1. Originals remain unchanged under `sources/`.
2. Adapters create locator-addressable Markdown under `ingest/SRC-XXXX/`.
3. Validation checks hashes, coverage, parsing signals, and visual-review needs.
4. A local fidelity review compares selected Markdown units with originals.
5. Evidence extraction and audit work only from assigned validated Markdown.
6. Domain builders create knowledge and question proposals under `state/workshop/`.
7. An independent release review checks schema, evidence, authority, duplicates,
   links and dependencies.
8. Human approval permits deterministic integration into `brain wiki/`.

The active assembler first previews the exact ordered candidate and its digest.
It writes only when every proposal manifest and complete human decision record
is `APPROVED`:

```sh
uv run --offline --no-sync python -m gov360_brain.workshop integrate \
  --proposal state/workshop/proposals/<lot-1> \
  --proposal state/workshop/proposals/<lot-2>
# Repeat the same command with --apply only after approval is recorded.
```

The assembler validates before and after atomic note writes, rejects undeclared
files and path conflicts, and emits deterministic integration receipts.

Integrity means that generated files match their recorded hashes. It does not
prove extraction fidelity, legal correctness, source authority, or approval.
Only reviewed binding material can support an obligation or prohibition.

## Deterministic ingestion

The source ingestion CLI remains available for configuration-only Domain Packs:

```sh
uv run gov360 status
uv run gov360 inventory --domain legal-regulatory
uv run gov360 run --domain legal-regulatory --profile no-llm
uv run gov360 validate-ingest --domain legal-regulatory
```

`run` stops at validated Markdown and makes no LLM call. Source authority is
classified only after appropriate review:

```sh
uv run gov360 source classify SRC-0001 --normativity GUIDANCE --reviewer reviewer-id
```

Original files are never rewritten. A replacement source receives a new ID and
the prior record remains available. Retire a source through metadata.

The legacy v1 vault commands `generate`, `approve`, `normalize-vault`, and
`audit` are disabled when the active vault is present. They must not publish to
the current vault. The legacy `context` implementation is also not the
active Brain retrieval path. Use `gov360 brain context` instead.

## Domains and questionnaires

`config/brain-domains.json` contains the seven macro domains used by existing
notes and the ten active Domain Pack IDs. New domain IDs require a reviewed
taxonomy proposal; active IDs and question prefixes remain stable.

Question selection is represented as a common core plus conditional modules
using existing `domains`, `tags`, and acyclic `depends_on` fields. Questions
sharing the same information intent reuse a stable `topic`. This repository
publishes the catalogue and does not store answers.

The original questionnaire Canvas is preserved under
`state/workshop/questionnaire-canvas/reference/`. Its inventory and derived
preview support review; neither is authoritative evidence.

The active `brain wiki/Risk analysis questionnaire.canvas` and
`state/derived/question-registry.jsonl` are generated from the canonical
Markdown questions. Build or check them with:

```sh
uv run --offline --no-sync python -m gov360_brain.workshop build-derived
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
```

Approved integration rebuilds both outputs. VS Codium also starts the versioned
watch task when the repository is opened.

## OpenCode

Start OpenCode from the repository root:

```sh
opencode
```

Project agents, including `domain-builder`, `release-reviewer` and
`cdo-program-lead`, live in `.opencode/agents/`; canonical provider-independent
instructions live in `prompts/roles/`. Reusable procedures stay in
`.agents/skills/`. OpenCode commands in `.opencode/commands/` guide the next
domain release construction, independent review and deterministic integration.
The `questionnaire-reviewer` and `vault-reviewer` remain available for strict
or legacy proposal reviews.

Model selection belongs to `opencode.json` and the provider wrappers. Prefer
deterministic tools for inventories, indexes and validation, and use a separate
reviewer for content. Escalate only where evidence or complexity warrants it;
missing usage and cost measurements remain `unknown`.

OpenRouter provider entries request zero-data-retention routing and deny data
collection. Direct local reading of `sources/` can be authorised for a specific
fidelity check, while role agents still consume only `ingest/`. Editing
`sources/` and `ingest/` remains denied.

## Repository map

- `sources/`: immutable original documents.
- `ingest/`: normalised Markdown and lineage metadata.
- `brain wiki/`: reviewed Obsidian knowledge and questions.
- `state/workshop/`: coverage, proposals, review records, and editorial input.
- `state/derived/`: deterministic registries generated from active Markdown.
- `domain_packs/`: source routing and active domain governance.
- `config/schemas/brain-note.schema.json`: active note schema.
- `prompts/roles/`: canonical role prompts.
- `.opencode/agents/`, `.codex/agents/`: provider wrappers.
- `.agents/skills/`: repository procedures.

The consolidated learning manual is `manuel.md`; it includes the source-format
toolchain and daily operating sequence. `WORKSHOP.md` remains the active release contract.

## Local retrieval, OKF and sharing

```sh
uv run gov360 brain status
uv run gov360 brain validate
uv run gov360 brain build
uv run gov360 brain context "human oversight" --token-budget 6000
uv run gov360 brain evaluate
uv run gov360 brain export --output dist/okf
uv run gov360 brain release-kit --output dist/release-kit
```

Markdown stays canonical. Section and evidence sidecars establish retrieval
eligibility independently of a note's existing `active` status. Assistance mode
excludes unresolved or unreviewed evidence and returns explicit gaps. Research
mode is an explicit documentary lookup, not an approval fallback.

`build --check` and `export --check` detect stale derived output. Public exports
require explicit redistribution policy; original code uses Apache-2.0 without
relicensing source documents or third-party content. The kit omits the working
Git history and ingest. A recipient supplies originals locally and previews
`uv run gov360 brain bootstrap --source-root sources` before `--apply`.
`git_helper` prepares a local release dossier; it does not push or publish.

The operator-authorized private CDO snapshot is separate from the sanitized
public kit:

```sh
uv run gov360 brain handoff --output dist/cdo-handoff
uv run gov360 brain handoff --output dist/cdo-handoff --check
```

It contains the current corpus, ingest, vault, workshop state and derived
outputs and is restricted to the private target recorded in
`config/private-handoff-policy.json`.
