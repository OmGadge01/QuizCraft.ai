from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingService:

    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def embed_documents(self, documents):
        texts = [doc.page_content for doc in documents]
        return self.model.embed_documents(texts)

    def embed_query(self, query: str):
        return self.model.embed_query(query)