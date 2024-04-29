import os
from datetime import datetime, timedelta
from typing import Optional, Union

import jwt
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from schemas.user import UserSignin
from starlette.responses import FileResponse
from modules.routes.app import router as routes_router

app = FastAPI()
app.include_router(routes_router, prefix="/routes")

current_dir = os.path.dirname(os.path.realpath(__file__))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/example_dates")
def get_example_dates():
    dates_path = os.path.join(current_dir, 'data', 'example_dates.json')
    return FileResponse(dates_path)


@app.get("/list_nit")
def get_list_nit():
    nit_path = os.path.join(current_dir, 'data', 'list_nit.json')
    return FileResponse(nit_path)


# Clave secreta para firmar el token (¡cambia esto en producción!)
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Función para generar un token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Ruta para autenticación y generación de token
@app.post("/login", status_code=200)
def login(request: Request, credentials: UserSignin) -> dict:
    email = credentials.email
    password = credentials.password

    # Verifica las credenciales (¡cambia esto con tu lógica de autenticación real!)
    if email == "prueba@gmail.com" and password == "Password123!":
        token = create_access_token({"sub": email})
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")


def get_token(authorization: Optional[str] = Header(None)):
    if authorization:
        scheme, _, param = authorization.partition(' ')
        if scheme.lower() == 'bearer':
            return param
    raise HTTPException(status_code=401, detail='Invalid credentials')


@app.get("/hola-mundo-token")
def hola_mundo_token(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        return {"message": f"Hola, usuario con email {email}!"}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token inválido")
