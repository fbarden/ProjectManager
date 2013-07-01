
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from tim import *
from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem

class TIMDiagramScene(QGraphicsScene):

    def __init__(self,  parent, TIM=None):
        super(TIMDiagramScene, self).__init__(parent)
        self.TIM = TIM
       
    def updateTIMImage(self):
        rootsList = self.TIM.getRootsList()
        offset = 0
        for rootName in rootsList :
            self.drawTIMNode(rootName, 0, offset)
            offset += 1

    def drawTIMNode(self, nodeName, level, offset):
        node = self.TIM.getType(nodeName)
        nodeItem = NodeGraphicItem(50, 30)
        nodeItem.setText(node.getPrefix())
        nodeItem.setTitle(node.getName())
        nodeItem.moveBy(-220+level*70, -150 + offset*50)
        self.addItem(nodeItem)
        for childName in node.getPossibleChildrenList() :
            self.drawTIMNode(childName, level+1, offset+1)
            offset += 1
        return offset