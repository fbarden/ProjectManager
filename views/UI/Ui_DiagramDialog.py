# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiagramDialog.ui'
#
# Created: Tue Jul  9 15:58:33 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DiagramDialog(object):
    def setupUi(self, DiagramDialog):
        DiagramDialog.setObjectName(_fromUtf8("DiagramDialog"))
        DiagramDialog.resize(800, 632)
        self.verticalLayout = QtGui.QVBoxLayout(DiagramDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(DiagramDialog)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(DiagramDialog)
        QtCore.QMetaObject.connectSlotsByName(DiagramDialog)

    def retranslateUi(self, DiagramDialog):
        DiagramDialog.setWindowTitle(QtGui.QApplication.translate("DiagramDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

