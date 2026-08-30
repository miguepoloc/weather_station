from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.users.auth import Authorizer, Hasher
from app.users.schemas import UserCreate, UserLogin

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, db: Session = Depends(get_db)) -> dict:
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya está registrado")

    user = User(
        email=payload.email,
        password=Hasher().get_password_hash(payload.password),
        first_name=payload.first_name,
        last_name=payload.last_name,
    )
    db.add(user)
    db.commit()
    return {"status": "success", "data": user.id}


@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)) -> dict:
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not Hasher().verify_password(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credenciales inválidas")

    token = Authorizer().create_access_token(user_id=user.id)
    return {"status": "success", "data": token}
