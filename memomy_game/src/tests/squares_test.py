import unittest
from objects.squares import Squares


class TestSquares(unittest.TestCase):
    def setUp(self):
        self.squares = Squares()

    # __init__

    def test_width_correct(self):
        self.assertEqual(self.squares.square_width, 90)

    def test_nine_squares(self):
        self.assertEqual(len(self.squares.squares), 9)
