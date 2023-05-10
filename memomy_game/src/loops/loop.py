import sys
import pygame
from objects.difficulties import Difficulties


class Loop:
    """A class that runs the game after logging in

    Attributes:
        variables: an object for Variables class
        check: an object for Check class
        display: an object for Display class (game UI)
        settings_display: an object for SettingsDisplay class (settings UI)
        game_over_display: an object for GameOverDisplay class (game over UI)
        scoreboard_display: an object for ScoreboardDisplay class (scoreboard UI)
        database: an object for the Database class (handles database logic)
        buttons: a list of buttons for differents UI views
    """

    def __init__(self, variables, check, displays, buttons):
        self.variables = variables
        self.check = check
        self.display = displays[0]
        self.settings_display = displays[1]
        self.game_over_display = displays[2]
        self.scoreboard_display = displays[3]
        self.game_over_buttons = buttons[1]
        self.scoreboard_buttons = buttons[2]
        self.settings_buttons = buttons[3]
        self.running = True
        pygame.init()

    def settings(self):
        self.settings_display.draw_screen()

        while self.running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                for button in self.settings_buttons:
                    if button.if_hovered(pos):
                        self.settings_display.draw_button(True, button)

                        if event.type == pygame.MOUSEBUTTONDOWN and button.name == "START GAME":
                            try:
                                choice.pressed = False
                            except:
                                print("Please choose a difficulty.")
                                continue
                            return Difficulties(choice.name)

                        elif event.type == pygame.MOUSEBUTTONDOWN and button.name == "LOG OUT":
                            return None

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            try:
                                choice.pressed = False
                            except:
                                pass
                            choice = button
                            button.pressed = True

                    elif not button.pressed:
                        self.settings_display.draw_button(False, button)

                self.closed_game(event)
                pygame.display.update()

    def start_game(self):

        difficulty = self.settings()
        if difficulty is None:
            return None

        self.display.draw_screen(
            self.variables.high_score(difficulty), difficulty.name)
        self.variables.default()

        while True:
            for _ in range(difficulty.addition):
                self.variables.add_random_press()

            round_number = self.round(difficulty)
            if round_number == -1:
                self.game_over()
                break

    def round(self, difficulty):

        pattern_drawn = False
        clicks = 0

        print(self.variables.pattern_list)

        while self.running:

            for event in pygame.event.get():

                self.closed_game(event)

                if not pattern_drawn:
                    pattern_drawn = self.display.draw_pattern(
                        self.variables.pattern_list, self.variables.level,
                        self.variables.high_score(difficulty), difficulty)
                    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                    continue

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if not self.check.check_misclick(pos):
                        continue

                    if not self.check.check_click(pos, self.variables.pattern_list[clicks]):
                        self.display.draw_click(pos)
                        return -1

                    self.display.draw_click(pos)
                    clicks += 1

                if clicks >= len(self.variables.pattern_list):
                    self.variables.level_up()
                    self.variables.change_high_score(difficulty)
                    self.display.draw_level_up_text()
                    return 1

        return None

    def game_over(self):

        self.game_over_display.draw_screen()

        while self.running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                for button in self.game_over_buttons:
                    if button.if_hovered(pos):
                        self.game_over_display.draw_button(True, button)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.button_pressed(button.name)
                            return None
                    else:
                        self.game_over_display.draw_button(False, button)

                self.closed_game(event)
                pygame.display.update()
        return None

    def scoreboard(self):

        self.scoreboard_buttons[1].pressed = True
        self.scoreboard_display.draw_screen(Difficulties("EASY"))
        self.scoreboard_display.draw_button(True, self.scoreboard_buttons[1])

        while self.running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                for button in self.scoreboard_buttons:
                    if button.if_hovered(pos):
                        self.scoreboard_display.draw_button(True, button)
                        if event.type == pygame.MOUSEBUTTONDOWN and button.name == "RETURN":
                            self.button_pressed(button.name)
                            return None
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            try:
                                if choice.name != button.name:
                                    choice.pressed = False
                            except:
                                pass
                            self.update_scoreboard(button)
                            button.pressed = True
                            choice = button
                    elif not button.pressed:
                        self.scoreboard_display.draw_button(
                            False, button)

                self.closed_game(event)
                pygame.display.update()
        return None

    def update_scoreboard(self, button):
        self.scoreboard_display.draw_screen(Difficulties(button.name))

    def closed_game(self, event):
        if event.type == pygame.QUIT:
            print("Player closed the game")
            sys.exit()

    def button_pressed(self, button):
        if button == "TRY AGAIN":
            self.start_game()
        elif button == "SCOREBOARD":
            self.scoreboard()
        elif button == "RETURN":
            self.game_over()
        elif button == "EASY":
            return
        return None
