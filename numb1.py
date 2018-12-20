
from random import randint
FULL_HEIGHT = 600
FULL_WIDTH = 600
SQUARE_HEIGHT = 10
SQUARE_WIDTH = 10
SET = (FULL_WIDTH / SQUARE_WIDTH, FULL_HEIGHT / SQUARE_HEIGHT)
bonuses = []
for i in range(10):
    bonuses.append((randint(0, SET[0]) * 10, randint(0, SET[1]) * 10))
print(bonuses)
