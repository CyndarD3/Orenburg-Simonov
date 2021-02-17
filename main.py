import sys

from PyQt5 import uic
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Окружности')
        self.do_paint = False
        self.pushButton_5.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ell(self, qp):
        w = random.randint(20, 400)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 100, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())