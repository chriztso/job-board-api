from fastapi import FastAPI
from app.api.routes import users, jobs

app = FastAPI()

app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])