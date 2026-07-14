import streamlit as st


def insights_panel():

    st.markdown("## 🧠 AI Career Insights")

    st.success(
        "Your resume is competitive for Data Scientist internships."
    )

    st.info(
        "Adding Docker and AWS could increase your ATS score."
    )

    st.warning(
        "Practice SQL interview questions this week."
    )

    st.error(
        "Resume project metrics can still be improved."
    )