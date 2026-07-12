import requests
import streamlit as st

from components.sidebar import render_sidebar
from config import API_BASE_URL
from utils.session_manager import SessionManager

st.set_page_config(
    page_title="AI Job Match",
    page_icon="💼",
    layout="wide",
)

render_sidebar()

st.title("💼 AI Job Matching")

resume = SessionManager.get_resume()

if not resume:

    st.warning("Analyze your resume first.")

    st.stop()

st.success(f"Resume Loaded : {resume.get('name','Unknown')}")

target_role = st.text_input(
    "Target Role",
    placeholder="AI Engineer",
)

location = st.text_input(
    "Preferred Location",
    placeholder="Hyderabad",
)

if st.button("Find Matching Jobs", use_container_width=True):

    payload = {
        "resume_data": resume,
        "target_role": target_role,
        "location": location,
    }

    with st.spinner("Finding Jobs..."):

        response = requests.post(
            f"{API_BASE_URL}/job-match/search",
            json=payload,
            timeout=120,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    jobs = response.json()["data"]["jobs"]

    st.success(f"{len(jobs)} Jobs Found")

    for job in jobs:

        with st.container(border=True):

            st.subheader(job["role"])

            st.write("🏢 Company:", job["company"])

            st.write("📍 Location:", job["location"])

            st.metric(
                "Match Score",
                f'{job["match_score"]}%'
            )

            st.write("### Required Skills")

            st.write(job["required_skills"])

            st.write("### Missing Skills")

            st.write(job["missing_skills"])

            st.write("### Why this Match?")

            st.info(job["reason"])