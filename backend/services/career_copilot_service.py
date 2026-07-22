import time

from backend.use_cases.career_copilot_use_case import CareerCopilotUseCase
from backend.utils.response_builder import ResponseBuilder
from backend.repositories.career_history_repository import (
    CareerHistoryRepository,
)


class CareerCopilotService:

    def __init__(self):
        self.use_case = CareerCopilotUseCase()
        self.history_repo = CareerHistoryRepository()

    def execute(
        self,
        resume_data,
        target_role,
    ):

        start = time.time()

        result = self.use_case.execute(
            resume_data,
            target_role,
        )

        # -----------------------------
        # Save report to Career History
        # -----------------------------
        try:

            ats_score = (
                result.get("ats", {})
                .get("overall_score", 0)
            )

            self.history_repo.save(
                resume_id=1,
                goal=target_role,
                ats_score=str(ats_score),
                report=result,
            )

        except Exception as e:
            print("Career History Save Error:", e)

        return ResponseBuilder.success(
            message="Career Copilot completed successfully.",
            data=result,
            processing_time=round(
                time.time() - start,
                2,
            ),
        )