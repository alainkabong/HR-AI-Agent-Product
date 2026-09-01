import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.job import Job
from app.services.ai_evaluation import evaluate_resume
from app.services.email_service import send_rejection_email, send_shortlist_email
from app.services.resume_parser import extract_text_from_pdf

router = APIRouter(
    prefix="/apply",
    tags=["Applications"],
)

UPLOAD_DIR = "uploads"

def save_upload_file(upload_file: UploadFile) -> str:
    file_extension = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
        
    return file_path

@router.post("/{job_id}")
def apply_to_job(
        job_id: int, 
        name: str = Form(...),
        email: str = Form(...),
        resume: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    job = db.query(Job).filter(Job.id == job_id).first()
    
    if not job:
        raise HTTPException(status_code = 404, detail="Job not found.")
        
    if not resume.filename.endwith(".pdf"):
        raise HTTPException(status_code = 400, detail="Only PDF resumes are allowed.")
        
    saved_file_path = save_upload_file(resume)
    
    try:
        resume_text = extract_text_from_pdf(saved_file_path)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
        
    try:
        ai_result = evaluate_resume(
            job_description=job.description,
            job_requirements=job.requirements,
            resume_text=resume_text
        )
        
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
        
    if ai_result["status"] == "shortlisted":
        send_shortlist_email(
            applicant_name=name,
            applicant_email=email,
            job_title=job.title,
            score=ai_result["score"],
            reason=ai_result["reason"],
        )
        
    else:
        send_rejection_email(
            applicant_name=name,
            applicant_email=email,
            job_title=job.title,
            reason=ai_result["reason"],
        )
        
    return{
        "message": "Application processed successfully.", 
        "applicant_name": name,
        "applicant_email": email,
        "job_id": job.id,
        "job_title": job.title,
        "ai_result": ai_result,
    }

        
        
        

