
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem
from project import Project

class ClauseDiagramScene(QGraphicsScene):

    def __init__(self,  parent, clause = None):
        super(ClauseDiagramScene, self).__init__(parent)
        self.updateClausesImage(clause)

    def updateClausesImage(self, clause):
        self.nodeList = {}
        self.offset = {}
        self.nodeList[clause.getID()] = self.drawNode(clause, 0, 0)
        self.drawParentsPath(clause, -1)
        self.drawChildrenPath(clause, 1)
    
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
    
    def drawChildrenPath(self, clause, level):
        childrenList = clause.getChildClausesList()
        if level not in self.offset.keys():
            self.offset[level] = 0
        for childID in childrenList :
            child = clause.getChildLinkClause(childID)
            if childID not in self.nodeList.keys():
                self.nodeList[childID] = self.drawNode(child, level, self.offset[level])
                self.drawLine(clause, child)
                self.drawParentsPath(child, level+1)
                self.offset[level] += 1

    def drawNode(self, clause, level, offset):
        nodeItem = NodeGraphicItem(75, 75)
        nodeItem.setText(clause.getType().getPrefix())
        nodeItem.setTitle(clause.getCode(docPrefix=True))
        nodeItem.translate(170*level, 110*offset)
        self.addItem(nodeItem)
        return nodeItem

    def drawLine(self, start, end):
        startNode = {}
        endNode = {}
        startNode['node'] = self.nodeList[start.getID()]
        endNode['node'] = self.nodeList[end.getID()]
        lineItem = LineGraphicItem(startNode, endNode)
        self.addItem(lineItem)
