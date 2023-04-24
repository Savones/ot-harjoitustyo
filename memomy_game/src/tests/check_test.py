import unittest
from logic.check import Check
from database.player_database import Database


class TestPattern(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.check = Check(self.database)

    # tests check_click method

    def test_returns_true_when_click_correct(self):
        pos = (155, 100)
        self.assertEqual(self.check.check_click(pos, 1), True)

    def test_returns_false_when_click_incorrect(self):
        pos = (155, 100)
        self.assertEqual(self.check.check_click(pos, 2), False)

    def test_return_False_when_missclick(self):
        pos = (100, 100)
        self.assertEqual(self.check.check_click(pos, 2), False)

    # tests check_misclick method

    def test_returns_true_when_clicked_square_found(self):
        pos = (155, 100)
        self.assertEqual(self.check.check_misclick(pos), True)

    def test_returns_false_when_clicked_square_not_found(self):
        pos = (100, 100)
        self.assertEqual(self.check.check_misclick(pos), False)

    # tests if_hovered

    def test_returns_true_if_try_again_hovered(self):
        pos = (85, 405)
        self.assertEqual(self.check.if_hovered(pos, 75, 405, 200, 60), True)

    def test_returns_false_if_try_again_not_hovered(self):
        pos = (70, 405)
        self.assertEqual(self.check.if_hovered(pos, 75, 405, 200, 60), False)

    # test if_valid

    def test_returns_true_username_valid(self):
        self.assertEqual(self.check.valid_username("Testi"), True)

    def test_returns_false_username_too_short(self):
        self.assertEqual(self.check.valid_username("T"), False)

    def test_returns_false_username_too_long(self):
        self.assertEqual(self.check.valid_username("TestiTe"), False)
