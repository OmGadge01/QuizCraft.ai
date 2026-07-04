from app.embeddings.service import EmbeddingService
from app.llm.service import LLMService
from app.prompts.rag_prompt import rag_prompt
from app.vectorstore.service import VectorStoreService


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