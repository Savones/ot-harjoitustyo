import pygame
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

class Display:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def draw_screen(self):
        self.display.fill(VIOLET)

        pygame.draw.rect(self.display, (DARK_VIOLET), pygame.Rect(125, 70, 350, 350), 0, 15)

        x = 155
        y = 100
        for i in range(1, 10):
            pygame.draw.rect(self.display, LIGHT_PINK, pygame.Rect(x, y, 90, 90), 0, 15)
            if i % 3 == 0:
                y += 100
                x = 155
            else:
                x += 100

        pygame.display.update()
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
        
        pygame.draw.rect(self.display, (SALMON), pygame.Rect(x, y, 90, 90), 0, 15)
        pygame.display.update()
        pygame.time.delay(100)
        pygame.draw.rect(self.display, (LIGHT_PINK), pygame.Rect(x, y, 90, 90), 0, 15)
        pygame.display.update()
        


    def draw_pattern(self, pattern: list, level: int, high_score: int):
        self.draw_level(level)
        self.draw_high_score(high_score)
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
        pygame.draw.rect(self.display, (GREEN), pygame.Rect(x, y, 90, 90), 0, 15)
        pygame.display.update()
        pygame.time.delay(150)

        pygame.draw.rect(self.display, (LIGHT_PINK), pygame.Rect(x, y, 90, 90), 0 ,15)
        pygame.display.update()
        pygame.time.delay(150)
    

    def draw_level(self, level):
        font = pygame.font.SysFont("Inter", 42)
        # pygame.draw.rect(self.display, DARK_VIOLET, pygame.Rect(125, 445, 200, 60), 0, 15)
        pygame.draw.rect(self.display, DARK_VIOLET, pygame.Rect(125, 445, 165, 60), 0, 15)
        pygame.display.update()
        text = font.render(f"Score: {level}", True, BABY_PINK)
        self.display.blit(text,(143, 461))
        pygame.display.update()
    

    def draw_high_score(self, hs):
        font = pygame.font.SysFont("Inter", 42)
        # pygame.draw.rect(self.display, DARK_VIOLET, pygame.Rect(125, 520, 200, 60), 0, 15)
        pygame.draw.rect(self.display, DARK_VIOLET, pygame.Rect(305, 445, 165, 60), 0, 15)
        pygame.display.update()
        text = font.render(f"HS: {hs}", True, YELLOW)
        self.display.blit(text,(323, 461))
        pygame.display.update()



    


