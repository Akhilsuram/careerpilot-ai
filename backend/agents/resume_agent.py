import json
from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager


class ResumeAgent:

    def __init__(self):
        self.provider = ProviderManager()

    def analyze(self, resume_text: str):

        prompt = f"""
You are an expert Resume Analysis AI.

Extract the resume information and return ONLY a valid JSON object.

Rules:
- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT wrap the response in triple backticks.
- Do NOT include explanations.
- The response must start with '{{' and end with '}}'.

Return this exact schema:

{{
    "name": "",
    "email": "",
    "phone": "",
    "summary": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Resume:

{resume_text}
"""

        response = self.provider.generate(prompt)

        print("\n========== RAW RESPONSE ==========")
        print(response)
        print("==================================\n")

        # Remove markdown code fences if present
        response = response.strip()

        if response.startswith("```json"):
            response = response[7:]

        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        # Extract only the JSON object
        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                f"No valid JSON found in model response.\n\nResponse:\n{response}"
            )

        json_text = response[start:end + 1]

        try:
            return JSONParser.parse(response)

        except json.JSONDecodeError as e:
            print("\n========= JSON PARSE ERROR =========")
            print(json_text)
            print("====================================\n")
            raise e