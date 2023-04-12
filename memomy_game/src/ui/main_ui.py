import pygame
HEIGHT = 600
WIDTH = 600

class MainUi():
    def __init__(self, display):
        self.display = display


    def draw_box(self, color, x, y, width, height):
        pygame.draw.rect(self.display, color, pygame.Rect(x, y, width, height), 0, 15)


    def draw_text(self, color, x, y, font_size, content):
        font = pygame.font.SysFont("Inter", font_size)
        text = font.render(content, True, color)
        self.display.blit(text,(x, y))