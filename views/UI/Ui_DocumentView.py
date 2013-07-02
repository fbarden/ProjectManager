# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocumentView.ui'
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

class Ui_documentViewWidget(object):
    def setupUi(self, documentViewWidget):
        documentViewWidget.setObjectName(_fromUtf8("documentViewWidget"))
        documentViewWidget.resize(610, 580)
        self.verticalLayout = QtGui.QVBoxLayout(documentViewWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.showLinksButton = QtGui.QPushButton(documentViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showLinksButton.sizePolicy().hasHeightForWidth())
        self.showLinksButton.setSizePolicy(sizePolicy)
        self.showLinksButton.setCheckable(True)
        self.showLinksButton.setChecked(True)
        self.showLinksButton.setObjectName(_fromUtf8("showLinksButton"))
        self.horizontalLayout.addWidget(self.showLinksButton)
        self.titleLabel = QtGui.QLabel(documentViewWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.horizontalLayout.addWidget(self.titleLabel)
        self.upButton = QtGui.QToolButton(documentViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMaximumSize(QtCore.QSize(50, 50))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.horizontalLayout.addWidget(self.upButton)
        self.titleButton = QtGui.QPushButton(documentViewWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleButton.sizePolicy().hasHeightForWidth())
        self.titleButton.setSizePolicy(sizePolicy)
        self.titleButton.setObjectName(_fromUtf8("titleButton"))
        self.horizontalLayout.addWidget(self.titleButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtGui.QTextBrowser(documentViewWidget)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(documentViewWidget)
        QtCore.QMetaObject.connectSlotsByName(documentViewWidget)

    def retranslateUi(self, documentViewWidget):
        documentViewWidget.setWindowTitle(QtGui.QApplication.translate("documentViewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.showLinksButton.setText(QtGui.QApplication.translate("documentViewWidget", "Links", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("documentViewWidget", "Document Title", None, QtGui.QApplication.UnicodeUTF8))
        self.upButton.setText(QtGui.QApplication.translate("documentViewWidget", "î", None, QtGui.QApplication.UnicodeUTF8))
        self.titleButton.setText(QtGui.QApplication.translate("documentViewWidget", "Alt. Título", None, QtGui.QApplication.UnicodeUTF8))

