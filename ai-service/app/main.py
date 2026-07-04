from app.core.paths import NOTES_DIR
from app.embeddings.service import EmbeddingService
from app.parser.service import PDFService
from app.splitter.service import TextSplitterService
from app.vectorstore.service import VectorStoreService
from app.rag.service import RAGService

def main():

    pdf_service = PDFService()
    splitter_service = TextSplitterService()
    embedding_service = EmbeddingService()
    vector_store = VectorStoreService()

    # Index PDF
    pdf_path = NOTES_DIR / "Java Interview Prep.pdf"

    documents = pdf_service.load_pdf(pdf_path)

    chunks = splitter_service.split(documents)

    vectors = embedding_service.embed_documents(chunks)

    # Development only
    vector_store.recreate_collection()
    vector_store.create_collection()
    vector_store.store(chunks, vectors)

    # Test Retrieval
    # query = "Explain Dependency Injection"

    # query_vector = embedding_service.embed_query(query)

    # results = vector_store.search(query_vector)

    # for result in results:
    #     print("=" * 80)
    #     print(f"Score : {result['score']:.4f}")
    #     print(f"Page  : {result['page']}")
    #     print(result["text"][:300])


    

    rag = RAGService()

    response = rag.ask(
        "Generate 5 MCQs on Dependency Injection."
    )

    print(response)

if __name__ == "__main__":
    main()