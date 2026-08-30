import fastapi
from sqlalchemy import orm

from app import database
from app import models
from app.users import auth
from app.users import schemas

router = fastapi.APIRouter()


@router.post("/signup", status_code=fastapi.status.HTTP_201_CREATED)
def signup(payload: schemas.UserCreate, db: orm.Session = fastapi.Depends(database.get_db)) -> dict:
    if db.query(models.User).filter(models.User.email == payload.email).first():
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail="El correo ya está registrado")

    user = models.User(
        email=payload.email,
        password=auth.Hasher().get_password_hash(payload.password),
        first_name=payload.first_name,
        last_name=payload.last_name,
    )
    db.add(user)
    db.commit()
    return {"status": "success", "data": user.id}


@router.post("/login")
def login(credentials: schemas.UserLogin, db: orm.Session = fastapi.Depends(database.get_db)) -> dict:
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    if not user or not auth.Hasher().verify_password(credentials.password, user.password):
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail="Credenciales inválidas")

    token = auth.Authorizer().create_access_token(user_id=user.id)
    return {"status": "success", "data": token}
