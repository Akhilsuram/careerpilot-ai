import requests
import streamlit as st

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Resume Analysis")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"],
)

if uploaded_file is not None:

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf",
                )
            }

            response = requests.post(
                "http://127.0.0.1:8000/resume/analyze",
                files=files,
            )

            if response.status_code == 200:

                result = response.json()["data"]

                st.success("Resume analyzed successfully!")

                st.subheader("Extracted Information")

                st.json(result["parsed"])

            else:

                st.error(response.text)