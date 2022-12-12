import unittest
import os
from database.scores import Scores

class TestScores(unittest.TestCase):
    def setUp(self) -> None:
        self.database = Scores("test_scores.db")
        self.database.set_up()

    def tearDown(self) -> None:
        if os.path.exists(self.database.file_path):
            os.remove(self.database.file_path)

    def test_adds_a_board(self):
        prev_length = len(self.database.get_all_boards())
        self.database.add_board(20, 30, 40)
        length = len(self.database.get_all_boards())
        self.assertEqual(length, prev_length + 1)

    def test_setups_correctly(self):
        length = len(self.database.get_all_boards())
        self.assertEqual(length, 3)

    def test_add_board_does_not_add_board_if_invalid_inputs(self):
        prev_length = len(self.database.get_all_boards())
        self.database.add_board("a", 30, 40)
        length = len(self.database.get_all_boards())
        self.assertEqual(length, prev_length)

    def test_adds_a_score(self):
        prev_length = len(self.database.get_all_scores())
        self.database.add_score("a", 1, 20.0)
        length = len(self.database.get_all_scores())
        self.assertEqual(length, prev_length + 1)

    def test_deletes_a_score(self):
        self.database.add_score("a", 1, 20.0)
        prev_length = len(self.database.get_all_scores())
        self.database.delete_score(1)
        length = len(self.database.get_all_scores())
        self.assertEqual(length, prev_length - 1)

    def test_gets_board_id_correctly(self):
        board_id = self.database.get_board_id(10, 10, 15)
        self.assertEqual(board_id, 1)

    def test_get_board_id_adds_new_board_if_board_does_not_exist(self):
        prev_length = len(self.database.get_all_boards())
        self.database.get_board_id(30, 30, 30)
        length = len(self.database.get_all_boards())
        self.assertEqual(length, prev_length + 1)

    def test_sorts_scores_correctly(self):
        self.database.add_score("a", 1, 20.0)
        self.database.add_score("a", 1, 15.0)
        self.database.add_score("a", 1, 25.0)
        scores = self.database.get_sorted_scores_for_board(1, 10)
        self.assertEqual(scores[0][3], 15.0)

    def test_limits_scores_correctly(self):
        self.database.add_score("a", 1, 20.0)
        self.database.add_score("a", 1, 15.0)
        self.database.add_score("a", 1, 25.0)
        scores = self.database.get_sorted_scores_for_board(1, 2)
        self.assertEqual(len(scores), 2)