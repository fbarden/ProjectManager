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
    
    def loadDocument(self,  document):
        self.document = document
        cursor = self.ui.textBrowser.textCursor()
        self.loadTitle()
        self.loadClauses()
    
    def loadTitle(self):
        cursor = self.ui.textBrowser.textCursor()
        cursor.insertText(self.document.getTitle())

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
