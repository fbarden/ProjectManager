import sys
from UI import Ui_ClauseView
from AddRelatedFileDialog import AddRelatedFileDialog
from ImportFileDialog import ImportFileDialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project

class ClauseViewWidget(QWidget):

    openDocumentSignal = pyqtSignal(str);
    newClauseSignal = pyqtSignal(dict);
    
    def __init__(self, project, clause=None):
        super(ClauseViewWidget, self).__init__()
        self.project = project
        self.clause = None
        self.links = {}
        self.ui = Ui_ClauseView.Ui_clauseViewWidget()
        self.ui.setupUi(self)
        if (clause is not None) :
            self.loadClause(clause)
        self.ui.previousClauseShortcut = QShortcut('ALT+Left', self)
        self.ui.previousButton.clicked.connect(self.previousClause)
        self.ui.previousClauseShortcut.activated.connect(self.previousClause)
        self.ui.nextClauseShortcut = QShortcut('ALT+Right', self)
        self.ui.nextClauseShortcut.activated.connect(self.nextClause)
        self.ui.nextButton.clicked.connect(self.nextClause)
        self.ui.uplinksTreeWidget.itemActivated.connect(self.loadLink)
        self.ui.downlinksTreeWidget.itemActivated.connect(self.loadLink)
#        self.ui.returnButton.triggered.connect(self.returnClause)
        self.closeClauseShortcut = QShortcut('CTRL+W', self)
        self.closeClauseShortcut.activated.connect(self.upToDocument)
        self.ui.upButton.clicked.connect(self.upToDocument)
        self.ui.titleEdit.textChanged.connect(self.changeTitle)
        self.ui.importFileButton.clicked.connect(self.importFile)
        self.ui.addFileButton.clicked.connect(self.addFile)
        self.ui.textEdit.textChanged.connect(self.enableSave)
        self.ui.titleEdit.textChanged.connect(self.enableSave)
        self.ui.saveButton.clicked.connect(self.saveClause)
        self.ui.createChildClauseButton.clicked.connect(self.createClause)

    def createClause(self):
        param = {}
        param['parentClause'] = self.clause
        print "Enviando Sinal"
        self.newClauseSignal.emit(param)

    def enableSave(self):
        self.ui.saveButton.setEnabled(True)

    def importFile(self):
        importFileDialog = ImportFileDialog(self, self.project)
        importFileDialog.show()

    def addFile(self):
        addRelatedFileDialog = AddRelatedFileDialog(self, self.project, self.clause)
        addRelatedFileDialog.show()
        addRelatedFileDialog.updateFileTreeSignal.connect(self.loadRelatedDocs)
        self.enableSave()

    def changeTitle(self, text):
        if (self.clause.getConsolidatedID() != ""):
            text += " (" + self.clause.getConsolidatedID() + ")"
        self.ui.titleLabel.setText(text)

    def upToDocument(self):
        if (self.askSave()):
            self.openDocumentSignal.emit(self.clause.getDocument().getName())

    def clearWidget(self):
        self.ui.uplinksTreeWidget.clear()
        self.ui.downlinksTreeWidget.clear()
