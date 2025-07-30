class Inventario:
    def __init__(self):
        self._productos = []
        
    def agregar_productos  (self, producto):
        self._productos.append(producto)
        
    def listar_productos (self):
        for producto in self._productos:
            print(producto.mostar_info())