import streamlit as st

st.set_page_config(
    page_title="QuizCraft AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

st.title("🧠 QuizCraft AI")

st.markdown(
"""
### AI Powered Examination Platform

Generate university-level examinations directly from your notes using RAG and Large Language Models.
"""
)

st.divider()

c1, c2 = st.columns(2)

with c1:

    st.markdown(
    """
    <div class='card'>
        <h3>📚 Upload Notes</h3>
        <p>Upload one or more PDFs.</p>
    </div>
    """,
    unsafe_allow_html=True,
    )

with c2:

    st.markdown(
    """
    <div class='card'>
        <h3>📝 Generate Exam</h3>
        <p>Create AI-generated examinations.</p>
    </div>
    """,
    unsafe_allow_html=True,
    )

st.divider()

st.info(
"""
Use the navigation on the left to:

- 📚 Upload PDFs
- 📝 Generate Exams
- ⏳ Take Exam
- 📊 View Results
"""
)