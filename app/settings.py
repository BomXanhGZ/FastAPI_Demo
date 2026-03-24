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

# --- PostgreSQL Configuration ---
DB_SERVER = "dpg-d710ph75gffc73fepm3g-a.oregon-postgres.render.com"
DB_NAME = "test_icj7"
DB_USER = "testuser"
DB_PASSWORD = "joDTyAHRi37e2LVLWOTi7q1CjeBqBkQw"
DB_PORT = "5432"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_SERVER}:{DB_PORT}/{DB_NAME}?sslmode=require"
)
