from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, User as UserSchema
from app.schemas.auth import Token, LoginRequest
from app.services.auth import register_user, login_user, get_current_user

router = APIRouter()


@router.post("/register", response_model=UserSchema)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_in.username, user_in.password)


@router.post("/login", response_model=Token)
def login_for_access_token(
        request: LoginRequest,
        db: Session = Depends(get_db)):

    return login_user(db, request.username, request.password)


@router.get("/me", response_model=UserSchema)
def read_users_me(current_user: UserSchema = Depends(get_current_user)):
    return current_user
