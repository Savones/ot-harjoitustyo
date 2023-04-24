import unittest
from logic.variables import Variables
from database.player_database import Database


class TestVariables(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.database.add_player("Milla", "testi123", 0)
        self.name = "Milla"
        self.pattern = Variables(self.name, self.database)

    # tests __init__ construct

    def test_pattern_first_empty_list(self):
        self.assertEqual(self.pattern.pattern_list, [])

    def test_level_first_zero(self):
        self.assertEqual(self.pattern.level, 0)

    # tests add_random_press method

    def test_picked_square_exists(self):
        self.pattern.add_random_press()
        self.assertTrue(1 <= self.pattern.pattern_list[0] <= 9)

    def test_adds_one_press(self):
        self.pattern.add_random_press()
        self.assertEqual(len(self.pattern.pattern_list), 1)

    # tests level_up method

    def test_level_ups_by_one(self):
        self.pattern.level_up()
        self.assertEqual(self.pattern.level, 1)

    # tests default method

    def test_empties_pattern_list(self):
        self.pattern.add_random_press()
        self.pattern.default()
        self.assertEqual(len(self.pattern.pattern_list), 0)

    def test_sets_level_to_zero(self):
        self.pattern.add_random_press()
        self.pattern.default()
        self.assertEqual(self.pattern.level, 0)

    # tests change_high_score method

    def test_hs_change_when_greater_level(self):
        self.pattern.level_up()
        self.pattern.change_high_score()
        self.assertEqual(self.pattern.high_score, 1)

    def test_hs_not_change_when_lower_level(self):
        self.pattern.high_score = 10
        self.pattern.change_high_score()
        self.assertEqual(self.pattern.high_score, 10)

    # tests update_hs_in_db method

    # def test_changes_hs_in_db(self):
    #     self.pattern.level_up()
    #     self.pattern.change_high_score()
    #     self.pattern.update_hs_in_db()
    #     self.assertEqual(self.pattern.high_score, 10)
