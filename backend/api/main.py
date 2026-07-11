from fastapi import FastAPI

from backend.api.health import router

app = FastAPI(
    title="CareerPilot AI"
)

app.include_router(router)