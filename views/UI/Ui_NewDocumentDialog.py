# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewDocumentDialog.ui'
#
# Created: Sun Jun 30 22:27:28 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewDocumentDialog(object):
    def setupUi(self, NewDocumentDialog):
        NewDocumentDialog.setObjectName(_fromUtf8("NewDocumentDialog"))
        NewDocumentDialog.resize(494, 180)
        self.verticalLayout = QtGui.QVBoxLayout(NewDocumentDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.createDocumentLabel = QtGui.QLabel(NewDocumentDialog)
        self.createDocumentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createDocumentLabel.setObjectName(_fromUtf8("createDocumentLabel"))
        self.verticalLayout.addWidget(self.createDocumentLabel)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.titleLabel = QtGui.QLabel(NewDocumentDialog)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.titleLabel)
        self.titleEdit = QtGui.QLineEdit(NewDocumentDialog)
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.titleEdit)
        self.initialsLabel = QtGui.QLabel(NewDocumentDialog)
        self.initialsLabel.setObjectName(_fromUtf8("initialsLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.initialsLabel)
        self.initialsEdit = QtGui.QLineEdit(NewDocumentDialog)
        self.initialsEdit.setObjectName(_fromUtf8("initialsEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.initialsEdit)
        self.nameLabel = QtGui.QLabel(NewDocumentDialog)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(NewDocumentDialog)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.nameEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(NewDocumentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.titleLabel.setBuddy(self.titleEdit)
        self.initialsLabel.setBuddy(self.initialsEdit)
        self.nameLabel.setBuddy(self.nameEdit)

        self.retranslateUi(NewDocumentDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewDocumentDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewDocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewDocumentDialog)

    def retranslateUi(self, NewDocumentDialog):
        NewDocumentDialog.setWindowTitle(QtGui.QApplication.translate("NewDocumentDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.createDocumentLabel.setText(QtGui.QApplication.translate("NewDocumentDialog", "Criação de novo documento", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("NewDocumentDialog", "Título:", None, QtGui.QApplication.UnicodeUTF8))
        self.initialsLabel.setText(QtGui.QApplication.translate("NewDocumentDialog", "Sigla:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("NewDocumentDialog", "Nome do arquivo:", None, QtGui.QApplication.UnicodeUTF8))

