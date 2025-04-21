from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.job import Job, JobCreate
from app.database import get_db
from app.models.job import JobModel
router = APIRouter()

@router.get("/", response_model=List[Job])
def get_jobs():
    return [{'id': 1, 'title': "Software Engineer", 'company': "Google", 'location': "Remote"},
            {'id': 2, 'title': "Software Engineer", 'company': "Tesla", 'location': "Remote"},
            {'id': 3, 'title': "Software Engineer", 'company': "Amazon", 'location': "Remote"},
            ]

@router.post("/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = JobModel(
        title=job.title,
        company=job.company,
        location=job.location
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
