# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Aug 14 09:50:26 2013
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
        self.menuDocuments = QtGui.QMenu(self.menubar)
        self.menuDocuments.setObjectName(_fromUtf8("menuDocuments"))
        self.menuClauses = QtGui.QMenu(self.menubar)
        self.menuClauses.setObjectName(_fromUtf8("menuClauses"))
        self.menuConsolidation = QtGui.QMenu(self.menubar)
        self.menuConsolidation.setObjectName(_fromUtf8("menuConsolidation"))
        self.menuVerifications = QtGui.QMenu(self.menubar)
        self.menuVerifications.setObjectName(_fromUtf8("menuVerifications"))
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
        self.actionNewDocument = QtGui.QAction(MainWindow)
        self.actionNewDocument.setEnabled(False)
        self.actionNewDocument.setObjectName(_fromUtf8("actionNewDocument"))
        self.actionNewClause = QtGui.QAction(MainWindow)
        self.actionNewClause.setEnabled(False)
        self.actionNewClause.setObjectName(_fromUtf8("actionNewClause"))
        self.actionCheckSpaces = QtGui.QAction(MainWindow)
        self.actionCheckSpaces.setObjectName(_fromUtf8("actionCheckSpaces"))
        self.actionCheckGranularity = QtGui.QAction(MainWindow)
        self.actionCheckGranularity.setObjectName(_fromUtf8("actionCheckGranularity"))
        self.actionSuspectClauses = QtGui.QAction(MainWindow)
        self.actionSuspectClauses.setObjectName(_fromUtf8("actionSuspectClauses"))
        self.actionRedundantPaths = QtGui.QAction(MainWindow)
        self.actionRedundantPaths.setObjectName(_fromUtf8("actionRedundantPaths"))
        self.actionPathDiagram = QtGui.QAction(MainWindow)
        self.actionPathDiagram.setObjectName(_fromUtf8("actionPathDiagram"))
        self.actionTotalDiagram = QtGui.QAction(MainWindow)
        self.actionTotalDiagram.setObjectName(_fromUtf8("actionTotalDiagram"))
        self.actionProjectConsolidation = QtGui.QAction(MainWindow)
        self.actionProjectConsolidation.setObjectName(_fromUtf8("actionProjectConsolidation"))
        self.actionIndexHistory = QtGui.QAction(MainWindow)
        self.actionIndexHistory.setObjectName(_fromUtf8("actionIndexHistory"))
        self.actionUpdateConsolidation = QtGui.QAction(MainWindow)
        self.actionUpdateConsolidation.setEnabled(False)
        self.actionUpdateConsolidation.setObjectName(_fromUtf8("actionUpdateConsolidation"))
        self.menuProject.addAction(self.actionNewProject)
        self.menuProject.addAction(self.actionOpenProject)
        self.menuProject.addAction(self.actionSaveProject)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionEditTIM)
        self.menuProject.addAction(self.actionTIMDiagram)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionManageFiles)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuDocuments.addAction(self.actionNewDocument)
        self.menuClauses.addAction(self.actionNewClause)
        self.menuClauses.addAction(self.actionPathDiagram)
        self.menuClauses.addAction(self.actionTotalDiagram)
        self.menuConsolidation.addAction(self.actionProjectConsolidation)
        self.menuConsolidation.addAction(self.actionIndexHistory)
        self.menuConsolidation.addAction(self.actionUpdateConsolidation)
        self.menuVerifications.addAction(self.actionCheckSpaces)
        self.menuVerifications.addAction(self.actionCheckGranularity)
        self.menuVerifications.addAction(self.actionSuspectClauses)
        self.menuVerifications.addAction(self.actionRedundantPaths)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuDocuments.menuAction())
        self.menubar.addAction(self.menuClauses.menuAction())
        self.menubar.addAction(self.menuConsolidation.menuAction())
        self.menubar.addAction(self.menuVerifications.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProject.setTitle(QtGui.QApplication.translate("MainWindow", "Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDocuments.setTitle(QtGui.QApplication.translate("MainWindow", "Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.menuClauses.setTitle(QtGui.QApplication.translate("MainWindow", "Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConsolidation.setTitle(QtGui.QApplication.translate("MainWindow", "Consolidação", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVerifications.setTitle(QtGui.QApplication.translate("MainWindow", "Verificações", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject.setText(QtGui.QApplication.translate("MainWindow", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject_as.setText(QtGui.QApplication.translate("MainWindow", "Salvar como...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManageFiles.setText(QtGui.QApplication.translate("MainWindow", "Arquivos importados", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditTIM.setText(QtGui.QApplication.translate("MainWindow", "Editar TIM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTIMDiagram.setText(QtGui.QApplication.translate("MainWindow", "Diagrama TIM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDocument.setText(QtGui.QApplication.translate("MainWindow", "Novo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDocument.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewClause.setText(QtGui.QApplication.translate("MainWindow", "Nova Cláusula", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckSpaces.setText(QtGui.QApplication.translate("MainWindow", "Lacunas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckGranularity.setText(QtGui.QApplication.translate("MainWindow", "Granularidade", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuspectClauses.setText(QtGui.QApplication.translate("MainWindow", "Cláusulas suspeitas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedundantPaths.setText(QtGui.QApplication.translate("MainWindow", "Caminhos redundantes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathDiagram.setText(QtGui.QApplication.translate("MainWindow", "Diagrama de caminho", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTotalDiagram.setText(QtGui.QApplication.translate("MainWindow", "Diagrama total", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjectConsolidation.setText(QtGui.QApplication.translate("MainWindow", "Nova Consolidação de Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndexHistory.setText(QtGui.QApplication.translate("MainWindow", "HIstórico de Índices", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdateConsolidation.setText(QtGui.QApplication.translate("MainWindow", "Atualizar consolidação anterior", None, QtGui.QApplication.UnicodeUTF8))

