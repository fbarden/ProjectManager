# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTIMDialog.ui'
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

class Ui_EditTIMDialog(object):
    def setupUi(self, EditTIMDialog):
        EditTIMDialog.setObjectName(_fromUtf8("EditTIMDialog"))
        EditTIMDialog.resize(555, 563)
        self.verticalLayout = QtGui.QVBoxLayout(EditTIMDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TIMTreeWidget = QtGui.QTreeWidget(EditTIMDialog)
        self.TIMTreeWidget.setObjectName(_fromUtf8("TIMTreeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.TIMTreeWidget)
        self.verticalLayout.addWidget(self.TIMTreeWidget)
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
        self.TIMTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("EditTIMDialog", "TIM", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.TIMTreeWidget.isSortingEnabled()
        self.TIMTreeWidget.setSortingEnabled(False)
        self.TIMTreeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("EditTIMDialog", "Adicionar tipo...", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMTreeWidget.setSortingEnabled(__sortingEnabled)

