from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from app.core.config import settings


class VectorStoreService:

    def __init__(self):
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
        )

    def health_check(self):
        return self.client.get_collections()

    def create_collection(self):
        collections = self.client.get_collections().collections

        # Don't create again if already exists
        for collection in collections:
            if collection.name == settings.QDRANT_COLLECTION:
                print(f"Collection '{settings.QDRANT_COLLECTION}' already exists.")
                return

        self.client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{settings.QDRANT_COLLECTION}' created successfully.")

    def store(self, chunks, vectors):
        points = []

        for chunk, vector in zip(chunks, vectors):

            point = PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload={
                    "text": chunk.page_content,
                    "page": chunk.metadata.get("page", 0),
                    "source": chunk.metadata.get("source", ""),
                },
            )

            points.append(point)

        self.client.upsert(
            collection_name=settings.QDRANT_COLLECTION,
            points=points,
        )

        print(f"Successfully stored {len(points)} vectors.")