import streamlit as st


def metric_card(title, value, delta=None):

    st.markdown(
        f"""
<div style="
background:white;
padding:20px;
border-radius:18px;
box-shadow:0 10px 30px rgba(0,0,0,.08);
">

<h5>{title}</h5>

<h2 style="color:#5B5CEB;">{value}</h2>

</div>
""",
        unsafe_allow_html=True,
    )