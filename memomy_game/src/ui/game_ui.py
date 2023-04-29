import pygame
from ui.main_ui import MainUi

WHITE = (255, 255, 255)
YELLOW = (255, 255, 224)
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)
GREEN = (88, 179, 104)


class Display:
    def __init__(self, screen, player, squares):
        self.display = screen
        self.player = player
        self.main = MainUi(self.display)
        self.square_width = squares.square_width
        self.squares = squares.squares

    def draw_screen(self, high_score, difficulty):
        self.display.fill(VIOLET)
        self.main.draw_box(DARK_VIOLET, 125, 70, 350, 350)

        for square in self.squares:
            self.main.draw_box(
                LIGHT_PINK, square[0], square[1], self.square_width, self.square_width)

        self.main.draw_text(LIGHT_PINK, 25, 25, 42, self.player)
        self.main.draw_text(SALMON, 450, 25, 42, difficulty)
        self.draw_level(0)
        self.draw_high_score(high_score)

        pygame.display.update()

    def draw_click(self, pos):
        for square in self.squares:
            if (square[0] + self.square_width) >= pos[0] >= square[0] and (
                    square[1] + self.square_width) >= pos[1] >= square[1]:
                break

        self.draw_flash(square[0], square[1], 100, SALMON)

    def draw_pattern(self, pattern: list, level: int, high_score: int, difficulty):
        self.draw_level(level)
        self.draw_high_score(high_score)
        pygame.time.delay(1000)

        for element in pattern:
            self.draw_flash(
                self.squares[element][0], self.squares[element][1], difficulty.speed, GREEN)

    def draw_flash(self, x, y, time, color):
        self.main.draw_box(color, x, y, 90, 90)
        pygame.display.update()
        pygame.time.delay(time)

        self.main.draw_box(LIGHT_PINK, x, y, 90, 90)
        pygame.display.update()
        pygame.time.delay(time)

    def draw_level(self, level):
        self.main.draw_box(DARK_VIOLET, 125, 445, 165, 60)
        self.main.draw_text(BABY_PINK, 143, 464, 34, f"SCORE: {level}")
        pygame.display.update()

    def draw_high_score(self, hs):
        self.main.draw_box(DARK_VIOLET, 305, 445, 165, 60)
        self.main.draw_text(YELLOW, 326, 464, 34, f"HS: {hs}")
        pygame.display.update()

    def draw_level_up_text(self):
        self.main.draw_text(GREEN, 210, 535, 48, "CORRECT!")
        pygame.display.update()
        pygame.time.delay(750)
        self.main.draw_box(VIOLET, 210, 530, 200, 60)
        pygame.display.update()
