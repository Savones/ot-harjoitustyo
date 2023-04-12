import pygame
from ui.main_ui import MainUi

HEIGHT = 600
WIDTH = 600
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)

# kaikki toiminnalliset elementit omissa metodeissaan

class GameOverDisplay:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.main = MainUi(self.display)
    

    def draw_screen(self):
        self.display.fill((BABY_PINK))

        # Game over text
        self.main.draw_text(SALMON, 130, 210, 82, "GAME OVER")

        # Draws buttons
        self.try_again_button(False)
        self.scoreboard_button(False)
        self.log_out_button()


    def try_again_button(self, hovered: bool):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = VIOLET
        else:
            text_color = VIOLET
            box_color = LIGHT_PINK
        
        self.main.draw_box(box_color, 75, 405, 200, 60)
        self.main.draw_text(text_color, 105, 423, 36, "TRY AGAIN")
        pygame.display.update()


    def scoreboard_button(self, hovered: bool):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = VIOLET
        else:
            text_color = VIOLET
            box_color = LIGHT_PINK
        
        self.main.draw_box(box_color, 325, 405, 200, 60)
        self.main.draw_text(text_color, 340, 423, 36, "SCOREBOARD")
        pygame.display.update()


    def log_out_button(self):

        self.main.draw_box(DARK_VIOLET, 450, 25, 120, 45)
        self.main.draw_text(LIGHT_PINK, 465, 39, 28, "LOG OUT")
        pygame.display.update()
