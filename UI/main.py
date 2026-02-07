#Integrantes:
#Palma Bowen Ricardo David
#Reina Mera Roxana Rocio
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska
import sys

from PySide6.QtWidgets import QApplication

from Servicio.venta import VentaServicio



app = QApplication()
vtn_principal = VentaServicio()
vtn_principal.show()
sys.exit(app.exec())