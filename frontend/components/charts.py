import pandas as pd
import streamlit as st


class DashboardCharts:

    @staticmethod
    def line(data):

        df = pd.DataFrame(data)

        st.line_chart(
            df,
            x="Attempt",
            y="Score",
            use_container_width=True
        )

    @staticmethod
    def bar(data):

        df = pd.DataFrame(data)

        st.bar_chart(
            df,
            use_container_width=True
        )