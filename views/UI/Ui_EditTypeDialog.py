# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTypeDialog.ui'
#
# Created: Mon Aug  5 09:43:43 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditTypeDialog(object):
    def setupUi(self, EditTypeDialog):
        EditTypeDialog.setObjectName(_fromUtf8("EditTypeDialog"))
        EditTypeDialog.resize(400, 395)
        self.verticalLayout_21 = QtGui.QVBoxLayout(EditTypeDialog)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.nameLabel = QtGui.QLabel(EditTypeDialog)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.verticalLayout_19.addWidget(self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(EditTypeDialog)
        self.nameEdit.setEnabled(True)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.verticalLayout_19.addWidget(self.nameEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.prefixLabel = QtGui.QLabel(EditTypeDialog)
        self.prefixLabel.setObjectName(_fromUtf8("prefixLabel"))
        self.verticalLayout_20.addWidget(self.prefixLabel)
        self.prefixEdit = QtGui.QLineEdit(EditTypeDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefixEdit.sizePolicy().hasHeightForWidth())
        self.prefixEdit.setSizePolicy(sizePolicy)
        self.prefixEdit.setObjectName(_fromUtf8("prefixEdit"))
        self.verticalLayout_20.addWidget(self.prefixEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_20)
        self.verticalLayout_21.addLayout(self.horizontalLayout_4)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.checkBox = QtGui.QCheckBox(EditTypeDialog)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_18.addWidget(self.checkBox)
        self.descriptionLabel = QtGui.QLabel(EditTypeDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.verticalLayout_18.addWidget(self.descriptionLabel)
        self.descriptionEdit = QtGui.QLineEdit(EditTypeDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.verticalLayout_18.addWidget(self.descriptionEdit)
        self.verticalLayout_21.addLayout(self.verticalLayout_18)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.parentChildLabel = QtGui.QLabel(EditTypeDialog)
        self.parentChildLabel.setObjectName(_fromUtf8("parentChildLabel"))
        self.verticalLayout_11.addWidget(self.parentChildLabel)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.minCardChildLabel = QtGui.QLabel(EditTypeDialog)
        self.minCardChildLabel.setObjectName(_fromUtf8("minCardChildLabel"))
        self.verticalLayout_12.addWidget(self.minCardChildLabel)
        self.minCardChildEdit = QtGui.QLineEdit(EditTypeDialog)
        self.minCardChildEdit.setObjectName(_fromUtf8("minCardChildEdit"))
        self.verticalLayout_12.addWidget(self.minCardChildEdit)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.maxCardChildLabel = QtGui.QLabel(EditTypeDialog)
        self.maxCardChildLabel.setObjectName(_fromUtf8("maxCardChildLabel"))
        self.verticalLayout_13.addWidget(self.maxCardChildLabel)
        self.maxCardChildEdit = QtGui.QLineEdit(EditTypeDialog)
        self.maxCardChildEdit.setObjectName(_fromUtf8("maxCardChildEdit"))
        self.verticalLayout_13.addWidget(self.maxCardChildEdit)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        self.childDependencyCheckBox = QtGui.QCheckBox(EditTypeDialog)
        self.childDependencyCheckBox.setObjectName(_fromUtf8("childDependencyCheckBox"))
        self.verticalLayout_11.addWidget(self.childDependencyCheckBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.line_5 = QtGui.QFrame(EditTypeDialog)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_3.addWidget(self.line_5)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.childParentLabel = QtGui.QLabel(EditTypeDialog)
        self.childParentLabel.setObjectName(_fromUtf8("childParentLabel"))
        self.verticalLayout_14.addWidget(self.childParentLabel)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.minCardParentLabel = QtGui.QLabel(EditTypeDialog)
        self.minCardParentLabel.setObjectName(_fromUtf8("minCardParentLabel"))
        self.verticalLayout_15.addWidget(self.minCardParentLabel)
        self.minCardParentEdit = QtGui.QLineEdit(EditTypeDialog)
        self.minCardParentEdit.setObjectName(_fromUtf8("minCardParentEdit"))
        self.verticalLayout_15.addWidget(self.minCardParentEdit)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.maxCardParentLabel = QtGui.QLabel(EditTypeDialog)
        self.maxCardParentLabel.setObjectName(_fromUtf8("maxCardParentLabel"))
        self.verticalLayout_16.addWidget(self.maxCardParentLabel)
        self.maxCardParentEdit = QtGui.QLineEdit(EditTypeDialog)
        self.maxCardParentEdit.setObjectName(_fromUtf8("maxCardParentEdit"))
        self.verticalLayout_16.addWidget(self.maxCardParentEdit)
        self.verticalLayout_14.addLayout(self.verticalLayout_16)
        self.parentDependencyCheckBox = QtGui.QCheckBox(EditTypeDialog)
        self.parentDependencyCheckBox.setObjectName(_fromUtf8("parentDependencyCheckBox"))
        self.verticalLayout_14.addWidget(self.parentDependencyCheckBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)
        self.verticalLayout_21.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(EditTypeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_21.addWidget(self.buttonBox)

        self.retranslateUi(EditTypeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditTypeDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditTypeDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(EditTypeDialog)

    def retranslateUi(self, EditTypeDialog):
        EditTypeDialog.setWindowTitle(QtGui.QApplication.translate("EditTypeDialog", "Editar TIM", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Nome do tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefixLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Prefixo:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("EditTypeDialog", "Recursivo?", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.parentChildLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Pai -> Filho", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardChildLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Nº mínimo de filhos", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardChildEdit.setText(QtGui.QApplication.translate("EditTypeDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardChildLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Nº máximo de filhos", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardChildEdit.setText(QtGui.QApplication.translate("EditTypeDialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.childDependencyCheckBox.setText(QtGui.QApplication.translate("EditTypeDialog", "Filho é dependente?", None, QtGui.QApplication.UnicodeUTF8))
        self.childParentLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Filho -> Pai", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardParentLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Nº mínimo de pais", None, QtGui.QApplication.UnicodeUTF8))
        self.minCardParentEdit.setText(QtGui.QApplication.translate("EditTypeDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardParentLabel.setText(QtGui.QApplication.translate("EditTypeDialog", "Nº máximo de pais", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCardParentEdit.setText(QtGui.QApplication.translate("EditTypeDialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.parentDependencyCheckBox.setText(QtGui.QApplication.translate("EditTypeDialog", "Pai é dependente?", None, QtGui.QApplication.UnicodeUTF8))

