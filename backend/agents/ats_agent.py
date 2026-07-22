import json
from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager
from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata

class ATSAgent(BaseAgent):

    metadata = AgentMetadata(
        name="ATS Agent",
        version="1.0.0",
        description="Analyzes ATS compatibility.",
        priority=1,
    )

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
"overall_score":85,
"category_scores":{{
"skills":90,
"experience":75,
"projects":80,
"education":95,
"keywords":85
}},
"matched_keywords":[],
"missing_keywords":[],
"strengths":[],
"weaknesses":[],
"recommendations":[]
}}
IMPORTANT:
- overall_score MUST be an INTEGER between 0 and 100.
- Never return decimals like 0.85 or 0.72.
- category_scores MUST also be integers from 0 to 100.
- Do NOT use percentages as strings.
- Do NOT include the % symbol.

Resume:

{json.dumps(resume_data, indent=2)}

Job Description:

{job_description}
"""

        response = self.provider.generate(prompt)

        result = JSONParser.parse(response)

        overall = result.get("overall_score")

        if isinstance(overall, float):
            if overall <= 1:
                result["overall_score"] = round(overall * 100)
            else:
                result["overall_score"] = round(overall)

        for key, value in result.get("category_scores", {}).items():
            if isinstance(value, float):
                if value <= 1:
                    result["category_scores"][key] = round(value * 100)
                else:
                    result["category_scores"][key] = round(value)

        return result
    

    def execute(
        self,
        context,
    ):

        return self.analyze(
            context.resume_data,
            context.user_goal,
        )