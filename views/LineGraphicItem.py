
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LineGraphicItem(QGraphicsItem):

    def __init__(self, start, end):
        super(LineGraphicItem, self).__init__()
        self.start = start
        self.end = end
        self.setZValue(0)
    
    def paint(self, painter, option, widget):
        print "VAI"
        startPoint = self.start.mapToScene(self.start.getCenter())
        print startPoint
        endPoint = self.end.mapToScene(self.end.getCenter())
        print endPoint
        lineFormat = QLineF(startPoint, endPoint)
        print "VAI PLANETA!"
        print startPoint
        print endPoint
        painter.drawLine(lineFormat)
        print self.zValue()
        
    def boundingRect(self):
        return QRectF()
    
    def shape(self):
        shape = QPainterPath()