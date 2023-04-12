import pygame
from ui.main_ui import MainUi

HEIGHT = 600
WIDTH = 600
WHITE = (255, 255, 255)
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)


class ScoreboardDisplay:
    def __init__(self, screen, player, database):
        self.display = screen
        self.main = MainUi(self.display)
        self.database = database
        self.player = player


    def draw_screen(self):
        self.display.fill((BABY_PINK))
        self.main.draw_box(LIGHT_PINK, 100, 200, 400, 350)

        self.main.draw_text(VIOLET, 140, 120, 64, "SCOREBOARD")

        self.draw_grid()

        self.draw_scoreboard()

        self.return_button(False)

        pygame.display.update()

    
    def draw_grid(self):
        self.main.draw_box(BABY_PINK, 400, 200, 6, 350)
        self.main.draw_box(BABY_PINK, 200, 200, 6, 350)


        x = 100
        y = 200
        for _ in range(4):
            y += 70
            self.main.draw_box(BABY_PINK, x, y, 400, 6)
    

    def draw_scoreboard(self):
        data = self.database.get_players_table()

        y = 155

        for i, player in enumerate(data):
            if i >= 5:
                continue
            y += 70
            if player[1] == self.player:
                color = SALMON
            else:
                color = VIOLET
            self.main.draw_text(VIOLET, 135, y, 40, f"{i + 1}.")
            self.main.draw_text(color, 250, y, 38, player[1])
            self.main.draw_text(VIOLET, 445, y, 40, str(player[2]))


    def return_button(self, hovered: bool):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = SALMON
        else:
            text_color = SALMON
            box_color = LIGHT_PINK
        
        self.main.draw_box(box_color, 450, 25, 120, 45)
        self.main.draw_text(text_color, 468, 39, 28, "RETURN")
        pygame.display.update()
