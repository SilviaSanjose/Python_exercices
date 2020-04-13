# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listado.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list_canciones(object):
    def setupUi(self, list_canciones):
        list_canciones.setObjectName("list_canciones")
        list_canciones.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(list_canciones)
        self.centralwidget.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 235, 235, 206), stop:0.258706 rgba(255, 188, 188, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:0.507463 rgba(255, 162, 162, 80), stop:1 rgba(255, 255, 255, 0));")
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado.setGeometry(QtCore.QRect(20, 30, 471, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_listado.setFont(font)
        self.lbl_listado.setObjectName("lbl_listado")
        self.lstw_canciones = QtWidgets.QListWidget(self.centralwidget)
        self.lstw_canciones.setGeometry(QtCore.QRect(70, 130, 641, 311))
        self.lstw_canciones.setStyleSheet("background-color: rgb(223, 210, 205);")
        self.lstw_canciones.setObjectName("lstw_canciones")
        list_canciones.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(list_canciones)
        self.statusbar.setObjectName("statusbar")
        list_canciones.setStatusBar(self.statusbar)

        self.retranslateUi(list_canciones)
        QtCore.QMetaObject.connectSlotsByName(list_canciones)

    def retranslateUi(self, list_canciones):
        _translate = QtCore.QCoreApplication.translate
        list_canciones.setWindowTitle(_translate("list_canciones", "Listado De Canciones"))
        self.lbl_listado.setText(_translate("list_canciones", "<html><head/><body><p><span style=\" font-weight:600; color:#b3024f;\">LISTADO DE CANCIONES REGISTRADAS</span></p></body></html>"))
