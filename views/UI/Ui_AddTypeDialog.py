# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTypeDialog.ui'
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

class Ui_AddTypeDialog(object):
    def setupUi(self, AddTypeDialog):
        AddTypeDialog.setObjectName(_fromUtf8("AddTypeDialog"))
        AddTypeDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddTypeDialog.resize(536, 503)
        AddTypeDialog.setModal(True)
        self.verticalLayout_11 = QtGui.QVBoxLayout(AddTypeDialog)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
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
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(AddTypeDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_11.addWidget(self.line)
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
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkBox = QtGui.QCheckBox(AddTypeDialog)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_4.addWidget(self.checkBox)
        self.descriptionLabel = QtGui.QLabel(AddTypeDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.verticalLayout_4.addWidget(self.descriptionLabel)
        self.descriptionEdit = QtGui.QLineEdit(AddTypeDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.verticalLayout_4.addWidget(self.descriptionEdit)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.line_2 = QtGui.QFrame(AddTypeDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_11.addWidget(self.line_2)
        self.existingTypeLabel = QtGui.QLabel(AddTypeDialog)
        self.existingTypeLabel.setObjectName(_fromUtf8("existingTypeLabel"))
        self.verticalLayout_11.addWidget(self.existingTypeLabel)
        self.typeComboBox = QtGui.QComboBox(AddTypeDialog)
        self.typeComboBox.setEnabled(False)
        self.typeComboBox.setObjectName(_fromUtf8("typeComboBox"))
        self.verticalLayout_11.addWidget(self.typeComboBox)
        self.line_3 = QtGui.QFrame(AddTypeDialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_11.addWidget(self.line_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.parentChildLabel = QtGui.QLabel(AddTypeDialog)
        self.parentChildLabel.setObjectName(_fromUtf8("parentChildLabel"))
        self.verticalLayout_7.addWidget(self.parentChildLabel)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.minCardChildLabel = QtGui.QLabel(AddTypeDialog)
        self.minCardChildLabel.setObjectName(_fromUtf8("minCardChildLabel"))
        self.verticalLayout_6.addWidget(self.minCardChildLabel)
        self.minCardChildEdit = QtGui.QLineEdit(AddTypeDialog)
        self.minCardChildEdit.setObjectName(_fromUtf8("minCardChildEdit"))
        self.verticalLayout_6.addWidget(self.minCardChildEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.maxCardChildLabel = QtGui.QLabel(AddTypeDialog)
        self.maxCardChildLabel.setObjectName(_fromUtf8("maxCardChildLabel"))
        self.verticalLayout_5.addWidget(self.maxCardChildLabel)
        self.maxCardChildEdit = QtGui.QLineEdit(AddTypeDialog)
        self.maxCardChildEdit.setObjectName(_fromUtf8("maxCardChildEdit"))
        self.verticalLayout_5.addWidget(self.maxCardChildEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.childDependencyCheckBox = QtGui.QCheckBox(AddTypeDialog)
        self.childDependencyCheckBox.setObjectName(_fromUtf8("childDependencyCheckBox"))
        self.verticalLayout_7.addWidget(self.childDependencyCheckBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.line_4 = QtGui.QFrame(AddTypeDialog)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.childParentLabel = QtGui.QLabel(AddTypeDialog)
        self.childParentLabel.setObjectName(_fromUtf8("childParentLabel"))
        self.verticalLayout_8.addWidget(self.childParentLabel)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.minCardParentLabel = QtGui.QLabel(AddTypeDialog)
        self.minCardParentLabel.setObjectName(_fromUtf8("minCardParentLabel"))
        self.verticalLayout_9.addWidget(self.minCardParentLabel)
        self.minCardParentEdit = QtGui.QLineEdit(AddTypeDialog)
        self.minCardParentEdit.setObjectName(_fromUtf8("minCardParentEdit"))
        self.verticalLayout_9.addWidget(self.minCardParentEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.maxCardParentLabel = QtGui.QLabel(AddTypeDialog)
        self.maxCardParentLabel.setObjectName(_fromUtf8("maxCardParentLabel"))
        self.verticalLayout_10.addWidget(self.maxCardParentLabel)
        self.maxCardParentEdit = QtGui.QLineEdit(AddTypeDialog)
        self.maxCardParentEdit.setObjectName(_fromUtf8("maxCardParentEdit"))
        self.verticalLayout_10.addWidget(self.maxCardParentEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.parentDependencyCheckBox = QtGui.QCheckBox(AddTypeDialog)
        self.parentDependencyCheckBox.setObjectName(_fromUtf8("parentDependencyCheckBox"))
        self.verticalLayout_8.addWidget(self.parentDependencyCheckBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(AddTypeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_11.addWidget(self.buttonBox)

        self.retranslateUi(AddTypeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddTypeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddTypeDialog.reject)
        QtCore.QObject.connect(self.newTypeButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.newTypeEdit.setEnabled)
        QtCore.QObject.connect(self.newTypeButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.prefixEdit.setEnabled)
        QtCore.QObject.connect(self.newTypeButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.descriptionEdit.setEnabled)
        QtCore.QObject.connect(self.existingTypeButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.typeComboBox.setEnabled)
        QtCore.QObject.connect(self.newTypeButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(AddTypeDialog)
        AddTypeDialog.setTabOrder(self.newTypeButton, self.existingTypeButton)
        AddTypeDialog.setTabOrder(self.existingTypeButton, self.newTypeEdit)
        AddTypeDialog.setTabOrder(self.newTypeEdit, self.prefixEdit)
        AddTypeDialog.setTabOrder(self.prefixEdit, self.descriptionEdit)
        AddTypeDialog.setTabOrder(self.descriptionEdit, self.typeComboBox)
        AddTypeDialog.setTabOrder(self.typeComboBox, self.minCardChildEdit)
        AddTypeDialog.setTabOrder(self.minCardChildEdit, self.maxCardChildEdit)
        AddTypeDialog.setTabOrder(self.maxCardChildEdit, self.childDependencyCheckBox)
        AddTypeDialog.setTabOrder(self.childDependencyCheckBox, self.minCardParentEdit)
        AddTypeDialog.setTabOrder(self.minCardParentEdit, self.maxCardParentEdit)
        AddTypeDialog.setTabOrder(self.maxCardParentEdit, self.parentDependencyCheckBox)
        AddTypeDialog.setTabOrder(self.parentDependencyCheckBox, self.buttonBox)

    def retranslateUi(self, AddTypeDialog):
        AddTypeDialog.setWindowTitle(QtGui.QApplication.translate("AddTypeDialog", "Seleção de tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.newTypeButton.setText(QtGui.QApplication.translate("AddTypeDialog", "Criar novo tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.existingTypeButton.setText(QtGui.QApplication.translate("AddTypeDialog", "Selecionar tipo existente", None, QtGui.QApplication.UnicodeUTF8))
        self.newTypeLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Nome do tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefixLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Prefixo:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("AddTypeDialog", "Recursivo?", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.existingTypeLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Selecione tipo existente:", None, QtGui.QApplication.UnicodeUTF8))
        self.parentChildLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Pai -> Filho", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardChildLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Nº mínimo de filhos", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardChildEdit.setText(QtGui.QApplication.translate("AddTypeDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardChildLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Nº máximo de filhos", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardChildEdit.setText(QtGui.QApplication.translate("AddTypeDialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.childDependencyCheckBox.setText(QtGui.QApplication.translate("AddTypeDialog", "Filho é dependente?", None, QtGui.QApplication.UnicodeUTF8))
        self.childParentLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Filho -> Pai", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardParentLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Nº mínimo de pais", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardParentEdit.setText(QtGui.QApplication.translate("AddTypeDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardParentLabel.setText(QtGui.QApplication.translate("AddTypeDialog", "Nº máximo de pais", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardParentEdit.setText(QtGui.QApplication.translate("AddTypeDialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.parentDependencyCheckBox.setText(QtGui.QApplication.translate("AddTypeDialog", "Pai é dependente?", None, QtGui.QApplication.UnicodeUTF8))

