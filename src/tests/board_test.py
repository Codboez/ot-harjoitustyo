import unittest
from game.board import Board
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(10, 10, 20, None)

    def test_open_cell_returns_false_if_out_of_bounds(self):
        was_opened = self.board.open_cell((12, 12))
        self.assertEqual(was_opened, False)

    def test_open_cell_generates_a_board_if_has_generated_is_false(self):
        self.board.open_cell((3, 3))
        self.assertNotEqual(self.board.get_board(), [])

    def test_open_cell_board_stays_unchanged_if_has_generated_is_true(self):
        self.board.open_cell((3, 3))
        prev_board = self.board.get_board()
        self.board.open_cell((3, 4))
        self.assertEqual(self.board.get_board(), prev_board)

    def test_open_cell_opens_a_cell(self):
        self.board.open_cell((3, 3))
        self.assertEqual(self.board.get_board()[3][3].hidden, False)

    def test_opens_around_cell_if_content_was_0(self):
        self.board = Board(10, 10, 0, None)
        self.board.open_cell((3, 3))
        self.assertEqual(self.board.get_board()[3][4].hidden, False)

    def test_open_cell_returns_true_if_not_out_of_bounds(self):
        was_opened = self.board.open_cell((3, 3))
        self.assertEqual(was_opened, True)

    def test_generate_mines_does_nothing_when_has_generated_is_true(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((3, 3))
        self.board.generate_mines((7, 7))
        self.assertNotEqual(self.board.get_board()[3][3].content, -1)

    def test_does_not_generate_mines_around_start_position(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((3, 3))
        has_mine = False

        for i in range(2, 5):
            for j in range(2, 5):
                if self.board.get_board()[i][j].content == -1:
                    has_mine = True

        self.assertEqual(has_mine, False)

    def test_generates_mine_if_minechance_is_smaller_or_equal_to_random_int(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((3, 3))
        does_not_have_mine = False

        for i, row in enumerate(self.board.get_board()):
            for j, cell in enumerate(row):
                if j in range(2, 5) and i in range(2, 5):
                    continue

                if cell.content != -1:
                    does_not_have_mine = True

        self.assertEqual(does_not_have_mine, False)

    def test_does_not_generate_mine_if_minechance_is_larger_than_random_int(self):
        self.board = Board(10, 10, 0, None)
        self.board.open_cell((3, 3))
        has_mine = False

        for i, row in enumerate(self.board.get_board()):
            for j, cell in enumerate(row):
                if j in range(2, 5) and i in range(2, 5):
                    continue

                if cell.content == -1:
                    has_mine = True

        self.assertEqual(has_mine, False)

    def test_generate_numbers_does_nothing_when_has_generated_is_true(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((3, 3))
        self.board.get_board()[4][4].content = 2
        self.board.generate_numbers()
        self.assertNotEqual(self.board.get_board()[4][4].content, 5)

    def test_counts_numbers_correctly(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((3, 3))
        self.assertEqual(self.board.get_board()[4][4].content, 5)

    def test_open_around_cell_does_not_open_flagged_cell_when_open_flagged_is_false(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((3, 3))
        board_matrix = self.board.get_board()
        board_matrix[0][0].flagged = True
        self.board.open_around_cell((0, 1), False)
        self.assertEqual(board_matrix[0][0].hidden, True)

    def test_calculates_cell_size_correctly_when_too_big(self):
        self.board = Board(50, 30, 20, None)
        self.board.calculate_cell_size()
        self.assertEqual(Cell.size, 17)

    def test_counts_flags_around_cell_correctly(self):
        self.board = Board(10, 10, 100, None)
        self.board.open_cell((0, 0))
        self.board.get_board()[0][2].flagged = True
        amount = self.board.count_flags_around_cell((1, 0))
        self.assertEqual(amount, 1)