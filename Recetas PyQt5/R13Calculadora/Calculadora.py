# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculadora(object):
    def setupUi(self, calculadora):
        calculadora.setObjectName("calculadora")
        calculadora.resize(638, 307)
        self.horizontalLayoutWidget = QtWidgets.QWidget(calculadora)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 140, 561, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_suma = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_suma.setObjectName("btn_suma")
        self.horizontalLayout.addWidget(self.btn_suma)
        self.btn_resta = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_resta.setObjectName("btn_resta")
        self.horizontalLayout.addWidget(self.btn_resta)
        self.btn_multiplicar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_multiplicar.setObjectName("btn_multiplicar")
        self.horizontalLayout.addWidget(self.btn_multiplicar)
        self.btn_division = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_division.setObjectName("btn_division")
        self.horizontalLayout.addWidget(self.btn_division)
        self.lbl_primer_numero = QtWidgets.QLabel(calculadora)
        self.lbl_primer_numero.setGeometry(QtCore.QRect(40, 40, 151, 20))
        self.lbl_primer_numero.setObjectName("lbl_primer_numero")
        self.lbl_segundo_numero = QtWidgets.QLabel(calculadora)
        self.lbl_segundo_numero.setGeometry(QtCore.QRect(40, 90, 161, 20))
        self.lbl_segundo_numero.setObjectName("lbl_segundo_numero")
        self.txt_primer_numero = QtWidgets.QLineEdit(calculadora)
        self.txt_primer_numero.setGeometry(QtCore.QRect(260, 40, 113, 22))
        self.txt_primer_numero.setObjectName("txt_primer_numero")
        self.txt_segundo_numero = QtWidgets.QLineEdit(calculadora)
        self.txt_segundo_numero.setGeometry(QtCore.QRect(260, 90, 113, 22))
        self.txt_segundo_numero.setObjectName("txt_segundo_numero")
        self.lbl_resultado = QtWidgets.QLabel(calculadora)
        self.lbl_resultado.setGeometry(QtCore.QRect(210, 240, 251, 31))
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(calculadora)
        QtCore.QMetaObject.connectSlotsByName(calculadora)

    def retranslateUi(self, calculadora):
        _translate = QtCore.QCoreApplication.translate
        calculadora.setWindowTitle(_translate("calculadora", "Calculadora"))
        self.btn_suma.setText(_translate("calculadora", "+"))
        self.btn_resta.setText(_translate("calculadora", "-"))
        self.btn_multiplicar.setText(_translate("calculadora", "x"))
        self.btn_division.setText(_translate("calculadora", "/"))
        self.lbl_primer_numero.setText(_translate("calculadora", "Ingresar primer número"))
        self.lbl_segundo_numero.setText(_translate("calculadora", "Ingresar segundo número"))
