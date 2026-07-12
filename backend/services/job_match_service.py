import time

from backend.agents.job_match_agent import JobMatchAgent
from backend.tools.job_matcher import JobMatcher
from backend.utils.response_builder import ResponseBuilder


class JobMatchService:

    def __init__(self):
        self.agent = JobMatchAgent()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
        location: str,
    ):

        start = time.time()

        if "skills" in resume_data:
            resume_data["skills"] = JobMatcher.normalize_skills(
                resume_data["skills"]
            )

        result = self.agent.find_jobs(
            resume_data,
            target_role,
            location,
        )

        processing_time = round(
            time.time() - start,
            2,
        )

        return ResponseBuilder.success(
            message="Job matching completed successfully.",
            data=result,
            processing_time=processing_time,
        )