from app.services.ai_evaluation import evaluate_resume

job_description = """
we are looking for a backend developer to build and maintain REST APIs.
The candidate will work with databases, authentication, and AI integrations.
"""

job_requirements = """
Python, FastAPI, SQLAlchemy, REST APIs, database design, basic Docker knowledge.
"""

resume_text = """
John Doe is a Python backend developer with 3 years of experience.
He has built REST APIs using FASTAPI and Flask.
He has worked with  SQLAlchemy, PostgreSQL, and authentication systems.
He also has basic Docker experience.
"""

weak_resume_text = """
Jane Smith has 2 years of experience as a graphic designer.
She has worked with  Photoshop, Illustrator, branding, amd social media content.
She has basic knowledge of HTML and CSS but no backend API developement experience.
"""

def print_evaluation_result(result: dict):
    print("\n" + "=" * 60)
    print("AI Response: ")
    print("=" * 60)
    
    print("Score:", result["score"])
    print("Status:", result["status"])
    print("Reason:", result["reason"])
    
    print("\nStrengths:")
    for strength in result["strengths"]:
        print("-", strength)
        
    print("\nWeaknesses:")
    for weakness in result["weaknesses"]:
        print("-",weakness)
        
    print("\nRecommendation:")
    print(result["recommendation"])



try:
    
    result = evaluate_resume(job_description=job_description, job_requirements=job_requirements, resume_text=resume_text)
    print_evaluation_result(result)     
except Exception as error:
    print("AI evaluation failed.")
    print("Reason: ", error)