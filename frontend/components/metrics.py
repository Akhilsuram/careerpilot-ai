import streamlit as st


def show_metric(
    title,
    value,
):

    st.metric(
        title,
        value,
    )