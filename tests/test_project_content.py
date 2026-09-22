from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "config" / "schemas"

SEED_DOMAIN_SLUGS = {
    "governance-accountability",
    "legal-regulatory",
    "data-privacy",
    "ai-security",
    "model-risk",
    "operational-resilience-incidents",
    "third-parties-supply-chain",
    "human-oversight-responsible-ai",
    "transparency-disclosure",
    "audit-assurance",
}
ROLE_NAMES = {
    "cdo_program_lead",
    "source_extractor",
    "evidence_auditor",
    "knowledge_architect",
    "questionnaire_curator",
    "questionnaire_reviewer",
    "vault_reviewer",
    "domain_builder",
    "release_reviewer",
    "git_helper",
}
SKILL_NAMES = {
    "source-ingestion",
    "pdf-evidence-extraction",
    "knowledge-synthesis",
    "obsidian-graph",
    "questionnaire-design",
    "vault-audit",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), path
    return value


def test_public_json_schemas_are_valid() -> None:
    expected = {
        "domain-pack.schema.json",
        "source-manifest.schema.json",
        "ingested-unit.schema.json",
        "receipt.schema.json",
        "questionnaire.schema.json",
        "profile.schema.json",
        "relation.schema.json",
        "vault-frontmatter.schema.json",
        "context-packet.schema.json",
        "brain-note.schema.json",
        "brain-context.schema.json",
            "brain-research.schema.json",
            "brain-task.schema.json",
            "brain-coverage-review.schema.json",
        "brain-evidence.schema.json",
        "private-handoff.schema.json",
        "workshop-release.schema.json",
        "workshop-release-v3.schema.json",
    }
    assert {path.name for path in SCHEMAS.glob("*.json")} == expected
    for path in SCHEMAS.glob("*.json"):
        jsonschema.Draft202012Validator.check_schema(load_json(path))


def test_seed_domain_packs_validate_and_have_stable_unique_ids() -> None:
    validator = jsonschema.Draft202012Validator(
        load_json(SCHEMAS / "domain-pack.schema.json")
    )
    packs: list[dict] = []
    for path in sorted((ROOT / "domain_packs").glob("*/domain.yaml")):
        pack = load_yaml(path)
        validator.validate(pack)
        assert path.parent.name == "_template" or path.parent.name == pack["slug"]
        assert pack["review_policy"] == "HUMAN_APPROVAL"
        packs.append(pack)

    seeds = [pack for pack in packs if pack["slug"] != "example-domain"]
    assert {pack["slug"] for pack in seeds} == SEED_DOMAIN_SLUGS
    assert len({pack["domain_id"] for pack in seeds}) == len(seeds)
    assert len({pack["question_prefix"] for pack in seeds}) == len(seeds)
    assert all(pack["status"] == "ACTIVE" for pack in seeds)
    registry = json.loads((ROOT / "config" / "brain-domains.json").read_text(encoding="utf-8"))
    assert {pack["domain_id"] for pack in seeds} <= set(registry)
    assert {"AI", "LEGAL", "DATA_PROTECTION", "INTERNAL_REGULATION", "RISK", "PROCESS", "GENERAL"} <= set(registry)


def test_profiles_validate_and_enforce_egress_defaults() -> None:
    validator = jsonschema.Draft202012Validator(load_json(SCHEMAS / "profile.schema.json"))
    profiles = {
        path.stem: load_yaml(path)
        for path in sorted((ROOT / "config" / "profiles").glob("*.yaml"))
    }
    assert set(profiles) == {"strict-local", "approved-remote", "no-llm"}
    for name, profile in profiles.items():
        validator.validate(profile)
        assert profile["profile_id"] == name

    assert profiles["strict-local"]["network_policy"] == "local_only"
    assert profiles["approved-remote"]["requires_explicit_egress_authorization"] is True
    assert profiles["approved-remote"]["allowed_hosts_env"]
    assert profiles["approved-remote"]["egress_authorization_env"]
    assert profiles["no-llm"]["llm_enabled"] is False
    assert profiles["no-llm"]["network_policy"] == "none"
    assert profiles["no-llm"]["max_llm_workers"] == 0


