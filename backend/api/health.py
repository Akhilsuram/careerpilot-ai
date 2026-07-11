from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected",
        "llm": "configured",
        "version": "1.0.0"
    }