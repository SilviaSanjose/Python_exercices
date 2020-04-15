# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_bienvenida.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_music_window(object):
    def setupUi(self, music_window):
        music_window.setObjectName("music_window")
        music_window.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(music_window)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_bienvenida = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bienvenida.setGeometry(QtCore.QRect(50, 70, 381, 161))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_bienvenida.setFont(font)
        self.lbl_bienvenida.setObjectName("lbl_bienvenida")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(670, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("\n"
"color: rgb(167, 17, 91);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.txt_fecha = QtWidgets.QLabel(self.centralwidget)
        self.txt_fecha.setGeometry(QtCore.QRect(660, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_fecha.setFont(font)
        self.txt_fecha.setStyleSheet("color: rgb(167, 17, 91);")
        self.txt_fecha.setObjectName("txt_fecha")
        music_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(music_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuRegistro = QtWidgets.QMenu(self.menubar)
        self.menuRegistro.setObjectName("menuRegistro")
        self.menuListado = QtWidgets.QMenu(self.menubar)
        self.menuListado.setObjectName("menuListado")
        self.sub_menu_inicio = QtWidgets.QMenu(self.menubar)
        self.sub_menu_inicio.setObjectName("sub_menu_inicio")
        self.menuUsuarios = QtWidgets.QMenu(self.menubar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        music_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(music_window)
        self.statusbar.setObjectName("statusbar")
        music_window.setStatusBar(self.statusbar)
        self.sub_menu_registro = QtWidgets.QAction(music_window)
        self.sub_menu_registro.setObjectName("sub_menu_registro")
        self.sub_meni_listado_canciones = QtWidgets.QAction(music_window)
        self.sub_meni_listado_canciones.setObjectName("sub_meni_listado_canciones")
        self.sub_menu_tabla_Canciones = QtWidgets.QAction(music_window)
        self.sub_menu_tabla_Canciones.setObjectName("sub_menu_tabla_Canciones")
        self.actionVolver_Home = QtWidgets.QAction(music_window)
        self.actionVolver_Home.setObjectName("actionVolver_Home")
        self.sub_menu_registro_usuario = QtWidgets.QAction(music_window)
        self.sub_menu_registro_usuario.setObjectName("sub_menu_registro_usuario")
        self.menuRegistro.addAction(self.sub_menu_registro)
        self.menuListado.addAction(self.sub_meni_listado_canciones)
        self.menuListado.addAction(self.sub_menu_tabla_Canciones)
        self.menuUsuarios.addAction(self.sub_menu_registro_usuario)
        self.menubar.addAction(self.sub_menu_inicio.menuAction())
        self.menubar.addAction(self.menuRegistro.menuAction())
        self.menubar.addAction(self.menuListado.menuAction())
        self.menubar.addAction(self.menuUsuarios.menuAction())

        self.retranslateUi(music_window)
        QtCore.QMetaObject.connectSlotsByName(music_window)

    def retranslateUi(self, music_window):
        _translate = QtCore.QCoreApplication.translate
        music_window.setWindowTitle(_translate("music_window", "Música es Vida"))
        self.lbl_bienvenida.setText(_translate("music_window", "<html><head/><body><p><span style=\" font-weight:600; color:#a7115b;\">BIENVENIDOS A LA </span></p><p align=\"right\"><span style=\" font-weight:600; color:#a7115b;\">BASE MUSICAL</span></p><p align=\"center\"><span style=\" font-weight:600; color:#a7115b;\">SILVI_SIL</span></p></body></html>"))
        self.txt_fecha.setText(_translate("music_window", "2005-05-20"))
        self.menuRegistro.setTitle(_translate("music_window", "Registro"))
        self.menuListado.setTitle(_translate("music_window", "Listado"))
        self.sub_menu_inicio.setTitle(_translate("music_window", "Inicio"))
        self.menuUsuarios.setTitle(_translate("music_window", "Usuarios"))
        self.sub_menu_registro.setText(_translate("music_window", "Nueva Canción"))
        self.sub_meni_listado_canciones.setText(_translate("music_window", "Listado Canciones"))
        self.sub_menu_tabla_Canciones.setText(_translate("music_window", "Tabla de Canciones"))
        self.actionVolver_Home.setText(_translate("music_window", "Volver Home"))
        self.sub_menu_registro_usuario.setText(_translate("music_window", "Registro Usuario"))
