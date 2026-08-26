from app.services.email_service import send_rejection_email, send_shortlist_email

send_shortlist_email(
    applicant_name="John",
    applicant_email="user@example.com",
    job_title="Backend Developer",
    score=88,
    reason="The candidate has strong Python, FastAPI, SQLAlchemy, and API development experience."
)

send_rejection_email(
    applicant_name="Jane Smith",
    applicant_email="Jane@example.com",
    job_title="Game Developer",
    score=45,
    reason="The resume doesn't show enough game development experience for this role."
)