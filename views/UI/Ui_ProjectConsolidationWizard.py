# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectConsolidationWizard.ui'
#
# Created: Mon Aug  5 09:43:44 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProjectConsolidationWizard(object):
    def setupUi(self, ProjectConsolidationWizard):
        ProjectConsolidationWizard.setObjectName(_fromUtf8("ProjectConsolidationWizard"))
        ProjectConsolidationWizard.resize(603, 527)
        ProjectConsolidationWizard.setWizardStyle(QtGui.QWizard.ModernStyle)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        ProjectConsolidationWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.documentsTreeWidget = QtGui.QTreeWidget(self.wizardPage2)
        self.documentsTreeWidget.setObjectName(_fromUtf8("documentsTreeWidget"))
        self.verticalLayout.addWidget(self.documentsTreeWidget)
        ProjectConsolidationWizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtGui.QWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.wizardPage3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.typesTreeWidget = QtGui.QTreeWidget(self.wizardPage3)
        self.typesTreeWidget.setObjectName(_fromUtf8("typesTreeWidget"))
        self.verticalLayout_2.addWidget(self.typesTreeWidget)
        ProjectConsolidationWizard.addPage(self.wizardPage3)
        self.wizardPage4 = QtGui.QWizardPage()
        self.wizardPage4.setObjectName(_fromUtf8("wizardPage4"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.wizardPage4)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.prefixLabel = QtGui.QLabel(self.wizardPage4)
        self.prefixLabel.setEnabled(True)
        self.prefixLabel.setObjectName(_fromUtf8("prefixLabel"))
        self.verticalLayout_3.addWidget(self.prefixLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.documentPrefixCheckBox = QtGui.QCheckBox(self.wizardPage4)
        self.documentPrefixCheckBox.setEnabled(True)
        self.documentPrefixCheckBox.setChecked(True)
        self.documentPrefixCheckBox.setObjectName(_fromUtf8("documentPrefixCheckBox"))
        self.horizontalLayout.addWidget(self.documentPrefixCheckBox)
        self.typePrefixCheckBox = QtGui.QCheckBox(self.wizardPage4)
        self.typePrefixCheckBox.setEnabled(True)
        self.typePrefixCheckBox.setChecked(True)
        self.typePrefixCheckBox.setObjectName(_fromUtf8("typePrefixCheckBox"))
        self.horizontalLayout.addWidget(self.typePrefixCheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.orderLabel = QtGui.QLabel(self.wizardPage4)
        self.orderLabel.setEnabled(True)
        self.orderLabel.setObjectName(_fromUtf8("orderLabel"))
        self.verticalLayout_6.addWidget(self.orderLabel)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.typeOrderButton = QtGui.QRadioButton(self.wizardPage4)
        self.typeOrderButton.setEnabled(True)
        self.typeOrderButton.setChecked(True)
        self.typeOrderButton.setObjectName(_fromUtf8("typeOrderButton"))
        self.verticalLayout_5.addWidget(self.typeOrderButton)
        self.documentOrderButton = QtGui.QRadioButton(self.wizardPage4)
        self.documentOrderButton.setEnabled(True)
        self.documentOrderButton.setObjectName(_fromUtf8("documentOrderButton"))
        self.verticalLayout_5.addWidget(self.documentOrderButton)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.unifyDocumentsCheckBox = QtGui.QCheckBox(self.wizardPage4)
        self.unifyDocumentsCheckBox.setEnabled(True)
        self.unifyDocumentsCheckBox.setObjectName(_fromUtf8("unifyDocumentsCheckBox"))
        self.verticalLayout_9.addWidget(self.unifyDocumentsCheckBox)
        ProjectConsolidationWizard.addPage(self.wizardPage4)

        self.retranslateUi(ProjectConsolidationWizard)
        QtCore.QObject.connect(self.typeOrderButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.unifyDocumentsCheckBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ProjectConsolidationWizard)
        ProjectConsolidationWizard.setTabOrder(self.documentsTreeWidget, self.typesTreeWidget)
        ProjectConsolidationWizard.setTabOrder(self.typesTreeWidget, self.documentPrefixCheckBox)
        ProjectConsolidationWizard.setTabOrder(self.documentPrefixCheckBox, self.typePrefixCheckBox)
        ProjectConsolidationWizard.setTabOrder(self.typePrefixCheckBox, self.typeOrderButton)
        ProjectConsolidationWizard.setTabOrder(self.typeOrderButton, self.documentOrderButton)
        ProjectConsolidationWizard.setTabOrder(self.documentOrderButton, self.unifyDocumentsCheckBox)

    def retranslateUi(self, ProjectConsolidationWizard):
        ProjectConsolidationWizard.setWindowTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage1.setTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Consolidação de Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage2.setTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Escolha de documentos", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage2.setSubTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Escolha os documentos que irão fazer parte da consolidação:", None, QtGui.QApplication.UnicodeUTF8))
        self.documentsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("ProjectConsolidationWizard", "Documentos", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage3.setTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Escolha de Tipos", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage3.setSubTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Escolha quais tipos participarão da consolidação:", None, QtGui.QApplication.UnicodeUTF8))
        self.typesTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("ProjectConsolidationWizard", "Tipos", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage4.setTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Definições de Exibição", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage4.setSubTitle(QtGui.QApplication.translate("ProjectConsolidationWizard", "Defina como as cláusulas serão nomeadas e organizadas:", None, QtGui.QApplication.UnicodeUTF8))
        self.prefixLabel.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Prefixo:", None, QtGui.QApplication.UnicodeUTF8))
        self.documentPrefixCheckBox.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Prefixo de documento", None, QtGui.QApplication.UnicodeUTF8))
        self.typePrefixCheckBox.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Prefixo de tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.orderLabel.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Ordenamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.typeOrderButton.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Ordenar por tipos (tipos de ordem maior primeiro)", None, QtGui.QApplication.UnicodeUTF8))
        self.documentOrderButton.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Como ordenado nos documentos", None, QtGui.QApplication.UnicodeUTF8))
        self.unifyDocumentsCheckBox.setText(QtGui.QApplication.translate("ProjectConsolidationWizard", "Juntar todos documentos selecionados em um único", None, QtGui.QApplication.UnicodeUTF8))

