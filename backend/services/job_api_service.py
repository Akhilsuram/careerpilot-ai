import requests


class JobAPIService:

    BASE_URL = "https://remotive.com/api/remote-jobs"

    def search(
        self,
        keyword: str,
        location: str,
    ):

        params = {
            "search": keyword
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        jobs = response.json().get(
            "jobs",
            []
        )

        results = []

        for job in jobs[:20]:

            results.append(
                {
                    "company": job.get("company_name"),
                    "role": job.get("title"),
                    "location": job.get("candidate_required_location"),
                    "url": job.get("url"),
                    "description": job.get("description"),
                }
            )

        return results