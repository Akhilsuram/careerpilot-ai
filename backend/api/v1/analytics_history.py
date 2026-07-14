from fastapi import APIRouter

from backend.memory.memory_manager import MemoryManager

router = APIRouter(
    prefix="/analytics-history",
    tags=["Analytics"],
)

memory = MemoryManager()


@router.get("/")
async def analytics_history():

    history = memory.get_ats_history()

    return [
        {
            "id": item.id,
            "score": item.score,
            "created_at": str(item.created_at),
        }
        for item in history
    ]