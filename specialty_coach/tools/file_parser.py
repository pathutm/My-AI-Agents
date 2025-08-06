import PyPDF2
import re

def extract_text_from_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        raw_text = ''
        for page in reader.pages:
            raw_text += page.extract_text()

    # Clean up the text
    cleaned_text = re.sub(r'\s+', ' ', raw_text)  # Replace multiple spaces/newlines with single space
    cleaned_text = re.sub(r'\s([?.!,:;])', r'\1', cleaned_text)  # Remove space before punctuation
    return cleaned_text.strip()
