from backend.services.interview_service import InterviewService


class InterviewUseCase:

    def __init__(self):
        self.service = InterviewService()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
        job_description: str | None = None,
    ):

        return self.service.execute(
            resume_data,
            target_role,
            job_description,
        )