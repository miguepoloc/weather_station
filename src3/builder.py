class RegistroNotas:
    def __init__(self):
        self.registro = []

    def agregar_nota(self, nombre_estudiante, asignatura, nota):
        self.registro.append({"nombre_estudiante": nombre_estudiante, "asignatura": asignatura, "nota": nota})

    def obtener_registro(self):
        return self.registro

class RegistroNotasBuilder:
    def __init__(self):
        self.registro_notas = RegistroNotas()

    def agregar_nota(self, nombre_estudiante, asignatura, nota):
        self.registro_notas.agregar_nota(nombre_estudiante, asignatura, nota)
        return self

    def build(self):
        return self.registro_notas