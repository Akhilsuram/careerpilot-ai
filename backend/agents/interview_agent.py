import json
from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager
from backend.agents.base_agent import BaseAgent
from backend.orchestrator.agent_metadata import AgentMetadata

class InterviewAgent(BaseAgent):

    metadata = AgentMetadata(
        name="Interview Agent",
        version="1.0.0",
        description="Generates interview questions and answers.",
        priority=3,
    )

    def __init__(self):
        self.provider = ProviderManager()

    def generate_questions(
        self,
        resume_data: dict,
        target_role: str,
        job_description: str | None = None,
    ):

        prompt = f"""
You are an expert Technical Interviewer.

Generate exactly 15 interview questions.

For EACH question provide:

1. category
2. difficulty
3. interview question
4. a detailed model answer (150–250 words)

The answer should be interview-ready and technically accurate.

Mix questions from:

- HR
- Projects
- Python
- SQL
- Machine Learning
- Behavioral
- DSA

Return ONLY valid JSON.

Do NOT include markdown.
Do NOT include ```json.
Do NOT leave the answer field empty.

Return JSON in exactly this format:

{{
  "questions": [
    {{
      "category": "",
      "difficulty": "",
      "question": "",
      "answer": "A detailed interview-ready answer."
    }}
  ]
}}

Resume:

{json.dumps(resume_data, indent=2)}

Target Role:

{target_role}

Job Description:

{job_description if job_description else "Not Provided"}
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

        return self.generate_questions(
            context.resume_data,
            role,
            context.user_goal,
        )