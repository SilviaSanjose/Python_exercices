# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R09_10Pizza.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_pizzas(object):
    def setupUi(self, Ventana_pizzas):
        Ventana_pizzas.setObjectName("Ventana_pizzas")
        Ventana_pizzas.resize(501, 327)
        self.lbl_pizza = QtWidgets.QLabel(Ventana_pizzas)
        self.lbl_pizza.setGeometry(QtCore.QRect(40, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pizza.setFont(font)
        self.lbl_pizza.setObjectName("lbl_pizza")
        self.lbl_seleccion_extras = QtWidgets.QLabel(Ventana_pizzas)
        self.lbl_seleccion_extras.setGeometry(QtCore.QRect(40, 60, 131, 21))
        self.lbl_seleccion_extras.setObjectName("lbl_seleccion_extras")
        self.lbl_seleccion_bebida = QtWidgets.QLabel(Ventana_pizzas)
        self.lbl_seleccion_bebida.setGeometry(QtCore.QRect(290, 60, 131, 21))
        self.lbl_seleccion_bebida.setObjectName("lbl_seleccion_bebida")
        self.gbx_extras = QtWidgets.QGroupBox(Ventana_pizzas)
        self.gbx_extras.setGeometry(QtCore.QRect(30, 90, 151, 131))
        self.gbx_extras.setCheckable(True)
        self.gbx_extras.setObjectName("gbx_extras")
        self.chk_queso = QtWidgets.QCheckBox(self.gbx_extras)
        self.chk_queso.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.chk_queso.setObjectName("chk_queso")
        self.chl_aceitunas = QtWidgets.QCheckBox(self.gbx_extras)
        self.chl_aceitunas.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.chl_aceitunas.setObjectName("chl_aceitunas")
        self.chk_salsas = QtWidgets.QCheckBox(self.gbx_extras)
        self.chk_salsas.setGeometry(QtCore.QRect(20, 90, 81, 20))
        self.chk_salsas.setObjectName("chk_salsas")
        self.lbl_precio_final = QtWidgets.QLabel(Ventana_pizzas)
        self.lbl_precio_final.setGeometry(QtCore.QRect(30, 230, 391, 20))
        self.lbl_precio_final.setText("")
        self.lbl_precio_final.setObjectName("lbl_precio_final")
        self.gbx_bebidas = QtWidgets.QGroupBox(Ventana_pizzas)
        self.gbx_bebidas.setGeometry(QtCore.QRect(290, 90, 141, 101))
        self.gbx_bebidas.setCheckable(True)
        self.gbx_bebidas.setObjectName("gbx_bebidas")
        self.chk_refresco = QtWidgets.QCheckBox(self.gbx_bebidas)
        self.chk_refresco.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.chk_refresco.setObjectName("chk_refresco")
        self.chk_cerveza = QtWidgets.QCheckBox(self.gbx_bebidas)
        self.chk_cerveza.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.chk_cerveza.setObjectName("chk_cerveza")

        self.retranslateUi(Ventana_pizzas)
        QtCore.QMetaObject.connectSlotsByName(Ventana_pizzas)

    def retranslateUi(self, Ventana_pizzas):
        _translate = QtCore.QCoreApplication.translate
        Ventana_pizzas.setWindowTitle(_translate("Ventana_pizzas", "Pedido Pizza"))
        self.lbl_pizza.setText(_translate("Ventana_pizzas", "Precio Pizza 15€"))
        self.lbl_seleccion_extras.setText(_translate("Ventana_pizzas", "Seleccione extras: "))
        self.lbl_seleccion_bebida.setText(_translate("Ventana_pizzas", "Seleccione bebida:"))
        self.gbx_extras.setTitle(_translate("Ventana_pizzas", "Extras"))
        self.chk_queso.setText(_translate("Ventana_pizzas", "Queso"))
        self.chl_aceitunas.setText(_translate("Ventana_pizzas", "Aceitunas"))
        self.chk_salsas.setText(_translate("Ventana_pizzas", "Salsas"))
        self.gbx_bebidas.setTitle(_translate("Ventana_pizzas", "Bebidas:"))
        self.chk_refresco.setText(_translate("Ventana_pizzas", "Refresco"))
        self.chk_cerveza.setText(_translate("Ventana_pizzas", "Cerveza"))
