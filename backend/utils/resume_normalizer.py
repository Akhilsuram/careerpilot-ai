from copy import deepcopy


class ResumeNormalizer:

    @staticmethod
    def normalize(data: dict):

        data = deepcopy(data)

        # --------------------------
        # Projects
        # --------------------------

        projects = data.get("projects", [])

        for project in projects:

            description = project.get("description")

            if isinstance(description, str):

                project["description"] = [description]

            elif description is None:

                project["description"] = []

            technologies = project.get("technologies")

            if technologies is None:

                project["technologies"] = []

            elif isinstance(technologies, str):

                project["technologies"] = [technologies]

        # --------------------------
        # Experience
        # --------------------------

        experiences = data.get("experience", [])

        for exp in experiences:

            resp = exp.get("responsibilities")

            if isinstance(resp, str):

                exp["responsibilities"] = [resp]

            elif resp is None:

                exp["responsibilities"] = []

        # --------------------------
        # Certifications
        # --------------------------

        certs = data.get("certifications", [])

        normalized = []

        for cert in certs:

            if isinstance(cert, str):

                normalized.append({
                    "name": cert,
                    "year": None,
                })

            else:

                normalized.append(cert)

        data["certifications"] = normalized

        return data