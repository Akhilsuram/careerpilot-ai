import streamlit as st


def roadmap_card():

    st.markdown("### 🛣 Learning Roadmap")

    roadmap = {
        "Week 1": "Docker",
        "Week 2": "FastAPI",
        "Week 3": "AWS",
        "Week 4": "Deployment"
    }

    for week, topic in roadmap.items():
        st.success(f"{week} → {topic}")