import json

from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata
from backend.providers.provider_manager import ProviderManager
from backend.utils.json_parser import JSONParser


class SkillGapAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Skill Gap Agent",
        version="1.0.0",
        description="Finds missing skills.",
        priority=2,
    )

    def __init__(self):
        self.provider = ProviderManager()

    def execute(self, context):

        role = context.planner_output.get("target_role", "")

        prompt = f"""
You are an AI Career Coach.

Resume:

{json.dumps(context.resume_data, indent=2)}

Target Role:

{role}

Return ONLY JSON.

{{
    "missing_skills":[],
    "recommended_courses":[],
    "recommended_projects":[],
    "priority_skills":[]
}}
"""

        response = self.provider.generate(prompt)

        return JSONParser.parse(response)