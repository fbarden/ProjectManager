# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectView.ui'
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

class Ui_projectViewWidget(object):
    def setupUi(self, projectViewWidget):
        projectViewWidget.setObjectName(_fromUtf8("projectViewWidget"))
        projectViewWidget.resize(464, 366)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(projectViewWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.documentsListWidget = QtGui.QTreeView(projectViewWidget)
        self.documentsListWidget.setObjectName(_fromUtf8("documentsListWidget"))
        self.verticalLayout.addWidget(self.documentsListWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newDocumentButton = QtGui.QToolButton(projectViewWidget)
        self.newDocumentButton.setObjectName(_fromUtf8("newDocumentButton"))
        self.horizontalLayout.addWidget(self.newDocumentButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.moveUpButton = QtGui.QToolButton(projectViewWidget)
        self.moveUpButton.setObjectName(_fromUtf8("moveUpButton"))
        self.horizontalLayout.addWidget(self.moveUpButton)
        self.moveDownButton = QtGui.QToolButton(projectViewWidget)
        self.moveDownButton.setObjectName(_fromUtf8("moveDownButton"))
        self.horizontalLayout.addWidget(self.moveDownButton)
        self.deleteButton = QtGui.QToolButton(projectViewWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.graphicsView = QtGui.QGraphicsView(projectViewWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_2.addWidget(self.graphicsView)

        self.retranslateUi(projectViewWidget)
        QtCore.QMetaObject.connectSlotsByName(projectViewWidget)

    def retranslateUi(self, projectViewWidget):
        projectViewWidget.setWindowTitle(QtGui.QApplication.translate("projectViewWidget", "Visualização de Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.newDocumentButton.setText(QtGui.QApplication.translate("projectViewWidget", "Novo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.moveUpButton.setText(QtGui.QApplication.translate("projectViewWidget", "↑", None, QtGui.QApplication.UnicodeUTF8))
        self.moveDownButton.setText(QtGui.QApplication.translate("projectViewWidget", "↓", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("projectViewWidget", "X", None, QtGui.QApplication.UnicodeUTF8))

