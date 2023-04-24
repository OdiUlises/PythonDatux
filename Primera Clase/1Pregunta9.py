lista_python = []
lista_sql = []
lista_powerbi = []

opcion = int(input("Ingrese la opción que desee ejecutar: "))

if opcion == 1:
    elemento = input("Ingrese el elemento que desea agregar a la lista de Python: ")
    lista_python.append(elemento)
elif opcion == 2:
    elemento = input("Ingrese el elemento que desea agregar a la lista de SQL: ")
    lista_sql.append(elemento)
elif opcion == 3:
    elemento = input("Ingrese el elemento que desea agregar a la lista de Power BI: ")
    lista_powerbi.append(elemento)

print("Lista de Python:", lista_python)
print("Lista de SQL:", lista_sql)
print("Lista de Power BI:", lista_powerbi)