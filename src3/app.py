from typing import Annotated, Dict, List
from fastapi import APIRouter, HTTPException, Query,Form
from src3.funcionalidades import ( Estudiante, LibreriaSingleton, MatriculaFactory, RegistroAleatorioStrategy, RegistroAsistencias, Student, SubjectBuilder) 
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
    return [{"id": int(estudiante.id), "nombre": estudiante.nombre} for estudiante in estudiantes_inscritos]

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

#builder

builder = SubjectBuilder()

class Grades(BaseModel):
    name: str
    grades: Dict[str, float]

@router.post("/asignacionNotas/{subject}/")
async def assign_grades(subject: str, grades: List[Grades]) -> dict:
    for grade in grades:
        student = Student(name=grade.name, grades=grade.grades)
        builder.assign_grades(student, subject)
    return {"status": "Notas agregadas de manera Exitosa"}

@router.get("/Notas/{subject}/")
async def get_grades(subject: str) -> dict:
    return {"grades": builder.get_grades().get(subject, [])}

