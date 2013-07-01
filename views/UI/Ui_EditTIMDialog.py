# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTIMDialog.ui'
#
# Created: Sun Jun 30 15:21:26 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_orgTIMDialog(object):
    def setupUi(self, orgTIMDialog):
        orgTIMDialog.setObjectName(_fromUtf8("orgTIMDialog"))
        orgTIMDialog.resize(555, 563)
        self.verticalLayout = QtGui.QVBoxLayout(orgTIMDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.orgTIMLabel = QtGui.QLabel(orgTIMDialog)
        self.orgTIMLabel.setObjectName(_fromUtf8("orgTIMLabel"))
        self.verticalLayout.addWidget(self.orgTIMLabel)
        self.TIMTreeWidget = QtGui.QTreeWidget(orgTIMDialog)
        self.TIMTreeWidget.setObjectName(_fromUtf8("TIMTreeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.TIMTreeWidget)
        self.verticalLayout.addWidget(self.TIMTreeWidget)
        self.buttonBox = QtGui.QDialogButtonBox(orgTIMDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(orgTIMDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), orgTIMDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), orgTIMDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(orgTIMDialog)

    def retranslateUi(self, orgTIMDialog):
        orgTIMDialog.setWindowTitle(QtGui.QApplication.translate("orgTIMDialog", "Editar TIM", None, QtGui.QApplication.UnicodeUTF8))
        self.orgTIMLabel.setText(QtGui.QApplication.translate("orgTIMDialog", "Crie o TIM:", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("orgTIMDialog", "TIM", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.TIMTreeWidget.isSortingEnabled()
        self.TIMTreeWidget.setSortingEnabled(False)
        self.TIMTreeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("orgTIMDialog", "Adicionar tipo...", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMTreeWidget.setSortingEnabled(__sortingEnabled)

