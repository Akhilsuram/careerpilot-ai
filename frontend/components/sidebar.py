import streamlit as st

from utils.session_manager import SessionManager


def render_sidebar():

    st.sidebar.title("CareerPilot AI")

    st.sidebar.success("Multi-Agent Career Copilot")

    resume = SessionManager.get_resume()

    if resume:

        st.sidebar.success("✅ Resume Loaded")

        st.sidebar.write(
            resume.get("name", "Unknown")
        )

    else:

        st.sidebar.warning("No Resume Loaded")

    if st.sidebar.button("Clear Resume"):

        SessionManager.clear_resume()

        st.rerun()