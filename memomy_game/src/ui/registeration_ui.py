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
        self.display.fill(SALMON)
        pygame.display.update()
    
    def update_screen(self, text):
        self.display.fill(SALMON)
        self.main.draw_text(WHITE, 100, 100, 38, text)
        pygame.display.update()