# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#Integrantes:
#Palma Bowen Ricardo David
#Reina Mera Roxana Rocio
#Gurumendi Chonillo Mirelli Sabrina
#Villacis Leon Nayely Valeska

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_interfaz(object):
    def setupUi(self, interfaz):
        if not interfaz.objectName():
            interfaz.setObjectName(u"interfaz")
        interfaz.resize(691, 537)
        self.lblBuscarFactura = QLabel(interfaz)
        self.lblBuscarFactura.setObjectName(u"lblBuscarFactura")
        self.lblBuscarFactura.setGeometry(QRect(30, 10, 131, 51))
        font = QFont()
        font.setFamilies([u"Mongolian Baiti"])
        font.setPointSize(9)
        font.setBold(False)
        self.lblBuscarFactura.setFont(font)
        self.TxTBuscarFactura = QLineEdit(interfaz)
        self.TxTBuscarFactura.setObjectName(u"TxTBuscarFactura")
        self.TxTBuscarFactura.setGeometry(QRect(170, 20, 311, 31))
        self.TxTBuscarFactura.setMaxLength(10)
        self.btnBuscar = QPushButton(interfaz)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(540, 20, 93, 28))
        self.btnCrear = QPushButton(interfaz)
        self.btnCrear.setObjectName(u"btnCrear")
        self.btnCrear.setGeometry(QRect(540, 60, 93, 28))
        self.btnActualizar = QPushButton(interfaz)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(540, 110, 93, 28))
        self.btnEliminar = QPushButton(interfaz)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(540, 160, 93, 28))
        self.DetalleProducto = QGroupBox(interfaz)
        self.DetalleProducto.setObjectName(u"DetalleProducto")
        self.DetalleProducto.setGeometry(QRect(30, 230, 461, 251))
        self.DetalleFactura = QTableWidget(self.DetalleProducto)
        if (self.DetalleFactura.columnCount() < 6):
            self.DetalleFactura.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.DetalleFactura.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.DetalleFactura.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.DetalleFactura.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.DetalleFactura.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.DetalleFactura.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.DetalleFactura.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.DetalleFactura.setObjectName(u"DetalleFactura")
        self.DetalleFactura.setGeometry(QRect(40, 40, 371, 192))
        self.DatosCliente = QGroupBox(interfaz)
        self.DatosCliente.setObjectName(u"DatosCliente")
        self.DatosCliente.setGeometry(QRect(30, 80, 461, 131))
        self.TxTNumFactura = QLineEdit(self.DatosCliente)
        self.TxTNumFactura.setObjectName(u"TxTNumFactura")
        self.TxTNumFactura.setGeometry(QRect(80, 30, 131, 31))
        self.TxTNumFactura.setMaxLength(10)
        self.lblNumFactura = QLabel(self.DatosCliente)
        self.lblNumFactura.setObjectName(u"lblNumFactura")
        self.lblNumFactura.setGeometry(QRect(10, 20, 71, 51))
        font1 = QFont()
        font1.setFamilies([u"Mongolian Baiti"])
        font1.setPointSize(8)
        font1.setBold(False)
        self.lblNumFactura.setFont(font1)
        self.lblCodCliente = QLabel(self.DatosCliente)
        self.lblCodCliente.setObjectName(u"lblCodCliente")
        self.lblCodCliente.setGeometry(QRect(10, 70, 71, 51))
        self.lblCodCliente.setFont(font1)
        self.TxTCodCliente = QLineEdit(self.DatosCliente)
        self.TxTCodCliente.setObjectName(u"TxTCodCliente")
        self.TxTCodCliente.setGeometry(QRect(80, 80, 131, 31))
        self.TxTCodCliente.setMaxLength(10)
        self.lblNombre = QLabel(self.DatosCliente)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(240, 20, 71, 51))
        self.lblNombre.setFont(font1)
        self.TxTNombre = QLineEdit(self.DatosCliente)
        self.TxTNombre.setObjectName(u"TxTNombre")
        self.TxTNombre.setGeometry(QRect(310, 30, 131, 31))
        self.TxTNombre.setMaxLength(60)
        self.lblApellido = QLabel(self.DatosCliente)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(240, 70, 71, 51))
        self.lblApellido.setFont(font1)
        self.TxTApellido = QLineEdit(self.DatosCliente)
        self.TxTApellido.setObjectName(u"TxTApellido")
        self.TxTApellido.setGeometry(QRect(310, 80, 131, 31))
        self.TxTApellido.setMaxLength(60)
        self.btnGuardar = QPushButton(interfaz)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(540, 250, 93, 28))
        self.btnLimpiar = QPushButton(interfaz)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(540, 290, 93, 28))

        self.retranslateUi(interfaz)

        QMetaObject.connectSlotsByName(interfaz)
    # setupUi

    def retranslateUi(self, interfaz):
        interfaz.setWindowTitle(QCoreApplication.translate("interfaz", u"Sistema Consulta Ventas", None))
        self.lblBuscarFactura.setText(QCoreApplication.translate("interfaz", u"Buscar N.\u00ba Factura", None))
        self.btnBuscar.setText(QCoreApplication.translate("interfaz", u"Buscar", None))
        self.btnCrear.setText(QCoreApplication.translate("interfaz", u"Nueva Venta", None))
        self.btnActualizar.setText(QCoreApplication.translate("interfaz", u"Editar Venta", None))
        self.btnEliminar.setText(QCoreApplication.translate("interfaz", u"Eliminar Venta", None))
        self.DetalleProducto.setTitle(QCoreApplication.translate("interfaz", u"Detalle Producto", None))
        ___qtablewidgetitem = self.DetalleFactura.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("interfaz", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.DetalleFactura.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("interfaz", u"Nombre", None));
        ___qtablewidgetitem2 = self.DetalleFactura.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("interfaz", u"Precio", None));
        ___qtablewidgetitem3 = self.DetalleFactura.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("interfaz", u"Unidades", None));
        ___qtablewidgetitem4 = self.DetalleFactura.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("interfaz", u"Subtotal", None));
        ___qtablewidgetitem5 = self.DetalleFactura.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("interfaz", u"Total", None));
        self.DatosCliente.setTitle(QCoreApplication.translate("interfaz", u"Datos Cliente", None))
        self.lblNumFactura.setText(QCoreApplication.translate("interfaz", u"N.\u00ba Factura", None))
        self.lblCodCliente.setText(QCoreApplication.translate("interfaz", u"ID Cliente", None))
        self.lblNombre.setText(QCoreApplication.translate("interfaz", u"Nombres", None))
        self.lblApellido.setText(QCoreApplication.translate("interfaz", u"Apellidos", None))
        self.btnGuardar.setText(QCoreApplication.translate("interfaz", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("interfaz", u"Limpiar", None))
    # retranslateUi

