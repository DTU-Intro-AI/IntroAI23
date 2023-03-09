import numpy as np
from enum import Enum

class Player(Enum):
    RED = 1
    BLACK = 2
    NONE = 0

class Board:
    def __init__(self):
        self.board = np.array(8,8)
        self.turn = BLACK
        self.game_ended = False
        self.win = NONE

    def isFinished(self):
        pass

    def validMove(self, index_x, index_y):
        pass


