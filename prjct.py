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
        self.pole = Pole(self)

    def paintEvent(self, qp):
        qp = QPainter()
        qp.begin(self)
        self.pole.drawSnake(qp, self)
        self.pole.drawBonus(qp, self)
        qp.end()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.pole.snake.direction = 1
        elif key == Qt.Key_D:
            self.pole.snake.direction = 2
        elif key == Qt.Key_S:
            self.pole.snake.direction = 3
        elif key == Qt.Key_W:
            self.pole.snake.direction = 4


prep = []
bonuses = [(480, 480)]
FULL_HEIGHT = 600
FULL_WIDTH = 600
SQUARE_HEIGHT = 10
SQUARE_WIDTH = 10
SET = (FULL_WIDTH / SQUARE_WIDTH, FULL_HEIGHT / SQUARE_HEIGHT)


class Pole(QFrame):

    def __init__(self, form):
        super().__init__()
        self.snake = Snake()
        self.timer = QBasicTimer()
        self.timer.start(20, self)
        self.form = form

    def square_width(self):
        return SQUARE_WIDTH

    def square_height(self):
        return SQUARE_HEIGHT

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.snake.step()
            self.snake.checkBonus()
            self.form.repaint()

    def drawSnake(self, qp, sup):
        for i in self.snake.coords:
            qp.setBrush(QColor(255, 105, 180))
            qp.drawRect(i[0], i[1], self.square_width(), self.square_height())

    def drawBonus(self, qp, sup):
        for i in bonuses:
            qp.setBrush(QColor(0, 0, 255))
            qp.drawRect(i[0], i[1], self.square_width(), self.square_height())


class Bonus(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getRandPosBonus(self):
        bonuses.append((randint(0, SET[0]) * 10, randint(0, SET[1]) * 10))


class Snake(object):

    def __init__(self):
        self.coords = [(50, 50), (40, 50), (30, 50), (20, 50)]
        self.direction = 2

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.direction = 1
        elif key == Qt.Key_D:
            self.direction = 2
        elif key == Qt.Key_S:
            self.direction = 3
        elif key == Qt.Key_W:
            self.direction = 4

    def step(self):
        if self.direction:
            for i in range(len(self.coords) - 1, 0, -1):
                self.coords[i] = self.coords[i - 1]

        if self.direction == 1:
            self.coords[0] = (self.coords[0][0] - SQUARE_WIDTH, self.coords[0][1])
            if self.coords[0][0] < 0:
                self.coords[0] = (FULL_WIDTH - SQUARE_WIDTH, self.coords[0][1])
        if self.direction == 2:
            self.coords[0] = (self.coords[0][0] + SQUARE_WIDTH, self.coords[0][1])
            if self.coords[0][0] == FULL_WIDTH:
                self.coords[0] = (0, self.coords[0][1])
        if self.direction == 3:
            self.coords[0] = (self.coords[0][0], self.coords[0][1] + SQUARE_HEIGHT)
            if self.coords[0][1] == FULL_HEIGHT:
                self.coords[0] = (self.coords[0][0], 0)
        if self.direction == 4:
            self.coords[0] = (self.coords[0][0], self.coords[0][1] - SQUARE_HEIGHT)
            if self.coords[0][1] < 0:
                self.coords[0] = (self.coords[0][0], FULL_HEIGHT - SQUARE_HEIGHT)

    def checkBonus(self):
        for i in self.coords:
            for j in bonuses:
                if i[0] == j[0] and i[1] == j[1]:
                    if self.direction == 1:
                        self.coords.append((i[0] + 1, i[1]))
                        bonuses.remove((j[0], j[1]))
                        self.Bonus.getRandPosBonus()
                    elif self.direction == 2:
                        self.coords.append((i[0] - SQUARE_WIDTH, i[1]))
                        bonuses.remove((j[0], j[1]))
                        self.Bonus.getRandPosBonus()
                    elif self.direction == 3:
                        self.coords.append((i[0], i[1] + SQUARE_HEIGHT))
                        bonuses.remove((j[0], j[1]))
                        self.Bonus.getRandPosBonus()
                    elif self.direction == 4:
                        self.coords.append((i[0], i[1] - SQUARE_HEIGHT))
                        bonuses.remove((j[0], j[1]))
                        self.Bonus.getRandPosBonus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zm()
    sys.exit(app.exec_())
