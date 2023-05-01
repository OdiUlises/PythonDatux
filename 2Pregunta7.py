texto = """Lorem Ipsum es simplemente el texto de relleno de las imprentas y
archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el
año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó
una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos
electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más
recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye
versiones de Lorem Ipsum."""

def dividir_parrafos(texto):
    # Divide el texto en párrafos utilizando el carácter de nueva línea '\n'
    parrafos = texto.split("\n")
    return parrafos

def reemplazar_texto(texto, buscar, reemplazar_con):
    # Reemplaza todas las apariciones de "texto_buscar" con "texto_reemplazar_con"
    nuevo_texto = texto.replace(buscar, reemplazar_con)
    return nuevo_texto

def contar_palabras(texto, palabra):
    # Cuenta el número de veces que "palabra" aparece en "texto"
    num_palabras = texto.count(palabra)
    return num_palabras

# Dividir el texto en párrafos
parrafos = dividir_parrafos(texto)
print(parrafos)

# Reemplazar "texto" con "cadena"
nuevo_texto = reemplazar_texto(texto, "texto", "cadena")
print(nuevo_texto)

# Contar el número de veces que "Lorem" aparece en "texto"
num_palabras = contar_palabras(texto, "Lorem")
print(num_palabras)
