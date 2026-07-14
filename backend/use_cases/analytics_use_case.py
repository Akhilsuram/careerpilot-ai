from backend.services.analytics_service import AnalyticsService


class AnalyticsUseCase:

    def __init__(self):
        self.service = AnalyticsService()

    def execute(self):
        return self.service.execute()