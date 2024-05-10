import uuid
from src3.asistencia_adapter import AsistenciaClases
#from src3.notas_builder import RegistroNotas, RegistroNotasBuilder
#from src3.estudiantes_factory import FabricaEstudiante, FabricaAsignatura
#from src3.biblioteca_singleton import SingletonBiblioteca
#from src3.asignaturas_strategy import ContextoGestion, EstrategiaDisponibilidadClases
from pydantic import BaseModel
from typing import List
import random


##Aqui comienza el patron FActory ################################

class Estudiante:
    def __init__(self, nombre: str) -> None:
        self.id = hash(uuid.uuid4())
        self.nombre = nombre
        self.matriculado = False

    def matricular(self) -> None:
        self.matriculado = True

class MatriculaFactory:
    @staticmethod
    def crear_estudiante(nombre: str) -> Estudiante:
        return Estudiante(nombre)

#aqui termina el patron factory ################################

#aqui comienza el patron strategy ################################

class AsignaturasStrategy:
    def __init__(self, max_creditos: int) -> None:
        self.max_creditos = max_creditos

    def generar_asignaturas(self) -> List[str]:
        pass

class RegistroAleatorioStrategy(AsignaturasStrategy):
    def generar_asignaturas(self) -> List[str]:
        asignaturas = ["Matemáticas", "Ciencias", "Historia", "Literatura", "Arte"]
        creditos_disponibles = self.max_creditos
        asignaturas_elegidas = []

        while creditos_disponibles > 0 and len(asignaturas) > 0:
            asignatura = random.choice(asignaturas)
            creditos = random.randint(1, min(3, creditos_disponibles))
            asignaturas_elegidas.append(f"{asignatura} ({creditos} créditos)")
            creditos_disponibles -= creditos
            asignaturas.remove(asignatura)

        return asignaturas_elegidas


#aqui termina el patron strategy ################################


#aqui comienza el patron adapter################################

class RegistroAsistencias:
    def __init__(self, asignaturas: List[str]) -> None:
        self.asignaturas = {asignatura: [] for asignatura in asignaturas}

    def registrar_asistencia(self, asignatura: str, estudiante: str) -> None:
        if asignatura in self.asignaturas:
            self.asignaturas[asignatura].append(estudiante)

    def obtener_asistencias(self) -> dict:
        return self.asignaturas
# aqui termina el patron adapter ################################

#aqui comienza el patron singleton ################################

class Libro:
    def __init__(self, titulo: str) -> None:
        self.titulo = titulo
        self.apartado = False

    def reservar(self) -> None:
        self.apartado = True

    def liberar(self) -> None:
        self.apartado = False

class LibreriaSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.libros = [Libro(f"Libro {i+1}") for i in range(10)]
        return cls._instance

    def obtener_libros(self) -> list:
        return [{"titulo": libro.titulo, "apartado": libro.apartado} for libro in self.libros]

    def reservar_libro(self, libro_id: int) -> str:
        if libro_id < 1 or libro_id > 10:
            return "El ID del libro debe estar entre 1 y 10"

        libro = self.libros[libro_id - 1]
        if not libro.apartado:
            libro.reservar()
            return f"Libro {libro.titulo} reservado"
        else:
            return f"El libro {libro.titulo} ya está reservado"

    def liberar_libro(self, libro_id: int) -> str:
        if libro_id < 1 or libro_id > 10:
            return "El ID del libro debe estar entre 1 y 10"

        libro = self.libros[libro_id - 1]
        if libro.apartado:
            libro.liberar()
            return f"Reserva del libro {libro.titulo} liberada"
        else:
            return f"El libro {libro.titulo} no está reservado"


#aqui termina el patron singleton ################################

#aqui comienza el patron builder ################################

class RegistroNotasEstudiante(BaseModel):
    nombre_estudiante: str
    asignatura: str
    nota: float

class RegistroNotasBuilder:
    def __init__(self):
        self.registro_notas = RegistroNotas()

    def agregar_nota(self, nombre_estudiante:str, asignatura:str, nota:float):
        self.registro_notas.agregar_nota(nombre_estudiante, asignatura, nota)
        return self

    def build(self):
        return self.registro_notas

class RegistroNotas:
    def __init__(self):
        self.registro = []

    def agregar_nota(self, nombre_estudiante:str, asignatura:str, nota:float):
        self.registro.append({"nombre_estudiante": nombre_estudiante, "asignatura": asignatura, "nota": nota})

    def obtener_registro(self):
        return self.registro

#aqui termina el patron builder ################################




"""class RegistroNotasEstudiante:
    def __init__(self, nombre_estudiante: str, asignatura: str, nota: float):
        self.nombre_estudiante = nombre_estudiante
        self.asignatura = asignatura
        self.nota = nota

    def registrar_notas(self):
        registro_builder = RegistroNotasBuilder()
        registro_builder \
            .agregar_nota(self.nombre_estudiante, self.asignatura, self.nota)
        return "Nota registrada correctamente"""











