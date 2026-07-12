import google.generativeai as genai

from backend.core.settings import settings
from backend.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate(self, prompt: str) -> str:

        response = self.model.generate_content(prompt)

        return response.text

    def stream(self, prompt: str):
        raise NotImplementedError("Gemini streaming not implemented yet.")


    def health_check(self) -> bool:
        try:
            self.generate("Say OK")
            return True
        except Exception:
            return False