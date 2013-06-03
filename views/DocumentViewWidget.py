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
        cursor.insertBlock()
        self.loadClauses()
    
    def loadTitle(self):
        cursor = self.ui.textBrowser.textCursor()
        cursor.insertBlock()
        cursor.insertText(self.document.getTitle())

    def loadClauses(self):
        clausesList = self.document.getClausesList();
        for clause in clausesList :
            self.loadClause(clause)
            cursor = self.ui.textBrowser.textCursor()
            cursor.insertBlock()
            cursor.movePosition(QTextCursor.End)

    def loadClause(self,  clause):
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        table = cursor.insertTable(2,  3)
        table.mergeCells(0, 0, 1, 3)
        cursor = table.cellAt(1, 1).firstCursorPosition()
        cursor.insertText(self.document.getClause(clause).getText())
        
