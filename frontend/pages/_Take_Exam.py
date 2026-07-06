import streamlit as st
from components.navbar import navbar

navbar(
    "📝 Examination",
    "Answer all questions before submitting."
)

exam = st.session_state.get("exam")

if exam is None:

    st.warning("Generate an exam first.")

    st.stop()

questions = exam.split("\n\n")

answers = {}

for i, question in enumerate(questions):

    st.markdown(
        f"""
        <div class='card'>
            <h4>Question {i+1}</h4>
            <p>{question}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    answers[i] = st.text_area(
        "Your Answer",
        key=f"answer_{i}",
        height=120,
    )

st.divider()

if st.button("Submit Examination"):

    st.session_state.answers = answers

    st.success("Exam Submitted Successfully!")

    st.switch_page("pages/_Results.py")