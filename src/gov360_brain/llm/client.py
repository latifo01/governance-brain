from __future__ import annotations

import ipaddress
import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Protocol, Sequence, runtime_checkable
from urllib.parse import urlparse

from jsonschema import ValidationError, validate


class LLMConfigurationError(ValueError):
    pass


class LLMResponseError(RuntimeError):
    pass


@runtime_checkable
class LLMClient(Protocol):
    def generate(
        self,
        messages: Sequence[dict[str, Any]],
        response_schema: dict[str, Any],
        images: Sequence[str] | None = None,
        idempotency_key: str | None = None,
    ) -> dict[str, Any]: ...


def _truthy(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "on"}


def _allowed_hosts() -> set[str]:
    return {item.strip().lower() for item in os.getenv("GOV360_LLM_ALLOWED_HOSTS", "").split(",") if item.strip()}


def validate_endpoint(base_url: str, network_policy: str) -> str:
    parsed = urlparse(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise LLMConfigurationError("LLM base URL must be an absolute HTTP(S) URL")
    host = parsed.hostname.lower().rstrip(".")
    allowed = _allowed_hosts()
    is_local = host in {"localhost", "localhost.localdomain"}
    try:
        address = ipaddress.ip_address(host.strip("[]"))
        is_local = address.is_loopback or address.is_private or address.is_link_local
    except ValueError:
        pass
    if network_policy == "local_only":
        if not is_local and host not in allowed:
            raise LLMConfigurationError("strict-local profile rejected a public or unapproved LLM endpoint")
        if parsed.scheme != "https" and not is_local:
            raise LLMConfigurationError("Internal non-loopback endpoints must use HTTPS")
    elif network_policy == "approved_remote":
        if not _truthy(os.getenv("GOV360_AUTHORIZE_REMOTE")):
            raise LLMConfigurationError("Remote source processing requires GOV360_AUTHORIZE_REMOTE=true")
        if host not in allowed:
            raise LLMConfigurationError("Remote endpoint host must be explicitly allowlisted")
        if parsed.scheme != "https":
            raise LLMConfigurationError("Remote endpoints must use HTTPS")
    else:
        raise LLMConfigurationError(f"Unsupported network policy: {network_policy}")
    return base_url.rstrip("/")


@dataclass(frozen=True, slots=True)
class OpenAISettings:
    base_url: str
    api_key: str
    model: str
    api_style: str = "chat_completions"
    network_policy: str = "local_only"
    supports_json_schema: bool = True
    supports_vision: bool = False
    timeout_seconds: float = 120.0
    max_retries: int = 2

    @classmethod
    def from_env(cls, *, profile: str = "strict-local") -> "OpenAISettings":
        if profile == "no-llm":
            raise LLMConfigurationError("The no-llm profile does not configure an LLM client")
        base_url = os.getenv("GOV360_LLM_BASE_URL", "").strip()
        model = os.getenv("GOV360_LLM_MODEL", "").strip()
        if not base_url or not model:
            raise LLMConfigurationError("GOV360_LLM_BASE_URL and GOV360_LLM_MODEL are required")
        policy = "approved_remote" if profile == "approved-remote" else "local_only"
        return cls(
            base_url=validate_endpoint(base_url, policy),
            api_key=os.getenv("GOV360_LLM_API_KEY", ""),
            model=model,
            api_style=os.getenv("GOV360_LLM_API_STYLE", "chat_completions").strip(),
            network_policy=policy,
            supports_json_schema=_truthy(os.getenv("GOV360_LLM_SUPPORTS_JSON_SCHEMA", "true")),
            supports_vision=_truthy(os.getenv("GOV360_LLM_SUPPORTS_VISION", "false")),
            timeout_seconds=float(os.getenv("GOV360_LLM_TIMEOUT_SECONDS", "120")),
            max_retries=max(0, int(os.getenv("GOV360_LLM_MAX_RETRIES", "2"))),
        )

    def validate(self) -> None:
        validate_endpoint(self.base_url, self.network_policy)
        if self.api_style not in {"chat_completions", "responses"}:
            raise LLMConfigurationError("GOV360_LLM_API_STYLE must be chat_completions or responses")
        if not self.model:
            raise LLMConfigurationError("An LLM model identifier is required")


class OpenAICompatibleClient:
    def __init__(self, settings: OpenAISettings):
        settings.validate()
        self.settings = settings

    def generate(
        self,
        messages: Sequence[dict[str, Any]],
        response_schema: dict[str, Any],
        images: Sequence[str] | None = None,
        idempotency_key: str | None = None,
    ) -> dict[str, Any]:
        if images and not self.settings.supports_vision:
            raise LLMConfigurationError("Configured LLM endpoint does not declare vision support")
        raw = self._request(messages, response_schema, images, idempotency_key)
        try:
            parsed = self._parse_object(raw)
            validate(parsed, response_schema)
            return parsed
        except (ValidationError, LLMResponseError):
            repair_messages = [
                {"role": "system", "content": "Return only one JSON object conforming exactly to the supplied JSON Schema. Do not add facts."},
                {
                    "role": "user",
                    "content": json.dumps(
                        {"schema": response_schema, "invalid_response": raw},
                        ensure_ascii=False,
                        separators=(",", ":"),
                    ),
                },
            ]
            repaired_raw = self._request(
                repair_messages,
                response_schema,
                None,
                (idempotency_key + ":repair") if idempotency_key else None,
            )
            repaired = self._parse_object(repaired_raw)
            try:
                validate(repaired, response_schema)
            except ValidationError as exc:
                raise LLMResponseError("LLM response failed schema validation after one repair attempt") from exc
            return repaired

    def _request(
        self,
        messages: Sequence[dict[str, Any]],
        schema: dict[str, Any],
        images: Sequence[str] | None,
        idempotency_key: str | None,
    ) -> str:
        if self.settings.api_style == "responses":
            endpoint = self.settings.base_url + "/responses"
            payload: dict[str, Any] = {"model": self.settings.model, "input": list(messages)}
            if self.settings.supports_json_schema:
                payload["text"] = {"format": {"type": "json_schema", "name": "gov360_receipt", "schema": schema, "strict": True}}
        else:
            endpoint = self.settings.base_url + "/chat/completions"
            payload = {"model": self.settings.model, "messages": list(messages)}
            if self.settings.supports_json_schema:
                payload["response_format"] = {"type": "json_schema", "json_schema": {"name": "gov360_receipt", "schema": schema, "strict": True}}
        if images:
            payload["gov360_images"] = list(images)
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self.settings.api_key:
            headers["Authorization"] = f"Bearer {self.settings.api_key}"
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        request = urllib.request.Request(
            endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        for attempt in range(self.settings.max_retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=self.settings.timeout_seconds) as response:
                    decoded = json.loads(response.read().decode("utf-8"))
                return self._extract_text(decoded)
            except urllib.error.HTTPError as exc:
                if exc.code not in {408, 409, 429, 500, 502, 503, 504} or attempt >= self.settings.max_retries:
                    raise LLMResponseError(f"LLM endpoint returned HTTP {exc.code}") from exc
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                if attempt >= self.settings.max_retries:
                    raise LLMResponseError(f"LLM request failed: {type(exc).__name__}") from exc
            time.sleep(min(2.0, 0.5 * (2**attempt)))
        raise LLMResponseError("LLM request failed")

    def _extract_text(self, response: dict[str, Any]) -> str:
        if self.settings.api_style == "responses":
            if isinstance(response.get("output_text"), str):
                return response["output_text"]
            for output in response.get("output", []):
                for content in output.get("content", []):
                    if isinstance(content.get("text"), str):
                        return content["text"]
        else:
            try:
                content = response["choices"][0]["message"]["content"]
                if isinstance(content, str):
                    return content
            except (KeyError, IndexError, TypeError):
                pass
        raise LLMResponseError("LLM endpoint response contained no text result")

    @staticmethod
    def _parse_object(raw: str) -> dict[str, Any]:
        candidate = raw.strip()
        if candidate.startswith("```"):
            lines = candidate.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            candidate = "\n".join(lines).strip()
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError as exc:
            raise LLMResponseError("LLM returned invalid JSON") from exc
        if not isinstance(value, dict):
            raise LLMResponseError("LLM must return one JSON object")
        return value
