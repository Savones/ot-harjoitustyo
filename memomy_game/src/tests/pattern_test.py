import unittest
from game.pattern import Pattern


class TestPattern(unittest.TestCase):
    def setUp(self):
        self.pattern = Pattern()

    # tests __init__ construct

    def test_pattern_first_empty_list(self):
        self.assertEqual(self.pattern.pattern_list, [])

    # tests add_random_press method

    def test_picked_square_exists(self):
        self.pattern.add_random_press()
        self.assertTrue(1 <= self.pattern.pattern_list[0] <= 9)