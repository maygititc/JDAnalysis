# Job Description (JD) Analysis Tool

This project is a Streamlit web application designed to analyze job descriptions. It allows users to upload or paste job descriptions in text or PDF format and provides various analyses including:

- Extraction of job requirements
- Detection of biased language
- Salary benchmarking
- Generation of summaries, interview questions, and suggestions for improvement using large language model (LLM) integrations

## Features

- Upload or paste job descriptions for analysis
- Multi-tab interface for input, analysis, LLM insights, and reports
- Support for PDF and text file uploads
- Interactive and user-friendly UI built with Streamlit

## How to Run

1. Ensure you have Python installed (version 3.7 or higher recommended).
2. Install the required dependencies. You can use the following command if a requirements file is available or install Streamlit manually:

```bash
pip install streamlit
```

3. Run the Streamlit app with the following command:

```bash
streamlit run app.py
```

4. The app will open in your default web browser. If it does not open automatically, navigate to the URL shown in the terminal (usually http://localhost:8501).

## Project Structure

- `app.py`: Main Streamlit application file.
- `jd_processing.py`: Contains functions for processing job description text and PDFs.
- `llm_integration.py`: Contains functions for integrating with large language models to generate insights.
