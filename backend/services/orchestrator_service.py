import time

from backend.memory.memory_manager import MemoryManager
from backend.orchestrator.career_orchestrator import CareerOrchestrator
from backend.utils.response_builder import ResponseBuilder


class OrchestratorService:

    def __init__(self):

        self.orchestrator = CareerOrchestrator()

        self.memory = MemoryManager()

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

        # Save complete career report
        self.memory.save_career_report(
            resume_id=1,
            goal=user_goal,
            ats_score=str(ats_score),
            report=report,
        )

        # Save ATS score separately
        if ats_score:

            try:

                score = float(ats_score)

                if score <= 1:
                    score *= 100

                self.memory.save_ats_score(
                    resume_id=1,
                    score=score,
                )

            except Exception:
                pass

        processing_time = round(
            time.time() - start,
            2,
        )

        return ResponseBuilder.success(
            message="Career Report Generated Successfully.",
            data=report,
            processing_time=processing_time,
        )