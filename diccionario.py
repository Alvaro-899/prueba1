print("Gestionar diccionario")
productos = {}

while True:
    nombre_producto = input("Ingrese el nombre del producto (o escriba 'salir' para terminar): ")

    if nombre_producto.lower() == 'salir':
        break

    unidades_producto = int(input(f"Ingrese la cantidad de unidades para {nombre_producto}: "))
    precio_producto = float(input(f"Ingrese el precio para {nombre_producto}: "))

    productos[nombre_producto] = {
        "nombre": nombre_producto,
        "unidades": unidades_producto,
        "precio": precio_producto
    }

print("Productos ingresados:")
for producto, detalles in productos.items():
    print(f"Producto: {detalles['nombre']} | Unidades: {detalles['unidades']} | Precio: {detalles['precio']}")
    total_producto=detalles['unidades']*detalles['precio']
    print(f"Total del producto: {total_producto}")