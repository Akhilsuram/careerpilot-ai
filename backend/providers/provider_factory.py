from backend.core.settings import settings

from backend.providers.groq_provider import GroqProvider
from backend.providers.gemini_provider import GeminiProvider
from backend.providers.openrouter_provider import OpenRouterProvider
from backend.providers.ollama_provider import OllamaProvider


class ProviderFactory:

    @staticmethod
    def create_provider():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "groq":
            return GroqProvider()

        if provider == "gemini":
            return GeminiProvider()

        if provider == "openrouter":
            return OpenRouterProvider()

        if provider == "ollama":
            return OllamaProvider()

        raise ValueError("Unsupported provider")