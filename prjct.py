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


prep = []
bonuses = []
snake = []

#bonuses.append(Bonus.getRandomPositionBonus())


class Pole(QFrame):

    def square_width(self):
        return self.contentsRect().width() / 70

    def square_height(self):
        return self.contentsRect().height() / 50

class Bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getRandomPositionBonus(self):
        e = Bonus(randint(0, 70), randint(0, 50))
        return e


class Snake(object):

    def step(self, direction):
        pass

    def checkBonus(self):
        if bonuses[0] == snake[0] and bonuses[1] == snake[1]:
            snake.append(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zm()
    sys.exit(app.exec_())


