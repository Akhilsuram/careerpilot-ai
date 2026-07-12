class ResumeFormatter:

    @staticmethod
    def clean_resume(data: dict):

        if "skills" in data:
            data["skills"] = sorted(
                list(set(data["skills"]))
            )

        return data