import streamlit as st

from components.navbar import navbar

navbar(
    "📊 Examination Result",
    "AI Evaluation"
)

exam = st.session_state.get("exam")

answers = st.session_state.get("answers")

if exam is None:

    st.warning("No examination found.")

    st.stop()

st.success("Evaluation Completed")

col1,col2,col3=st.columns(3)

with col1:

    st.metric(
        "Questions",
        len(answers),
    )

with col2:

    st.metric(
        "Attempted",
        len(
            [
                x
                for x in answers.values()
                if x.strip()!=""

            ]
        ),
    )

with col3:

    st.metric(
        "Score",
        "Coming Soon",
    )

st.divider()

st.subheader("Your Answers")

for index,answer in answers.items():

    st.markdown(
        f"### Question {index+1}"
    )

    st.write(answer)

st.divider()

st.info(
"""
Next Version

✔ AI Evaluation

✔ Score

✔ Weak Topics

✔ Recommendations

✔ Practice Questions
"""
)