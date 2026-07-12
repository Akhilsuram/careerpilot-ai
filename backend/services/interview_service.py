import time
from backend.utils.response_builder import ResponseBuilder
from backend.agents.interview_agent import InterviewAgent
from backend.tools.interview_formatter import InterviewFormatter


class InterviewService:

    def __init__(self):
        self.agent = InterviewAgent()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
        job_description: str | None = None,
    ):

        start = time.time()

        result = self.agent.generate_questions(
            resume_data,
            target_role,
            job_description,
        )

        result["questions"] = InterviewFormatter.sort_questions(
            result["questions"]
        )

        processing_time = round(
            time.time() - start,
            2,
        )

        return ResponseBuilder.success(
    message="Interview questions generated successfully.",
    data=result,
    processing_time=processing_time,
)