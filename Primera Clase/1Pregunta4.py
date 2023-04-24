# Solicita al usuario ingresar un valor
valor = input("Ingrese un valor: ")

# Determina el tipo de dato
if valor.isdigit():
    print("El valor ingresado es un entero.")
elif valor.replace(".", "", 1).isdigit():
    print("El valor ingresado es un decimal.")
else:
    print("El valor ingresado es una cadena.")