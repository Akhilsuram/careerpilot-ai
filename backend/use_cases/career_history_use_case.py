from backend.services.career_history_service import CareerHistoryService


class CareerHistoryUseCase:

    def __init__(self):

        self.service = CareerHistoryService()

    def execute(self):

        return self.service.execute()