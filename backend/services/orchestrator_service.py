import time

from backend.orchestrator.career_orchestrator import CareerOrchestrator
from backend.repositories.career_history_repository import CareerHistoryRepository
from backend.utils.response_builder import ResponseBuilder


class OrchestratorService:

    def __init__(self):

        self.orchestrator = CareerOrchestrator()

        self.repository = CareerHistoryRepository()

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

        ats_score = ""

        if "ats" in report:

            ats_score = report["ats"].get(
                "overall_score",
                "",
            )

        self.repository.save(
            resume_id=1,
            goal=user_goal,
            ats_score=str(ats_score),
            report=report,
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