import streamlit as st

from components.api import generate
from components.navbar import navbar


navbar(
    "📝 Generate Examination",
    "Generate AI-powered examinations from your uploaded notes."
)

# -----------------------------
# Exam Details
# -----------------------------

subject = st.selectbox(
    "Subject",
    [
        "Java",
        "DBMS",
        "Operating Systems",
        "Computer Networks",
    ],
)

topic = st.text_input(
    "Topic",
    placeholder="Example: Dependency Injection",
)

difficulty = st.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard",
    ],
)

questions = st.slider(
    "Number of Questions",
    min_value=5,
    max_value=50,
    value=20,
)

question_type = st.multiselect(
    "Question Types",
    [
        "MCQ",
        "Theory",
        "Coding",
    ],
    default=["MCQ"],
)

duration = st.slider(
    "Duration (Minutes)",
    min_value=10,
    max_value=180,
    value=30,
)

st.divider()

# -----------------------------
# Generate Exam
# -----------------------------

if st.button("🚀 Generate Examination"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Generating Examination..."):

        response = generate(
            subject,
            topic,
            difficulty,
            questions,
        )

    exam = response.get("exam")

    if exam is None:
        st.error("Failed to generate examination.")
        st.json(response)
        st.stop()

    st.session_state.exam = exam

    st.success("✅ Examination Generated Successfully!")

    st.subheader("Generated Examination")

    st.json(exam)