# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectView.ui'
#
# Created: Sun Jun 30 22:27:28 2013
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
        projectViewWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(projectViewWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(projectViewWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.documentsListWidget = QtGui.QTreeWidget(self.splitter)
        self.documentsListWidget.setObjectName(_fromUtf8("documentsListWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.documentsListWidget)
        self.graphicsView = QtGui.QGraphicsView(self.splitter)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(projectViewWidget)
        QtCore.QMetaObject.connectSlotsByName(projectViewWidget)

    def retranslateUi(self, projectViewWidget):
        projectViewWidget.setWindowTitle(QtGui.QApplication.translate("projectViewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.documentsListWidget.headerItem().setText(0, QtGui.QApplication.translate("projectViewWidget", "Documentos", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.documentsListWidget.isSortingEnabled()
        self.documentsListWidget.setSortingEnabled(False)
        self.documentsListWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("projectViewWidget", "Novo documento...", None, QtGui.QApplication.UnicodeUTF8))
        self.documentsListWidget.setSortingEnabled(__sortingEnabled)

