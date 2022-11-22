import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(10, 10, 20)

    def test_open_cell_returns_false_if_out_of_bounds(self):
        was_opened = self.board.open_cell(12, 12)
        self.assertEqual(was_opened, False)

    def test_open_cell_generates_a_board_if_has_generated_is_false(self):
        self.board.open_cell(3, 3)
        self.assertNotEqual(self.board.get_board(), [])
