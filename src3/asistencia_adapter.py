class AsistenciaClases:
    def __init__(self):
        self.registro_asistencia = {}

    def registrar_asistencia(self, clase, estudiantes):
        if clase not in self.registro_asistencia:
            self.registro_asistencia[clase] = set()

        for estudiante in estudiantes:
            self.registro_asistencia[clase].add(estudiante)

    def obtener_lista(self):
        return self.registro_asistencia