def test_codex_wrappers_are_complete_and_do_not_pin_models() -> None:
    config = tomllib.loads((ROOT / ".codex" / "config.toml").read_text(encoding="utf-8"))
    agents = config["agents"]
    assert agents["max_concurrent_threads_per_session"] == 3
    assert ROLE_NAMES == {name for name, value in agents.items() if isinstance(value, dict)}

    for role in ROLE_NAMES:
        wrapper_path = ROOT / ".codex" / "agents" / f"{role}.toml"
        wrapper = tomllib.loads(wrapper_path.read_text(encoding="utf-8"))
        assert wrapper["name"] == role
        assert "prompts/roles/" in wrapper["developer_instructions"]
        assert not any(key.startswith("model") for key in wrapper)
        assert (ROOT / "prompts" / "roles" / f"{role}.md").is_file()


def test_opencode_primary_source_access_and_subagent_boundaries() -> None:
    config = load_json(ROOT / "opencode.json")
    assert config["permission"]["read"]["sources/**"] == "allow"
    assert config["permission"]["edit"]["sources/**"] == "deny"
    assert config["permission"]["edit"]["ingest/**"] == "deny"
    for builtin in ("explore", "general"):
        assert config["agent"][builtin]["permission"]["read"]["sources/**"] == "deny"

    opencode_agents = ROOT / ".opencode" / "agents"
    for path in opencode_agents.glob("*.md"):
        match = re.match(r"\A---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.DOTALL)
        assert match, path
        frontmatter = yaml.safe_load(match.group(1))
        assert frontmatter["permission"]["read"]["sources/**"] == "deny"
        if path.stem in {"questionnaire-reviewer", "vault-reviewer"}:
            assert frontmatter["permission"]["read"]["ingest/**"] == "deny"

    commands = {path.stem for path in (ROOT / ".opencode" / "commands").glob("*.md")}
    assert commands == {
        "brain-next",
        "brain-build",
        "brain-review",
        "brain-review-strict",
        "brain-release",
        "brain-git-helper",
        "brain-canvas-watch",
        "question-lot",
        "review-question-lot",
        "review-vault-lot",
    }

    assert config["model"] == "openrouter/deepseek/deepseek-v4-flash-0731"
    assert config["small_model"] == "openrouter/mistralai/mistral-small-3.2-24b-instruct"
    # DeepSeek Flash is the configured default and strict-review model for
    # OpenCode (operator directive 2026-09-18, replacing GLM 5.3). Other
    # wrappers remain provider-configured and do not pin models in prompts.
    assert "openrouter/deepseek/deepseek-v4-flash-0731" in (ROOT / ".opencode/agents/evidence-auditor.md").read_text(encoding="utf-8")


def test_provider_independent_prompts_define_safe_structured_outputs() -> None:
    forbidden_model = re.compile(r"\b(?:gpt|claude|gemini|mistral|llama)-?[a-z0-9.]*\b", re.I)
    for role in ROLE_NAMES:
        text = (ROOT / "prompts" / "roles" / f"{role}.md").read_text(encoding="utf-8")
        assert "Return JSON only" in text
        assert "response schema" in text
        assert forbidden_model.search(text) is None


def test_project_skills_have_valid_frontmatter_and_resolvable_references() -> None:
    skill_root = ROOT / ".agents" / "skills"
    assert {path.name for path in skill_root.iterdir() if path.is_dir()} == SKILL_NAMES

    link_pattern = re.compile(r"\[[^]]+\]\(([^)]+)\)")
    for skill_name in SKILL_NAMES:
        skill_file = skill_root / skill_name / "SKILL.md"
        text = skill_file.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        assert match, skill_file
        frontmatter = yaml.safe_load(match.group(1))
        assert frontmatter["name"] == skill_name
        assert isinstance(frontmatter["description"], str)
        assert len(frontmatter["description"]) >= 30

        links = link_pattern.findall(text)
        assert links, f"{skill_name} must progressively route to a contract or reference"
        for link in links:
            assert not link.startswith(("http://", "https://"))
            assert (skill_file.parent / link).resolve().is_file(), (skill_file, link)


def test_repository_invariants_and_onboarding_are_documented() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "Never modify, rename, overwrite, or delete a file under `sources/`" in agents
    assert "validated Markdown units under `ingest/`" in agents
    assert "Only a reviewed `BINDING` source can support an obligation" in agents
    assert "Publication requires the configured human approval" in agents

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required in (
        "ROADMAP.md",
        "brain-note.schema.json",
        "no-llm",
        "questionnaire-reviewer",
        "legacy v1",
        "Retire a source",
    ):
        assert required in readme

    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    assert "Governance coverage map" in roadmap
    assert "Sustainability and societal impact" in roadmap

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "sources/**" not in gitignore
    assert "ingest/**/*.parquet" not in gitignore
    assert "dist/cdo-handoff/" in gitignore
    assert ".offline/" in gitignore
    assert ".pytest_tmp/" in gitignore
