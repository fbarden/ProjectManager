# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditImportedFilesDialog.ui'
#
# Created: Sun Jul 28 02:41:54 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditImportedFilesDialog(object):
    def setupUi(self, EditImportedFilesDialog):
        EditImportedFilesDialog.setObjectName(_fromUtf8("EditImportedFilesDialog"))
        EditImportedFilesDialog.resize(525, 443)
        self.verticalLayout = QtGui.QVBoxLayout(EditImportedFilesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.editImportedFilesLabel = QtGui.QLabel(EditImportedFilesDialog)
        self.editImportedFilesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editImportedFilesLabel.setObjectName(_fromUtf8("editImportedFilesLabel"))
        self.verticalLayout.addWidget(self.editImportedFilesLabel)
        self.filesTree = QtGui.QTreeWidget(EditImportedFilesDialog)
        self.filesTree.setObjectName(_fromUtf8("filesTree"))
        item_0 = QtGui.QTreeWidgetItem(self.filesTree)
        self.verticalLayout.addWidget(self.filesTree)
        self.buttonBox = QtGui.QDialogButtonBox(EditImportedFilesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditImportedFilesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditImportedFilesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditImportedFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditImportedFilesDialog)

    def retranslateUi(self, EditImportedFilesDialog):
        EditImportedFilesDialog.setWindowTitle(QtGui.QApplication.translate("EditImportedFilesDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.editImportedFilesLabel.setText(QtGui.QApplication.translate("EditImportedFilesDialog", "Gerenciar arquivos importados:", None, QtGui.QApplication.UnicodeUTF8))
        self.filesTree.headerItem().setText(0, QtGui.QApplication.translate("EditImportedFilesDialog", "Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.filesTree.headerItem().setText(1, QtGui.QApplication.translate("EditImportedFilesDialog", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.filesTree.isSortingEnabled()
        self.filesTree.setSortingEnabled(False)
        self.filesTree.topLevelItem(0).setText(1, QtGui.QApplication.translate("EditImportedFilesDialog", "Importar novo arquivo...", None, QtGui.QApplication.UnicodeUTF8))
        self.filesTree.setSortingEnabled(__sortingEnabled)

