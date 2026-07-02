from app.parser.service import PDFService
from app.splitter.service import TextSplitterService
from app.embeddings.service import EmbeddingService


def main():

    pdf_service = PDFService()
    splitter = TextSplitterService()
    embedding_service = EmbeddingService()

    documents = pdf_service.load_pdf(
        "storage/notes/java.pdf"
    )

    chunks = splitter.split(documents)

    vectors = embedding_service.embed_documents(chunks)

    print(f"Chunks : {len(chunks)}")
    print(f"Vectors: {len(vectors)}")

    print()

    print(f"Vector Dimension: {len(vectors[0])}")