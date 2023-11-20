import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Paint point example')
        self.pushButton.clicked.connect(self.pain)
        self.point = None
        self.do_paint = False
        self.y = 0
        self.x = 0
        self.r = 0

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def pain(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        self.x = randint(0, 900)
        self.y = randint(0, 900)
        self.r = randint(10, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.r, 10, self.r, self.r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
