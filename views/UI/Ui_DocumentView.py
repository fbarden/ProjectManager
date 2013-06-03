# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fbarden/Documents/ProjectManager/views/UI/DocumentView.ui'
#
# Created: Mon Jun  3 07:32:33 2013
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
        self.textBrowser = QtGui.QTextBrowser(documentViewWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(documentViewWidget)
        QtCore.QMetaObject.connectSlotsByName(documentViewWidget)

    def retranslateUi(self, documentViewWidget):
        documentViewWidget.setWindowTitle(QtGui.QApplication.translate("documentViewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    documentViewWidget = QtGui.QWidget()
    ui = Ui_documentViewWidget()
    ui.setupUi(documentViewWidget)
    documentViewWidget.show()
    sys.exit(app.exec_())

