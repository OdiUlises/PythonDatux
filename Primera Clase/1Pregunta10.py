# Definir las listas de DNIs y datos anidados
dnis = [11111111, 22222222, 33333333, 44444444]
datos = [
    ['Juan', 25, 'Lima', True, 'Curso de Python'],
    ['María', 30, 'Arequipa', False, 'Curso de SQL'],
    ['Pedro', 20, 'Trujillo', True, 'Curso de Python'],
    ['Sofía', 19, 'Cusco', True, 'Curso de Power BI']
]

# Pedir al usuario que ingrese su DNI
dni = int(input("Ingrese su DNI: "))

# Verificar si el DNI es válido
if dni in dnis:
    # Obtener la posición del DNI en la lista
    pos = dnis.index(dni)
    
    # Obtener los datos de la persona en esa posición
    datos_persona = datos[pos]
    
    # Verificar si cumple con las condiciones para ingresar
    if datos_persona[1] > 18 and datos_persona[3] and datos_persona[4] == 'Curso de Python':
        print("Bienvenido,", datos_persona[0])
    else:
        print("Lo siento, no tiene permitido el ingreso.")
else:
    print("Lo siento, su DNI no está en la lista.")