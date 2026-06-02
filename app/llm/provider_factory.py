from app.config import (
    LLM_PROVIDER
)

from app.llm.providers.gemini_provider import (
    GeminiProvider
)

from app.llm.providers.openai_provider import (
    OpenAIProvider
)

from app.llm.providers.anthropic_provider import (
    AnthropicProvider
)

from app.llm.providers.bedrock_provider import (
    BedrockProvider
)


class ProviderFactory:

    @staticmethod
    def get_provider():

        try:

            if LLM_PROVIDER == "gemini":
                return GeminiProvider()

            if LLM_PROVIDER == "openai":
                return OpenAIProvider()

            if LLM_PROVIDER == "anthropic":
                return AnthropicProvider()

            if LLM_PROVIDER == "bedrock":
                return BedrockProvider()

        except Exception:
            return AnthropicProvider()

        supported = [
            "gemini",
            "openai",
            "anthropic",
            "bedrock"
        ]

        raise ValueError(
            (
                f"Unsupported provider "
                f"{LLM_PROVIDER}. "
                f"Supported: {supported}"
            )
        )
