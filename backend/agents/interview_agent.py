import json

from backend.providers.provider_manager import ProviderManager


class InterviewAgent:

    def __init__(self):

        self.provider = ProviderManager()

    def generate_questions(
        self,
        resume_data: dict,
        target_role: str,
        job_description: str | None = None,
    ):

        prompt = f"""
You are an Expert Technical Interviewer.

Generate 15 interview questions.

Mix:

HR

Projects

Python

SQL

Machine Learning

Behavioral

DSA

Return ONLY valid JSON.

Format

{{
"questions":[
{{
"category":"",
"difficulty":"",
"question":"",
"answer":""
}}
]
}}

Resume

{json.dumps(resume_data, indent=2)}

Role

{target_role}

Job Description

{job_description}
"""

        response = self.provider.generate(prompt)

        response = response.replace("```json", "")

        response = response.replace("```", "")

        response = response.strip()

        return json.loads(response)