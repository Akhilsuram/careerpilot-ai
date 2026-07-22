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

Your task is to generate EXACTLY 15 interview questions based on the candidate's resume and target role.

Generate a balanced mix of questions from these categories:

- HR
- Behavioral
- Projects
- Python
- SQL
- Machine Learning
- DSA

For EACH question provide:

1. category
2. difficulty (Easy, Medium, Hard)
3. question
4. answer

Rules:

- Generate EXACTLY 15 questions.
- Answers must be between 80 and 150 words.
- Answers should be technically accurate and interview-ready.
- Do NOT repeat questions.
- Keep answers concise.
- If SQL is required, write it as plain text.
- NEVER use Markdown.
- NEVER use bullet points.
- NEVER use headings.
- NEVER use code blocks.
- NEVER use ```json
- NEVER use ```sql
- NEVER use triple backticks.
- NEVER wrap anything inside markdown.
- Escape all quotation marks inside strings.
- Escape all newline characters using \\n.
- Output ONLY a valid JSON object.
- The first character of the response MUST be {{
- The last character of the response MUST be }}
- Do not write any explanation before or after the JSON.
- Do not include words like "Here is the JSON".
- Do not include notes.
- Do not include comments.

Return ONLY this JSON structure:

{{
    "questions": [
        {{
            "category": "Python",
            "difficulty": "Easy",
            "question": "Question here",
            "answer": "Answer here"
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

    def execute(self, context):

        role = context.planner_output.get(
            "target_role",
            "",
        )

        return self.generate_questions(
            context.resume_data,
            role,
            context.user_goal,
        )