import pygame
HEIGHT = 600
WIDTH = 600
RED_COLOR = (255, 87, 51)
WHITE_COLOR = (255, 255, 255)

class Display:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))

    def draw_screen(self):
        self.display.fill((0, 0, 0))
        x = 155
        y = 100
        for i in range(1, 10):
            pygame.draw.rect(self.display, WHITE_COLOR, pygame.Rect(x, y, 90, 90))
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100

        pygame.display.flip()
        pygame.time.delay(1000)

    def draw_click(self, pos):
        x = 155
        y = 100
        for i in range(1, 10):
            if (x + 90) >= pos[0] >= x and (y + 90) >= pos[1] >= y:
                break
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100
        
        pygame.draw.rect(self.display, (200, 0, 0), pygame.Rect(x, y, 90, 90))
        pygame.display.flip()
        pygame.time.delay(100)
        pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(x, y, 90, 90))
        pygame.display.flip()
        


    def draw_pattern(self, pattern: list, level: int):

        font = pygame.font.SysFont("Ariel", 58)
        text = font.render(f"Level: {level}", True, WHITE_COLOR)
        self.display.blit(text,(155, 450))
        pygame.display.flip()

        for element in pattern:
            x = 155
            y = 100
            for i in range(1, 10):
                if i == element:
                    self.draw_hit(x, y)
                if i % 3 == 0:
                    y += 100
                    x = 155
                else:
                    x += 100


    def draw_hit(self, x, y):
        pygame.draw.rect(self.display, (0, 200, 0), pygame.Rect(x, y, 90, 90))
        pygame.display.flip()
        pygame.time.delay(200)
        pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(x, y, 90, 90))
        pygame.display.flip()
        pygame.time.delay(200)


    def lost(self):
        self.display.fill(RED_COLOR)
        font = pygame.font.SysFont("Ariel", 64)
        text = font.render("YOU LOST", True, WHITE_COLOR)
        
        self.display.blit(text,(200, 255))
        pygame.display.flip()
        pygame.time.delay(2000)
