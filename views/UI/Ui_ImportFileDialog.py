# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportFileDialog.ui'
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

class Ui_ImportFileDialog(object):
    def setupUi(self, ImportFileDialog):
        ImportFileDialog.setObjectName(_fromUtf8("ImportFileDialog"))
        ImportFileDialog.resize(400, 180)
        self.verticalLayout = QtGui.QVBoxLayout(ImportFileDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.importLabel = QtGui.QLabel(ImportFileDialog)
        self.importLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.importLabel.setObjectName(_fromUtf8("importLabel"))
        self.verticalLayout.addWidget(self.importLabel)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.fileLabel = QtGui.QLabel(ImportFileDialog)
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.fileLabel)
        self.fileEdit = QtGui.QLineEdit(ImportFileDialog)
        self.fileEdit.setObjectName(_fromUtf8("fileEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fileEdit)
        self.descriptionLabel = QtGui.QLabel(ImportFileDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionEdit = QtGui.QLineEdit(ImportFileDialog)
        self.descriptionEdit.setObjectName(_fromUtf8("descriptionEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.descriptionEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchButton = QtGui.QPushButton(ImportFileDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ImportFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.fileLabel.setBuddy(self.fileEdit)
        self.descriptionLabel.setBuddy(self.descriptionEdit)

        self.retranslateUi(ImportFileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportFileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportFileDialog)

    def retranslateUi(self, ImportFileDialog):
        ImportFileDialog.setWindowTitle(QtGui.QApplication.translate("ImportFileDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.importLabel.setText(QtGui.QApplication.translate("ImportFileDialog", "Importar Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLabel.setText(QtGui.QApplication.translate("ImportFileDialog", "Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("ImportFileDialog", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("ImportFileDialog", "Procurar", None, QtGui.QApplication.UnicodeUTF8))

