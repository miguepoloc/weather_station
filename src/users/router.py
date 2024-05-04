from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.authorizer import Hasher, Authorizer
from src.database import get_db
from src.models import User
from src.repository import get_user
from src.users.schemas import UserLogin
from src.users.bridge import Funcional, Averiado, Mantenimiento
from src.users.bridge import InterfaceAutomovilRefinada
from src.send_email import send_email

router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
async def signin(
    credentials: UserLogin,
    db: Session = Depends(get_db),
) -> dict:

    user: User = get_user(db=db, email=credentials.email)

    error_detail: str = ""
    if not user:
        error_detail = "Invalid credentials"
    elif not Hasher().verify_password(plain_password=credentials.password, hashed_password=user.password):
        error_detail = "Invalid credentials"

    if error_detail:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_detail,
        )
    try:
        token: str = Authorizer().create_access_token(user_id=user.id)

        return {"status": "success", "data": token}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/change_password", status_code=status.HTTP_200_OK)
async def change_password(
    credentials: UserLogin,
    db: Session = Depends(get_db),
) -> dict:

    user: User = get_user(db=db, email=credentials.email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found",
        )

    new_password: str = Hasher().get_password_hash(password=credentials.password)
    user.password = new_password
    db.commit()
    db.refresh(user)
    return {"status": "success", "data": "Password changed successfully"}


@router.post("/sendEmail")
def sendEmail() -> None:
    send_email("j1andres2ariza@gmail.com", "test", "<h1>test</h1>")


@router.get("/ObtenerEstado")
def obtenerEstado() -> dict:
    funcional = Funcional()
    averiado = Averiado()
    mantenimiento = Mantenimiento()


    automovil_funcional = InterfaceAutomovilRefinada(funcional)
    automovil_averiado = InterfaceAutomovilRefinada(averiado)
    automovil_mantenimiento = InterfaceAutomovilRefinada(mantenimiento)


    print(automovil_funcional.obtener_estado('funcional', 'funcional', 'funcional', True))
    print(automovil_averiado.obtener_estado('averiado', 'funcional', 'bajo', False))
    print(automovil_mantenimiento.obtener_estado('funcional', 'funcional', 'funcional', True))

    return {"status": "success", "data": automovil_funcional.obtener_estado('funcional', 'funcional', 'funcional', True)}
