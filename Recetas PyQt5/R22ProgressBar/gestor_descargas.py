# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestor_descargas.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Descarga_Dialog(object):
    def setupUi(self, Descarga_Dialog):
        Descarga_Dialog.setObjectName("Descarga_Dialog")
        Descarga_Dialog.resize(476, 207)
        self.lbl_descarga = QtWidgets.QLabel(Descarga_Dialog)
        self.lbl_descarga.setGeometry(QtCore.QRect(160, 40, 131, 20))
        self.lbl_descarga.setObjectName("lbl_descarga")
        self.pgb_descarga = QtWidgets.QProgressBar(Descarga_Dialog)
        self.pgb_descarga.setGeometry(QtCore.QRect(70, 80, 331, 23))
        self.pgb_descarga.setProperty("value", 0)
        self.pgb_descarga.setObjectName("pgb_descarga")
        self.btn_descarga = QtWidgets.QPushButton(Descarga_Dialog)
        self.btn_descarga.setGeometry(QtCore.QRect(180, 130, 111, 28))
        self.btn_descarga.setObjectName("btn_descarga")

        self.retranslateUi(Descarga_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Descarga_Dialog)

    def retranslateUi(self, Descarga_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Descarga_Dialog.setWindowTitle(_translate("Descarga_Dialog", "Gestor de Descargas"))
        self.lbl_descarga.setText(_translate("Descarga_Dialog", "Descarga de Archivos"))
        self.btn_descarga.setText(_translate("Descarga_Dialog", "Iniciar Descarga"))
