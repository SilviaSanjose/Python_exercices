# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R08EleccionClase.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 518)
        self.lbl_escoger_vuelo = QtWidgets.QLabel(Dialog)
        self.lbl_escoger_vuelo.setGeometry(QtCore.QRect(60, 30, 181, 21))
        self.lbl_escoger_vuelo.setObjectName("lbl_escoger_vuelo")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 40, 221, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbtn_primera_clase = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_primera_clase.setObjectName("rbtn_primera_clase")
        self.verticalLayout.addWidget(self.rbtn_primera_clase)
        self.rbtn_clase_negocio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_clase_negocio.setObjectName("rbtn_clase_negocio")
        self.verticalLayout.addWidget(self.rbtn_clase_negocio)
        self.rbtn_clase_economica = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_clase_economica.setObjectName("rbtn_clase_economica")
        self.verticalLayout.addWidget(self.rbtn_clase_economica)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 240, 131, 20))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 250, 221, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbtn_tarjeta = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtn_tarjeta.setObjectName("rbtn_tarjeta")
        self.verticalLayout_2.addWidget(self.rbtn_tarjeta)
        self.rbtn_paypal = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtn_paypal.setObjectName("rbtn_paypal")
        self.verticalLayout_2.addWidget(self.rbtn_paypal)
        self.rbtn_transferencia = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtn_transferencia.setObjectName("rbtn_transferencia")
        self.verticalLayout_2.addWidget(self.rbtn_transferencia)
        self.lbl_precio_y_forma_pago = QtWidgets.QLabel(Dialog)
        self.lbl_precio_y_forma_pago.setGeometry(QtCore.QRect(40, 450, 471, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_precio_y_forma_pago.setFont(font)
        self.lbl_precio_y_forma_pago.setText("")
        self.lbl_precio_y_forma_pago.setObjectName("lbl_precio_y_forma_pago")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Elección clase"))
        self.lbl_escoger_vuelo.setText(_translate("Dialog", "Escoja la clase de vuelo: "))
        self.rbtn_primera_clase.setText(_translate("Dialog", "Primera clase"))
        self.rbtn_clase_negocio.setText(_translate("Dialog", "Clase negocio"))
        self.rbtn_clase_economica.setText(_translate("Dialog", "Clase económica"))
        self.label.setText(_translate("Dialog", "Forma de pago: "))
        self.rbtn_tarjeta.setText(_translate("Dialog", "Tarjeta"))
        self.rbtn_paypal.setText(_translate("Dialog", "Paypal"))
        self.rbtn_transferencia.setText(_translate("Dialog", "Transferencia"))
