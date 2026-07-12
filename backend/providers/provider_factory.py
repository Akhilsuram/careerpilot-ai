from backend.core.settings import settings


class ProviderFactory:

    @staticmethod
    def create_provider():
        provider = settings.LLM_PROVIDER.lower()

        if provider == "groq":
            from backend.providers.groq_provider import GroqProvider
            return GroqProvider()

        if provider == "gemini":
            from backend.providers.gemini_provider import GeminiProvider
            return GeminiProvider()

        if provider == "openrouter":
            from backend.providers.openrouter_provider import OpenRouterProvider
            return OpenRouterProvider()

        if provider == "ollama":
            from backend.providers.ollama_provider import OllamaProvider
            return OllamaProvider()

        raise ValueError(f"Unsupported provider: {provider}")