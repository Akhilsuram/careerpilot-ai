import time
from backend.utils.response_builder import ResponseBuilder
from backend.agents.resume_optimizer_agent import ResumeOptimizerAgent
from backend.tools.resume_formatter import ResumeFormatter
from backend.repositories.dashboard_repository import DashboardRepository

class ResumeOptimizerService:

    def __init__(self):

        self.agent = ResumeOptimizerAgent()
        self.dashboard = DashboardRepository()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
    ):

        start = time.time()

        resume_data = ResumeFormatter.clean_resume(
            resume_data
        )

        result = self.agent.optimize(
            resume_data,
            target_role,
        )
        score = result.get("resume_score", 0)

        if isinstance(score, (int, float)):
            self.dashboard.update_resume_score(int(score))

        processing_time = round(
            time.time() - start,
            2
        )

        return ResponseBuilder.success(
    message="Resume optimized successfully.",
    data=result,
    processing_time=processing_time,
)