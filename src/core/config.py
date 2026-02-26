from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    JWT_SECRET: str = "secret"
    JWT_REFRESH_SECRET: str

    ACCESS_EXPIRE_MINUTES: int = 15
    REFRESH_EXPIRE_DAYS: int = 30

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:"
            f"{self.DB_PASSWORD}@"
            f"{self.DB_HOST}/"
            f"{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()