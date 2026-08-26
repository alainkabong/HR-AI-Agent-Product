def print_mock_email(to_email: str, subject: str, body: str) -> None:
    print("\n", "=" * 60)
    print("MOCK EMAIL")
    print("=" * 60)
    print("To: ", to_email)
    print("Subject: ", subject)
    print("\nBody: ", body)
    print("=" * 60)
    
    
def send_shortlist_email(
        applicant_name: str,
        applicant_email: str,
        job_title: str,
        score: int,
        reason: str,
):

    subject = f"Application Update: {job_title}"
    body = f"""
Hello {applicant_name},

Thank you for applying for the {job_title} position.

We are happy to inform you that your application has been shortlisted for recruiter interview.

AI Evaluation Score: {score}/100

Reason:
{reason}

Our recruitment team may contact you for the next steps.

Best reagrds,
HR Recruitment Team

"""
    print_mock_email(to_email=applicant_email, subject=subject, body=body.strip())
    
    
def send_rejection_email(
        applicant_name: str,
        applicant_email: str,
        job_title: str,
        score: int,
        reason: str,
):
    subject = f"Application Update: {job_title}"
    body = f""" 
Hello {applicant_name},

Thank you for applying for the {job_title} position and for taking the time to participate in our application process.

After careful consideration of your application, we regret to inform you that we will not be progressing with your application at this stage.

AI Evaluation Score: {score}/100

Reason: 
{reason}

This decision does not diminish your skills or experience, and we encourage you to apply for future opportunities that match your qualifications and career aspirations.

We appreciate your interest in joining our organization and wish you every success in your future endeavors.

Best regards,

HR Recruitment Team

"""
    print_mock_email(to_email=applicant_email, subject=subject, body=body.strip())
    


