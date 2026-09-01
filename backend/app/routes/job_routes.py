from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.job import Job
from app.schemas.job_schema import JobCreate, JobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/", response_model=JobResponse)
def create_job(job_data: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(
        title=job_data.title,
        description=job_data.description,
        requirements=job_data.requirements,
        location=job_data.location
    )
    
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    
    return new_job

@router.get("/", response_model=List[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return jobs
