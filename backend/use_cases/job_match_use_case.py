from backend.services.job_match_service import JobMatchService


class JobMatchUseCase:

    def __init__(self):
        self.service = JobMatchService()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
        location: str,
    ):

        return self.service.execute(
            resume_data,
            target_role,
            location,
        )