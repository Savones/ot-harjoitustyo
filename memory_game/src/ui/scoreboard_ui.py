import pygame
from ui.main_ui import MainUi

DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)


class ScoreboardDisplay:
    def __init__(self, screen, player, database, buttons):
        self.display = screen
        self.buttons = buttons
        self.main = MainUi(self.display)
        self.database = database
        self.player = player

    def draw_screen(self, difficulty):
        self.display.fill((BABY_PINK))
        self.main.draw_box(LIGHT_PINK, 100, 200, 400, 350)
        self.main.draw_text(VIOLET, 140, 120, 64, "SCOREBOARD")
        self.draw_grid()
        self.draw_scoreboard(difficulty)
        for button in self.buttons:
            self.draw_button(False, button)
        pygame.display.update()

    def draw_grid(self):
        self.main.draw_box(BABY_PINK, 400, 200, 6, 350)
        self.main.draw_box(BABY_PINK, 200, 200, 6, 350)

        x = 100
        y = 200
        for _ in range(4):
            y += 70
            self.main.draw_box(BABY_PINK, x, y, 400, 6)

    def draw_scoreboard(self, difficulty):
        data = self.database.get_players_table(difficulty.name)

        y = 155
        i = 0

        for player in data:
            if i >= 5:
                break
            if player[0] == "Tietokone":
                continue
            y += 70
            if player[0] == self.player:
                color = SALMON
            else:
                color = VIOLET
            self.main.draw_text(VIOLET, 135, y, 40, f"{i + 1}.")
            self.main.draw_text(color, 250, y, 38, player[0])
            self.main.draw_text(VIOLET, 445, y, 40,
                                str(player[difficulty.column]))
            i += 1

    def draw_button(self, hovered: bool, button):
        self.main.draw_button(hovered, button)
