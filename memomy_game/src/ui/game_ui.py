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

class Display:
    def __init__(self, screen):
        self.display = screen
        self.main = MainUi(self.display)


    def draw_screen(self):
        self.display.fill(VIOLET)
        self.main.draw_box(DARK_VIOLET, 125, 70, 350, 350)

        x = 155
        y = 100
        for i in range(1, 10):
            self.main.draw_box(LIGHT_PINK, x, y, 90, 90)
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
        
        self.draw_flash(x, y, 100, SALMON)


    def draw_pattern(self, pattern: list, level: int, high_score: int):
        self.draw_level(level)
        self.draw_high_score(high_score)
        for element in pattern:
            x = 155
            y = 100
            for i in range(1, 10):
                if i == element:
                    self.draw_flash(x, y, 175, GREEN)
                if i % 3 == 0:
                    y += 100
                    x = 155
                else:
                    x += 100


    def draw_flash(self, x, y, time, color):
        self.main.draw_box(color, x, y, 90, 90)
        pygame.display.update()
        pygame.time.delay(time)

        self.main.draw_box(LIGHT_PINK, x, y, 90, 90)
        pygame.display.update()
        pygame.time.delay(time)
    

    def draw_level(self, level):
        self.main.draw_box(DARK_VIOLET, 125, 445, 165, 60)
        self.main.draw_text(BABY_PINK, 140, 461, 42, f"SCORE: {level}")
        pygame.display.update()
    

    def draw_high_score(self, hs):
        self.main.draw_box(DARK_VIOLET, 305, 445, 165, 60)
        self.main.draw_text(YELLOW, 323, 461, 42, f"HS: {hs}")
        pygame.display.update()




    


