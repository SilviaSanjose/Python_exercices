# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanas/ventana_usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_usuarios(object):
    def setupUi(self, usuarios):
        usuarios.setObjectName("usuarios")
        usuarios.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(usuarios)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_registro = QtWidgets.QLabel(self.centralwidget)
        self.lbl_registro.setGeometry(QtCore.QRect(20, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.lbl_registro.setFont(font)
        self.lbl_registro.setObjectName("lbl_registro")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 141, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_nombre_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nombre_usuario.setGeometry(QtCore.QRect(150, 100, 191, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_nombre_usuario.setFont(font)
        self.txt_nombre_usuario.setObjectName("txt_nombre_usuario")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 100, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_newsletter = QtWidgets.QLabel(self.centralwidget)
        self.txt_newsletter.setGeometry(QtCore.QRect(10, 350, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.txt_newsletter.setFont(font)
        self.txt_newsletter.setObjectName("txt_newsletter")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 350, 211, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(450, 100, 311, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.txt_email.setFont(font)
        self.txt_email.setObjectName("txt_email")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(130, 350, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.rbtn_no = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_no.setGeometry(QtCore.QRect(530, 350, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.rbtn_no.setFont(font)
        self.rbtn_no.setObjectName("rbtn_no")
        self.rbtn_si = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_si.setGeometry(QtCore.QRect(460, 350, 51, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.rbtn_si.setFont(font)
        self.rbtn_si.setObjectName("rbtn_si")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 80, 801, 311))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ventanas\\usuarios3.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.btn_save_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_usuario.setGeometry(QtCore.QRect(0, 390, 61, 61))
        self.btn_save_usuario.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ventanas\\save.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_usuario.setIcon(icon)
        self.btn_save_usuario.setIconSize(QtCore.QSize(55, 55))
        self.btn_save_usuario.setObjectName("btn_save_usuario")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(156, 430, 411, 161))
        self.label_3.setStyleSheet("background-color: rgb(212, 209, 202);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 430, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cbx_buscar_usuario = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_buscar_usuario.setGeometry(QtCore.QRect(340, 440, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        self.cbx_buscar_usuario.setFont(font)
        self.cbx_buscar_usuario.setObjectName("cbx_buscar_usuario")
        self.lbl_datos_usuario = QtWidgets.QLabel(self.centralwidget)
        self.lbl_datos_usuario.setGeometry(QtCore.QRect(160, 490, 401, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        self.lbl_datos_usuario.setFont(font)
        self.lbl_datos_usuario.setText("")
        self.lbl_datos_usuario.setObjectName("lbl_datos_usuario")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.txt_newsletter.raise_()
        self.label_5.raise_()
        self.checkBox.raise_()
        self.rbtn_no.raise_()
        self.rbtn_si.raise_()
        self.txt_email.raise_()
        self.txt_nombre_usuario.raise_()
        self.lbl_registro.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.cbx_buscar_usuario.raise_()
        self.btn_save_usuario.raise_()
        self.lbl_datos_usuario.raise_()
        usuarios.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(usuarios)
        self.statusbar.setObjectName("statusbar")
        usuarios.setStatusBar(self.statusbar)

        self.retranslateUi(usuarios)
        QtCore.QMetaObject.connectSlotsByName(usuarios)

    def retranslateUi(self, usuarios):
        _translate = QtCore.QCoreApplication.translate
        usuarios.setWindowTitle(_translate("usuarios", "Usuarios"))
        self.lbl_registro.setText(_translate("usuarios", "<html><head/><body><p><span style=\" font-weight:600; color:#a7115b;\">REGISTRO DE USUARIOS</span></p></body></html>"))
        self.label.setText(_translate("usuarios", "Nombre usuario"))
        self.label_2.setText(_translate("usuarios", "Email"))
        self.txt_newsletter.setText(_translate("usuarios", "Newsletter"))
        self.label_5.setText(_translate("usuarios", "Información de eventos"))
        self.rbtn_no.setText(_translate("usuarios", "No"))
        self.rbtn_si.setText(_translate("usuarios", "Si"))
        self.label_6.setText(_translate("usuarios", "Buscar usuario"))