from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI import Ui_NewClauseDialog

from clause import Clause
from link import Link

class NewClauseDialog(QDialog):
    
    openClauseSignal = pyqtSignal(str, str)
    
    def __init__(self,  parent,  project, document=None, parentClause=None):
        super(NewClauseDialog, self).__init__(parent)
        self.project = project
        self.document = document
        self.ui = Ui_NewClauseDialog.Ui_NewClauseDialog()
        self.ui.setupUi(self)
        documentList = self.project.getDocumentsList()
        self.ui.documentBox.addItems(documentList)
        if (self.document is not None):
            self.ui.documentBox.setCurrentIndex(self.ui.documentBox.findText(self.document.getName()))
        if (parentClause is not None):
            type = parentClause.getType()
            typeList = self.project.getTIM().getType(type).getPossibleChildrenList()
        else :
            typeList = self.project.getTIM().getTypesList()
        self.ui.typeBox.addItems(typeList)
        currentType = self.ui.typeBox.currentText()
        self.updateParentClauses()
        if (parentClause is not None):
            parentClauseName = parentClause.getDocument().getName() + ":" + parentClause.getID()
            self.ui.parentBox.setCurrentIndex(self.ui.parentBox.findText(parentClauseName))
        self.accepted.connect(self.setClause)
        self.ui.typeBox.currentIndexChanged.connect(self.updateParentClauses)

    def updateParentClauses(self):
        currentType = self.ui.typeBox.currentText()
        clausesList = []
        self.ui.parentBox.clear()
        documentList = self.project.getDocumentsList()
        type = self.project.getTIM().getType(str(currentType))
        parentTypeList = self.project.getTIM().getPossibleParentsList(type)
        for documentName in documentList :
            print "--------------------"
            print "Documento " + documentName
            print "**Total de Clausulas:"
            document = self.project.getDocument(documentName)
            print document.getClausesList()
            print "**Tipos desejados: "
            print parentTypeList
            print "Lista Parcial: "
            print [documentName + ":" + clauseName for clauseName in document.getClausesList() if self.isType(document, clauseName, parentTypeList)]
            clausesList += [documentName + ":" + clauseName for clauseName in document.getClausesList() if self.isType(document, clauseName, parentTypeList)]
            print "**Clausulas com tipo desejado:"
            print clausesList
        self.ui.parentBox.addItems(clausesList)
        if currentType in self.project.getTIM().getRootsList() :
            self.ui.parentBox.insertItem(0, "Sem Clausula Pai" )
        if (str(self.ui.parentBox.currentText()) is ""):
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def isType(self, document, clauseName, typeList):
        clause = document.getClause(clauseName)
        print "Passando pelo isType com " + clauseName + " e document " + document.getName()
        print "Lista de clausulas do documento"
        print document.getClausesList()
        print "Tipo analisado " + clause.getType()
        print "Lista de tipos "
        print typeList
        if (clause.getType() in typeList) :
            return True
        else :
            return False

    def setClause(self):
        title = str(self.ui.titleEdit.text())
        parent = str(self.ui.parentBox.currentText())
        self.clause = Clause()
        self.clause.setTitle(title)
        self.clause.setType(str(self.ui.typeBox.currentText()))
        self.document = self.project.getDocument(str(self.ui.documentBox.currentText()))
        self.document.addClause(self.clause)
        if (parent != "Sem Clausula Pai") :
            parentDocument, parentClause = str(self.ui.parentBox.currentText()).split(":")
            link = Link()
            link.addChild(self.document.getName(), self.clause.getID())
            link.addParent(parentDocument, parentClause)
            link.consolidateParent(self.project)
            link.consolidateChild(self.project)
        self.openClauseSignal.emit(self.document.getName(), self.clause.getID())
