#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem
from project import Project

class ClauseDiagramScene(QGraphicsScene):

    def __init__(self,  parent, clauseList = []):
        super(ClauseDiagramScene, self).__init__(parent)
        self.setBackgroundBrush(Qt.lightGray)
        self.updateClausesImage(clauseList)

    def updateClausesImage(self, clauseList):
        self.nodeList = {}
        self.offset = {}
        self.offset[0] = 0
        for clause in clauseList:
            if clause.getID() not in self.nodeList :
                self.nodeList[clause.getID()] = self.drawNode(clause, 0, self.offset[0])
                self.drawParentsPath(clause, -1)
                self.drawChildrenPath(clause, 1)
                self.offset[0] += 1
    
    def drawParentsPath(self, clause, level):
        parentsList = clause.getParentClausesList()
        if level not in self.offset.keys():
            self.offset[level] = 0
        for parentID in parentsList :
            parent = clause.getParentLinkClause(parentID)
            if parentID not in self.nodeList.keys():
                self.nodeList[parentID] = self.drawNode(parent, level, self.offset[level])
                self.drawParentsPath(parent, level-1)
                self.offset[level] += 1
            self.drawLine(clause, parent)
    
    def drawChildrenPath(self, clause, level):
        childrenList = clause.getChildClausesList()
        if level not in self.offset.keys():
            self.offset[level] = 0
        for childID in childrenList :
            child = clause.getChildLinkClause(childID)
            if childID not in self.nodeList.keys():
                self.nodeList[childID] = self.drawNode(child, level, self.offset[level])
                self.drawChildrenPath(child, level+1)
                self.offset[level] += 1
            self.drawLine(clause, child)

    def drawNode(self, clause, level, offset):
        nodeItem = NodeGraphicItem(75, 75)
        nodeItem.setText(clause.getType().getPrefix())
        nodeItem.setTitle(clause.getCode(docPrefix=True))
        nodeItem.translate(170*level, 125*offset)
        self.addItem(nodeItem)
        return nodeItem

    def drawLine(self, start, end):
        startNode = {}
        endNode = {}
        startNode['node'] = self.nodeList[start.getID()]
        endNode['node'] = self.nodeList[end.getID()]
        if start.isDependentOf(end) :
            startNode['arrow'] = True
        if end.isDependentOf(start) :
            endNode['arrow'] = True
        lineItem = LineGraphicItem(startNode, endNode)
        self.addItem(lineItem)
