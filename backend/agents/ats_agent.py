import json

from backend.providers.provider_manager import ProviderManager


class ATSAgent:

    def __init__(self):

        self.provider = ProviderManager()

    def analyze(
        self,
        resume_data: dict,
        job_description: str
    ):

        prompt = f"""
You are an ATS Resume Expert.

You will receive

1. Resume JSON
2. Job Description

Evaluate the resume exactly like an Applicant Tracking System.

Return ONLY valid JSON.

Do not use markdown.

Output format:

{{
"overall_score":0,
"category_scores":{{
"skills":0,
"experience":0,
"projects":0,
"education":0,
"keywords":0
}},
"matched_keywords":[],
"missing_keywords":[],
"strengths":[],
"weaknesses":[],
"recommendations":[]
}}

Resume:

{json.dumps(resume_data, indent=2)}

Job Description:

{job_description}
"""

        response = self.provider.generate(prompt)

        response = response.replace("```json", "")

        response = response.replace("```", "")

        response = response.strip()

        return json.loads(response)