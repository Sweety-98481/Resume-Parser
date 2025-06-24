# ========== Import Libraries ==========
import pdfplumber
from docx import Document
import re
import spacy

# Load spaCy English model (only once)
nlp = spacy.load("en_core_web_sm")


# ========== Resume Text Extraction ==========

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"


def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading DOCX: {e}"


# ========== Preprocessing Text ==========

def clean_text(text):
    if not text:
        return ""

    text = re.sub(r'\n+', '\n', text)              # Remove multiple newlines
    text = re.sub(r'[ ]{2,}', ' ', text)           # Collapse multiple spaces
    return text.strip()


# ========== Extract Fields ==========

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r'(\+?\d{1,3})?\s?[\(\[\-]?\d{3,5}[\)\]\-]?\s?\d{3,4}[\s\-]?\d{3,4}', text)
    return match.group(0) if match else None


def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None
def extract_skills(text, skill_keywords=None):
    if skill_keywords is None:
        skill_keywords = [
            'python', 'java', 'c++', 'machine learning', 'deep learning', 'sql', 'excel',
            'data analysis', 'communication', 'leadership', 'tensorflow', 'pandas', 'numpy'
        ]
    
    found_skills = []
    text_lower = text.lower()
    for skill in skill_keywords:
        if skill in text_lower:
            found_skills.append(skill)
    
    return list(set(found_skills))
def extract_education(text):
    education_keywords = ['b.tech', 'bachelor', 'msc', 'm.tech', 'mba', 'phd', 'graduation', 'degree', 'university', 'college']
    lines = text.lower().split('\n')
    education_lines = [line for line in lines if any(keyword in line for keyword in education_keywords)]
    return education_lines
def extract_experience(text):
    experience_keywords = ['experience', 'worked at', 'intern', 'company', 'project']
    lines = text.lower().split('\n')
    experience_lines = [line for line in lines if any(word in line for word in experience_keywords)]
    return experience_lines
