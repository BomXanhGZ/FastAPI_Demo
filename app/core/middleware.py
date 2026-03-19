from fastapi import FastAPI
from app.middlewares.exceptions import ExceptionMiddleware


def init_middlewares(app: FastAPI):
    # Add exception middleware
    app.add_middleware(ExceptionMiddleware)

    # You can add more middlewares here in the future
    # app.add_middleware(CORSMiddleware, ...)
