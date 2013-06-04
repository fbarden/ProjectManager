import sys
from UI import Ui_ClauseView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from project import Project

class ClauseViewWidget(QWidget):

    openDocumentSignal = pyqtSignal(str);
    
    def __init__(self, clause=None):
        super(ClauseViewWidget, self).__init__()
        self.clause = None
        self.ui = Ui_ClauseView.Ui_clauseViewWidget()
        self.ui.setupUi(self)
        if (clause is not None) :
            self.loadClause(clause)
        self.ui.previousButton.clicked.connect(self.previousClause)
        self.ui.nextButton.clicked.connect(self.nextClause)
        self.ui.uplinksTreeWidget.itemActivated.connect(self.loadUplink)
        self.ui.downlinksTreeWidget.itemActivated.connect(self.loadDownlink)
#        self.ui.returnButton.triggered.connect(self.returnClause)
        self.ui.upButton.clicked.connect(self.upToDocument)

    def upToDocument(self):
        self.openDocumentSignal.emit(self.clause.getDocument().getName())

    def clearWidget(self):
        self.ui.uplinksTreeWidget.clear()
        self.ui.downlinksTreeWidget.clear()
#        self.ui.relatedFilesTreeWidget.clear()

    def loadUplink(self, selectedItem, column):
        if (selectedItem.parent() is not None) :
            newClause = self.clause.getParentLinkClause(str(selectedItem.parent().text(0)),  str(selectedItem.text(0)))
            self.loadClause(newClause)

    def loadDownlink(self, selectedItem, column):
        if (selectedItem.parent() is not None) :
            newClause = self.clause.getChildLinkClause(str(selectedItem.parent().text(0)),  str(selectedItem.text(0)))
            self.loadClause(newClause)

    def changeClause(self,  step):
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

    def loadText(self):
        self.ui.textEdit.setText(self.clause.getText())

    def loadTitle(self):
        self.ui.titleLabel.setText(self.clause.getDocument().getName() + ": " + self.clause.getTitle())
        self.ui.titleEdit.setText(self.clause.getTitle())
    
    def loadUplinks(self):
        linksDict = self.clause.getParentLinksDoc2Clause()
        widgetList = []
        for document in linksDict :
            documentWidgetItem = QTreeWidgetItem()
            documentWidgetItem.setText(0,  document)
            widgetList += [documentWidgetItem]
            for clause in linksDict[document] :
                clauseWidgetItem = QTreeWidgetItem(documentWidgetItem)
                clauseWidgetItem.setText(0,  clause)
                widgetList += [clauseWidgetItem]
        self.ui.uplinksTreeWidget.addTopLevelItems(widgetList)

    def loadDownlinks(self):
        linksDict = self.clause.getChildLinksDoc2Clause()
        widgetList = []
        for document in linksDict :
            documentWidgetItem = QTreeWidgetItem()
            documentWidgetItem.setText(0,  document)
            widgetList += [documentWidgetItem]
            for clause in linksDict[document] :
                clauseWidgetItem = QTreeWidgetItem(documentWidgetItem)
                clauseWidgetItem.setText(0,  clause)
                widgetList += [clauseWidgetItem]
        self.ui.downlinksTreeWidget.addTopLevelItems(widgetList)

    def loadHistory(self):
        pass
   
    def loadRelatedDocs(self):
        pass
