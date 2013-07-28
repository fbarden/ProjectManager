# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrderClausesDialog.ui'
#
# Created: Wed Jul 24 03:11:25 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OrderClausesDialog(object):
    def setupUi(self, OrderClausesDialog):
        OrderClausesDialog.setObjectName(_fromUtf8("OrderClausesDialog"))
        OrderClausesDialog.resize(544, 484)
        self.verticalLayout_2 = QtGui.QVBoxLayout(OrderClausesDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.clausesListWidget = QtGui.QListWidget(OrderClausesDialog)
        self.clausesListWidget.setObjectName(_fromUtf8("clausesListWidget"))
        self.verticalLayout.addWidget(self.clausesListWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.moveUpButton = QtGui.QToolButton(OrderClausesDialog)
        self.moveUpButton.setObjectName(_fromUtf8("moveUpButton"))
        self.horizontalLayout.addWidget(self.moveUpButton)
        self.moveDownButton = QtGui.QToolButton(OrderClausesDialog)
        self.moveDownButton.setObjectName(_fromUtf8("moveDownButton"))
        self.horizontalLayout.addWidget(self.moveDownButton)
        self.deleteButton = QtGui.QToolButton(OrderClausesDialog)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(OrderClausesDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(OrderClausesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OrderClausesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OrderClausesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OrderClausesDialog)

    def retranslateUi(self, OrderClausesDialog):
        OrderClausesDialog.setWindowTitle(QtGui.QApplication.translate("OrderClausesDialog", "Ordernar Cláusulas", None, QtGui.QApplication.UnicodeUTF8))
        self.moveUpButton.setText(QtGui.QApplication.translate("OrderClausesDialog", "↑", None, QtGui.QApplication.UnicodeUTF8))
        self.moveDownButton.setText(QtGui.QApplication.translate("OrderClausesDialog", "↓", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("OrderClausesDialog", "X", None, QtGui.QApplication.UnicodeUTF8))

