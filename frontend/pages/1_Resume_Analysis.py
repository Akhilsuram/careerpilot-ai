import requests
import streamlit as st

from frontend.config import API_BASE_URL

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Resume Analysis")
st.write("Upload your resume and let CareerPilot AI analyze it.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"],
)

if uploaded_file is not None:

    if st.button("Analyze Resume", use_container_width=True):

        with st.spinner("🔍 AI is analyzing your resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf",
                )
            }

            try:

                response = requests.post(
                    f"{API_BASE_URL}/resume/analyze",
                    files=files,
                    timeout=120,
                )

            except requests.exceptions.ConnectionError:

                st.error("❌ Backend server is not running.")
                st.info(
                    "Start the backend first:\n\n"
                    "uvicorn backend.api.main:app --reload"
                )
                st.stop()

            except requests.exceptions.Timeout:

                st.error("⏱ Request timed out.")
                st.stop()

            except Exception as e:

                st.error(str(e))
                st.stop()

            if response.status_code != 200:

                st.error(response.text)
                st.stop()

            result = response.json()

            data = result["data"]

            st.success("✅ Resume analyzed successfully!")

            st.divider()

            # ===================================
            # Personal Information
            # ===================================

            st.header("👤 Personal Information")

            col1, col2 = st.columns(2)

            with col1:

                st.metric("Name", data["name"])

                st.metric("Email", data["email"])

            with col2:

                st.metric("Phone", data["phone"])

                st.metric("AI Provider", result["provider"])

            st.divider()

            # ===================================
            # Summary
            # ===================================

            st.header("📝 Professional Summary")

            st.info(data["summary"])

            st.divider()

            # ===================================
            # Skills
            # ===================================

            st.header("🛠 Technical Skills")

            skill_columns = st.columns(4)

            for index, skill in enumerate(data["skills"]):

                skill_columns[index % 4].success(skill)

            st.divider()

            # ===================================
            # Education
            # ===================================

            st.header("🎓 Education")

            for education in data["education"]:

                with st.expander(
                    education.get("degree", "Education"),
                    expanded=True,
                ):

                    st.write(
                        f"**Institution:** {education.get('institution','')}"
                    )

                    st.write(
                        f"**Duration:** {education.get('duration','')}"
                    )

                    st.write(
                        f"**CGPA:** {education.get('cgpa','')}"
                    )

            st.divider()

            # ===================================
            # Experience
            # ===================================

            st.header("💼 Experience")

            for experience in data["experience"]:

                with st.expander(
                    experience.get("role", "Experience"),
                    expanded=False,
                ):

                    st.write(
                        f"**Company:** {experience.get('company','')}"
                    )

                    st.write(
                        f"**Duration:** {experience.get('duration','')}"
                    )

                    st.write("### Responsibilities")

                    for responsibility in experience.get(
                        "responsibilities", []
                    ):

                        st.write(f"• {responsibility}")

            st.divider()

            # ===================================
            # Projects
            # ===================================

            st.header("🚀 Projects")

            for project in data["projects"]:

                with st.expander(
                    project.get("name", "Project"),
                    expanded=False,
                ):

                    st.write("### Technologies")

                    st.write(
                        ", ".join(
                            project.get(
                                "technologies",
                                [],
                            )
                        )
                    )

                    st.write("### Description")

                    for desc in project.get("description", []):

                        st.write(f"• {desc}")

            st.divider()

            # ===================================
            # Certifications
            # ===================================

            st.header("🏆 Certifications")

            for certification in data["certifications"]:

                st.success(
                    f"{certification.get('name','')} ({certification.get('year','')})"
                )

            st.divider()

            # ===================================
            # Metadata
            # ===================================

            st.header("📊 Analysis Details")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Status",
                    result["status"].upper(),
                )

            with col2:

                st.metric(
                    "Processing Time",
                    f"{result['processing_time']} sec",
                )

            with col3:

                st.metric(
                    "Model",
                    result["model"],
                )