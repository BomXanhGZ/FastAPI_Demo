from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import app.settings as settings
from app.models.user import User
from app.database import get_db
from app.utils.auth import (
    verify_password,
    create_access_token,
    get_password_hash,
    decode_access_token
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def register_user(db: Session, username: str, password: str):
    # Check if user already exists
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    hashed_password = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)
    if not payload:
        raise credentials_exception

    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user
