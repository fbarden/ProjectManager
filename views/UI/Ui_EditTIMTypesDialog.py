# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTIMTypesDialog.ui'
#
# Created: Tue Jul 16 12:58:58 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddTIMTypesDialog(object):
    def setupUi(self, AddTIMTypesDialog):
        AddTIMTypesDialog.setObjectName(_fromUtf8("AddTIMTypesDialog"))
        AddTIMTypesDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddTIMTypesDialog.resize(400, 463)
        self.verticalLayout = QtGui.QVBoxLayout(AddTIMTypesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addTIMTypesLabel = QtGui.QLabel(AddTIMTypesDialog)
        self.addTIMTypesLabel.setObjectName(_fromUtf8("addTIMTypesLabel"))
        self.verticalLayout.addWidget(self.addTIMTypesLabel)
        self.TIMListWidget = QtGui.QListWidget(AddTIMTypesDialog)
        self.TIMListWidget.setObjectName(_fromUtf8("TIMListWidget"))
        item = QtGui.QListWidgetItem()
        self.TIMListWidget.addItem(item)
        self.verticalLayout.addWidget(self.TIMListWidget)
        self.buttonBox = QtGui.QDialogButtonBox(AddTIMTypesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddTIMTypesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddTIMTypesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddTIMTypesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTIMTypesDialog)

    def retranslateUi(self, AddTIMTypesDialog):
        AddTIMTypesDialog.setWindowTitle(QtGui.QApplication.translate("AddTIMTypesDialog", "Editar tipos", None, QtGui.QApplication.UnicodeUTF8))
        self.addTIMTypesLabel.setText(QtGui.QApplication.translate("AddTIMTypesDialog", "Liste os tipos de cláusulas:", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.TIMListWidget.isSortingEnabled()
        self.TIMListWidget.setSortingEnabled(False)
        item = self.TIMListWidget.item(0)
        item.setText(QtGui.QApplication.translate("AddTIMTypesDialog", "Adicionar novo tipo...", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMListWidget.setSortingEnabled(__sortingEnabled)

