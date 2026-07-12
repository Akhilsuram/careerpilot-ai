from backend.agents.job_match_agent import JobMatchAgent
from backend.services.job_api_service import JobAPIService
from backend.tools.job_ranker import JobRanker


class JobProviderManager:

    def __init__(self):

        self.api = JobAPIService()

        self.ai = JobMatchAgent()

    def search_jobs(
        self,
        resume_data: dict,
        role: str,
        location: str,
    ):

        try:

            jobs = self.api.search(
                role,
                location,
            )

            ranked = JobRanker.rank(
                jobs,
                resume_data.get(
                    "skills",
                    [],
                ),
            )

            return {
                "provider": "Remotive API",
                "jobs": ranked[:10],
            }

        except Exception:

            ai_jobs = self.ai.find_jobs(
                resume_data,
                role,
                location,
            )

            return {
                "provider": "AI Fallback",
                "jobs": ai_jobs["jobs"],
            }