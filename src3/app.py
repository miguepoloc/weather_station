from fastapi import APIRouter
from src3.funcionalidades import (MatriculaEstudiante, CreditosAsignatura, DisponibilidadGestion,
                                    AsistenciaLista, BibliotecaLibros, RegistroNotasEstudiante) #ReservaGestion)

router = APIRouter()

@router.get("/matricula/")
async def matricular_estudiante():
    return MatriculaEstudiante().ejecutar()

@router.get("/creditos/")
async def creditos_asignatura():
    return CreditosAsignatura().ejecutar()

@router.get("/disponibilidad/")
async def gestion_disponibilidad():
    return DisponibilidadGestion().ejecutar()

"""@router.get("/reserva/")
async def gestion_reserva():
    return ReservaGestion().ejecutar()"""

@router.get("/asistencia/")
async def lista_asistencia():
    return AsistenciaLista().ejecutar()

@router.get("/biblioteca/")
async def libros_biblioteca():
    return BibliotecaLibros().ejecutar()

@router.post("/registro_notas/")
async def registrar_notas(notas: RegistroNotasEstudiante):
    return notas.registrar_notas()


