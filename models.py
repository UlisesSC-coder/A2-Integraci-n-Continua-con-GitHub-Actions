class Juego:
    def __init__(self, id, nombre, descripcion, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    @classmethod
    def desde_fila(cls, fila):
        # pymysql devuelve tuplas (id, nombre, descripcion, precio)
        return cls(*fila)