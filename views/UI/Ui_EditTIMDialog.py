# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTIMDialog.ui'
#
# Created: Mon Aug  5 09:43:45 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditTIMDialog(object):
    def setupUi(self, EditTIMDialog):
        EditTIMDialog.setObjectName(_fromUtf8("EditTIMDialog"))
        EditTIMDialog.resize(555, 563)
        self.verticalLayout = QtGui.QVBoxLayout(EditTIMDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TIMTreeView = QtGui.QTreeView(EditTIMDialog)
        self.TIMTreeView.setObjectName(_fromUtf8("TIMTreeView"))
        self.verticalLayout.addWidget(self.TIMTreeView)
        self.buttonBox = QtGui.QDialogButtonBox(EditTIMDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditTIMDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditTIMDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditTIMDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditTIMDialog)

    def retranslateUi(self, EditTIMDialog):
        EditTIMDialog.setWindowTitle(QtGui.QApplication.translate("EditTIMDialog", "Editar TIM", None, QtGui.QApplication.UnicodeUTF8))

