import unittest
from game.check import Check


class TestPattern(unittest.TestCase):
    def setUp(self):
        self.check = Check()
    
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
    
    # tests check_try_again

    def test_returns_true_if_try_again_hovered(self):
        pos = (85, 405)
        self.assertEqual(self.check.check_try_again(pos), True)

    def test_returns_false_if_try_again_not_hovered(self):
        pos = (80, 405)
        self.assertEqual(self.check.check_try_again(pos), False)