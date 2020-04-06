# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tabla_Dialog(object):
    def setupUi(self, tabla_Dialog):
        tabla_Dialog.setObjectName("tabla_Dialog")
        tabla_Dialog.resize(779, 482)
        self.tbl_lenguajes = QtWidgets.QTableWidget(tabla_Dialog)
        self.tbl_lenguajes.setGeometry(QtCore.QRect(40, 50, 501, 221))
        self.tbl_lenguajes.setObjectName("tbl_lenguajes")
        self.tbl_lenguajes.setColumnCount(2)
        self.tbl_lenguajes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_lenguajes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_lenguajes.setHorizontalHeaderItem(1, item)

        self.retranslateUi(tabla_Dialog)
        QtCore.QMetaObject.connectSlotsByName(tabla_Dialog)

    def retranslateUi(self, tabla_Dialog):
        _translate = QtCore.QCoreApplication.translate
        tabla_Dialog.setWindowTitle(_translate("tabla_Dialog", "Tabla de Lenguajes"))
        item = self.tbl_lenguajes.horizontalHeaderItem(0)
        item.setText(_translate("tabla_Dialog", "Lenguaje"))
        item = self.tbl_lenguajes.horizontalHeaderItem(1)
        item.setText(_translate("tabla_Dialog", "Versión"))
