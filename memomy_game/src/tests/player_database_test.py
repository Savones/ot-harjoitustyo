import unittest
import os
from database.player_database import Database

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
        self.database.add_player("Testi", 0)
        self.assertEqual(self.database.player_exists("Testi"), True)

    # tests change hs

    def test_change_hs_when_player_exists(self):
        self.database.create_table()
        self.database.add_player("Testi", 0)
        self.database.change_hs("Testi", 5)
        self.assertEqual(self.database.get_hs("Testi"), 5)