import time

from backend.orchestrator.career_orchestrator import CareerOrchestrator
from backend.utils.response_builder import ResponseBuilder


class OrchestratorService:

    def __init__(self):

        self.orchestrator = CareerOrchestrator()

    def execute(
        self,
        resume_data: dict,
        user_goal: str,
    ):

        start = time.time()

        report = self.orchestrator.execute(
            resume_data,
            user_goal,
        )

        processing_time = round(
            time.time() - start,
            2,
        )

        return ResponseBuilder.success(
            message="Career Report Generated Successfully.",
            data=report,
            processing_time=processing_time,
        )