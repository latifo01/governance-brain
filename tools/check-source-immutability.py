"""Verify current source hashes and reject changes to existing originals."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from gov360_brain.brain.portability import _verify_private_corpus


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--base", help="Git base revision used for pull-request immutability checks")
    args = parser.parse_args()
    root = args.root.resolve()
    counts = _verify_private_corpus(root)
    if args.base:
        result = subprocess.run(
            ["git", "diff", "--name-status", f"{args.base}...HEAD", "--", "sources/"],
            cwd=root, check=True, text=True, capture_output=True,
        )
        rows = [line.split("\t") for line in result.stdout.splitlines() if line.strip()]
        forbidden = [row for row in rows if row[0][0] in {"M", "D", "R", "C"}]
        if forbidden:
            raise SystemExit("Existing source files are immutable; modification, deletion, rename or copy detected.")
        if rows:
            changed = subprocess.run(
                ["git", "diff", "--name-only", f"{args.base}...HEAD", "--", "state/source_manifest.jsonl"],
                cwd=root, check=True, text=True, capture_output=True,
            ).stdout.strip()
            if not changed:
                raise SystemExit("A new source requires an updated source manifest.")
    print({"valid": True, **counts})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
