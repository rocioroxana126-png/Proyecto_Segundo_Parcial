#Integrantes:
#Palma Bowen Ricardo David
#Roxana Rocio Reina Mera
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska
class Cliente:
    """Clase Opcional 1: Representa un cliente de la tienda."""

    def __init__(self, id_cliente, nombre, apellido):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido


    @property
    def id_cliente(self):
        return self._id_cliente
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente


    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
