"""Synthetic retrieval tests; no repository source excerpts or project answers."""
from copy import deepcopy
from datetime import date
from hashlib import sha256
import json
from pathlib import Path

import jsonschema
import pytest

from gov360_brain.brain.retrieval import build_context, evaluate, _estimate


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[8]


def section(note_id="synthetic-note", *, text="Synthetic oversight controls", source="SYNTH-001", **overrides):
    item = {"section_id": note_id + "#summary", "note_id": note_id,
        "path": f"brain wiki/Synthetic/{note_id}.md", "title": "Synthetic human oversight",
        "heading": "Summary", "heading_path": ["Synthetic human oversight", "Summary"],
        "text": text, "sha256": sha256(text.encode()).hexdigest(), "note_sha256": "a" * 64,
        "type": "knowledge", "domains": ["RISK"], "tags": [], "aliases": [], "status": "active",
        "evidence_status": "REVIEWED", "derived_from": ["synthetic-evidence-001"],
        "citations": [{"evidence_ref": "synthetic-evidence-001", "source_id": source,
            "source_sha256": "b" * 64, "unit_path": "ingest/synthetic/unit.md",
            "unit_sha256": "c" * 64, "unit_file_sha256": "d" * 64, "locator": "Section 1",
            "authority": "GUIDANCE", "jurisdiction": ["EU"], "valid_from": None, "valid_until": None}]}
    item.update(overrides)
    return item


def context(tmp_path, items=None, **kwargs):
    return build_context(tmp_path, kwargs.pop("query", "oversight"),
        catalogue={"sections": items if items is not None else [section()], "edges": kwargs.pop("edges", [])}, **kwargs)


def test_cited_packet_schema_deterministic_and_no_files(tmp_path):
    result = context(tmp_path, as_of="2026-09-15")
    assert result == context(tmp_path, as_of="2026-09-15")
    assert result["sections"][0]["citations"][0]["locator"] == "Section 1"
    assert result["budget"]["estimated_tokens"] == _estimate(result)
    jsonschema.validate(result, json.loads((ROOT / "config/schemas/brain-context.schema.json").read_text()))
    assert not list(tmp_path.iterdir())
    assert "query" not in result


@pytest.mark.parametrize("overrides", [{"evidence_status": "UNRESOLVED"}, {"citations": []}, {"status": "deprecated"}, {"type": "index"}])
def test_assistance_fails_closed(tmp_path, overrides):
    packet = context(tmp_path, [section(**overrides)])
    assert packet["sections"] == []
    assert "no_eligible_evidence" in packet["gaps"]


def test_research_requires_explicit_mode_and_marks_unreviewed(tmp_path):
    item = section(evidence_status="UNRESOLVED", citations=[])
    assert not context(tmp_path, [item])["sections"]
    result = context(tmp_path, [item], mode="research")
    assert result["sections"]
    assert "research_contains_unreviewed_material" in result["gaps"]
    assert not context(tmp_path, [item], mode="research", allowed_source_ids=[])["sections"]


def test_mixed_citations_access_is_all_and_deny_wins(tmp_path):
    item = section()
    other = deepcopy(item["citations"][0])
    other.update(source_id="SYNTH-002", authority="BINDING")
    item["citations"].append(other)
    assert not context(tmp_path, [item], allowed_source_ids=["SYNTH-001"])["sections"]
    assert not context(tmp_path, [item], allowed_source_ids=["SYNTH-001", "SYNTH-002"], denied_source_ids=["SYNTH-002"])["sections"]
    retained = context(tmp_path, [item])["sections"][0]
    assert "authority" not in retained
    assert [c["authority"] for c in retained["citations"]] == ["GUIDANCE", "BINDING"]


def test_empty_access_list_and_domains_are_deny_all(tmp_path):
    assert not context(tmp_path, allowed_source_ids=[])["sections"]
    assert not context(tmp_path, domains=[])["sections"]
    assert context(tmp_path, domains=["RISK"])["sections"]


def test_missing_evidence_link_does_not_pass(tmp_path):
    item = section()
    item["citations"][0]["unit_file_sha256"] = None
    assert not context(tmp_path, [item])["sections"]


