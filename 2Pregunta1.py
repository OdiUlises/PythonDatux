'''Indicaciones: crear
1.Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la
pregunta):
- Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.
- Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
- Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]'''
def Dibujar_Cuadrado():
    lado = int(input("Ingrese la longitud del lado del cuadrado: "))
    for i in range(lado):
        for j in range(lado):
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def Identificar_Multiplos_de_2():
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in numeros:
        if num % 2 == 0:
            print(num)

def Imprimir_Mayores_Edad(personas):
    for persona in personas:
        if persona[1] >= 18:
            print(persona[0])

opcion = 0
while opcion != 4:
    print("MENU ITERATIVO")
    print("1. Dibujar un cuadrado en consola")
    print("2. Identificar múltiplos de 2 en una lista de números")
    print("3. Imprimir personas mayores de edad en una lista de nombre y edad")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        Dibujar_Cuadrado()
    elif opcion == 2:
        Identificar_Multiplos_de_2()
    elif opcion == 3:
        personas = [["Juan", 22], ["María", 16], ["Pedro", 38], ["Ana", 13]]
        Imprimir_Mayores_Edad(personas)
    elif opcion == 4:
        print("Hasta luego!")
    else:
        print("Opción inválida")