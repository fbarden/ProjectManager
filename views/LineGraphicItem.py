
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import math

class LineGraphicItem(QGraphicsItem):

    def __init__(self, start,  end):
        super(LineGraphicItem, self).__init__()
        self.start = start
        self.end = end
        self.setZValue(0)
    
    def paint(self, painter, option, widget):
        startNode = self.start['node']
        endNode = self.end['node']
        nodeHeight = startNode.boundingRect().height()
        nodeWidth = startNode.boundingRect().width()
        startPoint = startNode.mapToScene(startNode.getCenter())
        endPoint = endNode.mapToScene(endNode.getCenter())
        lineFormat = QLineF(startPoint, endPoint)
        lineAngle = lineFormat.angle()
        lineLength = lineFormat.length()
        painter.translate(startPoint)
        lineFormat.translate(-startPoint)
#         testVerticalLine = QLineF(nodeWidth/2, -nodeHeight/2, nodeWidth/2, nodeHeight/2)
#         testHorizontalLine = QLineF(-nodeWidth/2, nodeHeight/2, nodeWidth/2, nodeHeight/2)
#         intersectionPoint = QPointF()
#         print "TRIO"
#         print lineFormat
#         print testHorizontalLine
#         print testVerticalLine
#         if (lineFormat.intersect(testHorizontalLine, intersectionPoint) == QLineF.BoundedIntersection) :
#             print "EH HORIZONTAL!"
#             pass
#         elif (lineFormat.intersect(testVerticalLine, intersectionPoint) == QLineF.BoundedIntersection) :
#             print "EH VERTICAL!"
#             pass
#         else :
#             print "NAO FOI NADA!"
#         intersectionLength = QLineF(startPoint, intersectionPoint).length()
#         print intersectionLength
        intersectionLength = math.sqrt(nodeHeight**2 + nodeWidth**2)/2
        painter.rotate(-lineAngle)
        newLine = QLineF(0, 0, lineLength, 0)
        painter.drawLine(newLine)
        if ('cardinality' in self.start.keys()):
            painter.drawText(intersectionLength -5, -15, self.start['cardinality'])
        if ('arrow' in self.start.keys()):
            path = QPainterPath()
            p1 = QPointF(intersectionLength, 0)
            p2 = QPointF(intersectionLength + 12, 10)
            p3 = QPointF(intersectionLength + 12, -10)
            path.addPolygon(QPolygonF([p1, p2, p3]))
            painter.drawPath(path)
            painter.fillPath(path, QBrush(Qt.black))
            #painter.drawText(intersectionLength+5, -10, "<---")
        if ('cardinality' in self.end.keys()):
            painter.drawText(lineLength- intersectionLength-20, -7, self.end['cardinality'])
        if ('arrow' in self.end.keys()):
            p1 = QPointF(lineLength - intersectionLength, 0)
            p2 = QPointF(lineLength - intersectionLength - 12, 10)
            p3 = QPointF(lineLength - intersectionLength - 12, -10)
            path.addPolygon(QPolygonF([p1, p2, p3]))
            painter.drawPath(path)
            painter.fillPath(path, QBrush(Qt.black))
            #painter.drawText(lineLength- intersectionLength-5, -10, "--->")
        
    def boundingRect(self):
        return QRectF()
    
    def shape(self):
        shape = QPainterPath()