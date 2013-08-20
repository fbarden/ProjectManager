# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditLinksDialog.ui'
#
# Created: Tue Aug 20 00:07:16 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditLinksDialog(object):
    def setupUi(self, EditLinksDialog):
        EditLinksDialog.setObjectName(_fromUtf8("EditLinksDialog"))
        EditLinksDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(EditLinksDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addLinkButton = QtGui.QToolButton(EditLinksDialog)
        self.addLinkButton.setObjectName(_fromUtf8("addLinkButton"))
        self.horizontalLayout.addWidget(self.addLinkButton)
        self.removeLinkButton = QtGui.QToolButton(EditLinksDialog)
        self.removeLinkButton.setObjectName(_fromUtf8("removeLinkButton"))
        self.horizontalLayout.addWidget(self.removeLinkButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.linksView = QtGui.QTreeView(EditLinksDialog)
        self.linksView.setObjectName(_fromUtf8("linksView"))
        self.verticalLayout.addWidget(self.linksView)
        self.buttonBox = QtGui.QDialogButtonBox(EditLinksDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditLinksDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditLinksDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditLinksDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditLinksDialog)

    def retranslateUi(self, EditLinksDialog):
        EditLinksDialog.setWindowTitle(QtGui.QApplication.translate("EditLinksDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.addLinkButton.setText(QtGui.QApplication.translate("EditLinksDialog", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.removeLinkButton.setText(QtGui.QApplication.translate("EditLinksDialog", "Remover", None, QtGui.QApplication.UnicodeUTF8))

