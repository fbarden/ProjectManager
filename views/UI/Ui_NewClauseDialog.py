# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewClauseDialog.ui'
#
# Created: Mon Aug  5 09:43:44 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewClauseDialog(object):
    def setupUi(self, NewClauseDialog):
        NewClauseDialog.setObjectName(_fromUtf8("NewClauseDialog"))
        NewClauseDialog.resize(400, 202)
        self.verticalLayout = QtGui.QVBoxLayout(NewClauseDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newClauseLabel = QtGui.QLabel(NewClauseDialog)
        self.newClauseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newClauseLabel.setObjectName(_fromUtf8("newClauseLabel"))
        self.verticalLayout.addWidget(self.newClauseLabel)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.titleLabel = QtGui.QLabel(NewClauseDialog)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.titleLabel)
        self.titleEdit = QtGui.QLineEdit(NewClauseDialog)
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.titleEdit)
        self.documentLabel = QtGui.QLabel(NewClauseDialog)
        self.documentLabel.setObjectName(_fromUtf8("documentLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.documentLabel)
        self.typeLabel = QtGui.QLabel(NewClauseDialog)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.typeLabel)
        self.parentLabel = QtGui.QLabel(NewClauseDialog)
        self.parentLabel.setObjectName(_fromUtf8("parentLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.parentLabel)
        self.parentBox = QtGui.QComboBox(NewClauseDialog)
        self.parentBox.setObjectName(_fromUtf8("parentBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.parentBox)
        self.documentBox = QtGui.QComboBox(NewClauseDialog)
        self.documentBox.setObjectName(_fromUtf8("documentBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.documentBox)
        self.typeBox = QtGui.QComboBox(NewClauseDialog)
        self.typeBox.setObjectName(_fromUtf8("typeBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.typeBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(NewClauseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewClauseDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewClauseDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewClauseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewClauseDialog)

    def retranslateUi(self, NewClauseDialog):
        NewClauseDialog.setWindowTitle(QtGui.QApplication.translate("NewClauseDialog", "Nova Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.newClauseLabel.setText(QtGui.QApplication.translate("NewClauseDialog", "Nova Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("NewClauseDialog", "Título", None, QtGui.QApplication.UnicodeUTF8))
        self.documentLabel.setText(QtGui.QApplication.translate("NewClauseDialog", "Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.typeLabel.setText(QtGui.QApplication.translate("NewClauseDialog", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.parentLabel.setText(QtGui.QApplication.translate("NewClauseDialog", "Cláusula Pai:", None, QtGui.QApplication.UnicodeUTF8))

