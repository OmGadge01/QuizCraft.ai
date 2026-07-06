import streamlit as st

from components.api import upload
from components.navbar import navbar

navbar(
    "📚 Upload Notes",
    "Upload one or more PDFs for indexing.",
)

subject = st.selectbox(
    "Subject",
    [
        "Java",
        "DBMS",
        "Operating System",
        "Computer Networks",
    ],
)

uploaded_files = st.file_uploader(
    "Choose PDF(s)",
    type=["pdf"],
    accept_multiple_files=True,
)

if st.button("🚀 Upload & Index"):

    if not uploaded_files:

        st.warning("Please select at least one PDF.")

    else:

        files = []

        for pdf in uploaded_files:

            files.append(
                (
                    "files",
                    (
                        pdf.name,
                        pdf.getvalue(),
                        "application/pdf",
                    ),
                )
            )

        with st.spinner("Indexing PDFs..."):

            response = upload(files)

        st.success(response["message"])

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Files", response["files"])

        with c2:
            st.metric("Pages", response["pages"])

        with c3:
            st.metric("Chunks", response["chunks"])