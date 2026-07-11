from backend.providers.provider_factory import ProviderFactory


class ProviderManager:

    def __init__(self):
        self.provider = ProviderFactory.create_provider()

    def generate(self, prompt: str):
        return self.provider.generate(prompt)

    def health_check(self):
        return self.provider.health_check()