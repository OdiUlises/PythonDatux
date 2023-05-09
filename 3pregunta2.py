'''Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
tener un método para agregar productos y otra para mostrar toda la lista de productos.'''

class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        print("Productos en el catálogo:")
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio} - {producto.descripcion}")
catalogo = Catalogo()

producto1 = Producto("Llantas", 100, "Juego de llantas para automóvil")
catalogo.agregar_producto(producto1)

producto2 = Producto("Frenos", 200, "Kit de frenos para automóvil")
catalogo.agregar_producto(producto2)

catalogo.mostrar_productos()            