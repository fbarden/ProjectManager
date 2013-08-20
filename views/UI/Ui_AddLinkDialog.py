# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddLinkDialog.ui'
#
# Created: Tue Aug 20 00:07:15 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddLinkDialog(object):
    def setupUi(self, AddLinkDialog):
        AddLinkDialog.setObjectName(_fromUtf8("AddLinkDialog"))
        AddLinkDialog.resize(400, 111)
        self.formLayout = QtGui.QFormLayout(AddLinkDialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.typeLabel = QtGui.QLabel(AddLinkDialog)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.typeLabel)
        self.typeComboBox = QtGui.QComboBox(AddLinkDialog)
        self.typeComboBox.setObjectName(_fromUtf8("typeComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.typeComboBox)
        self.clauseLabel = QtGui.QLabel(AddLinkDialog)
        self.clauseLabel.setObjectName(_fromUtf8("clauseLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.clauseLabel)
        self.clauseComboBox = QtGui.QComboBox(AddLinkDialog)
        self.clauseComboBox.setObjectName(_fromUtf8("clauseComboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.clauseComboBox)
        self.buttonBox = QtGui.QDialogButtonBox(AddLinkDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(AddLinkDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddLinkDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddLinkDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddLinkDialog)

    def retranslateUi(self, AddLinkDialog):
        AddLinkDialog.setWindowTitle(QtGui.QApplication.translate("AddLinkDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.typeLabel.setText(QtGui.QApplication.translate("AddLinkDialog", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.clauseLabel.setText(QtGui.QApplication.translate("AddLinkDialog", "Cláusula:", None, QtGui.QApplication.UnicodeUTF8))

