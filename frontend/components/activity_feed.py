import streamlit as st


def activity_feed():

    st.markdown("### 📌 Recent Activity")

    activities = [
        "✅ Resume analyzed",
        "📊 ATS score generated",
        "💼 Jobs matched",
        "🎤 Interview questions prepared",
        "🛣 Roadmap created"
    ]

    for activity in activities:
        st.info(activity)