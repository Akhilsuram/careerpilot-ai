import time

from backend.agents.ats_agent import ATSAgent


class ATSService:

    def __init__(self):

        self.agent = ATSAgent()

    def execute(
        self,
        resume_data: dict,
        job_description: str
    ):

        start = time.time()

        result = self.agent.analyze(
            resume_data,
            job_description
        )

        processing_time = round(
            time.time() - start,
            2
        )

        return {
            "success": True,
            "message": "ATS analysis completed successfully.",
            "data": result,
            "processing_time": processing_time,
        }