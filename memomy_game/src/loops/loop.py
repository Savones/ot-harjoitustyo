import sys
import pygame


class Loop:

    def __init__(self, variables, check, display, game_over_display, scoreboard_display, buttons):
        self.variables = variables
        self.check = check
        self.display = display
        self.game_over_display = game_over_display
        self.scoreboard_display = scoreboard_display
        self.game_over_buttons = buttons[1]
        self.scoreboard_buttons = buttons[2]
        self.running = True
        pygame.init()

    def start_game(self):

        self.display.draw_screen(self.variables.high_score)
        self.variables.default()

        while True:
            self.variables.add_random_press()

            round_number = self.round()
            if round_number == -1:
                self.variables.update_hs_in_db()
                self.game_over()
                break

    def round(self):

        self.display.draw_pattern(
            self.variables.pattern_list, self.variables.level, self.variables.high_score)
        clicks = 0

        while self.running:
            for event in pygame.event.get():
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
                    self.variables.change_high_score()
                    self.display.draw_level_up_text()
                    return 1

                self.closed_game(event)
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

        self.scoreboard_display.draw_screen()

        while self.running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                if self.scoreboard_buttons[0].if_hovered(pos):
                    self.scoreboard_display.draw_button(True, self.scoreboard_buttons[0])
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_over()
                        return None
                else:
                    self.scoreboard_display.draw_button(True, self.scoreboard_buttons[0])

                self.closed_game(event)
                pygame.display.update()
        return None

    def closed_game(self, event):
        if event.type == pygame.QUIT:
            print("Player closed the game")
            sys.exit()
    
    def button_pressed(self, button):
        if button == "TRY AGAIN":
            self.start_game()
        elif button == "SCOREBOARD":
            self.scoreboard()
        return None
