import re
from typing import List, Dict, Any
import PyPDF2

def extract_text_from_pdf(file) -> str:
    """Extract text from a PDF file-like object."""
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error extracting PDF text: {e}"

def clean_text(text: str) -> str:
    """Basic text cleaning."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_requirements(text: str) -> Dict[str, Any]:
    """
    Basic keyword-based requirement extraction.
    Returns a dictionary with keys like 'skills', 'qualifications', 'experience'.
    """
    skills_keywords = ["python", "django", "rest api", "aws", "cloud", "communication", "sql", "javascript", "react", "node.js", "docker", "kubernetes", "git", "linux"]
    qualifications_keywords = ["bachelor", "master", "phd", "degree", "certification", "diploma", "associate"]
    experience_pattern = r"(\d+)(\+)?\s*(years|yrs)?"

    text_lower = text.lower()

    skills = [skill for skill in skills_keywords if skill in text_lower]
    qualifications = [qual for qual in qualifications_keywords if qual in text_lower]

    import re
    experience_match = re.search(experience_pattern, text_lower)
    experience = experience_match.group(1) + " years" if experience_match else ""

    return {
        "skills": skills,
        "qualifications": qualifications,
        "experience": experience
    }

def map_competencies(requirements: Dict[str, Any]) -> Dict[str, Any]:
    """
    Placeholder for competency mapping logic.
    Maps extracted requirements to industry standards.
    """
    # TODO: Implement competency mapping
    return {}

def detect_bias(text: str) -> List[str]:
    """
    Basic bias detection by searching for common biased words/phrases.
    Returns a list of detected biased phrases or words.
    """
    biased_terms = ["aggressive", "ninja", "rockstar", "crazy", "dominant", "fearless"]
    text_lower = text.lower()
    detected = [term for term in biased_terms if term in text_lower]
    return detected

def salary_benchmarking(keywords: List[str]) -> Dict[str, Any]:
    """
    Placeholder for salary benchmarking.
    Returns suggested salary ranges based on keywords.
    """
    # TODO: Implement salary benchmarking
    return {}
