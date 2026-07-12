class InterviewFormatter:

    @staticmethod
    def sort_questions(questions: list):

        order = {
            "HR": 1,
            "Project": 2,
            "Python": 3,
            "SQL": 4,
            "Machine Learning": 5,
            "DSA": 6,
            "Behavioral": 7,
        }

        return sorted(
            questions,
            key=lambda q: order.get(
                q["category"],
                99,
            ),
        )