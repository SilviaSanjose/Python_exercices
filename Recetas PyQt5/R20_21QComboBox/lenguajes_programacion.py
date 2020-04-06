# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lenguajes_programacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lenguajes_programacion_Dialog(object):
    def setupUi(self, Lenguajes_programacion_Dialog):
        Lenguajes_programacion_Dialog.setObjectName("Lenguajes_programacion_Dialog")
        Lenguajes_programacion_Dialog.resize(654, 439)
        self.cbx_lenguajes = QtWidgets.QComboBox(Lenguajes_programacion_Dialog)
        self.cbx_lenguajes.setGeometry(QtCore.QRect(300, 40, 151, 21))
        self.cbx_lenguajes.setObjectName("cbx_lenguajes")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.lbl_seleccionar = QtWidgets.QLabel(Lenguajes_programacion_Dialog)
        self.lbl_seleccionar.setGeometry(QtCore.QRect(30, 40, 241, 16))
        self.lbl_seleccionar.setObjectName("lbl_seleccionar")
        self.lbl_eleccion = QtWidgets.QLabel(Lenguajes_programacion_Dialog)
        self.lbl_eleccion.setGeometry(QtCore.QRect(40, 100, 551, 21))
        self.lbl_eleccion.setText("")
        self.lbl_eleccion.setObjectName("lbl_eleccion")
        self.lbl_seleccion_fuente = QtWidgets.QLabel(Lenguajes_programacion_Dialog)
        self.lbl_seleccion_fuente.setGeometry(QtCore.QRect(30, 190, 131, 21))
        self.lbl_seleccion_fuente.setObjectName("lbl_seleccion_fuente")
        self.cbx_fuentes = QtWidgets.QFontComboBox(Lenguajes_programacion_Dialog)
        self.cbx_fuentes.setGeometry(QtCore.QRect(190, 190, 281, 22))
        self.cbx_fuentes.setObjectName("cbx_fuentes")
        self.lbl_editor_texto = QtWidgets.QLabel(Lenguajes_programacion_Dialog)
        self.lbl_editor_texto.setGeometry(QtCore.QRect(40, 270, 111, 16))
        self.lbl_editor_texto.setObjectName("lbl_editor_texto")
        self.txt_editor = QtWidgets.QTextEdit(Lenguajes_programacion_Dialog)
        self.txt_editor.setGeometry(QtCore.QRect(193, 270, 281, 141))
        self.txt_editor.setObjectName("txt_editor")

        self.retranslateUi(Lenguajes_programacion_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Lenguajes_programacion_Dialog)

    def retranslateUi(self, Lenguajes_programacion_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Lenguajes_programacion_Dialog.setWindowTitle(_translate("Lenguajes_programacion_Dialog", "Lenguajes de Programación y Fuentes"))
        self.cbx_lenguajes.setItemText(0, _translate("Lenguajes_programacion_Dialog", "Python"))
        self.cbx_lenguajes.setItemText(1, _translate("Lenguajes_programacion_Dialog", "JS"))
        self.cbx_lenguajes.setItemText(2, _translate("Lenguajes_programacion_Dialog", "PHP"))
        self.cbx_lenguajes.setItemText(3, _translate("Lenguajes_programacion_Dialog", "Java"))
        self.lbl_seleccionar.setText(_translate("Lenguajes_programacion_Dialog", "Seleccione un lenguaje de programación"))
        self.lbl_seleccion_fuente.setText(_translate("Lenguajes_programacion_Dialog", "Seleccione la fuente: "))
        self.lbl_editor_texto.setText(_translate("Lenguajes_programacion_Dialog", "Editor de Texto:"))
