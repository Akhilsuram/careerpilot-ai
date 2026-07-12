class JobRanker:

    @staticmethod
    def rank(
        jobs: list,
        skills: list,
    ):

        ranked = []

        skills = [
            s.lower()
            for s in skills
        ]

        for job in jobs:

            description = (
                job.get(
                    "description",
                    ""
                ).lower()
            )

            score = 0

            for skill in skills:

                if skill in description:
                    score += 1

            job["match_score"] = round(
                score / max(
                    len(skills),
                    1
                )
                * 100,
                1,
            )

            ranked.append(job)

        ranked.sort(
            key=lambda x: x["match_score"],
            reverse=True,
        )

        return ranked