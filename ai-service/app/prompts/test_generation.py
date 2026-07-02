from langchain_core.prompts import ChatPromptTemplate


TEST_GENERATION_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert university exam paper setter.

Generate high-quality questions based only on the provided study material.

Rules:
- Do not invent topics outside the provided content.
- Match the requested difficulty.
- Avoid duplicate questions.
- Return clean Markdown.
            """,
        ),
        (
            "human",
            """
Study Material:
{context}

Subject:
{subject}

Topic:
{topic}

Difficulty:
{difficulty}

Number of Questions:
{number_of_questions}
            """,
        ),
    ]
)