import streamlit as st


def apply_theme():

    st.markdown(
        """
        <style>

        .stApp{

            background:#F4F7FC;

        }

        section[data-testid="stSidebar"]{

            background:#101828;

        }

        section[data-testid="stSidebar"] *{

            color:white;

        }

        .main > div{

            padding-top:2rem;

        }

        .block-container{

            padding-top:2rem;
            padding-bottom:2rem;
            max-width:1500px;

        }

        div[data-testid="stMetric"]{

            border-radius:18px;
            border:1px solid #E5E7EB;
            background:#FFFFFF;
            transition:0.3s;

        }

        div[data-testid="stMetric"]:hover{

            transform:translateY(-4px);
            box-shadow:0 12px 30px rgba(0,0,0,.12);

        }

        button{

            border-radius:12px !important;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )