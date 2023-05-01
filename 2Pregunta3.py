'''3. Definir una función que retorne el mayor valor al ingresar 2 números.'''
# Pedimos al usuario que ingrese 2 números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Definir función para encontrar el mayor valor
def Mayor_Valor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Imprimir el resultado
print("El mayor valor es:", Mayor_Valor(num1, num2))