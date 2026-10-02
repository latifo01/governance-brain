# Documentation index

Use this page to find the right entry point. The repository files are the
reference documentation; the GitHub Wiki provides navigation to them.

## Getting started

| Document | Purpose |
| --- | --- |
| [Project README](../README.md) | Overview, prerequisites and main commands |
| [French manual](../manuel.md) | Detailed learning guide and daily workflow |
| [Ubuntu / WSL setup](ubuntu-setup.md) | Linux environment setup |
| [Windows setup](windows-setup.md) | Native Windows environment setup |
| [OpenCode setup](opencode-setup.md) | Provider configuration and agent operation |

## Architecture and operating contracts

| Document | Purpose |
| --- | --- |
| [Architecture programme](../plan.md) | Approved architecture and implementation programme |
| [Lifecycle diagram](architecture/governance-brain-lifecycle.svg) | Visual source-to-knowledge workflow |
| [Diagram source](architecture/governance-brain-lifecycle.puml) | Editable PlantUML source |
| [Roadmap](../ROADMAP.md) | Business coverage and completion criteria |
| [Workshop](../WORKSHOP.md) | Releases, evidence review, approval and integration |
| [Repository rules](../AGENTS.md) | Contributor and agent constraints |
| [Active note schema](../brain%20wiki/SCHEMA.md) | Canonical Markdown note contract |
| [Bounded task harness](brain-harness.md) | Task boundaries, provenance and telemetry |
| [OKF mapping](okf-mapping.md) | Derived export mapping |

## Knowledge navigation

Open `brain wiki/` as an Obsidian vault and start with its
[README](../brain%20wiki/README.md). Domain navigation is in
[`brain wiki/indexes/`](../brain%20wiki/indexes/), and canonical questions are in
[`brain wiki/questions/`](../brain%20wiki/questions/).
Folder names and note paths remain stable. Knowledge and question changes follow
the workshop release workflow.

## Collaboration and GitHub

- [Contributing](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security policy](../SECURITY.md)
- [Wiki and release guide](github.md)
- [GitHub Wiki](https://github.com/latifo01/governance-brain/wiki)
- [GitHub Releases — version history](https://github.com/latifo01/governance-brain/releases)

## Repository structure

| Path | Contents |
| --- | --- |
| `src/`, `tests/`, `tools/` | Application code, tests and local utilities |
| `docs/` | Technical documentation and Wiki navigation pages |
| `sources/`, `ingest/` | Immutable originals and normalized Markdown with lineage |
| `brain wiki/` | Reviewed knowledge, questions and navigation indexes |
| `domain_packs/`, `config/` | Source routing, profiles, schemas and registries |
| `prompts/roles/`, `.agents/skills/` | Canonical role prompts and reusable procedures |
| `.opencode/`, `.codex/` | Provider-specific wrappers and configuration |
| `state/workshop/` | Proposals, evidence records, reviews and coverage |
| `state/derived/`, `dist/` | Reproducible catalogues, exports and sharing bundles |
| `.github/` | CI workflow, code ownership and pull-request template |

Keep the root entry documents (`README.md`, `AGENTS.md`, `WORKSHOP.md`,
`ROADMAP.md`, `plan.md`, `manuel.md`) at their existing paths. Add technical
guides under `docs/` and link them here.
