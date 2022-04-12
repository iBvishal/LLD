import enum

class BoardStatus(enum.Enum):
    PUBLIC      = 1
    PRIVATE     = 2

class CardStatus(enum.Enum):
    TODO = 1
    WORKING = 2
    DONE = 3
    