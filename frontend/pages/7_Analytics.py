import requests
import streamlit as st

from components.sidebar import render_sidebar
from config import API_BASE_URL

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide",
)

render_sidebar()

st.title("📊 Career Analytics")

# ----------------------------
# Analytics Summary
# ----------------------------
response = requests.get(
    f"{API_BASE_URL}/analytics/",
    timeout=60,
)

if response.status_code != 200:
    st.error(response.text)
    st.stop()

data = response.json()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Career Reports",
        data.get("total_reports", 0),
    )

with c2:
    st.metric(
        "Average ATS",
        f"{data.get('average_ats_score', 0)}%",
    )

with c3:
    st.metric(
        "Highest ATS",
        f"{data.get('highest_ats_score', 0)}%",
    )

with c4:
    st.metric(
        "Resume Versions",
        data.get("total_resume_versions", 0),
    )

# ----------------------------
# ATS History
# ----------------------------
history_response = requests.get(
    f"{API_BASE_URL}/analytics-history/",
    timeout=60,
)

if history_response.status_code == 200:

    history = history_response.json()

    if history:

        st.divider()

        st.subheader("📈 ATS Score Trend")

        chart = []

        for item in history:

            chart.append(
                {
                    "Attempt": item.get("id", 0),
                    "ATS Score": item.get("score", 0),
                }
            )

        st.line_chart(
            chart,
            x="Attempt",
            y="ATS Score",
        )

    else:

        st.info("No analytics history available yet.")

else:

    st.warning("Unable to load analytics history.")