#        self.ui.relatedFilesTreeWidget.clear()

    def loadLink(self, selectedItem, column):
        if (self.askSave()):
            if (selectedItem.parent() is not None) :
                documentName = str(selectedItem.parent().text(0))
                clauseName = str(selectedItem.text(0))
                newClause = self.links[documentName+clauseName]
                self.loadClause(newClause)

    def changeClause(self,  step):
        print "Passou pelo changeclause"
        if (self.askSave()) :
            document = self.clause.getDocument()
            clausesList = document.getClausesList()
            index = clausesList.index(self.clause.getID()) + step
            if (index > (-1)) and (index < len(clausesList)):
                self.loadClause(document.getClause(clausesList[index]))

    def nextClause(self):
        self.changeClause(+1)

    def previousClause(self):
        self.changeClause(-1)

    def loadClause(self,  clause):
        self.clause = clause
        self.clearWidget()
        self.loadTitle()
        self.loadText()
        self.loadUplinks()
        self.loadDownlinks()
        self.loadHistory()
        self.loadRelatedDocs()
        self.ui.saveButton.setEnabled(False)

    def loadText(self):
        self.ui.textEdit.setText(self.clause.getText())
        self.ui.commentsEdit.setText(self.clause.getComments())

    def loadTitle(self):
        title = self.clause.getTitle()
        if (self.clause.getConsolidatedID() != ""):
            title += " (" + self.clause.getConsolidatedID() + ")"
        self.ui.titleLabel.setText(title)
        self.ui.documentLabel.setText("Documento: " + self.clause.getDocument().getTitle())
        self.ui.typeLabel.setText("Tipo: " + self.clause.getType().getName())
        self.ui.titleEdit.setText(self.clause.getTitle())
    
    def loadUplinks(self):
        linksDict = self.clause.getParentLinksDoc2Clause()
        print linksDict
        widgetList = []
        for documentName in linksDict :
            documentWidgetItem = QTreeWidgetItem()
            documentWidgetItem.setText(0,  documentName)
            widgetList += [documentWidgetItem]
            document = self.project.getDocument(documentName) 
            for clauseId in linksDict[documentName] :
                clause = document.getClause(clauseId)
                clauseWidgetItem = QTreeWidgetItem(documentWidgetItem)
                clauseWidgetItem.setText(0,  clause.getTitle())
                widgetList += [clauseWidgetItem]
                self.links[documentName+clause.getTitle()] = clause
        self.ui.uplinksTreeWidget.addTopLevelItems(widgetList)

    def loadDownlinks(self):
        linksDict = self.clause.getChildLinksDoc2Clause()
        widgetList = []
        for documentName in linksDict :
            documentWidgetItem = QTreeWidgetItem()
            documentWidgetItem.setText(0,  documentName)
            widgetList += [documentWidgetItem]
            document = self.project.getDocument(documentName) 
            for clauseId in linksDict[documentName] :
                clause = document.getClause(clauseId)
                clauseWidgetItem = QTreeWidgetItem(documentWidgetItem)
                clauseWidgetItem.setText(0,  clause.getTitle())
                widgetList += [clauseWidgetItem]
                self.links[documentName+clause.getTitle()] = clause
        self.ui.downlinksTreeWidget.addTopLevelItems(widgetList)

    def loadHistory(self):
        pass
   
    def loadRelatedDocs(self):
        self.ui.relatedFilesTreeWidget.clear()
        filesList = self.clause.getRelatedFilesList()
        for file in filesList:
            item = QTreeWidgetItem(self.ui.relatedFilesTreeWidget)
            item.setText(0, file)
            item.setText(1, self.project.getImportedFileDescription(file))
            item.setText(2, self.clause.getRelatedFileObservation(file))

    def askSave(self):
        if (self.ui.saveButton.isEnabled()):
            answer = QMessageBox.question(None,
                self.trUtf8("Salvar Alteracoes"),
                self.trUtf8("""Existem alteracoes nao salvas. Deseja salvar alteracoes?"""),
                QMessageBox.StandardButtons(\
                    QMessageBox.Cancel | \
                    QMessageBox.No | \
                    QMessageBox.Yes),
                QMessageBox.Yes)
            if (answer == QMessageBox.Cancel) :
                return False
            elif (answer == QMessageBox.Yes) :
                self.saveClause()
        return True


    def saveClause(self):
        self.clause.setTitle(str(self.ui.titleEdit.text()))
        self.clause.setText(str(self.ui.textEdit.toHtml()))
        self.clause.setComments(str(self.ui.commentsEdit.toHtml()))
        self.clause.emitChange()
            
        self.ui.saveButton.setEnabled(False)
        
