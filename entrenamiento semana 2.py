print("gestione una serie de calificaciones".center(100, "-"))
print("---------------------".center(100, "-"))

sumacalificaciones = 0
lista_calificaciones = []
while True:
    try:
        calificacion = float(input("Ingrese la calificación del estudiante, -1 para terminar: "))
        if 0 <= calificacion <= 100:
            lista_calificaciones.append(calificacion)
            sumacalificaciones += calificacion
        elif calificacion == -1:
            print("Fin de la entrada de calificaciones")
            print("---------------------".center(100, "-"))
            promedio = sumacalificaciones / len(lista_calificaciones)
            print(f"El promedio de las calificaciones es: {promedio}")
            break
    except ValueError:
        print("no se ingreso calificacion")

print("---------------------".center(100, "-"))
x=0
contadormayores=0
while x<len(lista_calificaciones):
    if lista_calificaciones[x]>promedio:
        contadormayores+=1
    x+=1
print(f"El número de calificaciones mayores al promedio es: {contadormayores}")
print("---------------------".center(100, "-"))

valormax=float(input("Ingrese la calificacion que desea buscar en la lista: "))
contar=0
for c in lista_calificaciones:
    if c<0:
        continue
    elif c==valormax:
        contar+=1
    elif c>lista_calificaciones[-1]:
        print("La calificacion no es valida")
        break
print(f"La calificacion {valormax} se repite {contar} veces en la lista")
print("---------------------".center(100, "-"))
print("Fin del programa".center(100, "-"))