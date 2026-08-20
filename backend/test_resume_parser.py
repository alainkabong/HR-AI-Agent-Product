from app.services.resume_parser import extract_text_from_pdf

filepath = "sample_resume/sample_resume.pdf"

resume_text = extract_text_from_pdf(filepath)

print("Extracted Resume Text: ")
print("===========================")
print(resume_text)
