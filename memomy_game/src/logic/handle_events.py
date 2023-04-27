import pygame
import bcrypt


class LoginEvents:

    def __init__(self, check, display, database, buttons):
        self.login_buttons = buttons[0]
        self.sign_up_buttons = buttons[1]
        self.check = check
        self.display = display
        self.database = database
        self.input = ""
        self.username = ""

    def reset_input(self):
        self.input = ""

    def get_username(self):
        return self.username

    def login_create_account(self, pos, event):
        return_value = False
        button = self.login_buttons[1]
        if button.if_hovered(pos):
            self.display.draw_button(True, button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.reset_input()
                return_value = True
        else:
            self.display.draw_button(False, button)
        return return_value

    def enter_button(self, pos, event, option):
        return_value = False
        button = self.login_buttons[0]
        if button.if_hovered(pos):
            self.display.draw_button(True, button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return_value = self.enter_pressed(option)
        else:
            self.display.draw_button(False, button)
        return return_value

    def return_button(self, pos, event):
        button = self.login_buttons[2]
        if button.if_hovered(pos):
            self.display.draw_button(True, button)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        else:
            self.display.draw_button(False, button)
        return False

    def login_username(self, player_input):
        if self.database.player_exists(player_input):
            self.username = player_input
            return True
        print("User not found")
        return False

    def sign_up_username(self, player_input):
        if self.database.player_exists(player_input):
            print("Username already in use")
            return False
        if not self.check.valid_username(player_input):
            print("Username has to be 2-6 characters")
            return False

        self.username = player_input
        return True

    def sign_up_password(self, password):
        if not self.check.valid_password(password):
            print("Password has to have 4-20 characters")
            return False
        password = password.encode()
        hashed_password = self.hash_password(password)
        self.database.add_player(self.username, hashed_password, 0)
        return True

    def hash_password(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def key_pressed(self, event, option: int):
        return_value = False
        if event.type != pygame.KEYDOWN:
            return return_value
        if event.key == pygame.K_BACKSPACE:
            self.input = self.input[0: -1]
        elif event.key == pygame.K_RETURN:
            return_value = self.enter_pressed(option)
        else:
            self.input += event.unicode
        self.display.update_screen(self.input, option)
        return return_value

    def enter_pressed(self, option):
        if option == 0 and not self.sign_up_password(self.input):
            return False
        if option == -1 and not self.sign_up_username(self.input):
            return False
        if option == 1 and not self.login_username(self.input):
            return False
        if option == 2 and not self.check.if_correct_password(self.username, self.input):
            return False
        return True
