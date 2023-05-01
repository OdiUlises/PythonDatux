'''2.Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
como un diccionario.
2.1 La biblioteca deberá tener las siguientes operaciones:
- Obtener la lista de categorías de libros.
-Obtener nombres de los libros y autores.
-poder cambiar el estado de un libro a prestado
-Lista de usuarios de la biblioteca.
'''
Biblioteca = {
    "Categorías": ["Ciencia Ficción", "Romance", "Historia", "Biografía"],
    "Libros": [
        {"Nombre": "Cien años de soledad", "Autor": "Gabriel García Márquez", "Estado": "Disponible"},
        {"Nombre": "La ciudad y los perros", "Autor": "Mario Vargas Llosa", "Estado": "Disponible"},
        {"Nombre": "Juego de tronos", "Autor": "George R. R. Martin", "Estado": "Disponible"}
    ],
    "Usuarios": ["Cristopher", "Juan", "Fabricio"]
}

def Obtener_Categorias():
    categorias = Biblioteca["Categorías"]
    for categoria in categorias:
        print(categoria)

def obtener_libros():
    libros = Biblioteca["Libros"]
    for libro in libros:
        nombre = libro["Nombre"]
        autor = libro["Autor"]
        print(nombre + " por " + autor)

def prestar_libro(nombre_libro):
    libros = Biblioteca["Libros"]
    for libro in libros:
        if libro["Nombre"] == nombre_libro:
            if libro["Estado"] == "Disponible":
                libro["Estado"] = "Prestado"
                print("El libro " + nombre_libro + " ha sido prestado")
            else:
                print("El libro " + nombre_libro + " no está disponible para préstamo")

def obtener_usuarios():
    usuarios = Biblioteca["Usuarios"]
    for usuario in usuarios:
        print(usuario)

opcion = 0
while opcion != 5:
    print("BIBLIOTECA")
    print("1. Obtener lista de categorías de libros")
    print("2. Obtener nombres de libros y autores")
    print("3. Cambiar el estado de un libro a prestado")
    print("4. Obtener lista de usuarios de la biblioteca")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        Obtener_Categorias()
    elif opcion == 2:
        obtener_libros()
    elif opcion == 3:
        nombre_libro = input("Ingrese el nombre del libro: ")
        prestar_libro(nombre_libro)
    elif opcion == 4:
        obtener_usuarios()
    elif opcion == 5:
        print("Adiós!")
    else:
        print("Opción inválida")