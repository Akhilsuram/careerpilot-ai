from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.init_db import init_database

from backend.api.health import router as health_router
from backend.api.v1.resume import router as resume_router
from backend.api.v1.ats import router as ats_router
from backend.api.v1.resume_optimizer import router as resume_optimizer_router
from backend.api.v1.job_match import router as job_match_router
from backend.api.v1.interview import router as interview_router
from backend.api.v1.roadmap import router as roadmap_router
from backend.api.v1.orchestrator import router as orchestrator_router
from backend.api.v1.analytics import router as analytics_router
from backend.api.v1.analytics_history import router as analytics_history_router
from backend.api.v1.career_history import router as career_history_router
from backend.api.v1 import career_copilot

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield


app = FastAPI(
    title="CareerPilot AI",
    version="1.0.0",
    lifespan=lifespan,
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://careerpilot-ai-ivory.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(health_router)
app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(
    resume_optimizer_router
)
app.include_router(job_match_router)
app.include_router(interview_router)
app.include_router(roadmap_router)
app.include_router(
    orchestrator_router
)
app.include_router(career_history_router)
app.include_router(analytics_router)
app.include_router(
    analytics_history_router
)
app.include_router(career_copilot.router)