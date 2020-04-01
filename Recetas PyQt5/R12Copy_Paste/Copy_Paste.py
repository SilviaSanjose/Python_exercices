# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R12_Copy_Paste.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CopiaryPegar(object):
    def setupUi(self, CopiaryPegar):
        CopiaryPegar.setObjectName("CopiaryPegar")
        CopiaryPegar.resize(495, 339)
        self.txt_origen = QtWidgets.QLineEdit(CopiaryPegar)
        self.txt_origen.setGeometry(QtCore.QRect(50, 40, 381, 22))
        self.txt_origen.setObjectName("txt_origen")
        self.txt_destino = QtWidgets.QLineEdit(CopiaryPegar)
        self.txt_destino.setGeometry(QtCore.QRect(50, 220, 381, 22))
        self.txt_destino.setObjectName("txt_destino")
        self.btn_copiar = QtWidgets.QPushButton(CopiaryPegar)
        self.btn_copiar.setGeometry(QtCore.QRect(170, 100, 111, 28))
        self.btn_copiar.setObjectName("btn_copiar")
        self.btn_pegar = QtWidgets.QPushButton(CopiaryPegar)
        self.btn_pegar.setGeometry(QtCore.QRect(170, 160, 111, 28))
        self.btn_pegar.setObjectName("btn_pegar")

        self.retranslateUi(CopiaryPegar)
        self.btn_copiar.pressed.connect(self.txt_origen.selectAll)
        self.btn_pegar.clicked.connect(self.txt_destino.paste)
        self.btn_copiar.released.connect(self.txt_origen.copy)
        QtCore.QMetaObject.connectSlotsByName(CopiaryPegar)

    def retranslateUi(self, CopiaryPegar):
        _translate = QtCore.QCoreApplication.translate
        CopiaryPegar.setWindowTitle(_translate("CopiaryPegar", "Copy / Paste"))
        self.btn_copiar.setText(_translate("CopiaryPegar", "PushButton"))
        self.btn_pegar.setText(_translate("CopiaryPegar", "PushButton"))
