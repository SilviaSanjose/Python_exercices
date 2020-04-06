# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_tabla_listado.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tabla_canciones(object):
    def setupUi(self, tabla_canciones):
        tabla_canciones.setObjectName("tabla_canciones")
        tabla_canciones.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(tabla_canciones)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado.setGeometry(QtCore.QRect(70, 40, 471, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_listado.setFont(font)
        self.lbl_listado.setObjectName("lbl_listado")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 130, 741, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        tabla_canciones.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tabla_canciones)
        self.statusbar.setObjectName("statusbar")
        tabla_canciones.setStatusBar(self.statusbar)

        self.retranslateUi(tabla_canciones)
        QtCore.QMetaObject.connectSlotsByName(tabla_canciones)

    def retranslateUi(self, tabla_canciones):
        _translate = QtCore.QCoreApplication.translate
        tabla_canciones.setWindowTitle(_translate("tabla_canciones", "MainWindow"))
        self.lbl_listado.setText(_translate("tabla_canciones", "<html><head/><body><p><span style=\" font-weight:600; color:#b3024f;\">TABLA DE CANCIONES REGISTRADAS</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tabla_canciones", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tabla_canciones", "TITULO"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tabla_canciones", "ARTISTA"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("tabla_canciones", "ALBUM"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("tabla_canciones", "AÑO"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("tabla_canciones", "ESTILO"))
