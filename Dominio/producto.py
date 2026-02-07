#Integrantes:
#Palma Bowen Ricardo David
#Roxana Rocio Reina Mera
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely valeska


class ProductoBase:
    """
    Clase que crea un objeto de tipo producto.
    """

    def __init__(self,codigo, nombre_producto, precio_base, unidades):
        self._codigo = codigo
        self._nombre_producto = nombre_producto
        self._precio_base = precio_base
        self._unidades = unidades

    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nombre_producto(self) -> str:
        return self._nombre_producto
    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self._nombre_producto = nombre_producto

    @property
    def precio_base(self):
        return self._precio_base
    @precio_base.setter
    def precio_base(self, precio_base):
        self._precio_base = precio_base

    @property
    def unidades(self):
        return self._unidades
    @unidades.setter
    def unidades(self, nuevo_unidades):
        if nuevo_unidades >= 0:
            self._unidades = nuevo_unidades
        else:
            print("Error: El stock no puede ser negativo.")

    @property
    def subtotal(self):
        return self._precio_base * self._unidades

    @property
    def total(self):
        IVA = 0.15
        return self.subtotal * (1 + IVA)



