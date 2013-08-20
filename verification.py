#!/usr/bin/python
# -*- coding: utf-8 -*-
from project import Project
from clause import Clause

class Verification(object):

    def __init__(self):
        pass
    
    def checkSpaces(self, project):
        project = Project()
        doc2Clause = project.getDocument2ClausesDict()
        windows = []
        orphans = []
        for documentName in doc2Clause:
            document = project.getDocument(documentName)
            for clauseId in doc2Clause[documentName]:
                clause = document.getClause(clauseId)
                clause = Clause()
                clauseType = clause.getType()
                parentsNeeded = {}
                childrenNeeded = {}
                possibleChildren = clauseType.getPossibleChildrenList()
                for child in possibleChildren:
                    childrenNeeded[child] = clauseType.getChildMinCard(child)
                childLinks = clause.getChildClausesList()
                for childId in childLinks:
                    child = clause.getChildLinkClause(childId)
                    childTypeName = child.getType().getName()
                    if child.getType().getName() in clauseType.getPossibleChildrenList():
                        childrenNeeded[childTypeName] -= 1
                for need in childrenNeeded.keys():
                    if childrenNeeded[need] > 0 :
                        windows.append(clauseId, need)
                
                possibleParents = clauseType.getPossibleParentsList()
                for parent in possibleParents:
                    parentsNeeded[parent] = clauseType.getParentMinCard(parent)
                for parent in possibleParents:
                    parentsNeeded[parent] = clauseType.getParentMinCard(parent)
                parentLinks = clause.getParentClausesList()
                for parentId in parentLinks:
                    parent = clause.getParentLinkClause(parentId)
                    parentTypeName = parent.getType().getName()
                    if parent.getType().getName() in clauseType.getPossibleParentsList():
                        parentsNeeded[parentTypeName] -= 1
                for need in parentsNeeded.keys():
                    if parentsNeeded[need] > 0 :
                        windows.append(clauseId, need)
        return (windows, orphans)
