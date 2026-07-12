from backend.services.resume_optimizer_service import ResumeOptimizerService


class OptimizeResumeUseCase:

    def __init__(self):

        self.service = ResumeOptimizerService()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
    ):

        return self.service.execute(
            resume_data,
            target_role,
        )