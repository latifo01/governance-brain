from __future__ import annotations

import json

import pytest

from gov360_brain.llm import LLMConfigurationError, OpenAICompatibleClient, OpenAISettings
from gov360_brain.llm.client import validate_endpoint


def test_network_policy_rejects_public_and_requires_remote_authorization(monkeypatch: pytest.MonkeyPatch) -> None:
    assert validate_endpoint("http://127.0.0.1:11434/v1", "local_only").startswith("http://127")
    with pytest.raises(LLMConfigurationError):
        validate_endpoint("https://example.invalid/v1", "local_only")
    monkeypatch.delenv("GOV360_AUTHORIZE_REMOTE", raising=False)
    monkeypatch.setenv("GOV360_LLM_ALLOWED_HOSTS", "internal.example")
    with pytest.raises(LLMConfigurationError):
        validate_endpoint("https://internal.example/v1", "approved_remote")
    monkeypatch.setenv("GOV360_AUTHORIZE_REMOTE", "true")
    assert validate_endpoint("https://internal.example/v1", "approved_remote").endswith("/v1")


def test_invalid_json_is_repaired_once_with_a_distinct_idempotency_key() -> None:
    settings = OpenAISettings(base_url="http://127.0.0.1:11434/v1", api_key="", model="local", max_retries=0)
    client = OpenAICompatibleClient(settings)
    calls: list[str | None] = []

    def fake_request(messages, schema, images, idempotency_key):
        calls.append(idempotency_key)
        return "not-json" if len(calls) == 1 else json.dumps({"answer": "ok"})

    client._request = fake_request  # type: ignore[method-assign]
    result = client.generate([], {"type": "object", "required": ["answer"], "properties": {"answer": {"type": "string"}}, "additionalProperties": False}, idempotency_key="job-1")
    assert result == {"answer": "ok"}
    assert calls == ["job-1", "job-1:repair"]

