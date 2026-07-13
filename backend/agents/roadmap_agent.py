import json
from backend.utils.json_parser import JSONParser
from backend.providers.provider_manager import ProviderManager


class RoadmapAgent:

    def __init__(self):

        self.provider = ProviderManager()

    def generate(
        self,
        resume_data: dict,
        target_role: str,
    ):

        prompt = f"""
You are an Expert Career Mentor.

Generate a personalized learning roadmap.

Requirements:

• 6-8 weeks

• Weekly goals

• Weekly topics

• Keep it practical.

Return ONLY valid JSON.

Format:

{{
"estimated_duration":"",

"roadmap":[
{{
"week":1,
"topics":[],
"goals":[]
}}
]
}}

Resume

{json.dumps(resume_data, indent=2)}

Target Role

{target_role}
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

        return self.generate(
            context.resume_data,
            role,
        )