def test_jurisdiction_and_temporal_scope(tmp_path):
    item = section()
    assert context(tmp_path, [item], jurisdiction="EU")["sections"]
    assert not context(tmp_path, [item], jurisdiction="US")["sections"]
    item["citations"][0]["jurisdiction"] = []
    assert not context(tmp_path, [item], jurisdiction="EU")["sections"]
    item["citations"][0].update(valid_from="2025-01-01", valid_until="2026-01-01")
    assert context(tmp_path, [item], as_of="2025-01-01")["sections"]
    assert not context(tmp_path, [item], as_of="2024-12-31")["sections"]
    assert not context(tmp_path, [item], as_of="2026-01-02")["sections"]
    item["citations"][0]["valid_from"] = "invalid"
    assert not context(tmp_path, [item])["sections"]


def test_entire_envelope_budget_and_oversized_section_gap(tmp_path):
    packet = context(tmp_path, token_budget=256)
    assert packet["budget"]["estimated_tokens"] <= 256
    assert _estimate(packet) <= 256
    packet = context(tmp_path, [section(text="Synthetic " * 10000)], token_budget=1000)
    assert packet["sections"] == []
    assert "sections_omitted_for_budget" in packet["gaps"]
    assert _estimate(packet) <= 1000


def test_empty_and_malformed_queries_are_sanitized(tmp_path):
    for query in ["", "   ", "!!!", "the and le"]:
        packet = context(tmp_path, query=query)
        assert not packet["sections"]
        assert "empty_search_terms" in packet["gaps"]
    packet = context(tmp_path, query='" OR * NEAR(oversight) - column:secret')
    assert isinstance(packet, dict)
    with pytest.raises(ValueError, match="at least 256"):
        context(tmp_path, token_budget=1)
    with pytest.raises(ValueError) as error:
        context(tmp_path, query="sensitive" * 2000)
    assert "sensitive" not in str(error.value)


def test_french_expansion_and_accent_handling(tmp_path):
    (tmp_path / "config").mkdir()
    (tmp_path / "config/brain-vocabulary.json").write_text(json.dumps({"groups": [{"terms": ["contrôle humain", "human oversight"]}]}))
    result = context(tmp_path, query="contrôle humain")
    assert result["sections"]


def test_one_hop_graph_cannot_bypass_access_or_expand_twice(tmp_path):
    a = section("alpha")
    b = section("beta", text="Synthetic neighbor", title="Neighbor", heading_path=["Neighbor"])
    c = section("gamma", text="Synthetic second hop", title="Second hop", heading_path=["Second hop"])
    hidden = section("hidden", text="Synthetic restricted", title="Restricted", heading_path=["Restricted"], source="SYNTH-SECRET")
    edges = [{"source": "alpha", "target": "beta", "kind": "link"}, {"source": "beta", "target": "gamma", "kind": "link"}, {"source": "alpha", "target": "hidden", "kind": "link"}]
    result = context(tmp_path, [a, b, c, hidden], edges=edges, denied_source_ids=["SYNTH-SECRET"])
    assert [s["note_id"] for s in result["sections"]] == ["alpha", "beta"]
    assert result["sections"][1]["selection"] == "graph_one_hop"
    assert "SYNTH-SECRET" not in json.dumps(result)


def test_bm25_title_weighted_and_result_diversity(tmp_path):
    body = section("body", title="Unrelated", heading_path=["Unrelated"], text="oversight")
    title = section("title", title="Oversight", heading_path=["Summary"], text="synthetic")
    result = context(tmp_path, [body, title])
    assert result["sections"][0]["note_id"] == "title"
    many = [section(f"note-{i:02}") for i in range(40)]
    assert len(context(tmp_path, many, token_budget=100000)["sections"]) == 10


def test_graph_seed_must_fit_packet(tmp_path):
    a = section("alpha", text="Synthetic " * 10000)
    b = section("beta", text="Synthetic neighbor", title="Neighbor", heading_path=["Neighbor"])
    packet = context(tmp_path, [a, b], edges=[{"source": "alpha", "target": "beta", "kind": "link"}], token_budget=1000)
    assert not packet["sections"]
    assert "sections_omitted_for_budget" in packet["gaps"]


def test_benchmark_inventory_and_unavailable_is_not_success(tmp_path):
    (tmp_path / "config").mkdir()
    payload = (REPO_ROOT / "config/brain-evaluation.json").read_text()
    (tmp_path / "config/brain-evaluation.json").write_text(payload)
    result = evaluate(tmp_path, catalogue={"sections": [], "edges": []})
    assert result["scenario_count"] == 45
    assert result["complete_suite"]
    assert result["ready_positive_count"] == 0
    assert result["unavailable_positive_count"] == 30
    assert result["recall_at_5"] is None
    assert result["negative_pass_count"] == 15
    assert not result["accepted"]
    assert all("query" not in row for row in result["results"])


