import sys
from UI import Ui_DocumentView
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from document import Document
from clause import Clause
from views.OrderClauseDialog import OrderClauseDialog

class DocumentViewWidget(QWidget):

    openElementSignal = pyqtSignal(str);
    newClauseSignal = pyqtSignal(dict);
    backHistorySignal = pyqtSignal();

    def __init__(self, document = None):
        super(DocumentViewWidget, self).__init__()
        self.ui = Ui_DocumentView.Ui_documentViewWidget()
        self.ui.setupUi(self)
        self.clausesDict  = {}
        if (document is not None) :
            self.loadDocument(document)
        self.ui.textBrowser.anchorClicked.connect(self.linkSelected)
        self.ui.titleButton.clicked.connect(self.changeTitle)
        self.closeDocumentShortcut = QShortcut('CTRL+W', self)
        self.closeDocumentShortcut.activated.connect(self.upToProject)
        self.backHistoryShortcut = QShortcut('ALT+Backspace', self)
        self.backHistoryShortcut.activated.connect(self.backHistory)
        self.ui.upButton.clicked.connect(self.upToProject)
        self.showLinksShortcut = QShortcut('CTRL+L', self)
        self.showLinksShortcut.activated.connect(self.ui.showLinksButton.click)
        self.ui.showLinksButton.clicked.connect(self.showLinksAction)
        self.newClauseShortcut = QShortcut('CTRL+T', self)
        self.newClauseShortcut.activated.connect(self.newClause)
        self.ui.orderButton.clicked.connect(self.orderClauses)

    def backHistory(self):
        self.backHistorySignal.emit()

    def orderClauses(self):
        orderDialog = OrderClauseDialog(self, self.document)
        orderDialog.show()
        orderDialog.accepted.connect(lambda : self.loadDocument(self.document))

    def showLinksAction(self):
        self.loadDocument(self.document)

    def changeTitle(self):
        newTitle, returnOK = QInputDialog.getText(\
            None,
            self.trUtf8("Alterar Titulo"),
            self.trUtf8("Alterar Titulo:"),
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

    def addLinkDoc(self, cursor, linkDoc):
        linkCharFormat = QTextCharFormat()
        linkCharFormat.setFontPointSize(10)
        linkCharFormat.setFontItalic(True)
        linkCharFormat.setAnchor(True)
        linkCharFormat.setAnchorHref("document:" + linkDoc)
        cursor.mergeCharFormat(linkCharFormat)
        cursor.insertText(linkDoc + "\n")

    def loadClause(self,  clauseID):
        clause = self.document.getClause(clauseID)
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        table = cursor.insertTable(2,  3)
        tableFormat = QTextTableFormat()
        textLength = QTextLength(QTextLength.FixedLength, 800)
        linkLength = QTextLength(QTextLength.FixedLength, 200)
        tableFormat.setColumnWidthConstraints([linkLength, textLength, linkLength])
        table.mergeCells(0, 0, 1, 3)
        table.setFormat(tableFormat)
        cursor = table.cellAt(0, 0).firstCursorPosition()
        titleBlockFormat = QTextBlockFormat()
        titleBlockFormat.setAlignment(Qt.AlignCenter)
        cursor.mergeBlockFormat(titleBlockFormat)
        titleCharFormat = QTextCharFormat()
        titleCharFormat.setFontPointSize(17)
        titleCharFormat.setFontWeight(QFont.Bold)
        titleCharFormat.setAnchor(True)
        titleCharFormat.setAnchorHref("clause:" + clause.getID())
        cursor.mergeCharFormat(titleCharFormat)
        cursor.insertText(clause.getTitle())
        cursor = table.cellAt(1, 1).firstCursorPosition()
        cursor.insertHtml(clause.getText())
        if (self.ui.showLinksButton.isChecked()):
            uplinks = clause.getParentLinksDoc2Clause()
            cursor = table.cellAt(1, 0).lastCursorPosition()
            for linkDoc in uplinks.keys() :
                self.addLinkDoc(cursor, linkDoc)
            cursor.deletePreviousChar()
            cursor = table.cellAt(1, 2).lastCursorPosition()
            downlinks = clause.getChildLinksDoc2Clause()
            for linkDoc in downlinks.keys() :
                self.addLinkDoc(cursor, linkDoc)
            cursor.deletePreviousChar()
        else:
            table.mergeCells(1, 0, 1, 3)
    
    def linkSelected(self,  url):
        link = unicode(url.toString())
        type, ID = link.split(":", 1)
        if (type == "clause") :
            self.openElementSignal.emit("clause:" + ID)
        elif (type == "document") :
            self.openElementSignal.emit("document:" + ID)
        elif (type == "newClause") :
            self.newClause()

    def newClause(self):
        param = {}
        param['document'] = self.document.getName()
        self.newClauseSignal.emit(param)

    def loadAddClause(self):
        cursor = self.ui.textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertBlock()
        cursor.insertBlock()
        link = '<a href="newClause:newClause">Adicionar nova clausula...</a>'
        cursor.insertHtml(link)

    def upToProject(self):
        self.openElementSignal.emit("project:project")
