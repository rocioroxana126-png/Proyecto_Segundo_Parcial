#Integrantes:
#Palma Bowen Ricardo David
#Reina Mera Roxana Rocio
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem,QLineEdit
from UI.vtnPrincipal import Ui_interfaz

from Dominio.cliente import Cliente
from Dominio.producto import ProductoBase
from Dominio.venta import Venta
from Datos.venta_DAO import VentaDAO


class VentaServicio(QMainWindow, Ui_interfaz):
    """
    Clase que genera la logica de los objetos de tipo servicio
    """
    def __init__(self):
        super(VentaServicio, self).__init__()
        self.ui = Ui_interfaz()
        self.ui.setupUi(self)

        self.ui.DetalleFactura.itemChanged.connect(self.calcular_totales_tabla)

        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnCrear.clicked.connect(self.crear)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)

    def calcular_totales_tabla(self, item):
        self.ui.DetalleFactura.blockSignals(True)
        try:
            fila = item.row()
            columna = item.column()
            texto = item.text()
            if columna == 0 and len(texto) > 10:
                item.setText(texto[:10])  # Recorta a 10
                QMessageBox.warning(self, "Límite excedido", "El código no puede tener más de 10 caracteres.")
            elif columna == 1 and len(texto) > 20:
                item.setText(texto[:20])  # Recorta a 20
                QMessageBox.warning(self, "Límite excedido", "El nombre no puede tener más de 20 caracteres.")
            if columna == 2 or columna == 3:
                item_precio = self.ui.DetalleFactura.item(fila, 2)
                item_unidades = self.ui.DetalleFactura.item(fila, 3)
                if item_precio and item_unidades:
                    try:
                        precio = float(item_precio.text().replace(',', '.'))
                        unidades = int(item_unidades.text())
                        subtotal = precio * unidades
                        total = subtotal * 1.15
                        self.ui.DetalleFactura.setItem(fila, 4, QTableWidgetItem(f"{subtotal:.2f}"))
                        self.ui.DetalleFactura.setItem(fila, 5, QTableWidgetItem(f"{total:.2f}"))
                    except ValueError:
                        pass
        finally:
            self.ui.DetalleFactura.blockSignals(False)

    def guardar(self):
        try:
            # 1. Validaciones de la interfaz (Campos de arriba)
            num_factura = self.ui.TxTNumFactura.text().strip()
            if not num_factura:
                raise ValueError("Falta el número de factura.")

            # --- ÚNICA ADICIÓN: VALIDACIÓN DE EXISTENCIA ---
            if VentaDAO.seleccionar_por_id(num_factura):
                raise ValueError(f"La factura N.° {num_factura} ya existe en el sistema.")
            # -----------------------------------------------

            if not self.ui.TxTCodCliente.text().strip():
                raise ValueError("Falta el ID del cliente.")
            if not self.ui.TxTNombre.text().strip():
                raise ValueError("El nombre del cliente es obligatorio.")
            if not self.ui.TxTApellido.text().strip():
                raise ValueError("El apellido del cliente es obligatorio.")
            if self.ui.DetalleFactura.rowCount() == 0:
                raise ValueError("Debe presionar 'Nueva Venta' y cargar un producto.")

            item_codigo = self.ui.DetalleFactura.item(0, 0)
            item_nombre = self.ui.DetalleFactura.item(0, 1)

            if not item_codigo or not item_codigo.text().strip():
                raise ValueError("Debe ingresar el código del producto en la tabla.")
            if not item_nombre or not item_nombre.text().strip():
                raise ValueError("Debe ingresar el nombre del producto en la tabla.")

            cliente = Cliente(
                self.ui.TxTCodCliente.text(),
                self.ui.TxTNombre.text(),
                self.ui.TxTApellido.text()
            )

            codigo = item_codigo.text()
            nombre_p = item_nombre.text()
            precio = float(self.ui.DetalleFactura.item(0, 2).text().replace(',', '.'))
            unidades = int(self.ui.DetalleFactura.item(0, 3).text())

            prod = ProductoBase(codigo, nombre_p, precio, unidades)
            nueva_venta = Venta(int(num_factura), cliente, prod)

            if VentaDAO.insertar(nueva_venta):
                QMessageBox.information(self, "Éxito", "Guardado correctamente.")
                self.limpiar()
            else:
                # Si llega aquí, es un error de conexión o SQL, no de validación
                raise Exception("Error al insertar en la base de datos.")

        except ValueError as e:
            QMessageBox.warning(self, "Validación", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error de Base de Datos", f"Detalle: {e}")


    def limpiar(self):
        for widget in self.findChildren(QLineEdit):
            widget.clear()
        self.ui.DetalleFactura.setRowCount(0)

    def crear(self):
        self.ui.DetalleFactura.setRowCount(0)
        self.ui.DetalleFactura.insertRow(0)
        self.ui.DetalleFactura.setItem(0, 2, QTableWidgetItem("0.00"))
        self.ui.DetalleFactura.setItem(0, 3, QTableWidgetItem("0"))
        self.ui.DetalleFactura.setItem(0, 4, QTableWidgetItem("0.00"))
        self.ui.DetalleFactura.setItem(0, 5, QTableWidgetItem("0.00"))

        self.ui.TxTNumFactura.setFocus()

    def buscar(self):
        try:
            id_f = self.ui.TxTBuscarFactura.text().strip()
            if id_f == "":
                QMessageBox.critical(self, "Error", "Debe ingresar la factura a consultar")
                return
            fila = VentaDAO.seleccionar_por_id(id_f)

            if fila:
                # Llenar datos de cabecera
                self.ui.TxTNumFactura.setText(str(fila[0]))
                self.ui.TxTCodCliente.setText(str(fila[1]))
                self.ui.TxTNombre.setText(fila[2])
                self.ui.TxTApellido.setText(fila[3])
                self.ui.DetalleFactura.setRowCount(0)
                self.ui.DetalleFactura.insertRow(0)
                for i in range(4, 10):
                    self.ui.DetalleFactura.setItem(0, i - 4, QTableWidgetItem(str(fila[i])))
            else:
                QMessageBox.critical(self, "Error", "Factura no encontrada")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error en búsqueda: {e}")

    def actualizar(self):
        try:
            id_f = self.ui.TxTNumFactura.text().strip()
            if not id_f:
                raise ValueError("El campo 'N.° Factura' no puede estar vacío.")
            cod_c = self.ui.TxTCodCliente.text().strip()
            if not cod_c:
                raise ValueError("El campo 'ID Cliente' es obligatorio.")
            nom_c = self.ui.TxTNombre.text().strip()
            if not nom_c:
                raise ValueError("El campo 'Nombres' del cliente es obligatorio.")
            ape_c = self.ui.TxTApellido.text().strip()
            if not ape_c:
                raise ValueError("El campo 'Apellidos' del cliente es obligatorio.")
            if self.ui.DetalleFactura.rowCount() == 0:
                raise ValueError("No hay productos en la tabla. Debe cargar un detalle para actualizar.")
            item_cod = self.ui.DetalleFactura.item(0, 0)
            if not item_cod or not item_cod.text().strip():
                raise ValueError("Falta el 'Código' del producto en la tabla.")
            item_nom = self.ui.DetalleFactura.item(0, 1)
            if not item_nom or not item_nom.text().strip():
                raise ValueError("Falta el 'Nombre' del producto en la tabla.")
            item_pre = self.ui.DetalleFactura.item(0, 2)
            if not item_pre or not item_pre.text().strip():
                raise ValueError("Falta el 'Precio' del producto en la tabla.")
            item_can = self.ui.DetalleFactura.item(0, 3)
            if not item_can or not item_can.text().strip():
                raise ValueError("Falta la 'Cantidad' (Unidades) en la tabla.")
            cliente = Cliente(cod_c, nom_c, ape_c)
            try:
                precio_val = float(item_pre.text().replace(',', '.'))
                unidades_val = int(item_can.text())
            except ValueError:
                raise ValueError("El Precio o las Unidades tienen un formato numérico inválido.")
            prod = ProductoBase(
                item_cod.text(),
                item_nom.text(),
                precio_val,
                unidades_val
            )
            venta_editada = Venta(id_f, cliente, prod)
            if VentaDAO.actualizar(venta_editada):
                QMessageBox.information(self, "Éxito", "Venta actualizada correctamente.")
                self.limpiar()
            else:
                QMessageBox.warning(self, "Error", "No se encontró la factura en la base de datos para actualizar.")
        except ValueError as e:
            QMessageBox.warning(self, "Dato Faltante", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error Crítico", f"Ocurrió un error inesperado: {e}")


    def eliminar(self):
        id_f = self.ui.TxTBuscarFactura.text().strip()
        if not id_f:
            id_f = self.ui.TxTNumFactura.text().strip()
        if not id_f:
            QMessageBox.warning(self, "Atención", "Ingrese un número de factura para eliminar.")
            return
        respuesta = QMessageBox.question(self, "Confirmar", "¿Está seguro de eliminar esta venta?",
                                         QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            if VentaDAO.eliminar(id_f):
                QMessageBox.information(self, "Éxito", "Venta eliminada correctamente.")
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "No se encontró la factura.")


