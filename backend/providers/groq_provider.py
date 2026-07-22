from groq import Groq

from backend.core.settings import settings
from backend.providers.base_provider import BaseProvider

class GroqProvider(BaseProvider):

    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.DEFAULT_MODEL

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
        )

        return response.choices[0].message.content

    def stream(self, prompt: str):

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def health_check(self) -> bool:

        try:
            self.generate("Say OK")
            return True
        except Exception:
            return False
        