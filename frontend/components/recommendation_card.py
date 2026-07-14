import streamlit as st


def recommendation_card():

    st.markdown("### 🤖 AI Recommendations")

    recommendations = [
        "Improve Docker skills",
        "Learn AWS basics",
        "Add measurable project metrics",
        "Practice SQL interviews",
        "Upload latest resume"
    ]

    for rec in recommendations:
        st.success(rec)