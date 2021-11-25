# constants variables

class Config:
    APP_NAME = 'overCook'
    APP_SIZE = (1000, 600)

    COOKING_TIME = 5
    LEFT_POT_NAME = 'Left Pot'
    RIGHT_POT_NAME = 'Right Pot'
    UP_POT_NAME = 'Up Pot'

    LEFT_COOKING_TEXT_COORDINATE = (15, 260)
    RIGHT_COOKING_TEXT_COORDINATE = (610, 480)
    UP_COOKING_TEXT_COORDINATE = (15, 120)

    COOKING_TEXT = 'Cooking ...'
    COOKED_DONE_TEXT = 'Done!'


class Ingredient:
    EMPTY = '0'
    TOMATO = 'tomato'
    TUNA = 'tuna'
    CORN = 'corn'


class Dish:
    GOOD = 'good'
    BAD = 'bad'


class Act:
    HIT = "hit"