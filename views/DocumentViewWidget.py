import sys
from UI import Ui_DocumentView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from document import Document
from clause import Clause

class DocumentViewWidget(QWidget):

    openProjectSignal = pyqtSignal()
    openDocumentSignal = pyqtSignal(str);
    openClauseSignal = pyqtSignal(str, str);
    newClauseSignal = pyqtSignal(str);

    def __init__(self, document = None):
        super(DocumentViewWidget, self).__init__()
        self.ui = Ui_DocumentView.Ui_documentViewWidget()
        self.ui.setupUi(self)
        self.clausesDict  = {}
        if (document is not None) :
            self.loadDocument(document)
        self.ui.textBrowser.anchorClicked.connect(self.linkSelected)
        self.ui.titleButton.clicked.connect(self.changeTitle)
        self.ui.upButton.clicked.connect(self.upToProject)
        self.ui.showLinksButton.clicked.connect(self.showLinksAction)

    def showLinksAction(self):
        self.loadDocument(self.document)

    def changeTitle(self):
        newTitle, returnOK = QInputDialog.getText(\
            None,
            self.trUtf8("Alterar Titulo"),
            self.trUtf8("Alterar Titulo:"),
            QLineEdit.Normal)
        if returnOK :
            self.document.setTitle(str(newTitle))
            self.ui.titleLabel.setText(newTitle)

    def loadDocument(self,  document):
        self.document = document
        self.ui.textBrowser.clear()
        self.ui.titleLabel.clear()
        self.loadTitle()
        self.loadClauses()
        self.loadAddClause()
    
    def loadTitle(self):
        self.ui.titleLabel.setText(self.document.getTitle())

    def loadClauses(self):
        clausesList = self.document.getClausesList();
        for clause in clausesList :
            cursor = self.ui.textBrowser.textCursor()
            cursor.movePosition(QTextCursor.End)
            cursor.insertBlock()
            cursor.insertBlock()
            self.loadClause(clause)

    def loadClause(self,  clauseID):
        clause = self.document.getClause(clauseID)
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        table = cursor.insertTable(2,  3)
        table.mergeCells(0, 0, 1, 3)
        cursor = table.cellAt(0, 0).firstCursorPosition()
        link = '<a href="clause:' + clause.getID() + '">' + clause.getTitle() + '</a>'
        cursor.insertHtml(link)
        cursor = table.cellAt(1, 1).firstCursorPosition()
        cursor.insertText(clause.getText())
        if (self.ui.showLinksButton.isChecked()):
            uplinks = clause.getParentLinksDoc2Clause()
            cursor = table.cellAt(1, 0).lastCursorPosition()
            for linkDoc in uplinks.keys() :
                link = '<a href="document:' + linkDoc + '">' + linkDoc + '</a>'
                cursor.insertHtml(link)
            cursor = table.cellAt(1, 2).lastCursorPosition()
            downlinks = clause.getChildLinksDoc2Clause()
            for linkDoc in downlinks.keys() :
                link = '<a href="document:' + linkDoc + '">' + linkDoc + '</a>'
                cursor.insertHtml(link)
        else:
            table.mergeCells(1, 0, 1, 3)
    
    def linkSelected(self,  url):
        link = url.toString()
        type,  ID = link.split(":")
        if (type == "clause") :
            self.openClauseSignal.emit(self.document.getName(), ID)
        elif (type == "document") :
            self.openDocumentSignal.emit(ID)
        elif (type == "newClause") :
            self.newClauseSignal.emit(self.document.getName())

    def loadAddClause(self):
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertBlock()
        cursor.insertBlock()
        link = '<a href="newClause:newClause">Adicionar nova clausula...</a>'
        cursor.insertHtml(link)

    def upToProject(self):
        self.openProjectSignal.emit()
