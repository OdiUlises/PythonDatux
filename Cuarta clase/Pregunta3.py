"""validar una entrada mediante una expresión regular (numérica , texto , email ,celular etc"""
import re

def validar_entrada(entrada, tipo):
    patron = ""

    if tipo == "numerica":
        patron = r'^\d+$'
    elif tipo == "texto":
        patron = r'^[a-zA-Z ]+$'
    elif tipo == "email":
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    elif tipo == "celular":
        patron = r'^\d{9}$'
    else:
        return False

    return re.match(patron, entrada) is not None

def main():
    entrada = input("Ingrese la entrada a validar: ")
    tipo = input("Ingrese el tipo de entrada (numerica, texto, email, celular): ")

    if validar_entrada(entrada, tipo):
        print("La entrada es válida.")
    else:
        print("La entrada no es válida.")

if __name__ == '__main__':
    main()