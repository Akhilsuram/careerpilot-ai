import json
from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager


class JobMatchAgent:

    def __init__(self):

        self.provider = ProviderManager()

    def find_jobs(
        self,
        resume_data: dict,
        target_role: str,
        location: str,
    ):

        prompt = f"""
You are an AI Job Matching Agent.

Based on the resume below, recommend the best 5 jobs.

Role:
{target_role}

Location:
{location}

Return ONLY valid JSON.

Format:

{{
"jobs":[
{{
"company":"",
"role":"",
"location":"",
"match_score":0,
"required_skills":[],
"missing_skills":[],
"reason":""
}}
]
}}

Resume:

{json.dumps(resume_data, indent=2)}
"""

        response = self.provider.generate(prompt)

        return JSONParser.parse(response)