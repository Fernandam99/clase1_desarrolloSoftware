from producto import *
    
class Medicamentos (Producto):
    def __init__(self, nombre, precio, cantidad, receta_requerida):
        super(). __init__(self, nombre, precio, cantidad)
        self.receta_requerida = receta_requerida
    def mostrar_info (self):
        receta = "Si" if self.receta_requerida else "No"
        return f"Medicamento: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}, Receta requeridad: {receta}"