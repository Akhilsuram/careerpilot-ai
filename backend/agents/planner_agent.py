import json

from backend.providers.provider_manager import ProviderManager
from backend.utils.json_parser import JSONParser


class PlannerAgent:

    def __init__(self):

        self.provider = ProviderManager()

    def plan(
        self,
        user_goal: str,
    ):

        prompt = f"""
You are an AI Planning Agent.

Your task is to analyze the user's goal and decide which AI agents should execute.

Available Agents

resume_analysis

ats

resume_optimizer

job_match

interview

roadmap

Rules

If the user wants interview preparation,
only include interview.

If the user wants resume improvement,
include ats and resume_optimizer.

If the user wants jobs,
include ats, job_match and roadmap.

If the user wants everything,
include every agent.

Extract

target_role

location

Return ONLY valid JSON.

Format

{{
    "target_role":"",
    "location":"",
    "agents":[]
}}

Goal

{user_goal}
"""

        response = self.provider.generate(prompt)

        return JSONParser.parse(response)