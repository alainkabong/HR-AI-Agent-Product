import pdfplumber

def clean_resume_text(text: str) -> str:
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return cleaned_lines

def extract_text_from_pdf(filepath: str) -> str:
    extracted_text = ""
    
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"
                
    cleaned_text = clean_resume_text(extracted_text)
    if not cleaned_text:
        raise ValueError("No readable text found in the PDF resume.")
        
    MAX_RESUME_CHAR = 12000
    cleaned_text = cleaned_text[:MAX_RESUME_CHAR]
        
    return cleaned_text