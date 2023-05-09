'''para la pregunta 4 al importar la funciones usar el manejo de errores (try ,except) y en las
sentencias de “ else “ imprimir la ruta del directorio de trabajo os.getcwd() y en la sentencia
finally imprimir “proceso terminado'''
import os

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        pais, lote, anio = self.codigo.split("-")
        return f"Producto: {self.nombre}, país de origen: {pais}, número de lote: {lote}"

try:
    producto1 = Producto("Pantalón", "PERU-0001-2023")
    print(producto1)
except Exception as e:
    print(f"Error: {str(e)}")
else:
    print(f"La ruta del directorio de trabajo es: {os.getcwd()}")
finally:
    print("Proceso terminado.")