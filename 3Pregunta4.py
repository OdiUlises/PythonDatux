'''Programa que tenga una clase Producto el cual solo tiene los atributo de nombre y codigo
el codigo tiene la siguiente estructura ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear
un método que permita imprimir el objeto de forma literal (__str__) y que me permita
identificar el país de origen , el numero de lote .'''
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        pais, lote, anio = self.codigo.split("-")
        return f"Producto: {self.nombre}, país de origen: {pais}, número de lote: {lote}"
producto1 = Producto("Pantalón", "PERU-0001-2023")
print(producto1)