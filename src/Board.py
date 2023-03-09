import numpy as np
from enum import Enum
import math

BOARD_DIM = 8

class Player(Enum):
    WHITE = 1
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
        self.turn = Player.BLACK
        self.game_ended = False
        self.win = Player.NONE
        self.black_pieces = 12
        self.white_pieces = 12

    def _create_place_piece(player, cord):
        if player.Lower == "w":
            self.board[cord[0]][cord[1]] = Pieces.WHITE
        else:
            self.board[cord[0]][cord[1]] = Pieces.BLACK


    def _setupBoard(self):
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
        from_x, from_y = from_cord
        to_x, to_y = to_cord
        # check that from_cord and to_cord are in range (0-7)
        if (from_x not in valid_range or from_y not in valid_range or to_x not in valid_range or to_y not in valid_range):
            raise ValueError("Board index out of range")
        # check that to_cord is unoccupied
        if (self.board[to_x][to_y] != Pieces.EMPTY):
            raise ValueError("Trying to move to an occupied field")
        
        move_piece = self.board[from_x][from_y]
        valid_range = range(0,BOARD_DIM-1)
        last_cord = from_cord
        opponents = [Pieces.WHITE, Pieces.WHITE_KING] if self.turn == Player.BLACK else [Pieces.BLACK, Pieces.BLACK_KING]
        player_multiplier = 1 if self.turn == Player.BLACK else -1 # for the player move direction

        # check that to_cord is a coordinate the piece is able to move

        # kings can move to any diagonals
        if (move_piece == Player.BLACK_KING or move_piece == Player.WHITE_KING):
            # single move
            if (math.abs(from_x - to_x) == 1 and math.abs(from_y - to_y) == 1):
                return True
            # jump over one player and land on empty space
            elif (math.abs(from_x - to_x) == 2 and math.abs(from_y - to_y) == 2):
                # check intermediate piece is an opponent
                intermediate_piece = self.board[last_cord[0] + abs(last_cord[0]-to_cord[0])/last_cord[0]-to_cord[0]][last_cord[1] + abs(last_cord[1]-to_cord[1])/last_cord[1]-to_cord[1]]
                if (intermediate_piece in opponents):
                    return True
                else:
                    return False
            else:
                return False
                
        # checks if the direction of the move is correct
        elif (move_piece == Player.BLACK or move_piece == Player.WHITE):
            # single move
            if (from_x - to_x == 1 * player_multiplier and math.abs(from_y - to_y) == 1):
                return True
            # jump over one player and land on empty space
            elif (from_x - to_x == 2 * player_multiplier and math.abs(from_y - to_y) == 2):
                # check intermediate piece is an opponent
                intermediate_piece = self.board[last_cord[0] + abs(last_cord[0]-to_cord[0])/last_cord[0]-to_cord[0]][last_cord[1] + abs(last_cord[1]-to_cord[1])/last_cord[1]-to_cord[1]]
                if (intermediate_piece in opponents):
                    return True
                else:
                    return False
            else:
                return False
        
        else:
            return False

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
                self.board[last_cord[0] + abs(last_cord[0]-to_cord[0])/last_cord[0]-to_cord[0]][last_cord[1] + abs(last_cord[1]-to_cord[1])/last_cord[1]-to_cord[1]] = Pieces.EMPTY
                self.board[current_cord][current_cord] = Pieces.BLACK if self.turn == Player.Black else Pieces.WHITE

            last_cord = current_cord
            ## Update game state with function?
        if not self.game_ended:
            self.turn = Player.BLACK if self.turn == Player.WHITE else Player.WHITE


            
            
        
        