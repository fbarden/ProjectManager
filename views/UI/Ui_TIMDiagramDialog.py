# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TIMDiagramDialog.ui'
#
# Created: Sun Jun 30 22:27:29 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TIMDiagramDialog(object):
    def setupUi(self, TIMDiagramDialog):
        TIMDiagramDialog.setObjectName(_fromUtf8("TIMDiagramDialog"))
        TIMDiagramDialog.resize(800, 632)
        self.verticalLayout = QtGui.QVBoxLayout(TIMDiagramDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(TIMDiagramDialog)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(TIMDiagramDialog)
        QtCore.QMetaObject.connectSlotsByName(TIMDiagramDialog)

    def retranslateUi(self, TIMDiagramDialog):
        TIMDiagramDialog.setWindowTitle(QtGui.QApplication.translate("TIMDiagramDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

