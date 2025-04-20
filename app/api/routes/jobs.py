from fastapi import APIRouter
from typing import List
from app.schemas.job import Job, JobCreate
router = APIRouter()

@router.get("/", response_model=List[Job])
def get_jobs():
    return [{'id': 1, 'title': "Software Engineer", 'company': "Google", 'location': "Remote"},
            {'id': 2, 'title': "Software Engineer", 'company': "Tesla", 'location': "Remote"},
            {'id': 3, 'title': "Software Engineer", 'company': "Amazon", 'location': "Remote"},
            ]

@router.post("/", response_model=Job)
def create_job(job: dict):
    return {"message": "Job created successfully", "job": job}
