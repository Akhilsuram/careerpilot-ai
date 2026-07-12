import requests
import streamlit as st

from components.sidebar import render_sidebar
from config import API_BASE_URL
from utils.session_manager import SessionManager

st.set_page_config(
    page_title="Interview Preparation",
    page_icon="🎤",
    layout="wide",
)

render_sidebar()

st.title("🎤 AI Interview Preparation")

resume = SessionManager.get_resume()

if not resume:

    st.warning("Please analyze your resume first.")

    st.stop()

st.success(f"Resume Loaded: {resume.get('name', 'Unknown')}")

target_role = st.text_input(
    "Target Role",
    placeholder="AI Engineer",
)

job_description = st.text_area(
    "Job Description (Optional)",
    height=180,
)

if st.button("Generate Interview Questions", use_container_width=True):

    if not target_role:

        st.warning("Please enter Target Role.")

        st.stop()

    payload = {
        "resume_data": resume,
        "target_role": target_role,
        "job_description": job_description,
    }

    with st.spinner("Generating Questions..."):

        response = requests.post(
            f"{API_BASE_URL}/interview/generate",
            json=payload,
            timeout=180,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    result = response.json()["data"]["questions"]

    st.success(f"{len(result)} Questions Generated")

    current_category = None

    for q in result:

        if current_category != q["category"]:

            current_category = q["category"]

            st.divider()

            st.header(current_category)

        with st.expander(
            f"{q['difficulty']} • {q['question']}"
        ):

            st.markdown("### Suggested Answer")

            st.write(q["answer"])