from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .utils import atomic_write_text


@dataclass(frozen=True, slots=True)
class ProjectPaths:
    root: Path

    @property
    def sources(self) -> Path:
        return self.root / "sources"

    @property
    def ingest(self) -> Path:
        return self.root / "ingest"

    @property
    def state(self) -> Path:
        return self.root / "state"

    @property
    def domain_packs(self) -> Path:
        return self.root / "domain_packs"

    @property
    def vault(self) -> Path:
        return self.root / "brain wiki"

    @classmethod
    def discover(cls, start: Path | None = None) -> "ProjectPaths":
        current = (start or Path.cwd()).resolve()
        for candidate in (current, *current.parents):
            if (candidate / "pyproject.toml").exists():
                return cls(candidate)
        raise FileNotFoundError("Could not find a Governance Brain project root")

    def ensure_layout(self) -> None:
        for path in (
            self.sources,
            self.sources / "_shared",
            self.ingest,
            self.state / "runs",
            self.domain_packs,
            self.vault,
        ):
            path.mkdir(parents=True, exist_ok=True)
        for name in (
            "source_manifest.jsonl",
            "source_classification_events.jsonl",
            "domain_registry.jsonl",
            "evidence_registry.jsonl",
            "knowledge_registry.jsonl",
            "question_registry.jsonl",
            "relations.jsonl",
            "unresolved.jsonl",
            "conflicts.jsonl",
            "taxonomy_proposals.jsonl",
            "approvals.jsonl",
        ):
            target = self.state / name
            if not target.exists():
                atomic_write_text(target, "")
