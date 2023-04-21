import sys
import pygame


class RegisterationLoop:
    def __init__(self, database, display, check):
        self.database = database
        self.display = display
        self.check = check
        self.input = ""

    def start(self):

        if self.database.table_exists() is False:
            self.database.create_table()

        self.display.draw_screen(1)

        running = True

        while running:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if self.handle_key_press(event, 1):
                        # self.display.password_display(1)
                        return self.input

                pos = pygame.mouse.get_pos()

                if self.handle_mouse_movement_login_display(pos, event):
                    return self.input

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()
        return None

    def create_account(self):
        self.display.draw_screen(-1)
        self.input = ""
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if self.handle_key_press(event, -1):
                        return None

                pos = pygame.mouse.get_pos()

                if self.handle_mouse_movement_create_display(pos, event):
                    return None

                if event.type == pygame.QUIT:
                    sys.exit()
        return None

    # def handle_mouse_movement_login_display(self, pos, event):
    #     return_value = False
    #     if self.check.if_hovered(pos, 340, 340, 150, 60):
    #         self.display.enter_button(True)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             return_value = self.handle_return_pressed(1)
    #     else:
    #         self.display.enter_button(False)

    #     if self.check.if_hovered(pos, 170, 490, 260, 55):
    #         self.display.create_account_button(True)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             self.create_account()
    #             self.input = ""
    #             self.display.draw_screen(1)
    #     else:
    #         self.display.create_account_button(False)
    #     return return_value

    # def handle_mouse_movement_create_display(self, pos, event):
    #     return_value = False
    #     if self.check.if_hovered(pos, 340, 340, 150, 60):
    #         self.display.enter_button(True)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             return_value = self.handle_return_pressed(-1)
    #     else:
    #         self.display.enter_button(False)

    #     if self.check.if_hovered(pos, 450, 25, 120, 45):
    #         self.display.return_button(True)
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             return_value = True
    #     else:
    #         self.display.return_button(False)
    #     return return_value

    # def login(self, player_input):
    #     if self.database.player_exists(player_input):
    #         return True
    #     print("User not found")
    #     return False

    # def sign_up(self, player_input):
    #     if self.database.player_exists(player_input):
    #         print("Username already in use")
    #         return False
    #     if not self.check.if_valid(player_input):
    #         print("Usename has to be 2-6 characters")
    #         return False
    #     self.database.add_player(player_input, 0)
    #     return True

    # def handle_key_press(self, event, option: int):
    #     return_value = False
    #     if event.key == pygame.K_BACKSPACE:
    #         self.input = self.input[0: -1]
    #     elif event.key == pygame.K_RETURN:
    #         return_value = self.handle_return_pressed(option)
    #     else:
    #         self.input += event.unicode
    #     self.display.update_screen(self.input)
    #     return return_value

    # def handle_return_pressed(self, option):
    #     if option == -1 and not self.sign_up(self.input):
    #         return False
    #     if option == 1 and not self.login(self.input):
    #         return False
    #     return True
