import pygame
from ui.main_ui import MainUi
from registeration.player_database import Database

HEIGHT = 600
WIDTH = 600
WHITE = (255, 255, 255)
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)

class ScoreboardDisplay:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.main = MainUi()
        self.database = Database()


    def draw_screen(self):
        self.display.fill((BABY_PINK))
        self.main.draw_box(LIGHT_PINK, 100, 200, 400, 350)

        # random text for now
        self.main.draw_text(VIOLET, 140, 120, 64, "SCOREBOARD")

        self.draw_scoreboard()

        # return button
        self.return_button(False)

        pygame.display.update()
    

    def draw_scoreboard(self):
        test = self.database.get_players_table()
        print(test)

        for player in test:
            print(player[1], player[2])


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
