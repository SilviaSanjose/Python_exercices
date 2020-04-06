# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservas.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reserva_Dialog(object):
    def setupUi(self, Reserva_Dialog):
        Reserva_Dialog.setObjectName("Reserva_Dialog")
        Reserva_Dialog.resize(589, 492)
        self.cal_fecha = QtWidgets.QCalendarWidget(Reserva_Dialog)
        self.cal_fecha.setGeometry(QtCore.QRect(180, 40, 341, 211))
        self.cal_fecha.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cal_fecha.setObjectName("cal_fecha")
        self.lbl_seleccion_fecha = QtWidgets.QLabel(Reserva_Dialog)
        self.lbl_seleccion_fecha.setGeometry(QtCore.QRect(40, 40, 121, 20))
        self.lbl_seleccion_fecha.setObjectName("lbl_seleccion_fecha")
        self.lbl_seleccion_dias = QtWidgets.QLabel(Reserva_Dialog)
        self.lbl_seleccion_dias.setGeometry(QtCore.QRect(40, 290, 111, 21))
        self.lbl_seleccion_dias.setObjectName("lbl_seleccion_dias")
        self.lbl_seleccion_habitacion = QtWidgets.QLabel(Reserva_Dialog)
        self.lbl_seleccion_habitacion.setGeometry(QtCore.QRect(40, 350, 101, 16))
        self.lbl_seleccion_habitacion.setObjectName("lbl_seleccion_habitacion")
        self.spx_dias = QtWidgets.QSpinBox(Reserva_Dialog)
        self.spx_dias.setGeometry(QtCore.QRect(150, 290, 71, 22))
        self.spx_dias.setObjectName("spx_dias")
        self.cbx_habitacion = QtWidgets.QComboBox(Reserva_Dialog)
        self.cbx_habitacion.setGeometry(QtCore.QRect(150, 350, 131, 22))
        self.cbx_habitacion.setObjectName("cbx_habitacion")
        self.cbx_habitacion.addItem("")
        self.cbx_habitacion.addItem("")
        self.cbx_habitacion.addItem("")
        self.cbx_habitacion.addItem("")
        self.btb_calcular = QtWidgets.QPushButton(Reserva_Dialog)
        self.btb_calcular.setGeometry(QtCore.QRect(410, 320, 101, 28))
        self.btb_calcular.setObjectName("btb_calcular")
        self.lbl_seleccion = QtWidgets.QLabel(Reserva_Dialog)
        self.lbl_seleccion.setGeometry(QtCore.QRect(40, 400, 431, 16))
        self.lbl_seleccion.setText("")
        self.lbl_seleccion.setObjectName("lbl_seleccion")
        self.lbl_precio = QtWidgets.QLabel(Reserva_Dialog)
        self.lbl_precio.setGeometry(QtCore.QRect(40, 440, 431, 16))
        self.lbl_precio.setText("")
        self.lbl_precio.setObjectName("lbl_precio")

        self.retranslateUi(Reserva_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Reserva_Dialog)

    def retranslateUi(self, Reserva_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Reserva_Dialog.setWindowTitle(_translate("Reserva_Dialog", "Reserva de Habitación"))
        self.lbl_seleccion_fecha.setText(_translate("Reserva_Dialog", "Fecha de Reserva"))
        self.lbl_seleccion_dias.setText(_translate("Reserva_Dialog", "Cantidad días:"))
        self.lbl_seleccion_habitacion.setText(_translate("Reserva_Dialog", "Tipo habitación:"))
        self.cbx_habitacion.setItemText(0, _translate("Reserva_Dialog", "Seleccionar"))
        self.cbx_habitacion.setItemText(1, _translate("Reserva_Dialog", "Individual"))
        self.cbx_habitacion.setItemText(2, _translate("Reserva_Dialog", "Doble"))
        self.cbx_habitacion.setItemText(3, _translate("Reserva_Dialog", "Suit"))
        self.btb_calcular.setText(_translate("Reserva_Dialog", "Calcular"))
