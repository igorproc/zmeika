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
        self.pole.Prep()

    def paintEvent(self, qp):
        qp = QPainter()
        qp.begin(self)
        self.pole.drawSnake(qp, self)
        self.pole.drawBonus(qp, self)
        self.pole.drawPrep(qp, self)
        qp.end()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            if self.pole.snake.direction == 2:
                return
            self.pole.snake.direction = 1
        elif key == Qt.Key_D:
            if self.pole.snake.direction == 1:
                return
            self.pole.snake.direction = 2
        elif key == Qt.Key_S:
            if self.pole.snake.direction == 4:
                return
            self.pole.snake.direction = 3
        elif key == Qt.Key_W:
            if self.pole.snake.direction == 3:
                return
            self.pole.snake.direction = 4


class Bonus(object):

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    @classmethod
    def getRandPosBonus(self):
        while 1:
            e = Bonus(randint(0, SET[0] - 1) * 10, (randint(0, SET[1] - 1) * 10), randint(1, 3))
            rerun = False
            for i in prep:
                if e.x == i[0] and e.y == i[1]:
                    rerun = True
                    break
            if rerun == False:
                return e


prep = []
colors = [(0, 0, 255), (156, 200, 165), (155, 24, 15)]
FULL_HEIGHT = 600
FULL_WIDTH = 600
SQUARE_HEIGHT = 10
SQUARE_WIDTH = 10
SET = (FULL_WIDTH / SQUARE_WIDTH, FULL_HEIGHT / SQUARE_HEIGHT)
bonuses = [Bonus(10, 10, 1)]


class Pole(QFrame):

    def __init__(self, form):
        super().__init__()
        self.timer = QBasicTimer()
        self.speed = 300
        self.timer.start(self.speed, self)
        self.snake = Snake()
        self.form = form

    def square_width(self):
        return SQUARE_WIDTH

    def square_height(self):
        return SQUARE_HEIGHT

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.snake.step()
            self.checkBonus()
            is_collision = self.snake.PrepCol()
            if is_collision:
                self.timer.stop()
            is_suicide = self.snake.isSuicide()
            if is_suicide:
                print('Suicide')
                self.timer.stop()
            self.form.repaint()

    def drawSnake(self, qp, sup):
        for i in self.snake.coords:
            qp.setBrush(QColor(255, 105, 180))
            qp.drawRect(i[0], i[1], self.square_width(), self.square_height())

    def drawBonus(self, qp, sup):
        for i in bonuses:
            qp.setBrush(QColor(*colors[i.type - 1]))
            qp.drawRect(i.x, i.y, self.square_width(), self.square_height())

    def drawPrep(self, qp, sup):
        for i in prep:
            qp.setBrush(QColor(255, 204, 0))
            qp.drawRect(i[0], i[1], self.square_width(), self.square_height())

    def Prep(self):
        for i in range(10):
            prep.append((randint(3, SET[0]) * 10, randint(1, SET[1]) * 10))

    def checkBonus(self):
        for i in self.snake.coords:
            for ind, j in enumerate(bonuses):
                if i[0] == j.x and i[1] == j.y:
                    if j.type == 1:
                        if self.snake.direction == 1:
                            self.snake.coords.append((i[0] + SQUARE_WIDTH, i[1]))
                            bonuses.pop(ind)
                            bonuses.append(Bonus.getRandPosBonus())
                        elif self.snake.direction == 2:
                            self.snake.coords.append((i[0] - SQUARE_WIDTH, i[1]))
                            bonuses.pop(ind)
                            bonuses.append(Bonus.getRandPosBonus())
                        elif self.snake.direction == 3:
                            self.snake.coords.append((i[0], i[1] + SQUARE_HEIGHT))
                            bonuses.pop(ind)
                            bonuses.append(Bonus.getRandPosBonus())
                        elif self.snake.direction == 4:
                            self.snake.coords.append((i[0], i[1] - SQUARE_HEIGHT))
                            bonuses.pop(ind)
                            bonuses.append(Bonus.getRandPosBonus())

                    if j.type == 2:
                        self.timer.stop()
                        self.speed = self.speed // 2
                        self.timer.start(self.speed, self)
                        bonuses.pop(ind)
                        bonuses.append(Bonus.getRandPosBonus())
                    if j.type == 3:
                        ll = len(self.snake.coords) // 2
                        for _ in range(ll):
                            self.snake.coords.pop()
                        bonuses.pop(ind)
                        bonuses.append(Bonus.getRandPosBonus())


class Snake(object):

    def __init__(self):
        self.coords = [(0, 0), (10, 0)]
        self.direction = 2

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

    def PrepCol(self):
        for i in prep:
            if self.coords[0][0] == i[0] and self.coords[0][1] == i[1]:
                return True
        return False

    def isSuicide(self):
        for i in range(len(self.coords) - 1, 1, -1):
            if self.coords[0][0] == self.coords[i][0] and self.coords[0][1] == self.coords[i][1]:
                return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zm()
    sys.exit(app.exec_())