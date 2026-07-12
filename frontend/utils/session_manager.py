import streamlit as st


class SessionManager:

    @staticmethod
    def set_resume(data: dict):
        st.session_state["resume_data"] = data

    @staticmethod
    def get_resume():

        return st.session_state.get(
            "resume_data",
            None,
        )

    @staticmethod
    def clear_resume():

        if "resume_data" in st.session_state:
            del st.session_state["resume_data"]