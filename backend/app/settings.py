import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Application Metadata ---
PROJECT_NAME: str = "Login Demo API"
DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

# --- Security & JWT ---
# Use environment variables, fallback is only for safe development environments
SECRET_KEY: str = os.getenv(
    "SECRET_KEY", "your-fallback-secret-key-for-dev-only")
ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# --- Database Configuration ---
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "fastapi_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "x=rfJ42|k(8<BVfz")
DB_NAME = os.getenv("DB_NAME", "fastapi_db")
INSTANCE_CONNECTION_NAME = os.getenv(
    "INSTANCE_CONNECTION_NAME", "spheric-algebra-494403-k4:asia-northeast1:fastapi-postgres")

DEFAULT_POSTGRES_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}"
    f"?host=/cloudsql/{INSTANCE_CONNECTION_NAME}"
)

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_POSTGRES_URL)
