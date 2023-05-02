import unittest
import bcrypt
from logic.check import Check
from database.player_database import Database
from objects.squares import Squares


class TestPattern(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.squares = Squares()
        self.check = Check(self.database, self.squares)

    # tests check_click method

    def test_returns_true_when_click_correct(self):
        pos = (155, 100)
        self.assertEqual(self.check.check_click(pos, 0), True)

    def test_returns_false_x_click_incorrect(self):
        pos = (100, 100)
        self.assertEqual(self.check.check_click(pos, 2), False)

    def test_returns_false_y_click_incorrect(self):
        pos = (155, 90)
        self.assertEqual(self.check.check_click(pos, 0), False)

    # tests check_misclick method

    def test_returns_true_when_clicked_square_found(self):
        pos = (155, 100)
        self.assertEqual(self.check.check_misclick(pos), True)

    def test_return_false_x_missclick(self):
        pos = (100, 110)
        self.assertEqual(self.check.check_misclick(pos), False)

    def test_return_false_y_missclick(self):
        pos = (155, 90)
        self.assertEqual(self.check.check_misclick(pos), False)

    # tests if_hovered

    def test_returns_true_if_try_again_hovered(self):
        pos = (85, 405)
        self.assertEqual(self.check.if_hovered(pos, 75, 405, 200, 60), True)

    def test_returns_false_if_try_again_not_hovered(self):
        pos = (70, 405)
        self.assertEqual(self.check.if_hovered(pos, 75, 405, 200, 60), False)

    # test valid username

    def test_returns_true_username_valid(self):
        self.assertEqual(self.check.valid_username("Testi"), True)

    def test_returns_false_username_too_short(self):
        self.assertEqual(self.check.valid_username("T"), False)

    def test_returns_false_username_too_long(self):
        self.assertEqual(self.check.valid_username("TestiTe"), False)

    # valid password

    def test_returns_true_password_valid(self):
        self.assertEqual(self.check.valid_password("Testi"), True)

    def test_returns_false_password_invalid(self):
        self.assertEqual(self.check.valid_password("Tes"), False)

    # correct password

    def test_returns_true_password_correct(self):
        password = "testi".encode()
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.database.add_player("Moi", hashed_password, 0)
        self.assertEqual(self.check.if_correct_password("Moi", "testi"), True)

    def test_returns_false_password_incorrect(self):
        password = "testi".encode()
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.database.add_player("Moi", hashed_password, 0)
        self.assertEqual(self.check.if_correct_password(
            "Moi", "testi123"), False)
