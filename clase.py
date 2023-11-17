print(("Productos con POO"))


class Producto:
    def __init__(self, nombre, unidades, precio):
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio
        self.total = unidades * precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Unidades: {self.unidades} | Precio: {self.precio} | Total: {self.total}")


productos = {}

while True:
    nombre_producto = input("Ingrese el nombre del producto (o escriba 'salir' para terminar): ")

    if nombre_producto.lower() == 'salir':
        break

    unidades_producto = int(input(f"Ingrese la cantidad de unidades para {nombre_producto}: "))
    precio_producto = float(input(f"Ingrese el precio para {nombre_producto}: "))

    producto = Producto(nombre_producto, unidades_producto, precio_producto)
    productos[nombre_producto] = producto

print("Productos ingresados:")
for producto in productos.values():
    producto.mostrar_info()