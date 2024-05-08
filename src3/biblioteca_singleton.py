class Biblioteca:
    def __init__(self):
        self.libros = {
            1: {"titulo": "Introducción a la Programación", "apartado": False},
            2: {"titulo": "Cálculo Integral", "apartado": False},
            3: {"titulo": "Historia Universal", "apartado": False},
            4: {"titulo": "El Principito", "apartado": False},
            5: {"titulo": "Inteligencia Artificial", "apartado": False},
        }

    def obtener_libros(self):
        return self.libros

    def apartar_libro(self, id_libro):
        if id_libro in self.libros:
            if not self.libros[id_libro]["apartado"]:
                self.libros[id_libro]["apartado"] = True
                return f"Libro '{self.libros[id_libro]['titulo']}' apartado con éxito"
            else:
                return f"El libro '{self.libros[id_libro]['titulo']}' ya está apartado"
        else:
            return "ID de libro no válido"

class SingletonBiblioteca(Biblioteca):
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia



