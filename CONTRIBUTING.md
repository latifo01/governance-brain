# Contributing to Governance Brain

Governance Brain welcomes focused improvements to its code, documentation and
evidence-backed knowledge. Start with the [documentation index](docs/README.md)
and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Set up a local environment

Use the Python version declared in `.python-version` and install
[uv](https://docs.astral.sh/uv/), then run:

```sh
uv sync --frozen --extra dev --extra data
uv run pytest -q
```

Platform instructions are available for [Ubuntu/WSL](docs/ubuntu-setup.md) and
[Windows](docs/windows-setup.md).

## Choose the contribution path

### Code and documentation

1. Describe the problem in an issue, or discuss the scope with the maintainer
   when issues are unavailable.
2. Create a focused branch from `main`, such as `docs/documentation-navigation`
   or `fix/retrieval-locators`.
3. Follow the existing structure and naming conventions. Keep current vault
   paths stable; folder names may contain spaces.
4. Run checks relevant to the change. Use synthetic fixtures for code tests.
5. Open a pull request describing the change, checks and any known limitations.
   Follow the repository's pull-request template; mark unrelated checks as
   not applicable with a short explanation.

### Knowledge, questions and domain navigation

Read [AGENTS.md](AGENTS.md), [ROADMAP.md](ROADMAP.md),
[WORKSHOP.md](WORKSHOP.md) and the [active note schema](brain%20wiki/SCHEMA.md)
before preparing a proposal.

- Original files under `sources/` are immutable.
- Canonical roles consume assigned, validated Markdown under `ingest/`.
- Claims and questions need reviewed evidence with hashes and precise locators.
- Only reviewed `BINDING` evidence supports obligations or prohibitions.
- Knowledge is written in English; questions have equivalent English and French
  wording and one assessable intent.
- Prepare changes under `state/workshop/` using a v3 domain-release manifest.
  Use the fast or strict lane required by the deterministic validator.
- Independent review and human approval of the exact candidate hash precede
  integration by the deterministic assembler.
- The question registry and questionnaire Canvas are generated outputs.

A merged pull request does not replace the evidence and knowledge-approval
workflow.

## Validation

For code or contract changes, run the relevant tests and validators. The main
repository checks are:

```sh
uv run pytest -q
uv run gov360 brain validate
uv run gov360 brain build --check
uv run --offline --no-sync python -m gov360_brain.workshop check-derived
```

For documentation-only changes, check links, paths and command examples, and
run `git diff --check`.

## Confidentiality and licensing

Keep secrets, project answers, personal data and raw source text out of issues,
pull-request discussions and operational logs. Report vulnerabilities through
the channels in [SECURITY.md](SECURITY.md).

Original code uses [Apache-2.0](LICENSE). Third-party documents and derived
material retain their own rights; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
The private handoff and public reconstruction kit have separate sharing rules.

## Versions and releases

Version history is maintained in
[GitHub Releases](https://github.com/latifo01/governance-brain/releases).
Include a short user-facing summary in your pull request so the maintainer can
reuse it in release notes. See the [GitHub documentation guide](docs/github.md)
for the release process.
