from dotenv import load_dotenv
from fastapi import FastAPI, Form, HTTPException

from src.data.router import router as data_router
from src.nodes.router import router as nodes_router
from src.users.router import router as users_router

from shadib import *


load_dotenv()

app = FastAPI()
app.include_router(nodes_router, prefix="/nodes", tags=["nodes"])
app.include_router(data_router, prefix="/data", tags=["data"])
app.include_router(users_router, prefix="/users", tags=["users"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


"""
    usuario de prueba: digitar estos datos para obtener una buena verificación
        usuarios = {
            "username" : "humanito",
            "password" : "Mi_Humanita<3",
            "state" : "True",
            "vistas" : 100,
            "vistasPermitidas" : 102
        }
    """


@app.post("/verificar-usuario/")
async def verificar_usuario(username: str = Form(...),
                            password: str = Form(...),
                            state: str = Form(...),
                            vistas: int = Form(...),
                            vistasPermitidas: int = Form(...)):
    datos_usuario = {
        'username': username,
        'password': password,
        'state': state,
        'vistas': vistas,
        'vistasPermitidas': vistasPermitidas
    }
    if verificador_usuario.verificar(datos_usuario):
        return {"mensaje": "El usuario ha sido verificado exitosamente."}
    else:
        raise HTTPException(status_code=400, detail="El usuario no ha pasado la verificación.")

