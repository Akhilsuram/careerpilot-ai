import requests
import streamlit as st

from config import API_BASE_URL

st.set_page_config(
    page_title="ATS Score",
    page_icon="📊",
    layout="wide",
)

st.title("📊 ATS Score Checker")

st.markdown("Analyze your resume against a Job Description.")

st.divider()

st.subheader("Resume JSON")

resume_json = st.text_area(
    "Paste Resume JSON",
    height=300,
)

st.subheader("Job Description")

job_description = st.text_area(
    "Paste Job Description",
    height=250,
)

if st.button("Analyze ATS Score", use_container_width=True):

    if not resume_json.strip():

        st.warning("Please paste Resume JSON.")

        st.stop()

    if not job_description.strip():

        st.warning("Please enter Job Description.")

        st.stop()

    try:

        payload = {
            "resume_data": eval(resume_json),
            "job_description": job_description,
        }

        with st.spinner("Analyzing ATS Score..."):

            response = requests.post(
                f"{API_BASE_URL}/ats/analyze",
                json=payload,
                timeout=120,
            )

        if response.status_code != 200:

            st.error(response.text)

            st.stop()

        result = response.json()

        ats = result["data"]

        st.success("ATS Analysis Completed")

        score = ats["overall_score"]

        st.metric(
            "Overall ATS Score",
            f"{score}/100",
        )

        st.divider()

        st.subheader("Category Scores")

        cols = st.columns(5)

        for i, (k, v) in enumerate(
            ats["category_scores"].items()
        ):

            cols[i].metric(
                k.title(),
                f"{v}%",
            )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("Matched Keywords")

            for keyword in ats["matched_keywords"]:
                st.success(keyword)

        with c2:

            st.subheader("Missing Keywords")

            for keyword in ats["missing_keywords"]:
                st.error(keyword)

        st.divider()

        st.subheader("Strengths")

        for item in ats["strengths"]:
            st.success(item)

        st.subheader("Weaknesses")

        for item in ats["weaknesses"]:
            st.warning(item)

        st.subheader("Recommendations")

        for item in ats["recommendations"]:
            st.info(item)

    except Exception as e:

        st.error(str(e))