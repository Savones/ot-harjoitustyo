import pygame
from ui.main_ui import MainUi

class SettingsDisplay:
    def __init__(self, screen, buttons):
        self.display = screen
        self.main = MainUi(self.display)
        self.buttons = buttons
    
    def draw_screen(self):
        self.display.fill((0, 0, 0))
        for button in self.buttons:
            self.draw_button(False, button)
        pygame.display.update()
    
    def draw_button(self, hovered: bool, button):
        self.main.draw_button(hovered, button)