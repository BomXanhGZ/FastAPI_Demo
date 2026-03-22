import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", "aB3xK9mP2vL7qR5n")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # MySQL Settings
    DB_SERVER: str = os.getenv("DB_SERVER", "localhost")
    DB_NAME: str = os.getenv("DB_NAME", "FastAPIDemo")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "PASS123!")
    DB_PORT: str = os.getenv("DB_PORT", "3306")

    @property
    def DATABASE_URL(self):
        # Ưu tiên lấy trực tiếp từ env nếu có, nếu không thì tự build
        env_url = os.getenv("DATABASE_URL")
        if env_url:
            return env_url
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
