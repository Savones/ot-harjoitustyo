import sys
import pygame


class Loop:

    def __init__(self, variables, check, display, game_over_display, scoreboard_display, buttons):
        self.variables = variables
        self.check = check
        self.display = display
        self.game_over_display = game_over_display
        self.scoreboard_display = scoreboard_display
        self.buttons = buttons
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

                self.game_over_display.try_again_button(False)
                self.game_over_display.scoreboard_button(False)
                self.game_over_display.log_out_button(False)

                for button in self.buttons:
                    if button.if_hovered(pos):
                        self.change_button_color(button.name)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.button_pressed(button.name)
                            return None
                        break

                self.closed_game(event)
                pygame.display.update()
        return None

    def scoreboard(self):

        self.scoreboard_display.draw_screen()

        while self.running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()
                self.scoreboard_display.return_button(False)

                if self.check.if_hovered(pos, 450, 25, 120, 45):
                    self.scoreboard_display.return_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_over()
                        return None

                self.closed_game(event)
                pygame.display.update()
        return None

    def closed_game(self, event):
        if event.type == pygame.QUIT:
            print("Player closed the game")
            sys.exit()
    
    def change_button_color(self, button):
        if button == "TRY AGAIN":
            self.game_over_display.try_again_button(True)
        elif button == "SCOREBOARD":
            self.game_over_display.scoreboard_button(True)
        else:
            self.game_over_display.log_out_button(True)
    
    def button_pressed(self, button):
        if button == "TRY AGAIN":
            self.start_game()
        elif button == "SCOREBOARD":
            self.scoreboard()
        return None
