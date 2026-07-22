import json

from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata
from backend.providers.provider_manager import ProviderManager
from backend.utils.json_parser import JSONParser


class PlannerAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Planner Agent",
        version="2.0.0",
        description="Analyzes user goals and creates an execution plan.",
        priority=0,
    )

    def __init__(self):
        self.provider = ProviderManager()

    def execute(self, context):

        prompt = f"""
You are the Planner Agent of CareerPilot AI.

Analyze the user's goal.

Return ONLY valid JSON.

Format:

{{
    "target_role":"",
    "location":"",
    "experience_level":"",
    "focus_areas":[]
}}

User Goal:

{context.user_goal}
"""

        response = self.provider.generate(prompt)

        plan = JSONParser.parse(response)

        context.planner_output = plan

        context.outputs["planner"] = plan

        return plan