
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NodeGraphicItem(QGraphicsItem):

    def __init__(self, width, height, text=None, title=None):
        super(NodeGraphicItem, self).__init__()
        self.title = title
        self.text = text
        self.width = width
        self.height = height
        self.uplinks = {}
        self.downlinks = {}
        self.setZValue(1)

    def setTitle(self, title):
        self.title = title
    
    def setText(self, text):
        self.text = text

    def paint(self, painter, option, widget):
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
        painter.setBrush(Qt.white)
        painter.drawRect(0, 0, self.width, self.height)
        if (self.text is not None):
            painter.drawText(-self.width, 0, self.width*3, self.height, Qt.AlignCenter|Qt.TextWordWrap, self.text)
        if (self.title is not None):
            painter.drawText(-self.width, -self.height/2, self.width*3, self.height/2, Qt.AlignCenter|Qt.TextWordWrap, self.title)
        print self.zValue()
    
    def getCenter(self):
        return QPointF(self.width/2, self.height/2) 

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

        
