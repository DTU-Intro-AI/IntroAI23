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
        game.printBoard()
        game.move((2, 1), [(4, 3)])
        game.printBoard()
        test1 = game.board[3][2]
        test2 = game.board[4][3]
        self.assertEqual(test1, Pieces.EMPTY)
        self.assertEqual(test2, Pieces.BLACK)

    def test_move_advanced(self):
        game = Checkers()
        game._create_place_piece("b", (2, 1))
        game._create_place_piece("w", (3, 2))
        game._create_place_piece("w", (5, 4))
        game.printBoard()
        game.move((2, 1), [(4, 3), (6, 5)])
        game.printBoard()
        test1 = game.board[3][2]
        test2 = game.board[5][4]
        test3 = game.board[6][5]
        self.assertEqual(test1, Pieces.EMPTY)
        self.assertEqual(test2, Pieces.EMPTY)
        self.assertEqual(test3, Pieces.BLACK)

    def test_move_opposite_direction(self):
        game = Checkers()
        game._create_place_piece("w", (2, 1))
        game._create_place_piece("w", (4, 3))
        game._create_place_piece("b", (5, 4))
        game.printBoard()
        game.move((5, 4), [(3, 2), (1, 0)])
        game.printBoard()
        test1 = game.board[3][2]
        test2 = game.board[5][4]
        test3 = game.board[1][0]
        self.assertEqual(test1, Pieces.EMPTY)
        self.assertEqual(test2, Pieces.EMPTY)
        self.assertEqual(test3, Pieces.BLACK)

    def test_move_3rd_direction(self):
        game = Checkers()
        game._create_place_piece("w", (1, 2))
        game._create_place_piece("w", (3, 4))
        game._create_place_piece("b", (4, 5))
        game.printBoard()
        game.move((4, 5), [(2, 3), (0, 1)])
        game.printBoard()
        test1 = game.board[3][2]
        test2 = game.board[5][4]
        test3 = game.board[0][1]
        self.assertEqual(test1, Pieces.EMPTY)
        self.assertEqual(test2, Pieces.EMPTY)
        self.assertEqual(test3, Pieces.BLACK)
    
    def test_valid_move(self):
        game = Checkers()
        game._create_place_piece("w", (2, 1))
        game._create_place_piece("b", (3, 2))
        valid = game.validMove((3, 2), (1, 0))
        self.assertTrue(valid)

    # tries to move other player's piece
    def test_invalid_move(self):
        game = Checkers()
        game._setupBoard("pieces")
        with self.assertRaises(ValueError):
            game.validMove((0, 0),(4, 3))

    # tries to move other player's piece
    def test_valid_jump(self):
        game = Checkers()
        game._setupBoard("pieces")
        game._create_place_piece("w", (4, 2))
        valid = game.validMove((5, 1), (3, 3))
        self.assertTrue(valid)

test = TestBoard()
test.test_valid_move()
test.test_invalid_move()
test.test_valid_jump()
