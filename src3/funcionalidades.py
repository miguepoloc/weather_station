from src3.asistencia_adapter import AsistenciaClases
from src3.builder import RegistroNotas, RegistroNotasBuilder
#from src3.estudiantes_factory import FabricaEstudiante, FabricaAsignatura
from src3.biblioteca_singleton import SingletonBiblioteca
#from src3.asignaturas_strategy import ContextoGestion, EstrategiaDisponibilidadClases
from pydantic import BaseModel


##Aqui comienza el patron FActory

class Estudiante:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class FabricaEstudiante:
    def matricular(self, nombre: str, edad: int):
        return Estudiante(nombre, edad)

    def matricular2(self):
        return f"Estudiante {self} matriculado"

class MatriculaEstudiante:
    def __init__(self):
        self.fabrica_estudiante = FabricaEstudiante()

    def ejecutar(self, nombre: str, edad: int):
        return self.fabrica_estudiante.matricular(nombre, edad)

class Asignatura:
    def __init__(self, nombre: str, creditos: int):
        self.nombre = nombre
        self.creditos = creditos

    def obtener_creditos(self):
        return f"El estudiante {self.nombre} verá en este semestre {self.creditos} créditos"

class FabricaAsignatura:
    def crear_asignatura(self, nombre: str, creditos: int):
        return Asignatura(nombre, creditos)

class CreditosAsignatura:
    def __init__(self):
        self.fabrica_asignatura = FabricaAsignatura()

    def ejecutar(self, nombre: str, creditos: int):
        asignatura = self.fabrica_asignatura.crear_asignatura(nombre, creditos)
        return asignatura


#aqui termina el patron factory

#aqui comienza el patron strategy

class Asignatura:
    def __init__(self, nombre: str, creditos: int):
        self.nombre = nombre
        self.creditos = creditos

class EstrategiaSeleccion:
    def seleccionar_asignatura(self, asignaturas_disponibles, asignaturas_seleccionadas):
        pass

class SeleccionAsignaturas:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def seleccionar_asignatura(self, asignaturas_disponibles, asignaturas_seleccionadas, nombre_asignatura):
        return self.estrategia.seleccionar_asignatura(asignaturas_disponibles, asignaturas_seleccionadas, nombre_asignatura)

class EstrategiaSeleccionSimple(EstrategiaSeleccion):
    def seleccionar_asignatura(self, asignaturas_disponibles, asignaturas_seleccionadas, nombre_asignatura):
        for asignatura in asignaturas_disponibles:
            if asignatura.nombre == nombre_asignatura:
                if self.total_creditos(asignaturas_seleccionadas) + asignatura.creditos <= 10:
                    asignaturas_seleccionadas.append(asignatura)
                    return True
                else:
                    return False
        return False

    def total_creditos(self, asignaturas_seleccionadas):
        return sum(asignatura.creditos for asignatura in asignaturas_seleccionadas)

class EstrategiaDisponibilidad:
    def gestionar_disponibilidad(self, asignaturas):
        pass

class ContextoGestion:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def gestionar_disponibilidad(self, asignaturas):
        return self.estrategia.gestionar_disponibilidad(asignaturas)

class EstrategiaDisponibilidadClases(EstrategiaDisponibilidad):
    def gestionar_disponibilidad(self, asignaturas):
        total_creditos = sum(asignatura.creditos for asignatura in asignaturas)
        if total_creditos <= 10:
            return f"Clases disponibles este semestre. Total de créditos: {total_creditos}"
        else:
            return f"No es posible inscribirse a más clases. Total de créditos excede 10."

class DisponibilidadGestion:
    def __init__(self, asignaturas):
        self.contexto = ContextoGestion(EstrategiaDisponibilidadClases())
        self.asignaturas = asignaturas

    def ejecutar(self):
        return self.contexto.gestionar_disponibilidad(self.asignaturas)


#aqui termina el patron strategy

#aqui comienza el patron adapter

class Target:


    def registrar_asistencia(self, clase: str, estudiantes: list) -> str:
        pass


class Adaptee:
    def registrar(self, clase: str, estudiantes: list) -> str:
        pass


class Adapter(Target, Adaptee):
    def registrar_asistencia(self, clase: str, estudiantes: list) -> str:
        return self.registrar(clase, estudiantes)


def client_code(target: "Target", clase: str, estudiantes: list) -> None:
    print(target.registrar_asistencia(clase, estudiantes))

# aqui termina el patron adapter


class BibliotecaLibros:
    def __init__(self):
        self.singleton = SingletonBiblioteca()

    def ejecutar(self):
        return self.singleton.obtener_libros()

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

class RegistroNotasEstudiante(BaseModel):
    nombre_estudiante: str
    asignatura: str
    nota: float

class RegistroNotasBuilder:
    def __init__(self):
        self.registro_notas = RegistroNotas()

    def agregar_nota(self, nombre_estudiante, asignatura, nota):
        self.registro_notas.agregar_nota(nombre_estudiante, asignatura, nota)
        return self

    def build(self):
        return self.registro_notas









