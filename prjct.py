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
        self.snake = Snake()
        self.timer = QBasicTimer()
        self.timer.start(300, self)

    def square_width(self):
        return FULL_HEIGHT / Pole.WEIGHT

    def square_height(self):
        return FULL_WEIGHT / Pole.HEIGHT

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.snake.step()

    def drawSnake(self, qp):
        for i in self.snake.coords:
            qp.setBrush(QColor(255, 105, 180))
            qp.drawRect(i[0], i[1], self.square_width(), self.square_height())

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.snake.direction = 1
        elif key == Qt.Key_D:
            self.snake.direction = 2
        elif key == Qt.Key_S:
            self.snake.direction = 3
        elif key == Qt.Key_W:
            self.snake.direction = 4


class Bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getRandomPositionBonus(self):
        e = Bonus(randint(0, 70), randint(0, 50))
        return e


class Snake(object):

    def __init__(self):
        self.coords = [(50, 50)]
        self.direction = 1

    def step(self):
        for i in range(len(self.coords) - 1, 1, -1):
            self.coords[i] = self.coords[i - 1]

        if self.direction == 1:
            self.coords[0] = (self.coords[0][0] - 1, self.coords[0][1])
            if self.coords[0][0] < 0:
                self.coords[0] = (Pole.WEIGHT - 1, self.coords[0][1])
        if self.direction == 2:
            self.coords[0] = (self.coords[0][0] + 1, self.coords[0][1])
            if self.coords[0][0] == Pole.WEIGHT:
                self.coords[0] = (0, self.coords[0][1])
        if self.direction == 3:
            self.coords[0] = (self.coords[0][0], self.coords[0][1] + 1)
            if self.coords[0][1] == Pole.WEIGHT:
                self.coords[0] = (self.coords[0][0], 0)
        if self.direction == 4:
            self.coords[0] = (self.coords[0][0], self.coords[0][1] - 1)
            if self.coords[0][1] < 0:
                self.coords[0] = (self.coords[0][0], Pole.WEIGHT)

    #def checkBonus(self):
        #if bonuses[0] == snake[0] and bonuses[1] == snake[1]:
            #pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zm()
    sys.exit(app.exec_())
