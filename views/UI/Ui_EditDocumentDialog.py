# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditDocumentDialog.ui'
#
# Created: Wed Aug 14 09:50:25 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditDocumentDialog(object):
    def setupUi(self, EditDocumentDialog):
        EditDocumentDialog.setObjectName(_fromUtf8("EditDocumentDialog"))
        EditDocumentDialog.resize(400, 173)
        self.verticalLayout = QtGui.QVBoxLayout(EditDocumentDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.propertiesLabel = QtGui.QLabel(EditDocumentDialog)
        self.propertiesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.propertiesLabel.setObjectName(_fromUtf8("propertiesLabel"))
        self.verticalLayout.addWidget(self.propertiesLabel)
        self.line = QtGui.QFrame(EditDocumentDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.titleLabel = QtGui.QLabel(EditDocumentDialog)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.titleLabel)
        self.titleEdit = QtGui.QLineEdit(EditDocumentDialog)
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.titleEdit)
        self.prefixLabel = QtGui.QLabel(EditDocumentDialog)
        self.prefixLabel.setObjectName(_fromUtf8("prefixLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.prefixLabel)
        self.prefixEdit = QtGui.QLineEdit(EditDocumentDialog)
        self.prefixEdit.setObjectName(_fromUtf8("prefixEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.prefixEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(EditDocumentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditDocumentDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditDocumentDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditDocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditDocumentDialog)

    def retranslateUi(self, EditDocumentDialog):
        EditDocumentDialog.setWindowTitle(QtGui.QApplication.translate("EditDocumentDialog", "Propriedades", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesLabel.setText(QtGui.QApplication.translate("EditDocumentDialog", "Propriedades:", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("EditDocumentDialog", "Título:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefixLabel.setText(QtGui.QApplication.translate("EditDocumentDialog", "Prefixo:", None, QtGui.QApplication.UnicodeUTF8))

