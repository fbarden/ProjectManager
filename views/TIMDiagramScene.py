
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *
from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem

class TIMDiagramScene(QGraphicsScene):

    def __init__(self,  parent, TIM=None):
        super(TIMDiagramScene, self).__init__(parent)
        self.TIM = TIM
        self.updateTIMImage()

    def getTIM(self):
        return self.TIM

    def setTIM(self, value):
        self.TIM = value

    def delTIM(self):
        del self.TIM

    def updateTIMImage(self):
        print "Vai pro update!"
        rootsList = self.TIM.getRootsList()
        self.offset = 0
        for rootName in rootsList :
            self.drawTIMNode(rootName, 0)
            self.offset += 1

    def drawTIMNode(self, nodeName, level):
        print "TIMNODE"
        node = self.TIM.getType(nodeName)
        print nodeName + " " + str(self.offset)
        nodeItem = NodeGraphicItem(80, 50)
        nodeItem.setText(node.getPrefix())
        print node.getPrefix()
        nodeItem.setTitle(node.getName())
        print node.getName()
        nodeItem.moveBy(-220+level*120, -150 + self.offset*70)
        self.addItem(nodeItem)
        for childName in node.getPossibleChildrenList() :
            childItem = self.drawTIMNode(childName, level+1)
            self.addItem(LineGraphicItem(nodeItem, childItem))
            self.offset += 1
        return nodeItem
