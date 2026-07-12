from backend.repositories.career_history_repository import CareerHistoryRepository


class CareerHistoryService:

    def __init__(self):

        self.repository = CareerHistoryRepository()

    def execute(self):

        history = self.repository.get_all()

        data = []

        for item in history:

            data.append(
                {
                    "id": item.id,
                    "goal": item.goal,
                    "ats_score": item.ats_score,
                    "created_at": str(item.created_at),
                }
            )

        return {
            "success": True,
            "message": "Career history fetched successfully.",
            "data": data,
        }