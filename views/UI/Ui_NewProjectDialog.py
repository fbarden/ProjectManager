# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProjectDialog.ui'
#
# Created: Tue Aug 20 00:07:15 2013
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
        NewProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        NewProjectDialog.resize(575, 540)
        NewProjectDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        NewProjectDialog.setModal(True)
        NewProjectDialog.setWizardStyle(QtGui.QWizard.ModernStyle)
        NewProjectDialog.setOptions(QtGui.QWizard.NoDefaultButton)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 145, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.projectNameLabel = QtGui.QLabel(self.wizardPage1)
        self.projectNameLabel.setObjectName(_fromUtf8("projectNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.projectNameLabel)
        self.folderLabel = QtGui.QLabel(self.wizardPage1)
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.folderLabel)
        self.folderEdit = QtGui.QLineEdit(self.wizardPage1)
        self.folderEdit.setObjectName(_fromUtf8("folderEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.folderEdit)
        self.searchButton = QtGui.QPushButton(self.wizardPage1)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.searchButton)
        self.projectNameEdit = QtGui.QLineEdit(self.wizardPage1)
        self.projectNameEdit.setObjectName(_fromUtf8("projectNameEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.projectNameEdit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 145, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        NewProjectDialog.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.wizardPage2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.TIMTreeWidget = QtGui.QTreeWidget(self.wizardPage2)
        self.TIMTreeWidget.setObjectName(_fromUtf8("TIMTreeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.TIMTreeWidget)
        self.verticalLayout_3.addWidget(self.TIMTreeWidget)
        self.label_6 = QtGui.QLabel(self.wizardPage2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        NewProjectDialog.addPage(self.wizardPage2)
        self.wizardPage3 = QtGui.QWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.wizardPage3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.projectNameLabel_2 = QtGui.QLabel(self.wizardPage3)
        self.projectNameLabel_2.setObjectName(_fromUtf8("projectNameLabel_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.projectNameLabel_2)
        self.locationLabel = QtGui.QLabel(self.wizardPage3)
        self.locationLabel.setObjectName(_fromUtf8("locationLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.locationLabel)
        self.locationForm = QtGui.QLabel(self.wizardPage3)
        self.locationForm.setText(_fromUtf8(""))
        self.locationForm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.locationForm.setObjectName(_fromUtf8("locationForm"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.locationForm)
        self.projectForm = QtGui.QLabel(self.wizardPage3)
        self.projectForm.setText(_fromUtf8(""))
        self.projectForm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.projectForm.setObjectName(_fromUtf8("projectForm"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.projectForm)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.label_5 = QtGui.QLabel(self.wizardPage3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.graphicsView = QtGui.QGraphicsView(self.wizardPage3)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.graphicsView.setInteractive(False)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_4.addWidget(self.graphicsView)
        NewProjectDialog.addPage(self.wizardPage3)
        self.folderLabel.setBuddy(self.folderEdit)

        self.retranslateUi(NewProjectDialog)
        QtCore.QObject.connect(self.projectNameEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.projectForm.setText)
        QtCore.QObject.connect(self.folderEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.locationForm.setText)
        QtCore.QObject.connect(self.TIMTreeWidget, QtCore.SIGNAL(_fromUtf8("itemChanged(QTreeWidgetItem*,int)")), self.graphicsView.invalidateScene)
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)
        NewProjectDialog.setTabOrder(self.projectNameEdit, self.folderEdit)
        NewProjectDialog.setTabOrder(self.folderEdit, self.searchButton)
        NewProjectDialog.setTabOrder(self.searchButton, self.TIMTreeWidget)
        NewProjectDialog.setTabOrder(self.TIMTreeWidget, self.graphicsView)

    def retranslateUi(self, NewProjectDialog):
        NewProjectDialog.setWindowTitle(QtGui.QApplication.translate("NewProjectDialog", "Novo Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage1.setTitle(QtGui.QApplication.translate("NewProjectDialog", "Novo Projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage1.setSubTitle(QtGui.QApplication.translate("NewProjectDialog", "Configure nome e localização do projeto:", None, QtGui.QApplication.UnicodeUTF8))
        self.projectNameLabel.setText(QtGui.QApplication.translate("NewProjectDialog", "Nome do Projeto:", None, QtGui.QApplication.UnicodeUTF8))
        self.folderLabel.setText(QtGui.QApplication.translate("NewProjectDialog", "Diretório:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("NewProjectDialog", "Procurar", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage2.setTitle(QtGui.QApplication.translate("NewProjectDialog", "Hierarquia de tipos", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage2.setSubTitle(QtGui.QApplication.translate("NewProjectDialog", "Defina a hierarquia dos tipos para ligações entre cláusulas:", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("NewProjectDialog", "TIM", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.TIMTreeWidget.isSortingEnabled()
        self.TIMTreeWidget.setSortingEnabled(False)
        self.TIMTreeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("NewProjectDialog", "<adicionar tipo>", None, QtGui.QApplication.UnicodeUTF8))
        self.TIMTreeWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(QtGui.QApplication.translate("NewProjectDialog", "A hierarquia irá definir o TIM (Traceability Model Information)", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage3.setTitle(QtGui.QApplication.translate("NewProjectDialog", "Novo projeto", None, QtGui.QApplication.UnicodeUTF8))
        self.wizardPage3.setSubTitle(QtGui.QApplication.translate("NewProjectDialog", "Resumo do novo projeto:", None, QtGui.QApplication.UnicodeUTF8))
        self.projectNameLabel_2.setText(QtGui.QApplication.translate("NewProjectDialog", "Nome do Projeto:", None, QtGui.QApplication.UnicodeUTF8))
        self.locationLabel.setText(QtGui.QApplication.translate("NewProjectDialog", "Localização:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("NewProjectDialog", "TIM (Traceability Information Model)", None, QtGui.QApplication.UnicodeUTF8))

