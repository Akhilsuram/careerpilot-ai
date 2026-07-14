from backend.agents.job_match_agent import JobMatchAgent
from backend.services.job_search_service import JobSearchService


class JobProviderManager:

    def __init__(self):

        self.search = JobSearchService()

        self.ai = JobMatchAgent()

    def search_jobs(
        self,
        resume_data,
        role,
        location,
    ):

        try:

            jobs = self.search.search(
                resume_data,
                role,
                location,
            )

            return {
                "provider": "Multi Provider",
                "jobs": jobs,
            }

        except Exception:

            result = self.ai.find_jobs(
                resume_data,
                role,
                location,
            )

            return {
                "provider": "AI Fallback",
                "jobs": result["jobs"],
            }