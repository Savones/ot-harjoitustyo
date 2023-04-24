import pygame
import bcrypt


class LoginEvents:

    def __init__(self, check, display, database):
        self.check = check
        self.display = display
        self.database = database
        self.input = ""
        self.username = ""

    def reset_input(self):
        self.input = ""

    def get_username(self):
        return self.username

    def login_enter(self, pos, event, option):
        return_value = False
        if self.check.if_hovered(pos, 340, 340, 150, 60):
            self.display.enter_button(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return_value = self.enter_pressed(option)
        else:
            self.display.enter_button(False)
        return return_value

    def login_create_account(self, pos, event):
        return_value = False
        if self.check.if_hovered(pos, 170, 490, 260, 55):
            self.display.create_account_button(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.reset_input()
                return_value = True
        else:
            self.display.create_account_button(False)
        return return_value

    def enter_button(self, pos, event, option):
        return_value = False
        if self.check.if_hovered(pos, 340, 340, 150, 60):
            self.display.enter_button(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return_value = self.enter_pressed(option)
        else:
            self.display.enter_button(False)
        return return_value

    def return_button(self, pos, event):
        if self.check.if_hovered(pos, 450, 25, 120, 45):
            self.display.return_button(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        else:
            self.display.return_button(False)
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