def test_benchmark_with_ready_miss_does_not_count_unavailability(tmp_path):
    (tmp_path / "config").mkdir()
    case = {"id": "synthetic-positive", "pillar": "synthetic-pillar", "kind": "positive", "language": "en", "query": "unfindabletoken", "expected_note_ids": ["synthetic-note"]}
    (tmp_path / "config/brain-evaluation.json").write_text(json.dumps({"scenarios": [case]}))
    result = evaluate(tmp_path, catalogue={"sections": [section()], "edges": []})
    assert result["ready_positive_count"] == 1
    assert result["recall_at_5"] == 0
    assert result["results"][0]["result"] == "MISS"


def test_v3_preserves_modality_review_and_temporal_qualification(tmp_path):
    item = section(modality="obligation", applicability={"roles": ["deployer"]},
                   conflicts=["synthetic-exception"], limits=["synthetic-limit"],
                   access_restrictions=["synthetic-restriction"])
    item["citations"][0].update(
        authority="BINDING", document_date="2024-01-02", applicable_from="2025-01-01",
        applicable_until="2027-01-01", reviewed_at="2026-09-01T10:00:00Z",
        review_expires_at="2026-12-31", evidence_status="REVIEWED", source_status="READY_FOR_LLM")
    packet = context(tmp_path, [item], as_of="2026-09-15")
    assert packet["schema_version"] == 3
    assert packet["temporal_policy"] == {"require_known_validity": False, "unknown_bounds": "report"}
    selected = packet["sections"][0]
    assert selected["modality"] == "obligation"
    assert selected["applicability"] == {"roles": ["deployer"]}
    assert selected["conflicts"] == ["synthetic-exception"]
    assert selected["limits"] == ["synthetic-limit"]
    assert selected["access_restrictions"] == ["synthetic-restriction"]
    assert selected["citations"][0]["document_date"] == "2024-01-02"
    assert selected["citations"][0]["reviewed_at"] == "2026-09-01T10:00:00Z"
    jsonschema.validate(packet, json.loads((ROOT / "config/schemas/brain-context.schema.json").read_text()))


def test_unknown_validity_is_reported_or_excluded_without_date_inference(tmp_path):
    item = section(modality="recommendation")
    item["citations"][0].update(reviewed_at="2026-09-15T10:00:00Z")
    reported = context(tmp_path, [item], as_of="2026-09-15")
    assert reported["sections"]
    assert "unknown_validity" in reported["gaps"]
    excluded = context(tmp_path, [item], as_of="2026-09-15", require_known_validity=True)
    assert not excluded["sections"]
    assert excluded["exclusions"]["unknown_validity"] == 1
    assert excluded["temporal_policy"]["unknown_bounds"] == "exclude"


@pytest.mark.parametrize("field, value, gap", [
    ("source_status", "REVOKED", "revoked_evidence"),
    ("source_status", "SUPERSEDED", "superseded_evidence"),
    ("hash_status", "CHANGED", "hash_changed"),
])
def test_revocation_supersession_and_hash_changes_fail_closed(tmp_path, field, value, gap):
    item = section()
    item["citations"][0][field] = value
    packet = context(tmp_path, [item])
    assert not packet["sections"]
    assert packet["exclusions"][gap] == 1


def test_review_expiry_and_non_binding_obligation_fail_closed(tmp_path):
    expired = section()
    expired["citations"][0]["review_expires_at"] = "2026-01-01"
    packet = context(tmp_path, [expired], as_of="2026-09-15")
    assert not packet["sections"]
    assert packet["exclusions"]["review_expired"] == 1

    non_binding = section(modality="prohibition")
    packet = context(tmp_path, [non_binding], as_of="2026-09-15")
    assert not packet["sections"]
    assert packet["exclusions"]["modality_authority"] == 1


def test_mixed_modalities_are_section_qualified_and_citations_remain_distinct(tmp_path):
    recommendation = section("recommendation", text="Synthetic recommendation", modality="recommendation")
    definition = section("definition", text="Synthetic definition", modality="definition")
    definition["citations"][0]["authority"] = "STANDARD"
    result = context(tmp_path, [recommendation, definition])
    assert {row["modality"] for row in result["sections"]} == {"recommendation", "definition"}
    assert all(row["citations"][0]["authority"] in {"GUIDANCE", "STANDARD"} for row in result["sections"])
