# Función para añadir un nuevo producto al inventario
def add_menu(a, b, c):
    inventory[code] = {
        "nombre": a,
        "precio": b,
        "unidades": c
    }
# Función para buscar un producto en el inventario por su nombre
def search_product(a):
    for id, inserted in inventory.items():
        if inserted["nombre"] == a:
            print(f"{id}: {inventory[id]}")
            continue
# Función para actualizar el precio de un producto
def update_product(a, b):
    for id, inserted in inventory.items():
        if inserted["nombre"] == b:
            inventory[id]["precio"] = a
# Función para eliminar un producto del inventario
def delete_product(a): 
    for id, inserted in inventory.items():
        if inserted["nombre"] == a:
            del inventory[id]
            break  # Se elimina solo el primero que coincida y se detiene
# Función para finalizar el programa con un mensaje
def end_program():
    print("-".center(100, "-"))
    print("gracias por usar esta herramienta".center(50, "-"))
    print("ten buen dia".center(50, "-"))
# Inicialización del inventario como diccionario vacío y código inicial en 1
inventory = {}
code = 1
# Mensaje de bienvenida
print("-".center(100, "-"))
print("Bienvenido a tu herramienta para gestionar tu inventario de compra".center(100, "-"))
# Ciclo principal del programa
while True:
    try:
        print("-".center(100, "-"))
        print("\nSelecciona la opcion que quieras operar:")
        print("1. Añadir productos")
        print("2. Consultar productos")
        print("3. Actualizar productos")
        print("4. Eliminar productos")
        print("5. Calcular el valor total del inventario")
        print("6. mostrar inventario")
        print("0. Salir del programa")
        # Entrada del usuario
        player = int(input("\nIngresa la opcion que deseas operar: "))
    
        if player == 1:
            # Añadir producto
            print("-".center(100, "-"))
            name = str(input("ingrese el nombre del producto: "))
            price = float(input("ingresa el precio: "))
            units = int(input("Cuantas unidades desea añadir: "))
            add_menu(name, price, units)
            code += 1
            continue
        elif player == 2:
            # Buscar producto
            print("-".center(100, "-"))
            item = str(input("que producto busca: "))
            print("si no obtuvo resultado no existe en tu inventario")
            search_product(item)
            continue
        elif player == 3:
            # Actualizar producto
            print("-".center(100, "-"))
            print("aqui veras tu inventario.".center(100, "-"))
            for id, inserted in inventory.items():
                print(f"{id} : {inserted}")
            print("-".center(100, "-"))
            update = str(input("que producto desea modificar: "))
            newprice = float(input("Ingrese el nuevo precio: "))
            update_product(newprice, update)
        elif player == 4:
            # Eliminar producto
            print("-".center(100, "-"))
            productdel = str(input("que producto solicita eliminar del inventario: "))
            delete_product(productdel)
            code -= 1
        elif player == 5:
            # Calcular valor total del inventario
            print("-".center(100, "-"))
            for id, inserted in inventory.items():
                print(f"{id} : {inserted}")
                print("-".center(100, "-"))
            total_value = sum(map(lambda product: product["precio"] * product["unidades"], inventory.values()))
            print(f"total a pagar: {total_value}")
            end_program()
            continue
        elif player == 6:
            # Mostrar inventario completo
            print("-".center(100, "-"))
            for id, inserted in inventory.items():
                print(f"{id} : {inserted}")
            continue
        elif player == 0:
            # Salir del programa
            end_program()
            exit()
        else:
            # Opción no válida
            print("opcion no valida")
            continue
    except ValueError:
        print("valor invalido")