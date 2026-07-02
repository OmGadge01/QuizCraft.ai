from langchain_ollama import ChatOllama
from langchain_core.prompt_values import ChatPromptValue

from app.core.config import settings


class LLMService:

    def __init__(self):
        self.llm = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0,
        )

    def generate(self, prompt) -> str:
        """
        Accepts either a ChatPromptValue or a list of messages.
        """

        if isinstance(prompt, ChatPromptValue):
            prompt = prompt.to_messages()
        print("Generating Responses....")
        response = self.llm.invoke(prompt)
        print("Generated Responses")
        return response.content