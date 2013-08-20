#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
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
        if (order == 'document'):
            orderedDoc2Clause = doc2Clauses
        return orderedDoc2Clause

    def initializeProject(self, project, settings):
        doc2Clauses = self.filterClauses(project, settings['documents'], settings['types'])
        orderedDoc2Clauses = self.orderClauses(project, settings['order'], settings['unifyDocuments'], doc2Clauses)
        return orderedDoc2Clauses

    def printSettings(self, settings):
        print "Printing Settings"
        print settings.keys()
        print settings['documents']
        print settings['types']
        print settings['order']
        print settings['unifyDocuments']

    def __init__(self, project, settings):
        self.project = project
#         self.printSettings(settings)
        self.doc2ClauseList = self.initializeProject(project, settings)
        self.consolidateIndexes(settings)

    def consolidateIndexes(self, settings):
        hasDocPrefix = settings['docPrefix']
        hasTypePrefix = settings['typePrefix']
        limits = settings['limits']
        for doc in self.doc2ClauseList:
            for clause in self.doc2ClauseList[doc]:
                if (clause.getConsolidatedID() == "") :
                    prefix = unicode()
                    if hasDocPrefix :
                        prefix += clause.getDocument().getPrefix()
                        if hasTypePrefix:
                            prefix += ":"
                    if hasTypePrefix:
                        prefix += clause.getType().getPrefix()
                    if prefix in limits.keys():
                        limits[prefix] += 1
                    else :
                        limits[prefix] = 1
                    prefix += unicode(limits[prefix])
                    clause.setConsolidatedID(prefix)

    def toPDF(self, file):
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
            cursor.insertText('\n\n')
            
        # Tracebility Information Model (TIM)
        cursor.insertText('\n\n\n')
        TIM = self.project.getTIM()
        cursor.mergeBlockFormat(docTitleBlockFormat)
        cursor.mergeCharFormat(docTitleCharFormat)
        cursor.insertText('Traceability Information Model (TIM)')
        cursor.insertText('\n\n')
        # DESENHAR DIAGRAMA
        cursor.mergeBlockFormat(clauseBlockFormat)
        cursor.mergeCharFormat(clauseTextCharFormat)
        for typeName in TIM.getTypesList() :
            type = TIM.getType(typeName)
            cursor.insertText(typeName + ": " + type.getDescription())
            cursor.insertText('\n')

        # RealatÃ³rio de Erros
        cursor.insertText('\n\n\n')
        clausesList = self.project.getAllClauses()
        cursor.mergeBlockFormat(docTitleBlockFormat)
        cursor.mergeCharFormat(docTitleCharFormat)
        cursor.insertText('Relatório de Erros')
        cursor.insertText('\n\n')
        cursor.mergeBlockFormat(clauseBlockFormat)
        cursor.mergeCharFormat(clauseTextCharFormat)
        for clause in clausesList.values() :
            warnings = clause.getWarnings()
            if (warnings != []) :
                warningsText = ' | '.join(warnings)
                cursor.insertText(clause.getConsolidatedID() + "->" + warningsText)
                cursor.insertText('\n')
        
        # HistÃ³rico de Ãndices
        cursor.insertText('\n\n\n')
        cursor.mergeBlockFormat(docTitleBlockFormat)
        cursor.mergeCharFormat(docTitleCharFormat)
        cursor.insertText('Mudanças de Índices')
        cursor.insertText('\n\n')
        cursor.mergeBlockFormat(clauseBlockFormat)
        cursor.mergeCharFormat(clauseTextCharFormat)
        for doc in self.doc2ClauseList.keys() :
            for clause in self.doc2ClauseList[doc]:
                history = clause.getIDHistory()
                if (history != None) :
                    cursor.insertText(clause.getConsolidatedID() + "  -  " + history)
                    cursor.insertText('\n')
            
        textDoc.print_(printer)