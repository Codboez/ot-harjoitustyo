import unittest
from game import button_functions
from game.board import Board
from ui.text_object import TextObject

class TestButtonFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(10, 10, 20, None)

    def test_open_cell_opens_a_cell(self):
        button_functions.open_cell(self.board, (3, 3))
        self.assertEqual(self.board.get_board()[3][3].hidden, False)

    def test_switching_flagged_to_true_decreases_non_flagged_mine_amount(self):
        self.board.open_cell((3, 3))
        amount = self.board.mines_non_flagged
        button_functions.switch_flagged(self.board.get_board()[0][0], self.board)
        self.assertEqual(self.board.mines_non_flagged, amount - 1)

    def test_switching_flagged_to_false_increases_non_flagged_mine_amount(self):
        self.board.open_cell((3, 3))
        button_functions.switch_flagged(self.board.get_board()[0][0], self.board)
        amount = self.board.mines_non_flagged
        button_functions.switch_flagged(self.board.get_board()[0][0], self.board)
        self.assertEqual(self.board.mines_non_flagged, amount + 1)

    def test_invalid_input_checker_returns_true_if_input_not_integer(self):
        has_invalid_inputs = button_functions.has_invalid_inputs_for_custom_board_creation(
            TextObject("1", None, None), TextObject("22", None, None), TextObject("abc", None, None))
        self.assertEqual(has_invalid_inputs[0], True)

    def test_invalid_input_checker_returns_true_if_width_is_invalid(self):
        has_invalid_inputs = button_functions.has_invalid_inputs_for_custom_board_creation(
            TextObject("0", None, None), TextObject("22", None, None), TextObject("22", None, None))
        self.assertEqual(has_invalid_inputs[0], True)

    def test_invalid_input_checker_returns_true_if_height_is_invalid(self):
        has_invalid_inputs = button_functions.has_invalid_inputs_for_custom_board_creation(
            TextObject("1", None, None), TextObject("50", None, None), TextObject("22", None, None))
        self.assertEqual(has_invalid_inputs[0], True)

    def test_invalid_input_checker_returns_true_if_mine_chance_is_invalid(self):
        has_invalid_inputs = button_functions.has_invalid_inputs_for_custom_board_creation(
            TextObject("1", None, None), TextObject("22", None, None), TextObject("200", None, None))
        self.assertEqual(has_invalid_inputs[0], True)

    def test_invalid_input_checker_returns_false_if_inputs_are_valid(self):
        has_invalid_inputs = button_functions.has_invalid_inputs_for_custom_board_creation(
            TextObject("5", None, None), TextObject("22", None, None), TextObject("22", None, None))
        self.assertEqual(has_invalid_inputs[0], False)

    def test_open_around_open_cell_does_not_open_around_cell_if_not_enough_flags(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((0, 0))
        button_functions.open_around_an_open_cell(self.board, (0, 1))
        self.assertEqual(self.board.get_board()[2][0].hidden, True)

    def test_open_around_open_cell_opens_around_cell_if_enough_flags(self):
        self.board = Board(10, 10, 0, None)
        button_functions.open_around_an_open_cell(self.board, (0, 0))
        self.assertEqual(self.board.get_board()[1][0].hidden, False)