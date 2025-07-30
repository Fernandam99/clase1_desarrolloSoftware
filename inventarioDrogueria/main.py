from inventario import *
from medicamento import *
from producto import *

inventario = Inventario()

med1 = Medicamentos("Paracetamol", 5000, 50, True)
med1 = Medicamentos("Ibuprofeno", 7000, 30, False)
prod1 = Producto("Alcohol Antiséptico, 4000, 20")

inventario.agregar_producto(med1)
inventario.agregar_producto(med1)
inventario.agregar_producto(prod1)

inventario.mostrar_inventario()