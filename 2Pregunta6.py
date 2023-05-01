'''6.Crear una funcion Main que valide el ingreso para un evento , 
dividir esta funcion main en al menos 3 sub-funciones.'''
def main():
    # Pedir la información del evento al usuario
    nombre_evento, fecha_evento, ubicacion_evento = pedir_informacion_evento()

    # Validar la fecha del evento
    if not validar_fecha(fecha_evento):
        print("La fecha ingresada es inválida.")
        return

    # Imprimir los detalles del evento
    print("Detalles del evento:")
    print("Nombre:", nombre_evento)
    print("Fecha:", fecha_evento)
    print("Ubicación:", ubicacion_evento)

def pedir_informacion_evento():
    # Pedir el nombre del evento al usuario
    nombre_evento = input("Ingrese el nombre del evento: ")

    # Pedir la fecha del evento al usuario
    fecha_evento = input("Ingrese la fecha del evento (DD/MM/AAAA): ")

    # Pedir la ubicación del evento al usuario
    ubicacion_evento = input("Ingrese la ubicación del evento: ")

    return nombre_evento, fecha_evento, ubicacion_evento

def validar_fecha(fecha):
    # Verificar que la fecha tenga el formato correcto (DD/MM/AAAA)
    if len(fecha) != 10 or fecha[2] != "/" or fecha[5] != "/":
        return False

    # Verificar que los componentes de la fecha sean números
    dia, mes, anio = fecha.split("/")
    if not (dia.isnumeric() and mes.isnumeric() and anio.isnumeric()):
        return False

    # Verificar que la fecha sea válida
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False