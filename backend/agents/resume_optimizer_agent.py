import json

from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager
from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata


class ResumeOptimizerAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Resume Optimizer",
        version="1.0.0",
        description="Optimizes resumes for target roles.",
        priority=2,
    )

    def __init__(self):
        self.provider = ProviderManager()

    def optimize(
        self,
        resume_data: dict,
        target_role: str,
    ):

        prompt = f"""
You are an Expert Resume Writer.

Improve this resume for the role:

{target_role}

Requirements:

1. Improve the professional summary.

2. Improve project descriptions.

3. Improve experience descriptions.

4. Suggest ATS keywords and resume recommendations.

5. List 3-5 strengths of the resume.

6. List 3-5 areas for improvement.

7. Give an overall Resume Score out of 100.

8. Keep every statement truthful.

Return ONLY valid JSON.

{{
    "resume_score": 95,
    "optimized_summary": "",
    "optimized_skills": [],
    "optimized_projects": [],
    "optimized_experience": [],
    "recommendations": [],
    "strengths": [],
    "improvements": []
}}

Resume:

{json.dumps(resume_data, indent=2)}
"""

        response = self.provider.generate(prompt)

        result = JSONParser.parse(response)
        result.setdefault("recommendations", [])
        result.setdefault("strengths", [])
        result.setdefault("improvements", [])

        # Ensure resume_score always exists
        score = result.get("resume_score", 0)

        # Convert decimal scores (0.91) to percentages (91)
        if isinstance(score, float):
            if score <= 1:
                score = round(score * 100)
            else:
                score = round(score)

        # Ensure integer
        if isinstance(score, int):
            result["resume_score"] = score
        else:
            result["resume_score"] = 0

        return result

    def execute(
        self,
        context,
    ):

        role = context.planner_output.get(
            "target_role",
            "",
        )

        return self.optimize(
            context.resume_data,
            role,
        )