from typing import Annotated
from fastapi import APIRouter, HTTPException, Query,Form
from src3.funcionalidades import (Adapter, Asignatura, EstrategiaSeleccionSimple, MatriculaEstudiante, CreditosAsignatura, DisponibilidadGestion,
                                     BibliotecaLibros, RegistroNotasEstudiante, SeleccionAsignaturas) #ReservaGestion,AsistenciaLista,)
from pydantic import BaseModel

router = APIRouter()

@router.get("/matricula/")
async def matricular_estudiante(nombre:str, edad:int):
    return MatriculaEstudiante().ejecutar(nombre, edad)

@router.get("/creditos/")
async def creditos_asignatura(nombre:str, creditos:int):
    return CreditosAsignatura().ejecutar(nombre, creditos)

adapter = Adapter()

@router.post("/asistencia/registrar/")
async def registrar_asistencia(clase: Annotated[str, Form()], estudiantes: Annotated[list, Form()]):
    return adapter.registrar_asistencia(clase, estudiantes)

"""asignaturas_disponibles = [
    Asignatura(nombre="Matemáticas", creditos=4),
    Asignatura(nombre="Historia", creditos=3),
    Asignatura(nombre="Literatura", creditos=2),
    Asignatura(nombre="Ciencias", creditos=3),
    Asignatura(nombre="Arte", creditos=2)
]

estrategia_seleccion = EstrategiaSeleccionSimple()
seleccion_asignaturas = SeleccionAsignaturas(estrategia_seleccion)

class AsignaturaSeleccionada(BaseModel):
    nombre: str

@router.post("/seleccionar/")
async def seleccionar_asignatura(asignatura: AsignaturaSeleccionada):
    if seleccion_asignaturas.seleccionar_asignatura(asignaturas_disponibles, seleccion_asignaturas.seleccionadas, asignatura.nombre):
        return {"mensaje": f"Asignatura {asignatura.nombre} seleccionada exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="No se puede seleccionar la asignatura, supera el límite de créditos")

@router.get("/total_creditos/")
async def obtener_total_creditos():
    return {"total_creditos": estrategia_seleccion.total_creditos(seleccion_asignaturas.seleccionadas)}"""




"""
@router.get("/biblioteca/")
async def libros_biblioteca():
    return BibliotecaLibros().ejecutar()


class RegistroNotasEstudianteModel(BaseModel):
    nombre_estudiante: str
    asignatura: str
    nota: float

@router.post("/registro_notas/")
async def registrar_notas(notas: RegistroNotasEstudianteModel):
    registro_notas = RegistroNotasEstudiante(
        notas.nombre_estudiante, notas.asignatura, notas.nota
    )
    return registro_notas.registrar_notas()
"""

"""@router.get("/reserva/")
async def gestion_reserva():
    return ReservaGestion().ejecutar()"""