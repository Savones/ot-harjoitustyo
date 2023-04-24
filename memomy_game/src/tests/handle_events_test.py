import os
import unittest
import pygame
from logic.check import Check
from ui.registeration_ui import RegisDisplay
from database.player_database import Database
from logic.handle_events import LoginEvents


class TestLoginEvents(unittest.TestCase):
    def setUp(self):
        screen = pygame.display.set_mode((1, 1))
        self.database = Database()
        self.check = Check(self.database)
        self.display = RegisDisplay(screen)
        self.events = LoginEvents(self.check, self.display, self.database)

    # tests __init__ construct

    def test_input_empty_string(self):
        self.assertEqual(self.events.input, "")

    def test_username_empty_string(self):
        self.assertEqual(self.events.username, "")

    # reset input

    def test_input_resets(self):
        self.events.input = "hei"
        self.events.reset_input()
        self.assertEqual(self.events.input, "")

    # get username

    def test_get_right_username(self):
        self.events.username = "Testi"
        self.assertEqual(self.events.get_username(), "Testi")

    # login_username

    def test_true_username_exists(self):
        self.database.add_player("Testi", "testi123", 0)
        self.assertEqual(self.events.login_username("Testi"), True)

    def test_false_username_doesnt_exist(self):
        self.database.add_player("Hei", "testi123", 0)
        self.assertEqual(self.events.login_username("Test"), False)

    # sign up username

    def test_false_username_in_use(self):
        self.database.add_player("Testi", "testi123", 0)
        self.assertEqual(self.events.sign_up_username("Testi"), False)

    def test_false_username_invalid(self):
        self.assertEqual(self.events.sign_up_username("T"), False)

    def test_true_username_valid(self):
        self.assertEqual(self.events.sign_up_username("Test"), True)

    def test_username_set_to_input(self):
        self.events.sign_up_username("Test")
        self.assertEqual(self.events.username, "Test")

    # sign up password

    def test_false_password_invalid(self):
        self.assertEqual(self.events.sign_up_password("T"), False)

    def test_true_password_valid(self):
        self.assertEqual(self.events.sign_up_password("testi123"), True)

    def test_adds_player_to_db(self):
        self.events.username = "Hey"
        self.events.sign_up_password("testi123")
        self.assertEqual(self.database.player_exists("Hey"), True)

    # hash password

    def test_password_changes(self):
        self.assertNotEqual(self.events.hash_password(
            "testi123".encode()), "testi123")

    # key_pressed

    # def test_letter_pressed(self):
    #     event = {'unicode': 'a', 'key': 97,
    #              'mod': 0, 'scancode': 4, 'window': None}
    #     self.assertEqual(self.events.key_pressed(event, 1), True)
