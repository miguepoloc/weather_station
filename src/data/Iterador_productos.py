# Definimos la interfaz del Iterador
class IteradorProductos:
    def __init__(self, productos):
        self._productos = productos
        self._indice = 0

    def siguiente(self):
        if self._indice < len(self._productos):
            producto = self._productos[self._indice]
            self._indice += 1
            return producto
        else:
            raise StopIteration()

# Clase que representa la lista de productos
class ListaDeProductos:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def __iter__(self):
        return IteradorProductos(self._productos)

    def producto_mas_caro(self):
        mas_caro = None
        precio_mas_alto = 0
        for producto, precio in self._productos:
            if precio > precio_mas_alto:
                mas_caro = producto
                precio_mas_alto = precio
        return mas_caro, precio_mas_alto

# Crear una lista de productos con sus precios
lista_de_productos = ListaDeProductos()
lista_de_productos.agregar_producto(("Leche", 2.50))
lista_de_productos.agregar_producto(("Pan", 1.20))
lista_de_productos.agregar_producto(("Huevos", 3.00))
lista_de_productos.agregar_producto(("Manzanas", 2.00))

# Encontrar el producto más caro
producto_mayor, precio_mayor = lista_de_productos.producto_mas_caro()
print(f"El producto más caro es: {producto_mayor}, con un precio de {precio_mayor}.")

