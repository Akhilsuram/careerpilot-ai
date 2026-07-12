import requests
import streamlit as st

from frontend.components.metrics import show_metric
from frontend.components.report_cards import section
from frontend.components.sidebar import render_sidebar
from frontend.config import BACKEND_URL
from frontend.utils.session_manager import SessionManager

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
)

render_sidebar()

st.title("🚀 CareerPilot AI")

st.caption("Your AI Career Copilot")

resume = SessionManager.get_resume()

if not resume:

    st.warning("Upload and analyze your resume first.")

    st.stop()

st.success(f"Resume Loaded: {resume.get('name')}")

goal = st.text_input(
    "Career Goal",
    placeholder="I want an AI Engineer internship in Hyderabad",
)

if st.button(
    "Generate Complete Career Report",
    use_container_width=True,
):

    payload = {
        "resume_data": resume,
        "user_goal": goal,
    }

    with st.spinner(
        "Running Multiple AI Agents..."
    ):

        response = requests.post(
            f"{BACKEND_URL}/career/analyze",
            json=payload,
            timeout=300,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    report = response.json()["data"]

    st.success("Career Report Generated")

    ats = report["ats"]

    show_metric(
        "ATS Score",
        f"{ats['overall_score']}",
    )

    section("Resume Recommendations")

    for item in report["resume_optimizer"]["recommendations"]:

        st.success(item)

    section("Matching Jobs")

    for job in report["job_matches"]["jobs"]:

        st.write(
            f"✅ {job['company']} • {job['role']} • {job['match_score']}%"
        )

    section("Interview Questions")

    for q in report["interview"]["questions"][:5]:

        with st.expander(q["question"]):

            st.write(q["answer"])

    section("Career Roadmap")

    for week in report["roadmap"]["roadmap"]:

        st.write(
            f"Week {week['week']}"
        )

        st.write(
            ", ".join(
                week["topics"]
            )
        )