# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venta_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(648, 366)
        self.lbl_mouse = QtWidgets.QLabel(Dialog)
        self.lbl_mouse.setGeometry(QtCore.QRect(30, 40, 141, 20))
        self.lbl_mouse.setObjectName("lbl_mouse")
        self.txt_valor_mouse = QtWidgets.QLineEdit(Dialog)
        self.txt_valor_mouse.setGeometry(QtCore.QRect(190, 40, 81, 22))
        self.txt_valor_mouse.setObjectName("txt_valor_mouse")
        self.sbx_cantidad_mouse = QtWidgets.QSpinBox(Dialog)
        self.sbx_cantidad_mouse.setGeometry(QtCore.QRect(310, 40, 61, 22))
        self.sbx_cantidad_mouse.setObjectName("sbx_cantidad_mouse")
        self.txt_total_mouse = QtWidgets.QLineEdit(Dialog)
        self.txt_total_mouse.setGeometry(QtCore.QRect(420, 40, 113, 22))
        self.txt_total_mouse.setObjectName("txt_total_mouse")
        self.lbl_teclado = QtWidgets.QLabel(Dialog)
        self.lbl_teclado.setGeometry(QtCore.QRect(30, 100, 131, 20))
        self.lbl_teclado.setObjectName("lbl_teclado")
        self.txt_valor_teclado = QtWidgets.QLineEdit(Dialog)
        self.txt_valor_teclado.setGeometry(QtCore.QRect(190, 100, 81, 22))
        self.txt_valor_teclado.setObjectName("txt_valor_teclado")
        self.sbx_cantidad_teclado = QtWidgets.QSpinBox(Dialog)
        self.sbx_cantidad_teclado.setGeometry(QtCore.QRect(310, 100, 61, 22))
        self.sbx_cantidad_teclado.setObjectName("sbx_cantidad_teclado")
        self.txt_total_teclado = QtWidgets.QLineEdit(Dialog)
        self.txt_total_teclado.setGeometry(QtCore.QRect(420, 100, 113, 22))
        self.txt_total_teclado.setObjectName("txt_total_teclado")
        self.lbl_total = QtWidgets.QLabel(Dialog)
        self.lbl_total.setGeometry(QtCore.QRect(380, 200, 181, 16))
        self.lbl_total.setText("")
        self.lbl_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_total.setObjectName("lbl_total")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Compras"))
        self.lbl_mouse.setText(_translate("Dialog", "valor Mouse HyperX"))
        self.txt_valor_mouse.setText(_translate("Dialog", "20"))
        self.lbl_teclado.setText(_translate("Dialog", "valor Teclado HyperX"))
        self.txt_valor_teclado.setText(_translate("Dialog", "30"))
