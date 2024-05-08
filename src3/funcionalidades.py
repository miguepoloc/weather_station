from src3.asistencia_adapter import AsistenciaClases
from src3.builder import RegistroNotasBuilder
from src3.estudiantes_factory import FabricaEstudiante, FabricaAsignatura
from src3.biblioteca_singleton import SingletonBiblioteca
from src3.asignaturas_strategy import ContextoGestion, EstrategiaDisponibilidadClases


class MatriculaEstudiante:
    def __init__(self):
        self.fabrica = FabricaEstudiante()

    def ejecutar(self):
        return self.fabrica.matricular()

class CreditosAsignatura:
    def __init__(self):
        self.fabrica = FabricaAsignatura()

    def ejecutar(self):
        return self.fabrica.creditos()

class DisponibilidadGestion:
    def __init__(self):
        self.contexto = ContextoGestion(EstrategiaDisponibilidadClases())

    def ejecutar(self):
        asignaturas = []  # Obtener las asignaturas disponibles
        return self.contexto.gestionar_disponibilidad(asignaturas)

class AsistenciaLista:
    def __init__(self):
        self.adaptador = AsistenciaClases()

    def ejecutar(self):
        return self.adaptador.obtener_lista()


class BibliotecaLibros:
    def __init__(self):
        self.singleton = SingletonBiblioteca()

    def ejecutar(self):
        return self.singleton.obtener_libros()

class RegistroNotasEstudiante:
    def __init__(self, nombre_estudiante: str, asignatura: str, nota: float):
        self.nombre_estudiante = nombre_estudiante
        self.asignatura = asignatura
        self.nota = nota

    def registrar_notas(self):
        registro_builder = RegistroNotasBuilder()
        registro_builder \
            .agregar_nota(self.nombre_estudiante, self.asignatura, self.nota)
        return "Nota registrada correctamente"








