import json

from backend.providers.provider_manager import ProviderManager
from backend.utils.json_parser import JSONParser


class PlannerAgent:

    def __init__(self):
        self.provider = ProviderManager()

    def plan(self, user_goal: str):

        prompt = f"""
You are an AI Planner Agent.

User Goal:

{user_goal}

Identify:

1. Target Role
2. Preferred Location

Return ONLY valid JSON.

Format:

{{
    "target_role":"",
    "location":""
}}
"""

        response = self.provider.generate(prompt)

        return JSONParser.parse(response)