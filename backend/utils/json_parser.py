import json
import re


class JSONParser:

    @staticmethod
    def parse(response: str):

        if not response:
            raise ValueError("Empty LLM response.")

        response = response.strip()

        # Remove markdown code blocks
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

        # Extract JSON object
        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found.")

        response = response[start:end + 1]

        # Normalize line endings
        response = response.replace("\r", "")

        # Escape invalid backslashes
        response = re.sub(
            r'\\(?!["\\/bfnrtu])',
            r'\\\\',
            response,
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError as e:

            print("\n========== INVALID JSON ==========\n")
            print(response)
            print("\n==================================\n")

            raise ValueError(
                f"Failed to parse LLM JSON: {e}"
            )