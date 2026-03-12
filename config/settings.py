import os


class Settings:
    NEO4J_URI: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "password")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    DATA_DIR: str = os.getenv("DATA_DIR", "data")


settings = Settings()
