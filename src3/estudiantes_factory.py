class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def matricular(self):
        return f"Estudiante {self.nombre} matriculado"

class Asignatura:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def creditos(self):
        return f"Créditos de {self.nombre}: {self.creditos}"

class FabricaEstudiante:
    def matricular(self, nombre, edad):
        return Estudiante(nombre, edad)

class FabricaAsignatura:
    def creditos(self, nombre, creditos):
        return Asignatura(nombre, creditos)


