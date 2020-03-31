# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoSaludo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogoSaludar(object):
    def setupUi(self, DialogoSaludar):
        DialogoSaludar.setObjectName("DialogoSaludar")
        DialogoSaludar.resize(405, 278)
        self.lbl_escriba_nombre = QtWidgets.QLabel(DialogoSaludar)
        self.lbl_escriba_nombre.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_escriba_nombre.setFont(font)
        self.lbl_escriba_nombre.setObjectName("lbl_escriba_nombre")
        self.txt_nombre = QtWidgets.QLineEdit(DialogoSaludar)
        self.txt_nombre.setGeometry(QtCore.QRect(170, 30, 181, 31))
        self.txt_nombre.setText("")
        self.txt_nombre.setObjectName("txt_nombre")
        self.lbl_saludo = QtWidgets.QLabel(DialogoSaludar)
        self.lbl_saludo.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.lbl_saludo.setObjectName("lbl_saludo")
        self.lbl_mensaje_saludo = QtWidgets.QLabel(DialogoSaludar)
        self.lbl_mensaje_saludo.setGeometry(QtCore.QRect(160, 110, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_mensaje_saludo.setFont(font)
        self.lbl_mensaje_saludo.setText("")
        self.lbl_mensaje_saludo.setObjectName("lbl_mensaje_saludo")
        self.btn_saludar = QtWidgets.QPushButton(DialogoSaludar)
        self.btn_saludar.setGeometry(QtCore.QRect(180, 180, 93, 28))
        self.btn_saludar.setObjectName("btn_saludar")

        self.retranslateUi(DialogoSaludar)
        QtCore.QMetaObject.connectSlotsByName(DialogoSaludar)

    def retranslateUi(self, DialogoSaludar):
        _translate = QtCore.QCoreApplication.translate
        DialogoSaludar.setWindowTitle(_translate("DialogoSaludar", "Saludo"))
        self.lbl_escriba_nombre.setText(_translate("DialogoSaludar", "Escribe tu nombre: "))
        self.lbl_saludo.setText(_translate("DialogoSaludar", "Saludo: "))
        self.btn_saludar.setText(_translate("DialogoSaludar", "Saludar"))
