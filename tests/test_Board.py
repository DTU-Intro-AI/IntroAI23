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
        game._create_place_piece("b", (2, 1))
        game._create_place_piece("w", (3, 2))
        game.validMove((2, 1), (4, 3))
        game.move((2, 1), [(4, 3)])
        game.printBoard()
        test = game.board[3][2]
        self.assertEqual(test, Pieces.EMPTY)
    
    def test_valid_move(self):
        game = Checkers()
        game._create_place_piece("w",(2,1))
        game._create_place_piece("b", (3,2))
        valid = game.validMove((3,2),(1,0))
        self.assertTrue(valid)

    # tries to move other player's piece
    def test_invalid_move(self):
        game = Checkers()
        game._setupBoard("pieces")
        with self.assertRaises(ValueError):
            game.validMove((0,0),(4,3))

    # tries to move other player's piece
    def test_valid_jump(self):
        game = Checkers()
        game._setupBoard("pieces")
        game._create_place_piece("w",(4,2))
        valid = game.validMove((5,1), (3,3))
        self.assertTrue(valid)

test = TestBoard()
test.test_valid_move()
test.test_invalid_move()
test.test_valid_jump()
