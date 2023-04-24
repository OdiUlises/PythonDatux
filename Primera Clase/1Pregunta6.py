valor_ingresado = int(input("Ingrese un número: "))
suma = 0

for i in range(valor_ingresado):
    suma += (i+1)

print("La suma de los números hasta", valor_ingresado, "es:", suma)