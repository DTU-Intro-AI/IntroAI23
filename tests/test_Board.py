import unittest
import os
import sys
os.chdir('../')
path = os.getcwd()
sys.path.append(path)

from src.Board import Checkers
from src.Board import Pieces

class TestBoard(unittest.TestCase):

    def test_move(self):
        game = Checkers()
        game._create_place_piece("b",(2,1))
        game._create_place_piece("w", (3,2))
        game.move((2,1),(4,3))
        test = game.board[3][2]
        print("test")
        self.assertEqual(test, Pieces.EMPTY)