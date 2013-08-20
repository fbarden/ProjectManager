# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditLinkDialog.ui'
#
# Created: Mon Aug 19 03:27:47 2013
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
        self.linksView = QtGui.QTreeView(EditLinksDialog)
        self.linksView.setObjectName(_fromUtf8("linksView"))
        self.verticalLayout.addWidget(self.linksView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton = QtGui.QToolButton(EditLinksDialog)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(EditLinksDialog)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(EditLinksDialog)
        QtCore.QMetaObject.connectSlotsByName(EditLinksDialog)

    def retranslateUi(self, EditLinksDialog):
        EditLinksDialog.setWindowTitle(QtGui.QApplication.translate("EditLinksDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("EditLinksDialog", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("EditLinksDialog", "Remover", None, QtGui.QApplication.UnicodeUTF8))

