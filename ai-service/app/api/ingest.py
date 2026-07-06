from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.embeddings.service import EmbeddingService
from app.parser.service import PDFService
from app.splitter.service import TextSplitterService
from app.vectorstore.service import VectorStoreService

router = APIRouter()


pdf_service = PDFService()
splitter = TextSplitterService()
embedding = EmbeddingService()
vector_store = VectorStoreService()


UPLOAD_DIR = Path("storage/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def ingest(files: list[UploadFile] = File(...)):

    total_pages = 0
    total_chunks = 0

    for file in files:

        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        documents = pdf_service.load_pdf(file_path)

        chunks = splitter.split(documents)

        vectors = embedding.embed_documents(chunks)

        vector_store.create_collection()
        vector_store.store(chunks, vectors)

        total_pages += len(documents)
        total_chunks += len(chunks)

    return {
        "message": "Documents indexed successfully.",
        "files": len(files),
        "pages": total_pages,
        "chunks": total_chunks,
    }