from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from authorizer import Hasher, Authorizer
from database import get_db
from models import User
from repository import get_user
from users.schemas import UserLogin
from users.mediator import Mediator,User

from send_email import send_email

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


@router.post("/SendEmail")
def sendEmail()-> None:
   send_email("ditruhoy@gmail.com","Prueba","<h1>Este es prueba de correo</h1>")



@router.post("/StartComunication")
def startComunication()-> None:
    mediator = Mediator()

    user1 = User("Alicia", mediator)
    user2 = User("Bob", mediator)
    user3 = User("Charlie", mediator)

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    user1.send_message("Hola a todos!")
    user2.send_message("Hola alicia!")

    
