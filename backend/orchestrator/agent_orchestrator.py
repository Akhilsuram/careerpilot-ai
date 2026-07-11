from backend.providers.provider_manager import ProviderManager


class AgentOrchestrator:

    def __init__(self):
        self.provider = ProviderManager()

    def generate(self, prompt: str):
        return self.provider.generate(prompt)