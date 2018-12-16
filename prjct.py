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


prep = [[]]
bonuses = [[]]
snake = [[]]


class Pole(QFrame):
    msg2Statusbar = pyqtSignal(str)
    HEIGHT = 50
    WEIGHT = 70
    Speed = 150

    def __init__(self):
        self.snake = [[5, 10], [5, 11]]
        self.timer = QBasicTimer()


    def square_width(self):
        return self.contentsRect().width() / Pole.WEIGHT

    def square_height(self):
        return self.contentsRect().height() / Pole.HEIGHT

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step()
            self.checkBonus()


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

    def keyPressEvent(self, event):
        key =  event.key()
        if key == Qt.Key_A:
            if self.direction != 2:
                self.direction = 1
        elif key == Qt.Key_D:
            if self.direction != 1:
                self.direction = 2
        elif key == Qt.Key_S:
            if self.direction != 4:
                self.direction = 3
        elif key == Qt.Key_W:
            if self.direction != 3:
                self.direction = 4


class Bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getRandomPositionBonus(self):
        e = Bonus(randint(0, 70), randint(0, 50))
        return e


class Snake(object):

    def step(self, direction):
        snake_head = self.head[0[0], 0[1]]
        if self.direction == 1:
            self.snake_head[0], self.snake_head[1] = self.snake_head[0] - 1, self.snake_head[1]
            if self.snake_head[0] < 0:
                self.snake_head[0] = Pole.width - 1
        if self.direction == 2:
            self.snake_head[0], self.snake_head[1] = self.snake_head[0] + 1, self.snake_head[1]
            if self.snake_head[0] == Pole.width:
                self.snake_head[0] = 0
        if self.direction == 3:
            self.snake_head[0], self.snake_head[1] = self.snake_head[0], self.snake_head[1] + 1
            if self.snake_head[1] == Pole.width:
                self.snake_head[1] = 0
        if self.direction == 4:
            self.snake_head[0], self.snake_head[1] = self.snake_head[0], self.snake_head[1] - 1
            if self.snake_head[1] < 0:
                self.snake_head[1] = Pole.width

    def checkBonus(self):
        if bonuses[0] == snake[0] and bonuses[1] == snake[1]:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zm()
    sys.exit(app.exec_())

