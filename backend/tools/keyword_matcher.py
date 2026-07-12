import re


class KeywordMatcher:

    @staticmethod
    def extract_keywords(text: str) -> list[str]:

        words = re.findall(r"\b[A-Za-z][A-Za-z0-9+#.-]*\b", text)

        words = [word.lower() for word in words]

        words = list(set(words))

        return sorted(words)

    @staticmethod
    def compare(
        resume_keywords: list[str],
        jd_keywords: list[str]
    ):

        resume_set = set(resume_keywords)

        jd_set = set(jd_keywords)

        matched = sorted(list(resume_set & jd_set))

        missing = sorted(list(jd_set - resume_set))

        return matched, missing