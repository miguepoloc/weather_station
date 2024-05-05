class VerificadorUsuario:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def verificar(self, datos_usuario):
        if datos_usuario['username'] == "humanito" and datos_usuario['password'] == "Mi_Humanita<3":
            if self.siguiente:
                return self.siguiente.verificar(datos_usuario)
            else:
                return True
        else:
            return False

class VerificadorEstado:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def verificar(self, datos_usuario):
        if datos_usuario['state'] == "True":
            if self.siguiente:
                return self.siguiente.verificar(datos_usuario)
            else:
                return True
        else:
            return False





class VerificadorVisitas:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def verificar(self, datos_usuario):
        if datos_usuario['vistas'] < datos_usuario['vistasPermitidas']:
            if self.siguiente:
                return self.siguiente.verificar(datos_usuario)
            else:
                return True
        else:
            return False

# Crea la cadena de responsabilidad
verificador_usuario = VerificadorUsuario()
verificador_estado = VerificadorEstado()
verificador_visitas = VerificadorVisitas()
verificador_usuario.siguiente = verificador_estado
verificador_estado.siguiente = verificador_visitas

"""
    usuario de prueba: digitar estos datos para obtener una buena verificación
        usuarios = {
            "username" : "humanito",
            "password" : "Mi_Humanita<3",
            "state" : "True",
            "vistas" : 100,
            "vistasPermitidas" : 102
        }
    """