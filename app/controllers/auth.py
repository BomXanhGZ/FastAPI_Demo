from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import Token, UserCreate, User as UserSchema
from app.services.auth import AuthService

router = APIRouter()


@router.post("/register", response_model=UserSchema)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    return AuthService.register_user(db, user_in.username, user_in.password)


@router.post("/login", response_model=Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return AuthService.login_user(db, form_data.username, form_data.password)


@router.get("/me", response_model=UserSchema)
def read_users_me(current_user: UserSchema = Depends(AuthService.get_current_user)):
    return current_user
