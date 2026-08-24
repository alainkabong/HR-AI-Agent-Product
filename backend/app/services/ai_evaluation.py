import json
from openai import OpenAI 
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def build_evaluation_prompt(job_description: str, job_requirements: str, resume_text: str) -> str:
    return f"""
You are an HR AI assistant.

Your task is to evaluate a candidate resume against a job description and job requirements.

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations outside JSON.

The JSON must follow this exact structure:
{{
  "score": 0,
  "status": "shortlisted",
  "reason": "Short explanation of the decision.",
  "strengths": ["strength 1", "strength 2"],
  "weaknesses": ["weakness 1", "weakness 2"],
  "recommendation": "Clear recommendation for the recruiter."
 }}

Rules:
- score must be a number from 0 to 100.
- status must be either "shortlisted" or "rejected".
- shortlist only if the candidate is reasonably suitable for the job.
- be fair and professional.
- do not invent experience that is not in the resume.

Job Description:
{job_description}

Job Requirements:
{job_requirements}

Candidate Resume:
{resume_text}

"""

def validate_ai_result(result: dict) -> dict:
    required_fields = [
        "score",
        "status",
        "reason",
        "strenghts",
        "weaknesses",
        "recommendation"
    ]
    
    for field in required_fields:
        if field not in result:
            raise ValueError(f"Missing field in AI response: {field}")
    
    if not isinstance(result["score"], int):
        raise ValueError("AI response field 'score' must be an integer")
    
    if result["score"] < 0 or result["score"] > 100:
        raise ValueError("AI response field 'score' must be between 0 and 100.")
        
    if result["status"] not in ["shortlisted", "rejected"]:
        raise ValueError("AI response field 'status' must be 'shortlisted' or 'rejected'.")
        
    if not isinstance(result["strengths"], list):
        raise ValueError("AI response field 'strengths' must be a list.")
        
    if not isinstance(result["weaknesses"], list):
        raise ValueError("AI response field 'weakness' must be a list.")
            

    return result

def evaluate_resume(job_description: str, job_requirements: str, resume_text: str) -> dict:
    prompt = build_evaluation_prompt(
        job_descrition=job_description,
        job_requirements=job_requirements,
        resume_text=resume_text
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt_4o_mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a careful HR AI assistant that returns only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )
        
        content = response.choices[0].message.content
        result = json.loads(content)
        
        return validate_ai_result(result=result)
        
    except json.JSONDecodeError:
        raise ValueError("AI response was not valid JSON.")
    except Exception as error:
        raise RuntimeError(f"AI evaluation failed: {error}")