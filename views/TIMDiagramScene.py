
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *
from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem

class TIMDiagramScene(QGraphicsScene):

    def __init__(self,  parent, TIM=None):
        super(TIMDiagramScene, self).__init__(parent)
        self.TIM = TIM
        self.typeNodes = {}
        self.setBackgroundBrush(Qt.lightGray)
        self.updateTIMImage()

    def getTIM(self):
        return self.TIM

    def setTIM(self, value):
        self.TIM = value

    def delTIM(self):
        del self.TIM

    def updateTIMImage(self):
        self.rootsList = self.TIM.getRootsList()
        self.offset = 0
        for rootName in self.rootsList :
            self.drawTIMNode(rootName, 0)
            self.offset += 1

    def drawTIMNode(self, nodeName, level):
        if nodeName not in self.typeNodes.keys() :
            nodeParams = {}
            node = self.TIM.getType(nodeName)
            nodeItem = NodeGraphicItem(80, 50, special = nodeName in self.rootsList)
            nodeItem.setText(node.getPrefix())
            nodeItem.setTitle(node.getName())
            nodeItem.moveBy(level*150, self.offset*90)
            nodeParams['node'] = nodeItem
            self.addItem(nodeItem)
            self.typeNodes[nodeName] = nodeItem
            for childName in node.getPossibleChildrenList() :
                child = self.TIM.getType(childName)
                childParams = {}
                childItem = self.drawTIMNode(childName, level+1)
                childParams['node'] = childItem
                if node.isDependantOf(childName):
                    nodeParams['arrow'] = True
                if child.isDependantOf(nodeName):
                    childParams['arrow'] = True
                self.addItem(LineGraphicItem(nodeParams, childParams))
                self.offset += 1
        else :
            nodeItem = self.typeNodes[nodeName]
        return nodeItem