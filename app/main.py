from fastapi import FastAPI
from app.database import engine, Base
from app.controllers import auth
from app.core.middleware import init_middlewares

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Login Demo API")

# Initialize middlewares
init_middlewares(app)

app.include_router(auth.router, tags=["Authentication"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Login Demo API. Go to /docs for Swagger UI."}
