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
                        return self.input

                pos = pygame.mouse.get_pos()

                if self.check.if_hovered(pos, 340, 340, 150, 60):
                    self.display.enter_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.database.player_exists(self.input):
                            return self.input
                else:
                    self.display.enter_button(False)

                if self.check.if_hovered(pos, 170, 490, 260, 55):
                    self.display.create_account_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.create_account()
                        self.input = ""
                        self.display.draw_screen(1)
                else:
                    self.display.create_account_button(False)

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()

    def create_account(self):
        self.display.draw_screen(-1)
        self.input = ""
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if self.handle_key_press(event, -1):
                        return

                pos = pygame.mouse.get_pos()

                if self.check.if_hovered(pos, 340, 340, 150, 60):
                    self.display.enter_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.sign_up(self.input):
                            return
                else:
                    self.display.enter_button(False)

                if self.check.if_hovered(pos, 450, 25, 120, 45):
                    self.display.return_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return
                else:
                    self.display.return_button(False)

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()

    def login(self, player_input):
        if self.database.player_exists(player_input):
            return True
        print("User not found")
        return False

    def sign_up(self, player_input):
        if self.database.player_exists(player_input):
            print("Username already in use")
            return False
        elif not self.check.if_valid(player_input):
            print("Usename has to be 2-6 characters")
            return False
        else:
            self.database.add_player(player_input, 0)
            return True

    def handle_key_press(self, event, option: int):
        if event.key == pygame.K_BACKSPACE:
            self.input = self.input[0: -1]

        elif event.key == pygame.K_RETURN:
            if option == -1:
                if self.sign_up(self.input):
                    return True
            elif option == 1:
                if self.login(self.input):
                    return True
        else:
            self.input += event.unicode
        self.display.update_screen(self.input)
        return False
