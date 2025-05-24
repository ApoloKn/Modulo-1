print("¡Bienvenido a AllMarket!")
print("te ayudare a calcular el total de su compra")
# Preguntar si desea calcular el precio de sus productos
respuesta = input("¿Desea calcular el precio de sus productos? (sí/no): ").lower()
# Variable para guardar el total acumulado de la compra
total_general = 0
# Mientras el usuario responda sí, seguimos agregando productos
while respuesta == "si" or respuesta == "Si" or respuesta == "SI" or respuesta == "S" or respuesta == "s":
    # Pedimos los datos del producto
    nombre = input("Ingrese el nombre del producto: ")
    # Validar entrada del precio y cantidad
    try:
        precio = float(input(f"Ingrese el precio de {nombre}: $"))
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    except ValueError:
        print("Por favor, ingrese valores válidos.")
        continue  # Vuelve al inicio del bucle si hay error
    # Calcular el total de este producto
    total_producto = precio * cantidad
    print(f"Total para {nombre}: ${total_producto:.2f}")
    # Sumarlo al total general
    total_general += total_producto
    # Preguntar si desea agregar otro producto
    respuesta = input("¿Desea agregar otro producto? (sí/no): ").lower()
# Mostrar el total de todos los productos ingresados
print(f"\nEl total de todos los productos es: ${total_general:.2f}")
# Preguntar si desea aplicar un descuento
descuento_respuesta = input("¿Desea aplicar un descuento? (sí/no): ").lower()
if descuento_respuesta == "si" or descuento_respuesta == "Si" or descuento_respuesta == "SI" or descuento_respuesta == "S" or descuento_respuesta == "s":
    # Validar entrada del descuento
    try:
        descuento = float(input("¿Cuánto porcentaje de descuento desea aplicar?: "))
        if descuento < 0:
            print("El descuento no puede ser negativo.")
        else:
            monto_descuento = (descuento / 100) * total_general
            total_con_descuento = total_general - monto_descuento
            print(f"Se aplicó un {descuento}% de descuento.")
            print(f"El total con descuento es: ${total_con_descuento:.2f}")
    except ValueError:
        print("Por favor, ingrese un número válido para el descuento.")
else:
    # Si no se aplica descuento, mostramos el total normal
    print(f"Total final sin descuento: ${total_general:.2f}")
print("¡Gracias por comprar en AllMarket!")