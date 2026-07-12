from backend.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Ollama provider not implemented.")

    def stream(self, prompt: str):
        raise NotImplementedError("Ollama provider not implemented.")

    def health_check(self) -> bool:
        return False