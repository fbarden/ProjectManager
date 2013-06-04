import sys
from UI import Ui_DocumentView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from document import Document
from clause import Clause

class DocumentViewWidget(QWidget):

    openDocumentSignal = pyqtSignal(str);
    openClauseSignal = pyqtSignal(str, str);

    def __init__(self, document = None):
        super(DocumentViewWidget, self).__init__()
        self.ui = Ui_DocumentView.Ui_documentViewWidget()
        self.ui.setupUi(self)
        self.clausesDict  = {}
        if (document is not None) :
            self.loadDocument(document)
        self.ui.textBrowser.anchorClicked.connect(self.linkSelected)
        self.ui.titleButton.clicked.connect(self.changeTitle)
    
    def changeTitle(self):
        newTitle, returnOK = QInputDialog.getText(\
            None,
            self.trUtf8("Change Title"),
            self.trUtf8("Change Title:"),
            QLineEdit.Normal)
        if returnOK :
            self.document.setTitle(newTitle)
            self.ui.titleLabel.setText(newTitle)

    def loadDocument(self,  document):
        self.document = document
        self.ui.textBrowser.clear()
        self.ui.titleLabel.clear()
        self.loadTitle()
        self.loadClauses()
    
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
    
    def linkSelected(self,  url):
        link = url.toString()
        type,  ID = link.split(":")
        if (type == "clause") :
            self.openClauseSignal.emit(self.document.getName(), ID)
        if (type == "document") :
            self.openDocumentSignal.emit(ID)
