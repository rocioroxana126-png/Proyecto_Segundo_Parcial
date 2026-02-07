#Integrantes:
#Palma Bowen Ricardo David
#Reina Mera Roxana Rocio
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska
import sys
import pyodbc as bd


class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    _SERVIDOR = r'ROXANA\SQLREINAR'
    _BBDD = 'Venta'
    _USUARIO = r'roxana SAP'
    _PASSWORD = '1234'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                                           + ';TrustServerCertificate=yes')
            except Exception as e:
                print(f"Error de conexión: {e}")
                sys.exit()
        return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            cls._cursor = cls.obtenerConexion().cursor()
        return cls._cursor

