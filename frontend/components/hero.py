import streamlit as st


def hero():

    st.markdown(
        """
        # 🚀 CareerPilot AI

        ### Your Personal Multi-Agent Career Copilot

        Analyze resumes, improve ATS, prepare interviews,
        discover jobs and build your roadmap — all in one place.
        """
    )

    st.info(
        "🎯 Tip: Start by analyzing your resume, then generate a complete career report."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button(
            "📄 Analyze Resume",
            use_container_width=True,
        )

    with c2:
        st.button(
            "💼 Find Jobs",
            use_container_width=True,
        )

    with c3:
        st.button(
            "🎤 Interview",
            use_container_width=True,
        )