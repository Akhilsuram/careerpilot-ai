import streamlit as st


class DashboardCard:

    @staticmethod
    def metric(
        title,
        value,
        delta=None,
    ):

        with st.container(border=True):

            st.metric(
                title,
                value,
                delta,
            )