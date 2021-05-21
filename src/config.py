from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str
    REDIS_URI: str
    TOKEN_SECRET_KEY: str
    TOKEN_DURATION: int
    ADMIN_TOKEN_SECRET_KEY:str

    class Config:
        env_file = ".env"

settings = Settings()