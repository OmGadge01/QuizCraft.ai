from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert university exam paper setter.

Answer ONLY using the provided study material.

If the answer is not present in the context,
say:
"I could not find this in the uploaded study material."

Do not use outside knowledge.
            """,
        ),
        (
            "human",
            """
Study Material:

{context}

------------------------------------

Question:

{question}
            """,
        ),
    ]
)