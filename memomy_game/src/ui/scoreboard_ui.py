import pygame
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

    def draw_screen(self):
        self.display.fill((BABY_PINK))
        pygame.draw.rect(self.display, (LIGHT_PINK), pygame.Rect(100, 200, 400, 350), 0, 15)

        # random text for now
        font = pygame.font.SysFont("Inter", 64)
        text = font.render(f"SCOREBOARD", True, VIOLET)
        self.display.blit(text,(140, 120))

        # return button
        pygame.draw.rect(self.display, SALMON, pygame.Rect(450, 25, 120, 45), 0, 15)

        font = pygame.font.SysFont("Inter", 28)
        text = font.render(f"RETURN", True, LIGHT_PINK)
        self.display.blit(text,(468, 39))

        pygame.display.update()
    
    def return_hover(self):
        pygame.draw.rect(self.display, LIGHT_PINK, pygame.Rect(450, 25, 120, 45), 0, 15)

        font = pygame.font.SysFont("Inter", 28)
        text = font.render(f"RETURN", True, SALMON)
        self.display.blit(text,(468, 39))

        pygame.display.update()

    def return_unhover(self):
        pygame.draw.rect(self.display, SALMON, pygame.Rect(450, 25, 120, 45), 0, 15)

        font = pygame.font.SysFont("Inter", 28)
        text = font.render(f"RETURN", True, LIGHT_PINK)
        self.display.blit(text,(468, 39))

        pygame.display.update()

