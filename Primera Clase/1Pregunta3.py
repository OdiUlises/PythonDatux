# Solicita al usuario ingresar tres valores
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))

# Realiza las operaciones aritméticas
suma = valor1 + valor2 + valor3
resta = valor1 - valor2 - valor3
multiplicacion = valor1 * valor2 * valor3
division = valor1 / valor2 / valor3
division_entera = valor1 // valor2 // valor3

# Imprime los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)