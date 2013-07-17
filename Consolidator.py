from project import Project
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Consolidator(object):

    def filterClauses(self, project, docList, typeList):
        doc2Clauses = {}
        for documentName in docList :
            doc2Clauses[documentName] = []
            document = project.getDocument(documentName)
            for clauseID in document.getClausesList():
                clause = document.getClause(clauseID)
                if clause.getType().getName() in typeList:
                    doc2Clauses[documentName].append(clause)
        return doc2Clauses

    def checkCompletionAndAdd(self, typeList, completedList, TIM):
        for typeName in typeList:
            parentsList = TIM.getType(typeName).getPossibleParentsList()
            auxList = [parent for parent in parentsList if parent not in completedList]
            if (len(auxList) == 0):
                completedList.append(typeName)
        for typeName in typeList:
            childrenList = TIM.getType(typeName).getPossibleChildrenList()
            completedList = self.checkCompletionAndAdd(childrenList, completedList, TIM)
        return completedList
    
    def orderTypes(self, TIM):
        rootTypes = TIM.getRootsList()
        orderedTypes = []
        orderedTypes = self.checkCompletionAndAdd(rootTypes, orderedTypes, TIM)
        return orderedTypes

    def orderClauses(self, project, order, unify, doc2Clauses):
        orderedDoc2Clause = {}
        if (order == 'type'):
            if unify:
                clausesList = []
                for clauses in doc2Clauses.values() :
                    clausesList += clauses
                doc2Clauses = {}
                doc2Clauses['unified'] = clausesList
            TIM = project.getTIM()
            orderedTypesList = self.orderTypes(TIM)
            for type in orderedTypesList :
                for doc in doc2Clauses.keys():
                    for clause in doc2Clauses[doc]:
                        orderedDoc2Clause[doc] = sorted(doc2Clauses[doc], key=lambda clause : orderedTypesList.index(clause.getType().getName()))
        return orderedDoc2Clause

    def initializeProject(self, project, settings):
        doc2Clauses = self.filterClauses(project, settings['documents'], settings['types'])
        orderedDoc2Clauses = self.orderClauses(project, settings['order'], settings['unifyDocuments'], doc2Clauses)
        return orderedDoc2Clauses

    def printSettings(self, settings):
        print "Printing Settings"
        print settings['documents']
        print settings['types']
        print settings['order']
        print settings['unifyDocuments']

    def __init__(self, project, settings):
        self.project = project
        self.printSettings(settings)
        self.doc2ClauseList = self.initializeProject(project, settings)
        self.consolidateIndexes(settings)

    def consolidateIndexes(self, settings):
        hasDocPrefix = settings['docPrefix']
        hasTypePrefix = settings['typePrefix']
        prefixIDDict = {}
        for doc in self.doc2ClauseList:
            for clause in self.doc2ClauseList[doc]:
                prefix = unicode()
                if hasDocPrefix :
                    prefix += clause.getDocument().getPrefix()
                    if hasTypePrefix:
                        prefix += ":" 
                if hasTypePrefix:
                    prefix += clause.getType().getPrefix()
                if prefix in prefixIDDict.keys():
                    prefixIDDict[prefix] += 1
                else :
                    prefixIDDict[prefix] = 1
                prefix += prefixIDDict[prefix]
                clause.setConsolidatedID(prefix)

    def toPDF(self, file='./teste1.pdf'):
        printer = QPrinter()
        
        docTitleBlockFormat = QTextBlockFormat()
        docTitleBlockFormat.setAlignment(Qt.AlignCenter)
        docTitleCharFormat = QTextCharFormat()
        docTitleCharFormat.setFontPointSize(17)
        docTitleCharFormat.setFontWeight(QFont.Bold)
        
        clauseBlockFormat = QTextBlockFormat()
        clauseBlockFormat.setAlignment(Qt.AlignJustify)
        clauseTitleCharFormat = QTextCharFormat()
        clauseTitleCharFormat.setFontPointSize(12)
        clauseTitleCharFormat.setFontWeight(QFont.Bold)
        clauseTextCharFormat = QTextCharFormat()
        clauseTextCharFormat.setFontPointSize(12)
        clauseTextCharFormat.setFontWeight(QFont.Normal)
        
        printer.setOutputFormat(QPrinter.PdfFormat);
        printer.setOutputFileName(file);
        printer.setPaperSize(QPrinter.A4)
        
        textDoc = QTextEdit()
        for doc in self.doc2ClauseList:
            
            if doc is not "unified":
                cursor = textDoc.textCursor()
                cursor.movePosition(QTextCursor.End)
                cursor.mergeBlockFormat(docTitleBlockFormat)
                cursor.mergeCharFormat(docTitleCharFormat)
                cursor.insertText(self.project.getDocument(doc).getTitle() + "\n\n")
            else :
                cursor = textDoc.textCursor()
                cursor.movePosition(QTextCursor.End)
                cursor.mergeBlockFormat(docTitleBlockFormat)
                cursor.mergeCharFormat(docTitleCharFormat)
                cursor.insertText(self.project.getName() + "\n\n")
            for clause in self.doc2ClauseList[doc]: 
                cursor.mergeBlockFormat(clauseBlockFormat)
                cursor.mergeCharFormat(clauseTitleCharFormat)
                cursor.insertText('   ' + clause.getConsolidatedID() + " - " + clause.getTitle() + '\n')
                cursor.mergeCharFormat(clauseTextCharFormat)
                cursor.insertHtml(clause.getText())
                cursor.insertText('\n\n')
            textDoc.print_(printer)
            printer.newPage()
