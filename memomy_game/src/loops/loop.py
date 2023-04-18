import sys
import pygame


class Loop:

    def __init__(self, variables, check, display, game_over_display, scoreboard_display):
        self.variables = variables
        self.check = check
        self.display = display
        self.game_over_display = game_over_display
        self.scoreboard_display = scoreboard_display
        pygame.init()

    def start_game(self):

        self.display.draw_screen()
        self.variables.default()

        while True:
            self.variables.add_random_press()

            round_number = self.round()
            if round_number == -1:
                self.variables.update_hs_in_db()
                self.game_over()
                break
        return None

    def round(self):

        self.display.draw_pattern(
            self.variables.pattern_list, self.variables.level, self.variables.high_score)
        clicks = 0
        running = True

        while running:
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
                    return 1

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()
        return None

    def game_over(self):

        self.game_over_display.draw_screen()
        running = True

        while running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                # if "try again" box is clicked -> starts game again
                if self.check.if_hovered(pos, 75, 405, 200, 60):
                    self.game_over_display.try_again_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.start_game()
                        return None
                else:
                    self.game_over_display.try_again_button(False)

                # if "scoreboard" box is clicked
                if self.check.if_hovered(pos, 325, 405, 200, 60):
                    self.game_over_display.scoreboard_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.scoreboard()
                        return None
                else:
                    self.game_over_display.scoreboard_button(False)

                # if "logout" clicked
                if self.check.if_hovered(pos, 450, 25, 120, 45):
                    self.game_over_display.log_out_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return None
                else:
                    self.game_over_display.log_out_button(False)

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()
        return None

    def scoreboard(self):

        self.scoreboard_display.draw_screen()
        running = True

        while running:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                # if "return" box is clicked -> starts game again
                if self.check.if_hovered(pos, 450, 25, 120, 45):
                    self.scoreboard_display.return_button(True)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_over()
                        return None
                else:
                    self.scoreboard_display.return_button(False)

                if event.type == pygame.QUIT:
                    print("Player closed the game")
                    sys.exit()
        return None
