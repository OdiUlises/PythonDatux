'''5.Crear una funcion que al mandar como parámetro un path me liste los elementos que
contiene esa carpeta ,en caso sea una carpeta llamar otra vez tu función que lista los
elementos de esa subcarpeta.'''
import os

def listar_elementos_carpeta(path):
    # Obtener los elementos del directorio
    elementos = os.listdir(path)

    # Iterar sobre los elementos
    for elemento in elementos:
        # Crear la ruta completa al elemento
        ruta_elemento = os.path.join(path, elemento)

        # Verificar si el elemento es una carpeta
        if os.path.isdir(ruta_elemento):
            print("Carpeta:", elemento)
            # Si el elemento es una carpeta, llamar a la función de forma recursiva
            listar_elementos_carpeta(ruta_elemento)
        else:
            print("Archivo:", elemento)

# Ejemplo de uso: listar los elementos del directorio actual
listar_elementos_carpeta(".")