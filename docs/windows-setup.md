# Windows setup for the CDO handoff

This repository supports native Windows 11 with PowerShell 7. WSL remains an
option, but it is not required. Keep the repository in a normal local folder;
OneDrive synchronisation is not recommended while tests or derived builders are
running.

## 1. Install the prerequisites

Install Git for Windows, PowerShell 7, `uv`, Obsidian, VSCodium and the official
OpenCode CLI. The OpenCode project configuration is already in `opencode.json`
and `.opencode/`. Install OpenCode from its official Windows download, or use
the official npm package documented by OpenCode. Confirm each command:

```powershell
git --version
uv --version
opencode --version
```

Do not copy a Linux or older Windows `.venv`. The project requests Python
3.12.12 through `.python-version`; `uv` installs it locally.

## 2. Clone and restore

```powershell
git clone https://github.com/latifo01/governance-brain.git
Set-Location "governance-brain"
uv python install
uv sync --frozen --extra dev --extra data
```

For local rendering of legacy Office files through Microsoft Office, rerun the
sync with `--extra office-windows`. This is optional and does not enable macros
or make Office originals valid evidence by itself.

## 3. Validate the handoff

```powershell
PowerShell -ExecutionPolicy Bypass -File .\tools\setup-windows.ps1 -CheckOnly
```

The script checks the Windows virtual environment, the vault, derived outputs,
tests and OpenCode configuration. It never calls an LLM. `brain wiki` contains
a space; always quote it in PowerShell commands.

Linux `Zone.Identifier` sidecar files are not source documents and contain no
document body. The portable handoff excludes the six such sidecars found beside
the originals because `:` is not a valid Windows filename character; every
manifested original and its recorded SHA-256 remain included.

Open the vault with Obsidian by choosing the `brain wiki` directory. The
questionnaire Canvas is derived from the Markdown questions and must be rebuilt,
not edited as canonical content.

## 4. Configure OpenCode and OpenRouter

From the repository root:

```powershell
opencode auth login
opencode debug config
opencode debug skill
opencode debug agent cdo-program-lead
opencode
```

Choose OpenRouter during authentication. Credentials remain in OpenCode's user
configuration and must never be committed. Project sharing is disabled. Do not
use `opencode --auto`: the permission prompts protect source, ingest, contracts
and publication-sensitive files.

The first message to OpenCode is:

```text
Read AGENTS.md, WORKSHOP.md, ROADMAP.md, brain wiki/SCHEMA.md, plan.md and
manuel.md. Inspect the current Brain status and evidence blockers. Select one
bounded uncovered need. Preserve source and ingest files, stable IDs,
frontmatter and evidence locators. Prepare a reviewed candidate and present its
exact hash before any publication.
```

## 5. Daily start

```powershell
git pull --ff-only
uv sync --frozen --extra dev --extra data
uv run gov360 brain status
uv run gov360 brain validate
uv run gov360 brain build --check
```

Follow `manuel.md` for adding a document, preparing a fast or strict lot,
independent review, human hash approval and deterministic integration.
