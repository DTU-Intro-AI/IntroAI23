import numpy as np
from enum import Enum
import math

BOARD_DIM = 8

class Player(Enum):
    WHITE = 1
    BLACK = 2
    NONE = 0

class Pieces(Enum):
    BLACK = " B "
    WHITE = " W "
    BLACK_KING = " BK"
    WHITE_KING = " WK"
    EMPTY = "   "

class Checkers:
    def __init__(self):
        self.board = [[Pieces.EMPTY for _ in range(BOARD_DIM)] for _ in range(BOARD_DIM)]
        self.turn = Player.BLACK
        self.game_ended = False
        self.win = Player.NONE

    def _create_place_piece(self, player, cord):
        if player.lower() == "w":
            self.board[cord[0]][cord[1]] = Pieces.WHITE
        else:
            self.board[cord[0]][cord[1]] = Pieces.BLACK


    def _setupBoard(self, init_type):
        if init_type.lower() == "pieces":
            for i in range(BOARD_DIM):
                for j in range(BOARD_DIM):
                    if (i+j)%2 == 0:
                        if i < 3:
                            self.board[i][j] = Pieces.WHITE
                        elif i > 4:
                            self.board[i][j] = Pieces.BLACK
                        else:
                            self.board[i][j] = Pieces.EMPTY
                    else:
                        self.board[i][j] = Pieces.EMPTY
        elif init_type.lower() == "clear":
            for i in range(BOARD_DIM):
                for j in range(BOARD_DIM):
                    self.board = Pieces.EMPTY
        
        else:
            raise ValueError

    def printBoard(self):
        print(" -------------------------------------------------")
        for row in self.board:
            print(" | ", end="")
            for col in row:
                print(col.value, end=" | ")
            print("\n -------------------------------------------------")

    def isFinished(self):
        pass

    def onBoard(self, cord):
        valid_range = range(0,BOARD_DIM-1)
        x, y = cord
        if (x in valid_range and y in valid_range):
            return True
        else:
            return False


    def possibleMoves(self, cord):
        if (not self.onBoard(cord)):
            raise ValueError("Board index out of range")
        
        x, y = cord
        opponents = [Pieces.WHITE, Pieces.WHITE_KING] if self.turn == Player.BLACK else [Pieces.BLACK, Pieces.BLACK_KING]
        player_multiplier = -1 if self.turn == Player.BLACK else 1 # for the player move direction
        piece = self.board[x][y]
        moves = []
        # get diagonals
        if (piece == Pieces.BLACK_KING or piece == Pieces.WHITE_KING):
            diagonals = [i for i in [(x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)] if self.onBoard(i)]
        else:
            diagonals = [i for i in [(x+ 1 * player_multiplier, y+1), (x + 1 * player_multiplier, y-1)] if self.onBoard(i)]

        for dx, dy in diagonals:
            # if the square is empty, we can move there
            if (self.board[dx][dy] == Pieces.EMPTY):
                moves.append((dx, dy))
            # if there's an opponent at a diagonal, we can jump over it
            if (self.board[dx][dy] in opponents):
                ddx = dx + dx - x
                ddy = dy + dy - y
                if (self.onBoard((ddx, ddy)) and self.board[ddx][ddy] == Pieces.EMPTY):
                    moves.append((ddx, ddy))
        return moves

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
        from_x, from_y = from_cord
        to_x, to_y = to_cord
        # check that from_cord and to_cord are in range (0-7)
        if (not self.onBoard(from_cord) or not self.onBoard(to_cord)):
            raise ValueError("Board index out of range")
        # check that to_cord is unoccupied
        if (self.board[to_x][to_y] != Pieces.EMPTY):
            raise ValueError("Trying to move to occupied field {}".format(to_cord))
        # check that the piece at cord belongs to the current player
        if (self.board[from_x][from_y] in [Pieces.WHITE, Pieces.WHITE_KING] if self.turn == Player.BLACK else [Pieces.BLACK, Pieces.BLACK_KING]):
            raise ValueError("Trying to move an opponent's piece at {}".format(from_cord))
        # check that cord is not empty
        if (self.board[from_x][from_y] == Pieces.EMPTY):
            raise ValueError("Trying to move an empty piece at {}".format(from_cord))

        return to_cord in self.possibleMoves(from_cord)

    def move(self, from_cord, to_cord):
        """
        :param from_cord: tuple (x, y) Where your move starts from
        :param to_cord: list of tuples (x, y) Where you are going. In case of multiple jumps in one turn, provide list of coordinate tuples
        """

        self.board[from_cord[0]][from_cord[1]] = Pieces.EMPTY
        last_cord = from_cord
        board_copy = self.board.copy
        for current_cord in to_cord:
            try: 
                self.validMove(from_cord, to_cord)
            except ValueError as e:
                print(e)
                self.board = board_copy

            if abs(last_cord[0]-to_cord[0]) > 1 and abs(last_cord[1]-to_cord[1]) > 1:
                self.board[int(last_cord[0] + abs(last_cord[0]-to_cord[0])/last_cord[0]-to_cord[0])][int(last_cord[1] + abs(last_cord[1]-to_cord[1])/last_cord[1]-to_cord[1])] = Pieces.EMPTY
                self.board[current_cord][current_cord] = Pieces.BLACK if self.turn == Player.BLACK else Pieces.WHITE

            last_cord = current_cord
            ## Update game state with function?
        if not self.game_ended:
            self.turn = Player.BLACK if self.turn == Player.WHITE else Player.WHITE

        