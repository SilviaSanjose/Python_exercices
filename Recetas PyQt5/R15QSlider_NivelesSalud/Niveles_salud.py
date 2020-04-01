# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Niveles_salud.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Niveles_Dialog(object):
    def setupUi(self, Niveles_Dialog):
        Niveles_Dialog.setObjectName("Niveles_Dialog")
        Niveles_Dialog.resize(733, 455)
        self.lbl_nivel_azucar = QtWidgets.QLabel(Niveles_Dialog)
        self.lbl_nivel_azucar.setGeometry(QtCore.QRect(50, 60, 101, 16))
        self.lbl_nivel_azucar.setObjectName("lbl_nivel_azucar")
        self.lbl_presion_arterial = QtWidgets.QLabel(Niveles_Dialog)
        self.lbl_presion_arterial.setGeometry(QtCore.QRect(50, 100, 101, 20))
        self.lbl_presion_arterial.setObjectName("lbl_presion_arterial")
        self.hsb_nivel_azucar = QtWidgets.QScrollBar(Niveles_Dialog)
        self.hsb_nivel_azucar.setGeometry(QtCore.QRect(270, 60, 271, 16))
        self.hsb_nivel_azucar.setOrientation(QtCore.Qt.Horizontal)
        self.hsb_nivel_azucar.setObjectName("hsb_nivel_azucar")
        self.hsd_presion_arterial = QtWidgets.QSlider(Niveles_Dialog)
        self.hsd_presion_arterial.setGeometry(QtCore.QRect(280, 100, 261, 22))
        self.hsd_presion_arterial.setOrientation(QtCore.Qt.Horizontal)
        self.hsd_presion_arterial.setObjectName("hsd_presion_arterial")
        self.lbl_pulso = QtWidgets.QLabel(Niveles_Dialog)
        self.lbl_pulso.setGeometry(QtCore.QRect(50, 160, 71, 20))
        self.lbl_pulso.setObjectName("lbl_pulso")
        self.lbl_colesterol = QtWidgets.QLabel(Niveles_Dialog)
        self.lbl_colesterol.setGeometry(QtCore.QRect(300, 160, 121, 20))
        self.lbl_colesterol.setObjectName("lbl_colesterol")
        self.txt_resultado_azucar = QtWidgets.QLineEdit(Niveles_Dialog)
        self.txt_resultado_azucar.setGeometry(QtCore.QRect(50, 360, 211, 22))
        self.txt_resultado_azucar.setReadOnly(True)
        self.txt_resultado_azucar.setObjectName("txt_resultado_azucar")
        self.vsb_pulso = QtWidgets.QScrollBar(Niveles_Dialog)
        self.vsb_pulso.setGeometry(QtCore.QRect(170, 150, 16, 171))
        self.vsb_pulso.setMinimum(40)
        self.vsb_pulso.setMaximum(200)
        self.vsb_pulso.setOrientation(QtCore.Qt.Vertical)
        self.vsb_pulso.setObjectName("vsb_pulso")
        self.vsd_colesterol = QtWidgets.QSlider(Niveles_Dialog)
        self.vsd_colesterol.setGeometry(QtCore.QRect(510, 160, 22, 160))
        self.vsd_colesterol.setMinimum(1)
        self.vsd_colesterol.setMaximum(100)
        self.vsd_colesterol.setTracking(False)
        self.vsd_colesterol.setOrientation(QtCore.Qt.Vertical)
        self.vsd_colesterol.setInvertedAppearance(True)
        self.vsd_colesterol.setInvertedControls(False)
        self.vsd_colesterol.setObjectName("vsd_colesterol")
        self.txt_resultado_pulso = QtWidgets.QLineEdit(Niveles_Dialog)
        self.txt_resultado_pulso.setGeometry(QtCore.QRect(50, 400, 211, 22))
        self.txt_resultado_pulso.setReadOnly(True)
        self.txt_resultado_pulso.setObjectName("txt_resultado_pulso")
        self.txt_resultado_pArterial = QtWidgets.QLineEdit(Niveles_Dialog)
        self.txt_resultado_pArterial.setGeometry(QtCore.QRect(370, 360, 201, 22))
        self.txt_resultado_pArterial.setReadOnly(True)
        self.txt_resultado_pArterial.setObjectName("txt_resultado_pArterial")
        self.txt_resultado_colesterol = QtWidgets.QLineEdit(Niveles_Dialog)
        self.txt_resultado_colesterol.setGeometry(QtCore.QRect(370, 400, 201, 22))
        self.txt_resultado_colesterol.setReadOnly(True)
        self.txt_resultado_colesterol.setObjectName("txt_resultado_colesterol")

        self.retranslateUi(Niveles_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Niveles_Dialog)

    def retranslateUi(self, Niveles_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Niveles_Dialog.setWindowTitle(_translate("Niveles_Dialog", "Niveles Salud"))
        self.lbl_nivel_azucar.setText(_translate("Niveles_Dialog", "Nivel de azucar:"))
        self.lbl_presion_arterial.setText(_translate("Niveles_Dialog", "Presión Arterial:"))
        self.lbl_pulso.setText(_translate("Niveles_Dialog", "Pulso:"))
        self.lbl_colesterol.setText(_translate("Niveles_Dialog", "Nivel colesterol:"))
