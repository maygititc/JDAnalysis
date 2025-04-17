import streamlit as st

import streamlit as st
from jd_processing import extract_text_from_pdf, clean_text
from llm_integration import generate_summary, generate_interview_questions, generate_suggestions, llm_extract_requirements, llm_detect_bias, llm_salary_benchmarking

def main():
    st.set_page_config(page_title="Job Description Analysis Tool", layout="wide")

    st.title("Job Description (JD) Analysis Tool")

    tabs = st.tabs(["JD Input", "Analysis", "LLM Insights", "Reports"])

    jd_text = ""
    use_example = st.session_state.get("use_example_jd", False)

    if "jd_text" not in st.session_state:
        st.session_state.jd_text = ""

    with tabs[0]:
        st.header("Job Description Input")
        st.write("Upload or paste a job description (text or PDF).")

        uploaded_file = st.file_uploader("Upload JD file (PDF or TXT)", type=["pdf", "txt"])
        if uploaded_file is not None:
            if uploaded_file.type == "application/pdf":
                jd_text = extract_text_from_pdf(uploaded_file)
                if jd_text.startswith("Error"):
                    st.error(jd_text)
                    jd_text = ""
                else:
                    jd_text = clean_text(jd_text)
            else:
                jd_text = uploaded_file.getvalue().decode("utf-8")
                jd_text = clean_text(jd_text)
            st.session_state.jd_text = jd_text
            st.text_area("Job Description Text", st.session_state.jd_text, height=300)
        else:
            jd_text = st.text_area("Or paste the job description text here", st.session_state.jd_text, height=300)
            st.session_state.jd_text = jd_text

        use_example = st.checkbox("Use example JD for demo", key="use_example_jd")
        if use_example:
            example_jd = (
                "We are looking for a Senior Python Developer with 5+ years of experience in "
                "developing scalable applications. Must have expertise in Python, Django, and REST APIs. "
                "Experience with cloud platforms like AWS is a plus. Strong communication skills required."
            )
            st.session_state.jd_text = example_jd
            st.text_area("Example Job Description", st.session_state.jd_text, height=300)

    with tabs[1]:
        st.header("Analysis")
        if st.session_state.jd_text:
            requirements = llm_extract_requirements(st.session_state.jd_text)
            bias_issues = llm_detect_bias(st.session_state.jd_text)
            salary_info = llm_salary_benchmarking(st.session_state.jd_text)

            st.subheader("Extracted Requirements")
            st.write(requirements)

            st.subheader("Bias Detection")
            if bias_issues:
                for issue in bias_issues:
                    st.warning(issue)
            else:
                st.write("No biased language detected.")

            st.subheader("Salary Benchmarking")
            st.write(salary_info)
        else:
            st.write("Please provide a job description to analyze.")

    with tabs[2]:
        st.header("LLM Insights")
        if jd_text:
            with st.spinner("Generating summary..."):
                summary = generate_summary(jd_text)
            st.subheader("Summary")
            st.write(summary)

            with st.spinner("Generating interview questions..."):
                questions = generate_interview_questions(jd_text)
            st.subheader("Interview Questions")
            st.write(questions)

            with st.spinner("Generating suggestions..."):
                suggestions = generate_suggestions(jd_text)
            st.subheader("Suggestions for Improvement")
            st.write(suggestions)
        else:
            st.write("Please provide a job description to generate insights.")

    with tabs[3]:
        st.header("Reports")
        st.write("Downloadable reports (PDF/CSV) will be available here.")

if __name__ == "__main__":
    main()
