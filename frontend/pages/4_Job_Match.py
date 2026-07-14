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

st.success(f"Resume Loaded: {resume.get('name', 'Unknown')}")

target_role = st.text_input(
    "Target Role",
    placeholder="AI Engineer",
)

location = st.text_input(
    "Preferred Location",
    placeholder="Hyderabad",
)

if st.button("Find Matching Jobs", use_container_width=True):

    if not target_role.strip():

        st.warning("Please enter a Target Role.")

        st.stop()

    if not location.strip():

        st.warning("Please enter a Preferred Location.")

        st.stop()

    payload = {
        "resume_data": resume,
        "target_role": target_role,
        "location": location,
    }

    with st.spinner("Finding Matching Jobs..."):

        response = requests.post(
            f"{API_BASE_URL}/job-match/search",
            json=payload,
            timeout=120,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    result = response.json()["data"]

    jobs = result.get("jobs", [])

    st.success(f"✅ {len(jobs)} Matching Jobs Found")

    if not jobs:

        st.info("No matching jobs were found.")

        st.stop()

    for job in jobs:

        with st.container(border=True):

            st.subheader(job.get("role", "Unknown Role"))

            st.write(f"🏢 **Company:** {job.get('company', 'N/A')}")

            st.write(f"📍 **Location:** {job.get('location', 'N/A')}")

            score = job.get("match_score", 0)

            try:
                score = float(score)
                if score <= 1:
                    score *= 100
            except Exception:
                score = 0

            st.metric(
                "Match Score",
                f"{int(score)}%",
            )

            st.write("### Required Skills")

            required = job.get("required_skills", [])

            if required:
                st.write(", ".join(required))
            else:
                st.write("N/A")

            st.write("### Missing Skills")

            missing = job.get("missing_skills", [])

            if missing:
                st.write(", ".join(missing))
            else:
                st.success("No missing skills 🎉")

            st.write("### Why this Match?")

            st.info(job.get("reason", "No explanation provided."))