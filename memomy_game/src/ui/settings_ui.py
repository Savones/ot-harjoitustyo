import pygame
from ui.main_ui import MainUi

class SettingsDisplay:
    def __init__(self, screen):
        self.display = screen
        self.main = MainUi(self.display)
    
    def draw_screen(self):
        self.display.fill(0, 0, 0)
        pygame.display.update()