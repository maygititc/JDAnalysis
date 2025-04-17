import os
from openai import OpenAI

client = OpenAI()

def generate_summary(jd_text: str) -> str:
    """Generate a summary of the job description using OpenAI GPT."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes job descriptions."},
                {"role": "user", "content": f"Summarize the following job description:\n{jd_text}"}
            ],
            max_tokens=200,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating summary: {e}"

def generate_interview_questions(jd_text: str) -> str:
    """Generate interview questions based on the job description using OpenAI GPT."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates interview questions based on job descriptions."},
                {"role": "user", "content": f"Generate interview questions for the following job description:\n{jd_text}"}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating interview questions: {e}"

def generate_suggestions(jd_text: str) -> str:
    """Suggest improvements for clarity and inclusivity using OpenAI GPT."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that suggests improvements for job descriptions to improve clarity and inclusivity."},
                {"role": "user", "content": f"Suggest improvements for the following job description:\n{jd_text}"}
            ],
            max_tokens=300,
            temperature=0.6,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating suggestions: {e}"

def llm_extract_requirements(jd_text: str) -> dict:
    """Use LLM to extract requirements from job description."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that extracts skills, qualifications, and experience from job descriptions."},
                {"role": "user", "content": f"Extract the skills, qualifications, and years of experience required from the following job description. Return the result as a JSON object with keys 'skills', 'qualifications', and 'experience'.\n{jd_text}"}
            ],
            max_tokens=300,
            temperature=0.3,
        )
        import json
        content = response.choices[0].message.content.strip()
        return json.loads(content)
    except Exception as e:
        return {"error": f"Error extracting requirements: {e}"}

def llm_detect_bias(jd_text: str) -> list:
    """Use LLM to detect biased language in job description."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that detects biased or non-inclusive language in job descriptions."},
                {"role": "user", "content": f"List any biased or non-inclusive words or phrases in the following job description. Return the result as a JSON array.\n{jd_text}"}
            ],
            max_tokens=200,
            temperature=0.3,
        )
        import json
        content = response.choices[0].message.content.strip()
        return json.loads(content)
    except Exception as e:
        return [f"Error detecting bias: {e}"]

def llm_salary_benchmarking(jd_text: str) -> dict:
    """Use LLM to suggest salary benchmarking based on job description."""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that suggests salary ranges based on job descriptions."},
                {"role": "user", "content": f"Suggest appropriate salary ranges based on the following job description. Return the result as a JSON object.\n{jd_text}"}
            ],
            max_tokens=200,
            temperature=0.3,
        )
        import json
        content = response.choices[0].message.content.strip()
        if not content:
            return {"error": "Empty response from LLM"}
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": f"Invalid JSON response: {content}"}
    except Exception as e:
        return {"error": f"Error in salary benchmarking: {e}"}
