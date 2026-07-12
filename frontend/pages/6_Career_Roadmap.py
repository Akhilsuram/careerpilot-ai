import requests
import streamlit as st

from components.sidebar import render_sidebar
from config import API_BASE_URL
from utils.session_manager import SessionManager

st.set_page_config(
    page_title="Career Roadmap",
    page_icon="🗺️",
    layout="wide",
)

render_sidebar()

st.title("🗺️ AI Career Roadmap")

resume = SessionManager.get_resume()

if not resume:

    st.warning("Please analyze your resume first.")

    st.stop()

st.success(f"Resume Loaded: {resume.get('name','Unknown')}")

target_role = st.text_input(
    "Target Role",
    placeholder="AI Engineer",
)

if st.button(
    "Generate Career Roadmap",
    use_container_width=True,
):

    if not target_role:

        st.warning("Please enter Target Role.")

        st.stop()

    payload = {
        "resume_data": resume,
        "target_role": target_role,
    }

    with st.spinner("Generating Roadmap..."):

        response = requests.post(
            f"{API_BASE_URL}/roadmap/generate",
            json=payload,
            timeout=180,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    result = response.json()["data"]

    st.success("Career Roadmap Generated")

    st.metric(
        "Estimated Duration",
        result["estimated_duration"],
    )

    st.divider()

    for week in result["roadmap"]:

        with st.expander(
            f"Week {week['week']}",
            expanded=True,
        ):

            st.subheader("Topics")

            for topic in week["topics"]:

                st.success(topic)

            st.subheader("Goals")

            for goal in week["goals"]:

                st.info(goal)