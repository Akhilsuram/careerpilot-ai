import time

from backend.agents.roadmap_agent import RoadmapAgent
from backend.tools.roadmap_formatter import RoadmapFormatter


class RoadmapService:

    def __init__(self):
        self.agent = RoadmapAgent()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
    ):

        start = time.time()

        result = self.agent.generate(
            resume_data,
            target_role,
        )

        result["roadmap"] = RoadmapFormatter.sort_weeks(
            result["roadmap"]
        )

        processing_time = round(
            time.time() - start,
            2,
        )

        return {
            "success": True,
            "message": "Career roadmap generated successfully.",
            "data": result,
            "processing_time": processing_time,
        }