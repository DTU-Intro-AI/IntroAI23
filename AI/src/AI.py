import os
import sys
os.chdir('../../Game/src/')
path = os.getcwd()
sys.path.append(path)
from Board import Checkers, Player, Pieces

BOARD_DIM = 8
class State:
    def __init__(self, game: Checkers, oldDepth, player: Player):
        '''
        game is of the type Checkers
        sets the initial attributes
        '''
        self.game = game
        self.depth = oldDepth + 1
        self.next_state = []
        self.utilityValue = 0
        
    def player(self):
        return self.game.turn
    
    def actions_result(self):
        '''
        we look at all pieces of current player, and for every possible move
        add the state to self.next_state
        We limit the depth of the tree to avoid ridiciously long computation time
        '''
        if self.depth < 4:
            for i in range(BOARD_DIM):
                for j in range(BOARD_DIM):
                    if self.game.turn == self.game.board[i][j]:
                        moves = self.game.possibleMoves((i,j))
                        for move in moves:
                            childState = State(
                                self.game.makeMove((i,j), move),
                                self.depth
                            )
                            childState.utility()
                            self.next_state.append(childState)
        else:
            pass

    def terminal_test(self):
        return self.game.isFinished()
    
    def utility(self):
        if (self.player() == Player.BLACK):
            self.utilityValue = 12 - self.game.ws
        else:
            self.utilityValue = 12 - self.game.bs

class Minimax():
    def __init__(self, color :Player, initial_state = None):
        self.stack = []
        self.initial_state = initial_state
        if self.initial_state is None:

game = Checkers() 
s = State(game, 0)
print(s.utility())