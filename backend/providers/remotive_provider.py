from backend.services.job_api_service import JobAPIService


class RemotiveProvider:

    def __init__(self):

        self.service = JobAPIService()

    def search(
        self,
        role: str,
        location: str,
    ):

        return self.service.search(
            role,
            location,
        )