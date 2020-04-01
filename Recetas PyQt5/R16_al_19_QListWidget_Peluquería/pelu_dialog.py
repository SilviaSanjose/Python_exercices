# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pelu_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pelu_Dialog(object):
    def setupUi(self, Pelu_Dialog):
        Pelu_Dialog.setObjectName("Pelu_Dialog")
        Pelu_Dialog.resize(815, 584)
        self.lbl_tratamientos = QtWidgets.QLabel(Pelu_Dialog)
        self.lbl_tratamientos.setGeometry(QtCore.QRect(30, 110, 181, 16))
        self.lbl_tratamientos.setObjectName("lbl_tratamientos")
        self.lst_tratamientos = QtWidgets.QListWidget(Pelu_Dialog)
        self.lst_tratamientos.setGeometry(QtCore.QRect(130, 140, 201, 281))
        self.lst_tratamientos.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lst_tratamientos.setObjectName("lst_tratamientos")
        item = QtWidgets.QListWidgetItem()
        self.lst_tratamientos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tratamientos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tratamientos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tratamientos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_tratamientos.addItem(item)
        self.lbl_resultados = QtWidgets.QLabel(Pelu_Dialog)
        self.lbl_resultados.setGeometry(QtCore.QRect(40, 430, 241, 21))
        self.lbl_resultados.setText("")
        self.lbl_resultados.setObjectName("lbl_resultados")
        self.lbl_seleccion = QtWidgets.QLabel(Pelu_Dialog)
        self.lbl_seleccion.setGeometry(QtCore.QRect(420, 110, 171, 16))
        self.lbl_seleccion.setObjectName("lbl_seleccion")
        self.lst_trat_seleccionados = QtWidgets.QListWidget(Pelu_Dialog)
        self.lst_trat_seleccionados.setGeometry(QtCore.QRect(530, 140, 201, 281))
        self.lst_trat_seleccionados.setObjectName("lst_trat_seleccionados")
        self.lbl_agregar_tto = QtWidgets.QLabel(Pelu_Dialog)
        self.lbl_agregar_tto.setGeometry(QtCore.QRect(30, 30, 131, 16))
        self.lbl_agregar_tto.setObjectName("lbl_agregar_tto")
        self.txt_agregar_tto = QtWidgets.QLineEdit(Pelu_Dialog)
        self.txt_agregar_tto.setGeometry(QtCore.QRect(170, 30, 181, 21))
        self.txt_agregar_tto.setObjectName("txt_agregar_tto")
        self.btn_agregar_tto = QtWidgets.QPushButton(Pelu_Dialog)
        self.btn_agregar_tto.setGeometry(QtCore.QRect(390, 20, 81, 31))
        self.btn_agregar_tto.setObjectName("btn_agregar_tto")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Pelu_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 480, 371, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hl_modificacion_lista = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hl_modificacion_lista.setContentsMargins(0, 0, 0, 0)
        self.hl_modificacion_lista.setObjectName("hl_modificacion_lista")
        self.btn_editar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_editar.setObjectName("btn_editar")
        self.hl_modificacion_lista.addWidget(self.btn_editar)
        self.btn_eliminar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.hl_modificacion_lista.addWidget(self.btn_eliminar)
        self.btn_eliminar_todos = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_eliminar_todos.setObjectName("btn_eliminar_todos")
        self.hl_modificacion_lista.addWidget(self.btn_eliminar_todos)

        self.retranslateUi(Pelu_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Pelu_Dialog)

    def retranslateUi(self, Pelu_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Pelu_Dialog.setWindowTitle(_translate("Pelu_Dialog", "Peluquería"))
        self.lbl_tratamientos.setText(_translate("Pelu_Dialog", "Tratamientos disponibles:"))
        __sortingEnabled = self.lst_tratamientos.isSortingEnabled()
        self.lst_tratamientos.setSortingEnabled(False)
        item = self.lst_tratamientos.item(0)
        item.setText(_translate("Pelu_Dialog", "Corte 10€"))
        item = self.lst_tratamientos.item(1)
        item.setText(_translate("Pelu_Dialog", "Peinado 10€"))
        item = self.lst_tratamientos.item(2)
        item.setText(_translate("Pelu_Dialog", "Tinte 25€"))
        item = self.lst_tratamientos.item(3)
        item.setText(_translate("Pelu_Dialog", "Mechas 30€"))
        item = self.lst_tratamientos.item(4)
        item.setText(_translate("Pelu_Dialog", "Alisado 50€"))
        self.lst_tratamientos.setSortingEnabled(__sortingEnabled)
        self.lbl_seleccion.setText(_translate("Pelu_Dialog", "Tratamiento seleccionado: "))
        self.lbl_agregar_tto.setText(_translate("Pelu_Dialog", "Agregar Tratamiento: "))
        self.btn_agregar_tto.setText(_translate("Pelu_Dialog", "Agregar"))
        self.btn_editar.setText(_translate("Pelu_Dialog", "Editar"))
        self.btn_eliminar.setText(_translate("Pelu_Dialog", "Eliminar"))
        self.btn_eliminar_todos.setText(_translate("Pelu_Dialog", "Eliminar Todos"))
