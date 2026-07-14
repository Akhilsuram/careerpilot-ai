import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():

    with st.sidebar:

        st.image(
            "frontend/assets/logo.png",
            width=55,
        )

        st.markdown(
            "## CareerPilot AI"
        )

        st.caption(
            "Production Version 1.0"
        )
        st.markdown("---")

        st.metric(
    "Current Provider",
    "Groq",
)

        st.metric(
    "Agents",
    "7 Active",
)

        st.metric(
    "Database",
    "Connected",
)

        option_menu(
            None,
            [
                "Dashboard",
                "Resume",
                "ATS Score",
                "Resume Optimizer",
                "Job Match",
                "Interview",
                "Roadmap",
                "Analytics",
                "History",
                "Settings",
            ],
            icons=[
                "house",
                "file-earmark-person",
                "speedometer2",
                "stars",
                "briefcase",
                "camera-video",
                "map",
                "graph-up",
                "clock-history",
                "gear",
            ],
            default_index=0,
        )

        st.divider()

        st.success(
            "🚀 AI Agents Ready"
        )

        st.info(
            "Provider: Groq"
        )

        st.warning(
            "Database Connected"
        )