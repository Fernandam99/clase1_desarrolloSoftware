class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def actualizar_cantidad (self, cantidad):
        self.cantidad += cantidad
        
    def mostrar_info (self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad disponible: {self.cantidad}"


    

    