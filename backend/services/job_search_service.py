from backend.providers.job_provider_factory import JobProviderFactory
from backend.tools.job_merger import JobMerger
from backend.tools.job_ranker import JobRanker


class JobSearchService:

    def __init__(self):

        self.factory = JobProviderFactory()

    def search(
        self,
        resume_data,
        role,
        location,
    ):

        all_jobs = []

        for provider in self.factory.get_all():

            try:

                jobs = provider.search(
                    role,
                    location,
                )

                all_jobs.append(jobs)

            except Exception:

                pass

        merged = JobMerger.merge(
            all_jobs,
        )

        ranked = JobRanker.rank(
            merged,
            resume_data.get(
                "skills",
                [],
            ),
        )

        return ranked[:20]