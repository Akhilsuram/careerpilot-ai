from backend.services.roadmap_service import RoadmapService


class RoadmapUseCase:

    def __init__(self):
        self.service = RoadmapService()

    def execute(
        self,
        resume_data: dict,
        target_role: str,
    ):

        return self.service.execute(
            resume_data,
            target_role,
        )