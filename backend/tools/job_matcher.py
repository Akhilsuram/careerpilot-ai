class JobMatcher:

    @staticmethod
    def normalize_skills(skills: list[str]):

        return sorted(
            list(
                {
                    skill.strip().lower()
                    for skill in skills
                }
            )
        )