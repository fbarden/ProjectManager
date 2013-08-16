
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from views.UI.Ui_ProjectConsolidationWizard import Ui_ProjectConsolidationWizard

class ProjectConsolidationWizard(QWizard):

    consolidateProjectSignal = pyqtSignal(dict)

    def __init__(self, parent, project):
        super(ProjectConsolidationWizard, self).__init__(parent)
        self.ui = Ui_ProjectConsolidationWizard()
        self.ui.setupUi(self)
        self.ui.orderButtonGroup = QButtonGroup(self)
        self.ui.orderButtonGroup.addButton(self.ui.documentOrderButton)
        self.ui.orderButtonGroup.addButton(self.ui.typeOrderButton)
        self.project = project
        settings = self.project.getConsolidationSettings()
        documentsList = self.project.getDocumentsList()
        self.documentsDict = {}
        for document in documentsList:
            documentTitle = self.project.getDocument(document).getTitle()
            documentItem = QTreeWidgetItem(self.ui.documentsTreeWidget)
            documentItem.setText(0, documentTitle)
            documentItem.setFlags(documentItem.flags() | Qt.ItemIsUserCheckable)
            documentItem.setCheckState(0, Qt.Unchecked)
            self.documentsDict[document] = documentItem
        TIM = self.project.getTIM()
        self.typesDict = {}
        for type in TIM.getTypesList():
            typeItem = QTreeWidgetItem(self.ui.typesTreeWidget)
            typeItem.setText(0, type)
            typeItem.setFlags(typeItem.flags() | Qt.ItemIsUserCheckable)
            typeItem.setCheckState(0, Qt.Unchecked)
            self.typesDict[type] = typeItem
        self.ui.buttonGroup = QButtonGroup()
        self.accepted.connect(self.saveSettingsAndConsolidate)
    
    def saveSettingsAndConsolidate(self):
        settings = {}
        selectedDocs = []
        for doc in self.documentsDict.keys() :
            if (self.documentsDict[doc].checkState(0) == Qt.Checked) :
                selectedDocs.append(doc)
        selectedTypes = []
        for type in self.typesDict.keys() :
            if (self.typesDict[type].checkState(0) == Qt.Checked) :
                selectedTypes.append(type)
        settings['documents'] = selectedDocs
        settings['types'] = selectedTypes
        settings['docPrefix'] =  self.ui.documentPrefixCheckBox.isChecked()
        settings['typePrefix'] =  self.ui.typePrefixCheckBox.isChecked()
        if self.ui.documentOrderButton.isChecked():
            settings['order'] = 'document'
        if self.ui.typeOrderButton.isChecked():
            settings['order'] = 'type'
        settings['unifyDocuments'] = self.ui.unifyDocumentsCheckBox.isChecked()
        settings['limits'] = {}
        self.project.setConsolidationSettings(settings)
        self.consolidateProjectSignal.emit(settings)