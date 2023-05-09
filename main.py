from operaciones import dividir

def menu():
    print("1. Dividir dos números")
    print("2. Salir")
    opcion = input("Elige una opción: ")
    return opcion

while True:
    opcion = menu()
    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = dividir(a, b)
        print(f"El resultado de la división de {a} entre {b} es: {resultado}")
    elif opcion == "2":
        print("Adiós!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")