import pygame
from ui.main_ui import MainUi

DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)

class SettingsDisplay:
    def __init__(self, screen, buttons):
        self.display = screen
        self.main = MainUi(self.display)
        self.buttons = buttons
    
    def draw_screen(self):
        self.display.fill(BABY_PINK)
        self.main.draw_text(VIOLET, 100, 115, 58, "CHOOSE DIFFICULTY")

        for button in self.buttons:
            self.draw_button(False, button)
        pygame.display.update()
    
    def draw_button(self, hovered: bool, button):
        self.main.draw_button(hovered, button)