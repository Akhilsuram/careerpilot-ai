class JobMerger:

    @staticmethod
    def merge(job_lists):

        merged = []

        seen = set()

        for jobs in job_lists:

            for job in jobs:

                key = (
                    job.get("company"),
                    job.get("role"),
                )

                if key in seen:

                    continue

                seen.add(key)

                merged.append(job)

        return merged