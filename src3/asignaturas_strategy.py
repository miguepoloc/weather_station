""""class Asignatura:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

class EstrategiaDisponibilidad:
    def gestionar_disponibilidad(self, asignaturas):
        pass

class EstrategiaDisponibilidadClases(EstrategiaDisponibilidad):
    def gestionar_disponibilidad(self, asignaturas):
        total_creditos = sum(asignatura.creditos for asignatura in asignaturas)
        if total_creditos <= 10:
            return f"Clases disponibles hoy. Total de créditos: {total_creditos}"
        else:
            return f"No es posible inscribirse a más clases. Total de créditos excede 10."

class ContextoGestion:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def gestionar_disponibilidad(self, asignaturas):
        return self.estrategia.gestionar_disponibilidad(asignaturas)"""


