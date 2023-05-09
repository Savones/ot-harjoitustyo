import unittest
import os
from database.player_database import Database
from objects.difficulties import Difficulties


class TestDatabase(unittest.TestCase):
    def setUp(self):
        os.remove("player_database.db")
        self.database = Database()

    # tests table exists

    def test_table_exists_returns_true(self):
        self.database.create_table()
        self.assertEqual(self.database.table_exists(), True)

    def test_table_exists_returns_false(self):
        self.assertEqual(self.database.table_exists(), False)

    # tests add player

    def test_add_player(self):
        self.database.create_table()
        self.database.add_player("Testi", "Testi123", 0)
        self.assertEqual(self.database.player_exists("Testi"), True)

    # tests change hs

    def test_change_hs_when_player_exists(self):
        difficulty = Difficulties("EASY")
        self.database.create_table()
        self.database.add_player("Testi", "Testi123", 0)
        self.database.change_high_score("Testi", 5, difficulty)
        self.assertEqual(self.database.get_high_score("Testi", difficulty), 5)

    # get players table

    # def test_return_table(self):
    #     difficulty = Difficulties("EASY")
    #     self.database.create_table()
    #     self.database.add_player("Testi", "Testi123", 0)
    #     self.assertEqual(self.database.get_players_table(difficulty),
    #                      [('Testi', 0, 0, 0)])

    # player exists

    def test_return_true_when_exists(self):
        self.database.create_table()
        self.database.add_player("Testi", "Testi123", 0)
        self.assertEqual(self.database.player_exists("Testi"), True)

    def test_return_false_doesnt_exist(self):
        self.database.create_table()
        self.assertEqual(self.database.player_exists("Moi"), False)
