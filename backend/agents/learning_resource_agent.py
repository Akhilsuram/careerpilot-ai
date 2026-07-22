import json

from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata
from backend.providers.provider_manager import ProviderManager
from backend.utils.json_parser import JSONParser


class LearningResourceAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Learning Resource Agent",
        version="1.0.0",
        description="Suggests learning resources.",
        priority=4,
    )

    def __init__(self):
        self.provider = ProviderManager()

    def execute(self, context):

        role = context.planner_output.get("target_role", "")

        prompt = f"""
Suggest the best learning resources for becoming a {role}.

Return ONLY JSON.

{{
    "courses": [],
    "youtube_channels": [],
    "books": [],
    "websites": [],
    "certifications": []
}}
"""

        response = self.provider.generate(prompt)

        return JSONParser.parse(response)