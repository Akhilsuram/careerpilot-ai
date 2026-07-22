from backend.orchestrator.career_copilot import CareerCopilot


class CareerCopilotUseCase:

    def __init__(self):
        self.copilot = CareerCopilot()

    def execute(
        self,
        resume_data,
        target_role,
    ):
        return self.copilot.run(
            resume_data,
            target_role,
        )