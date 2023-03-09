import numpy as np
from enum import Enum

BOARD_DIM = 8

class Player(Enum):
    RED = 1
    BLACK = 2
    NONE = 0

class Pieces(Enum):
    BLACK = 0
    WHITE = 1
    BLACK_KING = 2
    WHITE_KING = 3
    EMPTY = 4

class Checkers:
    def __init__(self):
        self.board = np.array(BOARD_DIM,BOARD_DIM)
        self.turn = BLACK
        self.game_ended = False
        self.win = NONE

    def printBoard(self):
        print(self.board)

    def isFinished(self):
        pass

    def validMove(self, from_cord, to_cord):
        """
        Checks that move is valid:
            normal pieces can move forward diagonals
            kings can move to any diagonals
            any pieces can capture an opponent's piece that is next to it
        :param from_cord: tuple (x, y) Where your move starts from
        :param to_cord: tuple (x, y) Where you are going. In case of multiple jumps in one turn, provide list of coordinate tuples
        :returns: boolean is valid move
        """
        # check that from_cord and to_cord are in range (0-7)
        from_x, from_y = from_cord
        to_x, to_y = to_cord
        valid_range = range(0,BOARD_DIM-1)
        if (from_x not in valid_range or from_y not in valid_range or to_x not in valid_range or to_y not in valid_range):
            raise Exception("Board index out of range")
        pass

    def move(self, from_cord, to_cord):
        """
        :param from_cord: tuple (x, y) Where your move starts from
        :param to_cord: list of tuples (x, y) Where you are going. In case of multiple jumps in one turn, provide list of coordinate tuples
        """

        if self.validMove:
            self.board[from_cord[0]][from_cord[1]] = Pieces.EMPTY
            last_cord = from_cord
            for current_cord in to_cord:
                if abs(last_cord[0]-to_cord[])

                last_cord = current_cord
            
        
        