from backend.services.orchestrator_service import OrchestratorService


class OrchestratorUseCase:

    def __init__(self):

        self.service = OrchestratorService()

    def execute(
        self,
        resume_data: dict,
        user_goal: str,
    ):

        return self.service.execute(
            resume_data,
            user_goal,
        )