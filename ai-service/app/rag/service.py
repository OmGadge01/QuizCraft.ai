from app.embeddings.service import EmbeddingService
from app.llm.service import LLMService
from app.prompts.rag_prompt import rag_prompt
from app.vectorstore.service import VectorStoreService
import json
from app.prompts.test_generation import TEST_GENERATION_PROMPT

class RAGService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStoreService()
        self.llm = LLMService()

    def ask(self, question: str):

        # Step 1: Convert question into vector
        query_vector = self.embedding_service.embed_query(question)

        # Step 2: Retrieve relevant chunks
        results = self.vector_store.search(query_vector)

        # Step 3: Build context
        context = "\n\n".join(
            result["text"] for result in results
        )

        # Step 4: Build prompt
        prompt = rag_prompt.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        # Step 5: Generate response
        return self.llm.generate(prompt.to_messages())
    
    def generate_exam(
        self,
        subject: str,
        topic: str,
        difficulty: str,
        number_of_questions: int,
        ):
        # Step 1: Build search query
        search_query = f"{subject} {topic}"

        # Step 2: Convert query into embedding
        query_vector = self.embedding_service.embed_query(search_query)

        # Step 3: Retrieve relevant chunks
        results = self.vector_store.search(query_vector)

        # Step 4: Build context
        context = "\n\n".join(
            result["text"] for result in results
        )

        # Step 5: Build exam prompt
        prompt = TEST_GENERATION_PROMPT.invoke(
            {
                "context": context,
                "subject": subject,
                "topic": topic,
                "difficulty": difficulty,
                "number_of_questions": number_of_questions,
            }
        )

        # Step 6: Generate response
        response = self.llm.generate(prompt.to_messages())

        # Step 7: Convert JSON string → Python dictionary
        try:
            return json.loads(response)

        except json.JSONDecodeError:

            raise Exception(
                "LLM returned invalid JSON. Check the prompt or model output."
            )