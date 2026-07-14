import requests


class ArbeitNowProvider:

    URL = "https://www.arbeitnow.com/api/job-board-api"

    def search(
        self,
        role: str,
        location: str,
    ):

        response = requests.get(
            self.URL,
            timeout=30,
        )

        response.raise_for_status()

        jobs = response.json().get(
            "data",
            [],
        )

        results = []

        for job in jobs:

            title = job.get(
                "title",
                "",
            )

            if role.lower() not in title.lower():

                continue

            results.append(
                {
                    "company": job.get(
                        "company_name",
                    ),
                    "role": title,
                    "location": location,
                    "url": job.get(
                        "url",
                    ),
                    "description": job.get(
                        "description",
                        "",
                    ),
                }
            )

        return results[:20]