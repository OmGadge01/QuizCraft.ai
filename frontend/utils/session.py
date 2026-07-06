import streamlit as st


def init_session():

    defaults = {
        "subject": "",
        "exam": None,
        "answers": {},
        "score": 0,
        "feedback": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value