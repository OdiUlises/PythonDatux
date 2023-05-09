''' Crear una clase Persona y que para instanciar los datos sean datos ingresados desde
teclado'''
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad de la persona: "))
ciudad = input("Ingresa la ciudad de la persona: ")

persona = Persona(nombre, edad, ciudad)

print("Nombre:", persona.nombre)
print("Edad:", persona.edad)
print("Ciudad:", persona.ciudad)