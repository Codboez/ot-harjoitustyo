import unittest
import button_functions
from board import Board

class TestButtonFunctions(unittest.TestCase):
    def test_open_cell_opens_a_cell(self):
        board = Board(10, 10, 20)
        button_functions.open_cell(board, (3, 3))
        self.assertEqual(board.get_board()[3][3].hidden, False)