import pygame
from ui.main_ui import MainUi

HEIGHT = 600
WIDTH = 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 153)
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)
GREEN = (88, 179, 104)

class RegisDisplay:
    def __init__(self, screen):
        self.display = screen
        self.main = MainUi(self.display)
    

    def draw_screen(self):
        self.display.fill(BABY_PINK)
        self.main.draw_box(VIOLET, 75, 200, 450, 250)
        self.main.draw_box(LIGHT_PINK, 270, 250, 220, 50)

        self.main.draw_text(VIOLET, 200, 100, 82, "LOG IN")
        self.main.draw_text(LIGHT_PINK, 110, 265, 32, "USERNAME:")

        self.enter_button(False)

        pygame.display.update()
    

    def update_screen(self, text):
        self.main.draw_box(LIGHT_PINK, 270, 250, 220, 50)
        self.main.draw_text(DARK_VIOLET, 290, 265, 32, text)
        pygame.display.update()
    

    def enter_button(self, hovered):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = SALMON
        else:
            text_color = SALMON
            box_color = LIGHT_PINK
        
        self.main.draw_box(box_color, 340, 340, 150, 60)
        self.main.draw_text(text_color, 365, 357, 42, "ENTER")
        pygame.display.update()