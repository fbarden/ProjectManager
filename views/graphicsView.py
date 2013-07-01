'''
Created on Jun 29, 2013

@author: fbarden
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from NodeGraphicItem import NodeGraphicItem
from LineGraphicItem import LineGraphicItem

if __name__ == '__main__':
    app = QApplication(sys.argv)
    graphicsView = QGraphicsView()
    scene = QGraphicsScene(graphicsView)
    graphicsView.setScene(scene)

    scene.setBackgroundBrush(Qt.lightGray)
    docWidth = 50
    docHeight = docWidth*1.5
    
    node = NodeGraphicItem(docWidth, docHeight)
    node.setTitle("Titulo2")
    node.setText("SRS")
    node.moveBy(20, 20)
    
    scene.addItem(node)

    node2 = NodeGraphicItem(docWidth, docHeight)
    node2.setTitle("Titulo hjhjhjhjhj")
    node2.setText("VAI")
    node2.moveBy(90, 50)
    
    node3 = NodeGraphicItem(docWidth, docHeight)
    node3.setTitle("Titul")
    node3.setText("VsAI")
    node3.moveBy(120, 160)
    
    line = LineGraphicItem(node, node2)
    line2 = LineGraphicItem(node, node3)
    
    scene.addItem(node3)
    scene.addItem(node2)

    scene.addItem(line)
    scene.addItem(line2)

    graphicsView.show()
    app.exec_()
    