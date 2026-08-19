from pydantic import ValidationError
from app.schemas.job_schema import JobCreate, JobResponse

try:
    job = JobCreate(
        title="Backend Developer",
        description="Build API using FastAPI and SQLAlchemy.",
        requirements="Python, FastAPI, SQLAlchemy, REST APIs",
    )
    
    print("Valid job data: ")
    print(job)
    
except ValidationError as error:
    print("Validation Error: ")
    print(error)
        