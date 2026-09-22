# Ubuntu / WSL setup

Keep the repository on the Linux filesystem and run these commands from its
root. Recreate the environment from the versioned Python and dependency files;
do not reuse a virtual environment copied from Windows.

```sh
uv python install
uv sync --frozen --extra dev --extra data
uv run python --version
uv run python -c "import sys; print(sys.executable)"
```

The interpreter path must end in `.venv/bin/python` or `.venv/bin/python3`.
Run the local checks without publishing or calling a remote model:

```sh
uv run pytest -q
uv run --offline --no-sync python -m gov360_brain.workshop quality
uv run --offline --no-sync python -m gov360_brain.workshop validate
uv run gov360 status
```

Open the repository in VSCodium Remote WSL and the vault in the Ubuntu-specific
Obsidian installation with the local shell helpers:

```sh
codium .
obs "brain wiki"
```

Use `raccourcis` in an interactive Zsh session to display the complete local
command summary.

The local Brain requires SQLite with FTS5 in the project Python environment.
Check the actual build before retrieval:

```sh
uv run python -c "import sqlite3; c=sqlite3.connect(':memory:'); c.execute('create virtual table smoke using fts5(content)'); print('FTS5: OK')"
uv run gov360 brain status
uv run gov360 brain build
uv run gov360 brain build --check
```

Do not substitute a Windows environment or install another database server.
`bootstrap --source-root sources` previews reconstruction using local originals;
its `--apply` flag performs the authorized reconstruction. Paths and manifests
remain portable, including the space in `brain wiki/`.
