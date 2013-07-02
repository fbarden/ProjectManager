# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(965, 643)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        self.menuDocumento = QtGui.QMenu(self.menubar)
        self.menuDocumento.setObjectName(_fromUtf8("menuDocumento"))
        self.menuCl_usula = QtGui.QMenu(self.menubar)
        self.menuCl_usula.setObjectName(_fromUtf8("menuCl_usula"))
        self.menuImportedFiles = QtGui.QMenu(self.menubar)
        self.menuImportedFiles.setObjectName(_fromUtf8("menuImportedFiles"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewProject = QtGui.QAction(MainWindow)
        self.actionNewProject.setObjectName(_fromUtf8("actionNewProject"))
        self.actionOpenProject = QtGui.QAction(MainWindow)
        self.actionOpenProject.setObjectName(_fromUtf8("actionOpenProject"))
        self.actionSaveProject = QtGui.QAction(MainWindow)
        self.actionSaveProject.setObjectName(_fromUtf8("actionSaveProject"))
        self.actionSaveProject_as = QtGui.QAction(MainWindow)
        self.actionSaveProject_as.setObjectName(_fromUtf8("actionSaveProject_as"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionManageFiles = QtGui.QAction(MainWindow)
        self.actionManageFiles.setObjectName(_fromUtf8("actionManageFiles"))
        self.actionEditTIM = QtGui.QAction(MainWindow)
        self.actionEditTIM.setObjectName(_fromUtf8("actionEditTIM"))
        self.actionTIMDiagram = QtGui.QAction(MainWindow)
        self.actionTIMDiagram.setObjectName(_fromUtf8("actionTIMDiagram"))
        self.menuProject.addAction(self.actionNewProject)
        self.menuProject.addAction(self.actionOpenProject)
        self.menuProject.addAction(self.actionSaveProject)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionEditTIM)
        self.menuProject.addAction(self.actionTIMDiagram)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuImportedFiles.addAction(self.actionManageFiles)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuDocumento.menuAction())
        self.menubar.addAction(self.menuCl_usula.menuAction())
        self.menubar.addAction(self.menuImportedFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProject.setTitle(QtGui.QApplication.translate("MainWindow", "Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDocumento.setTitle(QtGui.QApplication.translate("MainWindow", "Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCl_usula.setTitle(QtGui.QApplication.translate("MainWindow", "Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImportedFiles.setTitle(QtGui.QApplication.translate("MainWindow", "Arq. Importados", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject.setText(QtGui.QApplication.translate("MainWindow", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject_as.setText(QtGui.QApplication.translate("MainWindow", "Salvar como...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManageFiles.setText(QtGui.QApplication.translate("MainWindow", "Gerenciar arquivos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditTIM.setText(QtGui.QApplication.translate("MainWindow", "Editar TIM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTIMDiagram.setText(QtGui.QApplication.translate("MainWindow", "Diagrama TIM", None, QtGui.QApplication.UnicodeUTF8))

