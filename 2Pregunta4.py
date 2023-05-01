'''4. Definir una función que imprima los argumentos ingresados desde línea de comandos
Nota: Usar import sys.argv => *args
'''
import sys

def imprimir_args(*args):
    print("Los argumentos ingresados son: ")
    for arg in args:
        print(arg)

# Obtener los argumentos ingresados desde la línea de comandos
args = sys.argv[1:]

# Llamar a la función con los argumentos obtenidos
imprimir_args(*args)