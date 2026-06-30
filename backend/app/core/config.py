from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "GeoRAG"
    DEBUG: bool = True

    QDRANT_HOST: str = "qdrant"
    QDRANT_PORT: int = 6333

    OLLAMA_HOST: str = "http://host.docker.internal:11434"

    class Config:
        env_file = ".env"


settings = Settings()