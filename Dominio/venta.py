#Integrantes:
#Palma Bowen Ricardo David
#Reina Mera Roxana Rocio
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska

from Dominio.cliente import Cliente
from Dominio.producto import ProductoBase

class Venta:
    """
    Clase que representa una transacción
    """

    def __init__(self, id_venta: str, cliente: Cliente, producto: ProductoBase):
        self._id_venta = id_venta
        self._cliente = cliente
        self._producto = producto

    @property
    def id_venta(self):
        return self._id_venta

    @property
    def cliente(self):
        return self._cliente

    @property
    def producto(self):
        return self._producto




    def agregar_producto(self, producto: ProductoBase):
        if isinstance(producto, ProductoBase):
            self._productos.append(producto)
        else:
            print("Error: El objeto no es un producto válido.")

    @property
    def subtotal_factura(self):
        return sum(p.subtotal for p in self._productos)

    @property
    def total_factura(self):
        return sum(p.total for p in self._productos)