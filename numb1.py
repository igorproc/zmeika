from random import random, randint
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Zm(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 300, 800, 600)
        self.setWindowTitle('Snake')
        self.show()


class Pole(QFrame):
    msg2Statusbar = pyqtSignal(str)
    HEIGHT = 50
    WEIGHT = 70
    Speed = 150

    def __init__(self):
        self.snake = [[5, 11], [5, 10]]
        self.timer = QBasicTimer()

    def square_width(self):
        return self.contentsRect().width() / Pole.WEIGHT

    def square_height(self):
        return self.contentsRect().height() / Pole.HEIGHT

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawSnake(qp)
        qp.end()

    def drawSnake(self, qp):
        base = [self.snake[0[0]], self.snake[0[1]], self.square_width(), self.square_height()]
        for i in range(70):
            for j in range(50):
                qp.setBrush(QColor(255, 0, 0))
                qp.drawRect(*base)
                base[0] += self.square_width()
            base[1] += self.square_height()
            base[0] = self.snake[0[0]]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zm()
    sys.exit(app.exec_())