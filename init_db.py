from app.database import engine, Base
# Import all models here so SQLAlchemy knows about them
from app.models.user import User


def init_db():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database initialization complete.")


if __name__ == "__main__":
    init_db()
