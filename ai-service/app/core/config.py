from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:4b"

    # Qdrant
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "quizcraft_notes"

    # Embedding
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()