from typing import Annotated, List
from fastapi import APIRouter, HTTPException, Query,Form
from src3.funcionalidades import (LibreriaSingleton, MatriculaFactory, RegistroAleatorioStrategy, RegistroAsistencias, RegistroNotasBuilder, RegistroNotasEstudiante,) #ReservaGestion,AsistenciaLista, BibliotecaLibros, Adapter,,Asignatura, MatriculaEstudiante, CreditosAsignatura,)
from pydantic import BaseModel

router = APIRouter()

#Factory
estudiantes_inscritos = []

@router.post("/matricular/")
async def matricular_estudiante(nombre: str) -> dict:
    estudiante = MatriculaFactory.crear_estudiante(nombre)
    estudiante.matricular()
    estudiantes_inscritos.append(estudiante)
    return {"status": "Matriculado", "estudiante": {"id": estudiante.id, "nombre": estudiante.nombre}}

@router.get("/estudiantes/")
async def listar_estudiantes() -> List[dict]:
    return [{"id": estudiante.id, "nombre": estudiante.nombre} for estudiante in estudiantes_inscritos]

#strategy

strategy = RegistroAleatorioStrategy(max_creditos=10)

@router.get("/registro/{estudiante_id}")
async def registrar_asignaturas(estudiante_id: int) -> dict:
    asignaturas = strategy.generar_asignaturas()
    return {"estudiante_id": estudiante_id, "asignaturas": asignaturas}

#Adapter

class RegistroAdapter:
    def __init__(self, registro: RegistroAsistencias) -> None:
        self.registro = registro

    def registrar_asistencia(self, asignatura: str, estudiante: str) -> None:
        self.registro.registrar_asistencia(asignatura, estudiante)

    def obtener_asistencias(self) -> dict:
        return self.registro.obtener_asistencias()

registro = RegistroAsistencias(asignaturas=["Matemáticas", "Ciencias", "Historia", "Literatura", "Arte"])
adapter = RegistroAdapter(registro)

@router.post("/asistencias/")
async def registrar_asistencia(asignatura: str, estudiante: str) -> dict:
    adapter.registrar_asistencia(asignatura, estudiante)
    return {"status": "Asistencia registrada"}

@router.get("/asistencias/")
async def obtener_asistencias() -> dict:
    return adapter.obtener_asistencias()

#Singleton

libreria = LibreriaSingleton()

@router.post("/reservar/{libro_id}")
async def reservar_libro(libro_id: int) -> dict:
    return {"status": libreria.reservar_libro(libro_id)}

@router.post("/liberar/{libro_id}")
async def liberar_libro(libro_id: int) -> dict:
    return {"status": libreria.liberar_libro(libro_id)}

@router.get("/libros/")
async def obtener_libros() -> dict:
    return {"libros": libreria.obtener_libros()}



"""@router.get("/biblioteca/")
async def libros_biblioteca(id_libro: str):
    return BibliotecaLibros(id_libro).ejecutar()

class RegistroNotasEstudianteModel(BaseModel):
    nombre_estudiante: str
    asignatura: str
    nota: float

@router.post("/registro_notas/")
async def registrar_notas(notas: RegistroNotasEstudianteModel):
    registro_notas = RegistroNotasBuilder() \
                        .agregar_nota(notas.nombre_estudiante, notas.asignatura, notas.nota) \
                        .build()
    return registro_notas.obtener_registro()"""



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