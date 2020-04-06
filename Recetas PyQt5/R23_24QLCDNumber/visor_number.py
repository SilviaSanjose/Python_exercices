# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visor_number.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 303)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 10, 251, 71))
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.btn_decimal = QtWidgets.QPushButton(Dialog)
        self.btn_decimal.setGeometry(QtCore.QRect(40, 100, 81, 28))
        self.btn_decimal.setObjectName("btn_decimal")
        self.btn_binario = QtWidgets.QPushButton(Dialog)
        self.btn_binario.setGeometry(QtCore.QRect(130, 100, 81, 28))
        self.btn_binario.setObjectName("btn_binario")
        self.btn_hexa = QtWidgets.QPushButton(Dialog)
        self.btn_hexa.setGeometry(QtCore.QRect(310, 100, 81, 28))
        self.btn_hexa.setObjectName("btn_hexa")
        self.btn_octal = QtWidgets.QPushButton(Dialog)
        self.btn_octal.setGeometry(QtCore.QRect(220, 100, 81, 28))
        self.btn_octal.setObjectName("btn_octal")
        self.txt_introduccion = QtWidgets.QLineEdit(Dialog)
        self.txt_introduccion.setGeometry(QtCore.QRect(40, 30, 113, 22))
        self.txt_introduccion.setObjectName("txt_introduccion")
        self.lbl_hora = QtWidgets.QLabel(Dialog)
        self.lbl_hora.setGeometry(QtCore.QRect(30, 200, 91, 16))
        self.lbl_hora.setObjectName("lbl_hora")
        self.lcd_hora = QtWidgets.QLCDNumber(Dialog)
        self.lcd_hora.setGeometry(QtCore.QRect(170, 180, 191, 71))
        self.lcd_hora.setObjectName("lcd_hora")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_decimal.setText(_translate("Dialog", "Decimal"))
        self.btn_binario.setText(_translate("Dialog", "Binario"))
        self.btn_hexa.setText(_translate("Dialog", "Hexadecimal"))
        self.btn_octal.setText(_translate("Dialog", "Octal"))
        self.lbl_hora.setText(_translate("Dialog", "Mostrar Hora"))
