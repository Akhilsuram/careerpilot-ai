from backend.providers.provider_manager import ProviderManager


class PlannerService:

    def __init__(self):
        self.provider = ProviderManager()

    def generate_plan(self, prompt: str):

        return self.provider.generate(prompt)