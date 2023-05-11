import sys
import pygame
from objects.difficulties import Difficulties


class Loop:
    """A class that handles events after logging in

    Attributes:
        variables: an object for Variables class
        check: an object for Check class
        displays: a list of different display class objects
        buttons: a list of buttons for differents UI views
    """

    def __init__(self, variables, check, displays, buttons):
        """The classes constructor which initializes the classes variables

        Args:
            Listed above
        """

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

    def start_game(self):
        """Starts a new game for the logged in player: player
           chooses difficulty, then game loop starts

        Returns:
            None if player logs out in difficulty view
        """

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

    def settings(self):
        """Handles events in the settings view

        Returns:
            None if player logs out
            Difficulties object if the player chooses a difficulty
        """

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
                                return Difficulties(choice.name)
                            except UnboundLocalError:
                                print("Please choose a difficulty.")

                        elif event.type == pygame.MOUSEBUTTONDOWN and button.name == "LOG OUT":
                            return None

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            try:
                                choice.pressed = False
                            except UnboundLocalError:
                                pass
                            choice = button
                            button.pressed = True

                    elif not button.pressed:
                        self.settings_display.draw_button(False, button)

                self.closed_game(event)
                pygame.display.update()

    def round(self, difficulty):
        """Handles events in a round of a game

        Args:
            difficulty: the players chosen difficulty for the game

        Returns:
            -1 if the player clicks the wrong square and game ends
            1 if the player got the pattern right and moves to next round
        """

        pattern_drawn = False
        clicks = 0

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
                    self.variables.level_up(difficulty)
                    self.display.draw_level_up_text("CORRECT!")
                    return 1

        return None

    def game_over(self):
        """Handles events in the game over view

        Returns:
            None when a button is pressed
        """

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
        """Handles events in the scoreboard view

        Returns:
            None when return is pressed
        """

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
                        if event.type == pygame.MOUSEBUTTONDOWN:
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
        """Updates the scoreboard view depending on the difficulty chosen

        Args:
            button: the difficulty button the player clicked
        """

        self.scoreboard_display.draw_screen(Difficulties(button.name))

    def closed_game(self, event):
        """Closes the program if player exists the game

        Args:
            event: the current pygame event
        """
        
        if event.type == pygame.QUIT:
            print("Player closed the game")
            sys.exit()

    def button_pressed(self, button):
        """Does an action depending on the button clicked

        Args:
            button: the button the player clicked
        
        Returns:
            None
        """

        if button == "TRY AGAIN":
            self.start_game()
        elif button == "SCOREBOARD":
            self.scoreboard()
        elif button == "RETURN":
            self.game_over()
        return None
