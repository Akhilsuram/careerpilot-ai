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

        return JSONParser.parse(response)
    def execute(
        self,
        context,
    ):

        return self.analyze(
            context.resume_data,
            context.user_goal,
        )