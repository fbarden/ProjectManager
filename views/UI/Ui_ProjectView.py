# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectView.ui'
#
# Created: Wed Jul 24 03:11:24 2013
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
        projectViewWidget.resize(400, 366)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(projectViewWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.documentsListWidget = QtGui.QTreeWidget(projectViewWidget)
        self.documentsListWidget.setObjectName(_fromUtf8("documentsListWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.documentsListWidget)
        self.verticalLayout.addWidget(self.documentsListWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton = QtGui.QToolButton(projectViewWidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
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
        self.documentsListWidget.headerItem().setText(0, QtGui.QApplication.translate("projectViewWidget", "Documentos", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.documentsListWidget.isSortingEnabled()
        self.documentsListWidget.setSortingEnabled(False)
        self.documentsListWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("projectViewWidget", "Novo documento...", None, QtGui.QApplication.UnicodeUTF8))
        self.documentsListWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(QtGui.QApplication.translate("projectViewWidget", "Voltar ao Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.moveUpButton.setText(QtGui.QApplication.translate("projectViewWidget", "↑", None, QtGui.QApplication.UnicodeUTF8))
        self.moveDownButton.setText(QtGui.QApplication.translate("projectViewWidget", "↓", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("projectViewWidget", "X", None, QtGui.QApplication.UnicodeUTF8))

