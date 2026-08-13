def suma_primeros_n(n):
    suma = 0
    for numero in range(1, n + 1):
        suma += numero
    return suma

def divisibles_por_3(inicio, fin):
    divisibles = []
    for numero in range(inicio, fin + 1):
        if numero % 3 == 0:
            divisibles.append(numero)
    return divisibles

while True:
    print("\nMENU:")
    print("1. sumar los primeros N numeros naturales")
    print("2. encontrar divisibles por 3 en un rango")
    print("3. salir")
    opcion = input("elija una opcion: ")

    match opcion:
        case "1":
            n = int(input("ingrese N: "))
            resultado = suma_primeros_n(n)
            print(f"la suma de los primeros {n} numeros es: {resultado}")
        case "2":
            inicio = int(input("ingrese el inicio del rango: "))
            fin = int(input("ingrese el fin del rango: "))
            resultado = divisibles_por_3(inicio, fin)
            print(f"los divisibles por 3 entre {inicio} y {fin} son: {resultado}")
        case "3":
            print("saliendo...")
            break
        case _:
            print("opcion no valida, intenta de nuevo")