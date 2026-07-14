import streamlit as st


def job_card(job):

    st.markdown(
        f"""
<div style="
padding:20px;
border-radius:18px;
background:white;
box-shadow:0 8px 20px rgba(0,0,0,.08);
">

<h4>{job['role']}</h4>

<b>{job['company']}</b>

<br>

📍 {job['location']}

<br><br>

⭐ Match {job['score']}%

</div>
""",
        unsafe_allow_html=True,
    )