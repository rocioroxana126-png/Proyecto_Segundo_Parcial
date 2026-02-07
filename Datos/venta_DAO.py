#Integrantes:
#Palma Bowen Ricardo David
#Reina Mera Roxana Rocio
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska
from Datos.conexion import Conexion
from Dominio.venta import Venta
import pyodbc as bd

class VentaDAO:
    # Consultas SQL
    _INSERT = ("INSERT INTO Ventas (IdFactura, IdCliente, NombreCliente, ApellidoCLiente, "
               "IdProducto, NombreProducto, PrecioProducto, Unidades, Subtotal, Total) "
               "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    _UPDATE = ("UPDATE Ventas SET IdCliente=?, NombreCliente=?, ApellidoCliente=?, "
               "IdProducto=?, NombreProducto=?, PrecioProducto=?, Unidades=?, "
               "Subtotal=?, Total=? WHERE IdFactura=?")

    _DELETE = "DELETE FROM Ventas WHERE IdFactura=?"

    _SELECT = "SELECT * FROM Ventas WHERE IdFactura=?"

    @classmethod
    def insertar(cls, venta: Venta):
        try:
            cursor = Conexion.obtenerCursor()
            valores = (
                venta.id_venta,
                venta.cliente.id_cliente,
                venta.cliente.nombre,
                venta.cliente.apellido,
                venta.producto.codigo,
                venta.producto.nombre_producto,
                venta.producto.precio_base,
                venta.producto.unidades,
                venta.producto.subtotal,
                venta.producto.total
            )
            cursor.execute(cls._INSERT, valores)
            Conexion.obtenerConexion().commit()
            return True
        except Exception as e:
            print(f"Error DAO Insertar: {e}")
            return False

    @classmethod
    def actualizar(cls, venta: Venta):
        try:
            cursor = Conexion.obtenerCursor()
            valores = (
                venta.cliente.id_cliente,
                venta.cliente.nombre,
                venta.cliente.apellido,
                venta.producto.codigo,
                venta.producto.nombre_producto,
                venta.producto.precio_base,
                venta.producto.unidades,
                venta.producto.subtotal,
                venta.producto.total,
                venta.id_venta
            )
            cursor.execute(cls._UPDATE, valores)
            Conexion.obtenerConexion().commit()
            return True
        except Exception as e:
            print(f"Error DAO Actualizar: {e}")
            return False

    @classmethod
    def seleccionar_por_id(cls, id_factura):
        try:
            cursor = Conexion.obtenerCursor()
            cursor.execute(cls._SELECT, (id_factura,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error DAO Seleccionar: {e}")
            return None

    @classmethod
    def eliminar(cls, id_factura):
        try:
            cursor = Conexion.obtenerCursor()
            cursor.execute(cls._DELETE, (id_factura,))
            Conexion.obtenerConexion().commit()
            return True
        except Exception as e:
            print(f"Error DAO Eliminar: {e}")
            return False