# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTypeDialog.ui'
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

class Ui_AddTypeDialog(object):
    def setupUi(self, AddTypeDialog):
        AddTypeDialog.setObjectName(_fromUtf8("AddTypeDialog"))
        AddTypeDialog.resize(400, 300)
        AddTypeDialog.setModal(True)
        self.verticalLayout_5 = QtGui.QVBoxLayout(AddTypeDialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newTypeButton = QtGui.QRadioButton(AddTypeDialog)
        self.newTypeButton.setChecked(True)
        self.newTypeButton.setObjectName(_fromUtf8("newTypeButton"))
        self.verticalLayout.addWidget(self.newTypeButton)
        self.existingTypeButton = QtGui.QRadioButton(AddTypeDialog)
        self.existingTypeButton.setChecked(False)
        self.existingTypeButton.setObjectName(_fromUtf8("existingTypeButton"))
        self.verticalLayout.addWidget(self.existingTypeButton)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(AddTypeDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.newTypeLabel = QtGui.QLabel(AddTypeDialog)
        self.newTypeLabel.setObjectName(_fromUtf8("newTypeLabel"))
        self.verticalLayout_2.addWidget(self.newTypeLabel)
        self.newTypeEdit = QtGui.QLineEdit(AddTypeDialog)
        self.newTypeEdit.setEnabled(True)
        self.newTypeEdit.setObjectName(_fromUtf8("newTypeEdit"))
        self.verticalLayout_2.addWidget(self.newTypeEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.prefixLabel = QtGui.QLabel(AddTypeDialog)
        self.prefixLabel.setObjectName(_fromUtf8("prefixLabel"))
        self.verticalLayout_3.addWidget(self.prefixLabel)
        self.prefixEdit = QtGui.QLineEdit(AddTypeDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefixEdit.sizePolicy().hasHeightForWidth())
        self.prefixEdit.setSizePolicy(sizePolicy)
        self.prefixEdit.setObjectName(_fromUtf8("prefixEdit"))
        self.verticalLayout_3.addWidget(self.prefixEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.descriptionLabel = QtGui.QLabel(AddTypeDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.verticalLayout_4.addWidget(self.descriptionLabel)
        self.descriptionEdit = QtGui.QLineEdit(AddTypeDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.verticalLayout_4.addWidget(self.descriptionEdit)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.line_2 = QtGui.QFrame(AddTypeDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_5.addWidget(self.line_2)
        self.existingTypeLabel = QtGui.QLabel(AddTypeDialog)
        self.existingTypeLabel.setObjectName(_fromUtf8("existingTypeLabel"))
        self.verticalLayout_5.addWidget(self.existingTypeLabel)
        self.typeComboBox = QtGui.QComboBox(AddTypeDialog)
        self.typeComboBox.setEnabled(False)
        self.typeComboBox.setObjectName(_fromUtf8("typeComboBox"))
        self.verticalLayout_5.addWidget(self.typeComboBox)
        self.buttonBox = QtGui.QDialogButtonBox(AddTypeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(AddTypeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddTypeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddTypeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTypeDialog)
        AddTypeDialog.setTabOrder(self.newTypeButton, self.existingTypeButton)
        AddTypeDialog.setTabOrder(self.existingTypeButton, self.newTypeEdit)
        AddTypeDialog.setTabOrder(self.newTypeEdit, self.typeComboBox)
        AddTypeDialog.setTabOrder(self.typeComboBox, self.buttonBox)

    def retranslateUi(self, AddTypeDialog):
        AddTypeDialog.setWindowTitle(QtGui.QApplication.translate("AddTypeDialog", "Seleção de tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.newTypeButton.setText(QtGui.QApplication.translate("AddTypeDialog", "Criar novo tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.existingTypeButton.setText(QtGui.QApplication.translate("AddTypeDialog", "Selecionar tipo existente", None, QtGui.QApplication.UnicodeUTF8))
        self.newTypeLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Nome do tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefixLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Prefixo:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.existingTypeLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Selecione tipo existente:", None, QtGui.QApplication.UnicodeUTF8))

