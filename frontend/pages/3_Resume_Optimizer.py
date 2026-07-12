import json

import requests
import streamlit as st

from config import API_BASE_URL

st.set_page_config(
    page_title="Resume Optimizer",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 AI Resume Optimizer")

st.write("Improve your resume for your target role.")

resume_json = st.text_area(
    "Resume JSON",
    height=300,
)

target_role = st.text_input(
    "Target Role",
    placeholder="AI Engineer",
)

if st.button("Optimize Resume", use_container_width=True):

    if not resume_json.strip():

        st.warning("Please enter Resume JSON")

        st.stop()

    if not target_role:

        st.warning("Please enter Target Role")

        st.stop()

    payload = {
        "resume_data": json.loads(resume_json),
        "target_role": target_role,
    }

    with st.spinner("Optimizing Resume..."):

        response = requests.post(
            f"{API_BASE_URL}/resume-optimizer/optimize",
            json=payload,
            timeout=120,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    result = response.json()["data"]

    st.success("Resume Optimized Successfully")

    st.divider()

    st.subheader("Optimized Summary")

    st.info(result["optimized_summary"])

    st.divider()

    st.subheader("Optimized Skills")

    st.write(result["optimized_skills"])

    st.divider()

    st.subheader("Optimized Projects")

    st.json(result["optimized_projects"])

    st.divider()

    st.subheader("Optimized Experience")

    st.json(result["optimized_experience"])

    st.divider()

    st.subheader("Recommendations")

    for item in result["recommendations"]:

        st.success(item)