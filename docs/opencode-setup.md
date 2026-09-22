# OpenCode setup

OpenCode reads AGENTS.md from the repository root and discovers the project
skills under .agents/skills/. Canonical role prompts remain in prompts/roles/;
.opencode/agents/ contains only provider and permission adapters.

Start from the repository root:

```sh
opencode
```

The active model choices are in `opencode.json` and the provider wrappers.
Keep model names there, never in canonical prompts or Domain Packs. Prefer
local deterministic tools for inventories, indexes, exports and validation.
Use independent content review and escalate evidence/legal complexity through
configured profiles. Missing cost metrics remain `unknown`, not zero.

The default OpenCode model is `openrouter/deepseek/deepseek-v4-flash-0731`
(DeepSeek Flash), replacing GLM 5.3. The lower-cost `small_model` is Mistral
Small; the strict evidence-auditor and `/brain-review-strict` command also use
DeepSeek Flash. Terra remains registered as an optional provider entry for
compatibility, but is not selected by the repository's operational defaults.

Operator directives: `openai/gpt-5.6-sol-pro` and `anthropic/claude-opus-5`
must never be used (2026-09-17); GLM 5.3 is retired (2026-09-18). Heavy tasks,
complex blockers and legal second opinions escalate on DeepSeek Flash only.

Every registered OpenRouter model requests ZDR routing and denies data
collection. Session sharing is disabled. If OpenRouter cannot find a provider
matching the requested parameters, the request must fail rather than silently
relax those constraints.

## Source access

The primary OpenCode session may read sources/, ingest/, state/, and brain wiki/
without a repeated permission prompt. This supports the operator-authorised
local fidelity checks requested for this repository. Editing sources/ and
ingest/ is denied.

All governance subagents explicitly deny read access to sources/. Evidence
roles consume only their assigned validated Markdown under ingest/. The CDO
programme lead also denies ingest/ because it plans from inventories and review
metadata. Direct original-file inspection must remain a specific verification
step in the primary session and must not be delegated to a role agent.

## Agents

- @cdo-program-lead: selects one bounded roadmap lot.
- @source-extractor: extracts candidates from assigned ingest units.
- @evidence-auditor: verifies candidate evidence and locators.
- @knowledge-architect: proposes active-contract knowledge changes.
- @questionnaire-curator: proposes bilingual question changes.
- @questionnaire-reviewer: independently reviews question intent and logic.
- @vault-reviewer: performs the final cross-artifact review.
- @domain-builder: writes one assigned fast-lane shard under its proposal.
- @release-reviewer: reviews the consolidated release and writes its review record.
- @git-helper: prepares a sanitized local release dossier; never pushes or publishes.

Specialist agents remain read-only. The domain builder can write only under
state/workshop/proposals/, and the release reviewer only under the proposal's
review directory. Neither can edit the active vault. Human approval is still
required before deterministic integration.

## Commands

- /brain-next selects the next roadmap lot.
- /brain-build PATH builds an assigned domain release shard.
- /brain-review PATH independently reviews a consolidated release.
- /brain-review-strict PATH reviews a strict release with its configured model.
- /brain-release PATH validates and integrates an already approved release.
- /brain-git-helper prepares the local release kit and report.
- /brain-canvas-watch starts the local derived-output watcher.
- /question-lot DOMAIN_OR_TOPIC drafts a question proposal.
- /review-question-lot PATH independently reviews a question proposal.
- /review-vault-lot PATH reviews a complete proposal or bounded proposal set.

The command definitions live in .opencode/commands/. Permissions are bounded by
each wrapper; construction and review have assigned output directories. No role
output itself publishes or implies approval.

## Validation

```sh
opencode debug config
opencode debug skill
opencode agent list
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
uv run pytest -q
```

The expected agent list includes cdo-program-lead, domain-builder and
release-reviewer.
The project commands appear in the TUI command picker after OpenCode reloads the
project configuration.

If project configuration prevents startup, inspect it without loading a working
session:

```sh
OPENCODE_DISABLE_PROJECT_CONFIG=1 opencode debug config
```

Do not use --auto for this governance repository because it bypasses permission
prompts that protect configuration, proposals and publication-sensitive paths.

## Local Brain in OpenCode or Codex

Run `uv run gov360 brain status` before choosing the next lot. Then use the
generated reconciliation and 15-by-10 coverage matrix rather than stale wave
labels. `build`, `context`, `evaluate`, `export` and `release-kit` are local
commands and need no model call. See [`manuel.md`](../manuel.md) §18 for complete examples.

A suitable restart message is:

```text
Read AGENTS.md, WORKSHOP.md, ROADMAP.md, brain wiki/SCHEMA.md and plan.md.
Inspect Brain status and evidence blockers. Select one bounded uncovered need,
reuse valid audited evidence, and prepare an independently reviewed candidate.
Preserve IDs and FR/EN intent. Present its exact hash before knowledge publication.
```

In Codex the registered role is `git_helper`; in OpenCode it is `git-helper`.
It prepares the local sanitized kit and release report only. Remote publication
requires separate explicit authorization. Existing active notes with unresolved
evidence stay discoverable in Obsidian but are not automatically eligible for
assistance retrieval. Research mode must be explicitly requested.
