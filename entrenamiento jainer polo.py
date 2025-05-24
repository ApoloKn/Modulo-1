print("Bienvenido a la calculadora de precios de AllMarket")
print("Yo te audare a calcular el precio de tus productos")
while True:
    while True:
        continuar = input("¿Quieres agregar otro producto a la lista? (si/no): ")
        if continuar=="si"or continuar=="Si"or continuar=="SI"or continuar=="s"or continuar=="S":
            producto = input("Introduce el nombre del producto: ")
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad de productos: "))
            preciototal = precio * cantidad
            print(f"El precio total de {cantidad} {producto}(s) es: {preciototal}")
            continue
        elif continuar=="no"or continuar=="No"or continuar=="NO"or continuar=="n"or continuar=="N":
            print(f"El precio total de {cantidad} {producto}(s) es: {preciototal}")
            break
        else:
            print("Opcion no valida, por favor introduce 'si' o 'no'")
            continuar = input("¿Quieres agregar otro producto a la lista? (si/no): ")
            continue