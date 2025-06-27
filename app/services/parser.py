import pdfplumber
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return ' '.join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_email(text):
    match = re.search(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group(0) if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def parse_resume(file):
    text = extract_text_from_pdf(file)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "raw_text": text
    }