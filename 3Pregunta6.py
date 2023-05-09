''' Agregar 2 funcionalidades al catálogo (por ejemplo filtro segun año ) , asi mismo se
puede agregar mas atributos a la pelicula para que se puedan hacer otras funcionalidades.
https://github.com/gianzk/python0423/blob/main/clase3004/opp2.py '''
class Pelicula:
    def __init__(self, titulo, duracion, release) -> None:
        self.titulo = titulo
        self.duracion = duracion
        self.release = release
        
    def __str__(self) -> str:
        return f"{self.titulo} se estreno el {self.release} y dura {self.duracion} minutos"
    

class Catalogo:
    def __init__(self) -> None:
        self.name = "Catalogo Peliculas"
        self.listaPeliculas = []
        
    def agregar(self, pelicula):
        self.listaPeliculas.append(pelicula)
        
    def mostrar(self):
        for pelicula in self.listaPeliculas:
            print(pelicula)
    
    def filtroDuracion(self, duracion=0):
        resultadoFiltro = []
        for pelicula in self.listaPeliculas:
            if pelicula.duracion > duracion:
                resultadoFiltro.append(pelicula)
        return resultadoFiltro
    
    def filtroRelease(self, anio):
        resultadoFiltro = []
        for pelicula in self.listaPeliculas:
            if pelicula.release == anio:
                resultadoFiltro.append(pelicula)
        return resultadoFiltro
    

peli1 = Pelicula("Hombre Hormiga", 120, 2020)
peli2 = Pelicula("Mario B", 80, 2023)

catalogo = Catalogo()
catalogo.agregar(peli1)
catalogo.agregar(peli2)
catalogo.mostrar()

# Filtrar por duración mayor a 90 minutos
print("Filtro por duración mayor a 90 minutos:")
resultado = catalogo.filtroDuracion(90)
for pelicula in resultado:
    print(pelicula)

# Filtrar por release en 2023
print("Filtro por release en 2023:")
resultado = catalogo.filtroRelease(2023)
for pelicula in resultado:
    print(pelicula)