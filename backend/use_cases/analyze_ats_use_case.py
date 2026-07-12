from backend.services.ats_service import ATSService


class AnalyzeATSUseCase:

    def __init__(self):

        self.service = ATSService()

    def execute(
        self,
        resume_data: dict,
        job_description: str
    ):

        return self.service.execute(
            resume_data,
            job_description,
        )