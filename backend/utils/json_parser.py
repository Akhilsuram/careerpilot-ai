import json
import re


class JSONParser:

    @staticmethod
    def parse(response: str):

        if not response:
            raise ValueError("Empty LLM response.")

        response = response.strip()

        response = re.sub(
            r"^```(?:json)?",
            "",
            response,
            flags=re.IGNORECASE,
        )

        response = re.sub(
            r"```$",
            "",
            response,
        )

        response = response.strip()

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found.")

        response = response[start:end + 1]

        return json.loads(response)