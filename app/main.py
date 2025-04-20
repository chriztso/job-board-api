from fastapi import FastAPI
from app.api.routes import users, jobs
from app.database import test_db_connection
app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    test_db_connection()

app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])