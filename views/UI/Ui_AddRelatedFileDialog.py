# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddRelatedFileDialog.ui'
#
# Created: Sun Jun 30 15:21:25 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddRelatedFileDialog(object):
    def setupUi(self, AddRelatedFileDialog):
        AddRelatedFileDialog.setObjectName(_fromUtf8("AddRelatedFileDialog"))
        AddRelatedFileDialog.resize(530, 509)
        self.verticalLayout = QtGui.QVBoxLayout(AddRelatedFileDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.titleLabel = QtGui.QLabel(AddRelatedFileDialog)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.verticalLayout.addWidget(self.titleLabel)
        self.filesTreeWidget = QtGui.QTreeWidget(AddRelatedFileDialog)
        self.filesTreeWidget.setObjectName(_fromUtf8("filesTreeWidget"))
        self.verticalLayout.addWidget(self.filesTreeWidget)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.observationLabel = QtGui.QLabel(AddRelatedFileDialog)
        self.observationLabel.setObjectName(_fromUtf8("observationLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.observationLabel)
        self.observationEdit = QtGui.QLineEdit(AddRelatedFileDialog)
        self.observationEdit.setObjectName(_fromUtf8("observationEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.observationEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddRelatedFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddRelatedFileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddRelatedFileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddRelatedFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddRelatedFileDialog)

    def retranslateUi(self, AddRelatedFileDialog):
        AddRelatedFileDialog.setWindowTitle(QtGui.QApplication.translate("AddRelatedFileDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("AddRelatedFileDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.filesTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("AddRelatedFileDialog", "Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.filesTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("AddRelatedFileDialog", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        self.observationLabel.setText(QtGui.QApplication.translate("AddRelatedFileDialog", "Observação:", None, QtGui.QApplication.UnicodeUTF8))

