from app.parser.service import PDFService
from app.splitter.service import TextSplitterService
from app.embeddings.service import EmbeddingService
from app.vectorstore.service import VectorStoreService

from app.core.paths import NOTES_DIR


def main():

    pdf_service = PDFService()
    splitter = TextSplitterService()
    embedding_service = EmbeddingService()
    vector_store = VectorStoreService()

    documents = pdf_service.load_pdf(
        str(NOTES_DIR / "Java Interview Prep.pdf")
    )

    chunks = splitter.split(documents)

    vectors = embedding_service.embed_documents(chunks)

    vector_store.store(chunks, vectors)

    print("\nUpload Completed Successfully!")


if __name__ == "__main__":
    main()