import requests
import streamlit as st

from components.sidebar import render_sidebar
from components.hero import hero
from components.cards import DashboardCard
from components.charts import DashboardCharts
from components.footer import footer
from components.dashboard_sections import title
from components.activity_feed import activity_feed
from components.recommendation_card import recommendation_card
from components.job_card import job_card
from components.roadmap_card import roadmap_card
from components.insights_panel import insights_panel

from config import API_BASE_URL
from utils.session_manager import SessionManager

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
)

render_sidebar()

hero()

resume = SessionManager.get_resume()

if not resume:

    st.warning(
        "Please analyze your resume first."
    )

    st.stop()

st.success(
    f"Welcome back, {resume.get('name', 'User')} 👋"
)

st.subheader("⚡ Quick Actions")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("📄 Resume")

with c2:
    st.button("📊 ATS")

with c3:
    st.button("💼 Jobs")

with c4:
    st.button("🎤 Interview")

st.divider()

goal = st.text_input(
    "Career Goal",
    placeholder="I want an AI Engineer internship in Hyderabad",
)

if st.button(
    "🚀 Generate Complete Career Report",
    use_container_width=True,
):

    if not goal.strip():

        st.warning(
            "Please enter your career goal."
        )

        st.stop()

    with st.spinner(
        "Running AI Agents..."
    ):

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

    ats = report.get("ats") or {}

    resume_optimizer = report.get(
        "resume_optimizer"
    ) or {}

    job_matches = report.get(
        "job_matches"
    ) or {}

    interview = report.get(
        "interview"
    ) or {}

    roadmap = report.get(
        "roadmap"
    ) or {}

    score = ats.get(
        "overall_score",
        0,
    )

    try:

        score = float(score)

        if score <= 1:
            score *= 100

    except Exception:

        score = 0

    # =====================================
    # Career Overview
    # =====================================

    title("📈 Career Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        DashboardCard.metric(
            "ATS Score",
            f"{int(score)}%",
        )

    with c2:

        DashboardCard.metric(
            "Resume Health",
            "Excellent",
        )

    with c3:

        DashboardCard.metric(
            "Job Matches",
            len(
                job_matches.get(
                    "jobs",
                    [],
                )
            ),
        )

    with c4:

        DashboardCard.metric(
            "Roadmap",
            f"{len(roadmap.get('roadmap', []))} Weeks",
        )

    st.divider()

    # =====================================
    # Dashboard Grid
    # =====================================

    left, right = st.columns([2, 1])

    with left:

        DashboardCharts.line(
            {
                "Attempt": [1, 2, 3, 4],
                "Score": [
                    max(int(score) - 15, 0),
                    max(int(score) - 8, 0),
                    max(int(score) - 3, 0),
                    int(score),
                ],
            }
        )

    with right:

        insights_panel()

    st.divider()
        # =====================================
    # Jobs + Roadmap
    # =====================================

    left, right = st.columns(2)

    with left:

        title("💼 Recommended Jobs")

        jobs = job_matches.get(
            "jobs",
            [],
        )

        if jobs:

            for job in jobs:

                try:

                    job_card(job)

                except Exception:

                    with st.container(border=True):

                        st.subheader(
                            job.get(
                                "role",
                                "Unknown Role",
                            )
                        )

                        st.write(
                            f"🏢 {job.get('company', 'N/A')}"
                        )

                        st.write(
                            f"📍 {job.get('location', 'N/A')}"
                        )

                        match_score = job.get(
                            "match_score",
                            0,
                        )

                        try:

                            match_score = float(match_score)

                            if match_score <= 1:
                                match_score *= 100

                        except Exception:

                            match_score = 0

                        st.progress(
                            match_score / 100
                        )

                        st.write(
                            f"**Match Score:** {int(match_score)}%"
                        )

                        missing = job.get(
                            "missing_skills",
                            [],
                        )

                        st.write(
                            "### Missing Skills"
                        )

                        if missing:

                            st.write(
                                ", ".join(missing)
                            )

                        else:

                            st.success(
                                "No missing skills 🎉"
                            )

                        st.write(
                            "### Why this Match"
                        )

                        st.info(
                            job.get(
                                "reason",
                                "No reason available.",
                            )
                        )

        else:

            st.info(
                "No matching jobs found."
            )

    with right:

        try:

            roadmap_card()

        except Exception:

            weeks = roadmap.get(
                "roadmap",
                [],
            )

            if weeks:

                for week in weeks:

                    with st.container(
                        border=True
                    ):

                        st.subheader(
                            f"Week {week.get('week', '')}"
                        )

                        st.write(
                            "### Topics"
                        )

                        for topic in week.get(
                            "topics",
                            [],
                        ):

                            st.success(topic)

                        st.write(
                            "### Goals"
                        )

                        for goal_item in week.get(
                            "goals",
                            [],
                        ):

                            st.info(goal_item)

            else:

                st.info(
                    "Career roadmap not generated."
                )

    st.divider()

    # =====================================
    # Activity Feed + Recommendations
    # =====================================

    left, right = st.columns(2)

    with left:

        activity_feed()

    with right:

        try:

            recommendation_card()

        except Exception:

            title("🎯 AI Recommendations")

            recommendations = resume_optimizer.get(
                "recommendations",
                [],
            )

            if recommendations:

                for item in recommendations:

                    st.success(item)

            else:

                st.info(
                    "No recommendations available."
                )

    st.divider()

        # =====================================
    # Interview Preparation
    # =====================================

    title("🎤 Interview Preparation")

    questions = interview.get(
        "questions",
        [],
    )

    if questions:

        for q in questions[:5]:

            with st.expander(
                q.get(
                    "question",
                    "Interview Question",
                )
            ):

                if q.get("category"):

                    st.caption(
                        f"Category: {q['category']}"
                    )

                if q.get("difficulty"):

                    st.caption(
                        f"Difficulty: {q['difficulty']}"
                    )

                answer = q.get(
                    "answer",
                    "",
                )

                if answer:

                    st.write(answer)

                else:

                    st.warning(
                        "Answer not available."
                    )

    else:

        st.info(
            "Interview questions were not generated."
        )

    st.divider()

    # =====================================
    # Analytics
    # =====================================

    title("📊 Analytics")

    history = report.get(
        "analytics"
    ) or {}

    chart_data = history.get(
        "ats_history",
        [],
    )

    if chart_data:

        DashboardCharts.line(
            chart_data,
            x="Attempt",
            y="ATS Score",
        )

    else:

        DashboardCharts.line(
            {
                "Attempt": [
                    1,
                    2,
                    3,
                    4,
                ],
                "ATS Score": [
                    max(
                        int(score) - 15,
                        0,
                    ),
                    max(
                        int(score) - 8,
                        0,
                    ),
                    max(
                        int(score) - 3,
                        0,
                    ),
                    int(score),
                ],
            },
            x="Attempt",
            y="ATS Score",
        )

    st.divider()

    st.success(
        "🎉 Career Report Generated Successfully!"
    )
        # =====================================
    # Footer
    # =====================================

footer()