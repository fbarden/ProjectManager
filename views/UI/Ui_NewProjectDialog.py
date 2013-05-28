# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fbarden/Documents/ProjectManager/views/UI/NewProjectDialog.ui'
#
# Created: Tue May 28 02:22:44 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        NewProjectDialog.setObjectName(_fromUtf8("NewProjectDialog"))
        NewProjectDialog.resize(514, 119)
        self.verticalLayout_3 = QtGui.QVBoxLayout(NewProjectDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.projectNameLabel = QtGui.QLabel(NewProjectDialog)
        self.projectNameLabel.setObjectName(_fromUtf8("projectNameLabel"))
        self.horizontalLayout_2.addWidget(self.projectNameLabel)
        self.projectNameEdit = QtGui.QLineEdit(NewProjectDialog)
        self.projectNameEdit.setObjectName(_fromUtf8("projectNameEdit"))
        self.horizontalLayout_2.addWidget(self.projectNameEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.folderLabel = QtGui.QLabel(NewProjectDialog)
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.horizontalLayout.addWidget(self.folderLabel)
        self.folderEdit = QtGui.QLineEdit(NewProjectDialog)
        self.folderEdit.setObjectName(_fromUtf8("folderEdit"))
        self.horizontalLayout.addWidget(self.folderEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.searchBrowser = QtGui.QPushButton(NewProjectDialog)
        self.searchBrowser.setObjectName(_fromUtf8("searchBrowser"))
        self.verticalLayout.addWidget(self.searchBrowser)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(NewProjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(NewProjectDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewProjectDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)

    def retranslateUi(self, NewProjectDialog):
        NewProjectDialog.setWindowTitle(QtGui.QApplication.translate("NewProjectDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.projectNameLabel.setText(QtGui.QApplication.translate("NewProjectDialog", "Nome do Projeto:", None, QtGui.QApplication.UnicodeUTF8))
        self.folderLabel.setText(QtGui.QApplication.translate("NewProjectDialog", "Diretório:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBrowser.setText(QtGui.QApplication.translate("NewProjectDialog", "Procurar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewProjectDialog = QtGui.QDialog()
    ui = Ui_NewProjectDialog()
    ui.setupUi(NewProjectDialog)
    NewProjectDialog.show()
    sys.exit(app.exec_())

