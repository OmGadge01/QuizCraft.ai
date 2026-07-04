from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ----------------------------
    # Ollama
    # ----------------------------
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:4b"

    OLLAMA_TEMPERATURE: float = 0.0
    OLLAMA_TOP_P: float = 0.9
    OLLAMA_NUM_CTX: int = 4096

    # ----------------------------
    # Qdrant
    # ----------------------------
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "quizcraft_notes"

    # ----------------------------
    # Embeddings
    # ----------------------------
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()