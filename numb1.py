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
        self.pole = Pole()

    def paintEvent(self, qp):
        qp = QPainter()
        qp.begin(self)
        self.pole.drawSnake(qp)
        qp.end()


prep = []
bonuses = []
FULL_HEIGHT = 500
FULL_WEIGHT = 700


class Pole(QFrame):
    HEIGHT = 50
    WEIGHT = 70

    def __init__(self):
        super().__init__()

    def drawSnake(self, qp):
        for i in self.coords:0
            qp.drawRect(i[0], i[1], self.square_width(), self.square_height())


coords = [(49, 50)]