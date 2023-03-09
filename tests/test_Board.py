import unittest
import Checkers
from . import Pieces

class TestBoard(unittest.TestCase):

    def test_move(self):
        game = Checkers()
        game._create_place_piece("b",(2,1))
        game._create_place_piece("w", (3,2))
        game.move((2,1),(4,3))
        assert game.board[3][2] is Pieces.EMPTY