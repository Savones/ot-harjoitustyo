import pygame
HEIGHT = 600
WIDTH = 600
WHITE = (255, 255, 255)
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)


class GameOverDisplay:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
    
    def draw_screen(self):
        self.display.fill((BABY_PINK))

        # Game over text
        font = pygame.font.SysFont("Inter", 82)
        text = font.render(f"GAME OVER", True, SALMON)
        self.display.blit(text,(130, 210))

        # Try again button
        pygame.draw.rect(self.display, VIOLET, pygame.Rect(75, 405, 200, 60), 0, 15)

        font = pygame.font.SysFont("Inter", 36)
        text = font.render(f"TRY AGAIN", True, LIGHT_PINK)
        self.display.blit(text,(105, 423))

        # Scoreboard button
        pygame.draw.rect(self.display, VIOLET, pygame.Rect(325, 405, 200, 60), 0, 15)

        font = pygame.font.SysFont("Inter", 36)
        text = font.render(f"SCOREBOARD", True, LIGHT_PINK)
        self.display.blit(text,(340, 423))

        # Log-out button
        pygame.draw.rect(self.display, DARK_VIOLET, pygame.Rect(450, 25, 120, 45), 0, 15)

        font = pygame.font.SysFont("Inter", 28)
        text = font.render(f"LOG OUT", True, LIGHT_PINK)
        self.display.blit(text,(465, 39))

        pygame.display.update()
    

    def try_again_hover(self):
        pygame.draw.rect(self.display, LIGHT_PINK, pygame.Rect(75, 405, 200, 60), 0, 15)
        font = pygame.font.SysFont("Inter", 36)
        text = font.render(f"TRY AGAIN", True, VIOLET)
        self.display.blit(text,(105, 423))

        pygame.display.update()

    def try_again_unhover(self):
        pygame.draw.rect(self.display, VIOLET, pygame.Rect(75, 405, 200, 60), 0, 15)
        font = pygame.font.SysFont("Inter", 36)
        text = font.render(f"TRY AGAIN", True, LIGHT_PINK)
        self.display.blit(text,(105, 423))

        pygame.display.update()


    def scoreboard_hover(self):
        pygame.draw.rect(self.display, LIGHT_PINK, pygame.Rect(325, 405, 200, 60), 0, 15)
        font = pygame.font.SysFont("Inter", 36)
        text = font.render(f"SCOREBOARD", True, VIOLET)
        self.display.blit(text,(340, 423))

        pygame.display.update()

    def scoreboard_unhover(self):
        pygame.draw.rect(self.display, VIOLET, pygame.Rect(325, 405, 200, 60), 0, 15)
        font = pygame.font.SysFont("Inter", 36)
        text = font.render(f"SCOREBOARD", True, LIGHT_PINK)
        self.display.blit(text,(340, 423))

        pygame.display.update()
