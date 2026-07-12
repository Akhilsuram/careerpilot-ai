import json

from backend.providers.provider_manager import ProviderManager


class ResumeOptimizerAgent:

    def __init__(self):

        self.provider = ProviderManager()

    def optimize(
        self,
        resume_data: dict,
        target_role: str,
    ):

        prompt = f"""
You are an Expert Resume Writer.

Improve this resume for the role:

{target_role}

Requirements:

1. Improve Summary.

2. Improve Project descriptions.

3. Improve Experience descriptions.

4. Suggest ATS keywords.

5. Keep information truthful.

Return ONLY valid JSON.

{{
"optimized_summary":"",
"optimized_skills":[],
"optimized_projects":[],
"optimized_experience":[],
"recommendations":[]
}}

Resume:

{json.dumps(resume_data, indent=2)}
"""

        response = self.provider.generate(prompt)

        response = response.replace("```json", "")

        response = response.replace("```", "")

        response = response.strip()

        return json.loads(response)