import json
from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager
from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata

class JobMatchAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Job Match Agent",
        version="1.0.0",
        description="Finds matching jobs based on resume and goals.",
        priority=4,
    )

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

Based on the resume below, recommend the best min 7 and max 10 jobs.

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
    def execute(
        self,
        context,
    ):

        role = context.planner_output.get(
            "target_role",
            "",
        )

        location = context.planner_output.get(
            "location",
            "",
        )

        return self.find_jobs(
            context.resume_data,
            role,
            location,
        )