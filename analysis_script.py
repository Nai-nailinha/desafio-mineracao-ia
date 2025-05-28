import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

pdf_path = "docs/exemplo.pdf"
text = extract_text_from_pdf(pdf_path)

print("Texto extraído com sucesso.")
