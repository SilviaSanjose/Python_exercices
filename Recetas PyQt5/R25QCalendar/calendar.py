# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar_Dialog(object):
    def setupUi(self, Calendar_Dialog):
        Calendar_Dialog.setObjectName("Calendar_Dialog")
        Calendar_Dialog.resize(442, 379)
        self.cld_calendar = QtWidgets.QCalendarWidget(Calendar_Dialog)
        self.cld_calendar.setGeometry(QtCore.QRect(30, 20, 371, 201))
        self.cld_calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cld_calendar.setObjectName("cld_calendar")
        self.ded_fecha = QtWidgets.QDateEdit(Calendar_Dialog)
        self.ded_fecha.setGeometry(QtCore.QRect(160, 270, 110, 22))
        self.ded_fecha.setObjectName("ded_fecha")

        self.retranslateUi(Calendar_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Calendar_Dialog)

    def retranslateUi(self, Calendar_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Calendar_Dialog.setWindowTitle(_translate("Calendar_Dialog", "Calendario"))
