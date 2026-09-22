"""Provider-independent LLM interface and OpenAI-compatible client."""

from .client import (
    LLMClient,
    LLMConfigurationError,
    LLMResponseError,
    OpenAICompatibleClient,
    OpenAISettings,
)

__all__ = [
    "LLMClient",
    "LLMConfigurationError",
    "LLMResponseError",
    "OpenAICompatibleClient",
    "OpenAISettings",
]
