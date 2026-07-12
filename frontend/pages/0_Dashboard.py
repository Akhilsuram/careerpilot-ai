import requests
import streamlit as st

from components.dashboard_cards import metric_card
from components.dashboard_sections import title
from components.sidebar import render_sidebar
from config import API_BASE_URL
from utils.session_manager import SessionManager

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
)

render_sidebar()

st.title("🚀 CareerPilot AI")
st.caption("Your Personal Multi-Agent Career Copilot")

resume = SessionManager.get_resume()

if not resume:
    st.warning("Please analyze your resume first.")
    st.stop()

st.success(f"Resume Loaded: {resume.get('name', 'Unknown')}")

goal = st.text_input(
    "Career Goal",
    placeholder="I want an AI Engineer internship in Hyderabad",
)

if st.button(
    "🚀 Generate Complete Career Report",
    use_container_width=True,
):

    if not goal.strip():
        st.warning("Please enter your career goal.")
        st.stop()

    with st.spinner("Running AI Agents..."):

        response = requests.post(
            f"{API_BASE_URL}/career/analyze",
            json={
                "resume_data": resume,
                "user_goal": goal,
            },
            timeout=300,
        )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    report = response.json()["data"]

    ats = report.get("ats", {})
    resume_optimizer = report.get("resume_optimizer", {})
    job_matches = report.get("job_matches", {})
    interview = report.get("interview", {})
    roadmap = report.get("roadmap", {})

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        score = ats.get("overall_score", 0)

        try:
            score = float(score)
            if score <= 1:
                score *= 100
        except Exception:
            score = 0

        metric_card(
            "ATS Score",
            f"{int(score)}%",
        )

    with c2:
        metric_card(
            "Job Matches",
            len(job_matches.get("jobs", [])),
        )

    with c3:
        metric_card(
            "Interview Questions",
            len(interview.get("questions", [])),
        )

    with c4:
        metric_card(
            "Roadmap Weeks",
            len(roadmap.get("roadmap", [])),
        )

    st.divider()

    title("Resume Recommendations")

    recommendations = resume_optimizer.get("recommendations", [])

    if recommendations:
        for item in recommendations:
            st.success(item)
    else:
        st.info("No recommendations available.")

    st.divider()

    title("Matching Jobs")

    jobs = job_matches.get("jobs", [])

    if jobs:

        for job in jobs:

            with st.container(border=True):

                st.subheader(job.get("role", "Unknown Role"))

                st.write(f"🏢 {job.get('company', 'N/A')}")
                st.write(f"📍 {job.get('location', 'N/A')}")

                score = job.get("match_score", 0)

                try:
                    score = float(score)
                    if score <= 1:
                        score *= 100
                except Exception:
                    score = 0

                st.progress(int(score) / 100)

                st.write(f"**Match Score:** {int(score)}%")

                st.write("**Missing Skills**")

                missing = job.get("missing_skills", [])

                if missing:
                    st.write(", ".join(missing))
                else:
                    st.success("No missing skills 🎉")

    else:
        st.info("No matching jobs found.")

    st.divider()

    title("Interview Questions")

    questions = interview.get("questions", [])

    if questions:

        for q in questions[:5]:

            with st.expander(q.get("question", "Question")):

                answer = q.get("answer")

                if answer:
                    st.write(answer)
                else:
                    st.warning("Suggested answer not available.")

    else:
        st.info("Interview questions not generated.")

    st.divider()

    title("Career Roadmap")

    weeks = roadmap.get("roadmap", [])

    if weeks:

        for week in weeks:

            with st.container(border=True):

                st.subheader(f"Week {week.get('week', '')}")

                st.write("### Topics")

                for topic in week.get("topics", []):
                    st.success(topic)

                st.write("### Goals")

                for goal in week.get("goals", []):
                    st.info(goal)

    else:
        st.info("Roadmap not generated.")