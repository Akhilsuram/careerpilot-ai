import time

from backend.agents.resume_optimizer_agent import ResumeOptimizerAgent
from backend.tools.resume_formatter import ResumeFormatter


class ResumeOptimizerService:

    def __init__(self):

        self.agent = ResumeOptimizerAgent()

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

        processing_time = round(
            time.time() - start,
            2
        )

        return {
            "success": True,
            "message": "Resume optimized successfully.",
            "data": result,
            "processing_time": processing_time,
        }