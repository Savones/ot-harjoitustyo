import unittest
from objects.difficulties import Difficulties


class TestDifficulties(unittest.TestCase):
    def setUp(self):
        self.easy = Difficulties("EASY")
        self.medium = Difficulties("MEDIUM")
        self.hard = Difficulties("HARD")

    def test_easy(self):
        self.assertEqual(self.easy.speed, 300)
        self.assertEqual(self.easy.name, "EASY")
    
    def test_medium(self):
        self.assertEqual(self.medium.speed, 200)
        self.assertEqual(self.medium.name, "MEDIUM")

    def test_hard(self):
        self.assertEqual(self.hard.speed, 150)
        self.assertEqual(self.hard.name, "HARD")