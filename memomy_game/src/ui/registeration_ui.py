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
SOFT_BLACK = (39, 14, 35)


class RegisDisplay:
    def __init__(self, screen, buttons):
        self.display = screen
        self.buttons = buttons[0]
        self.main = MainUi(self.display)

    def draw_screen(self, option: int):
        if option == 1:
            color1 = BABY_PINK
            color2 = VIOLET
            color3 = LIGHT_PINK
            color4 = VIOLET
            text = "LOG IN"
            font = 82
            x = 200
            y = 100
        else:
            color1 = VIOLET
            color2 = DARK_VIOLET
            color3 = LIGHT_PINK
            color4 = LIGHT_PINK
            text = "CREATE ACCOUNT"
            font = 62
            x = 100
            y = 125

        self.display.fill(color1)
        self.main.draw_box(YELLOW, 65, 190, 470, 270)
        self.main.draw_box(color2, 75, 200, 450, 250)
        self.main.draw_box(color3, 270, 250, 220, 50)

        self.main.draw_text(color4, x, y, font, text)
        self.main.draw_text(color3, 110, 265, 32, "USERNAME:")

        self.draw_button(False, self.buttons[0])

        if option == 1:
            self.draw_button(False, self.buttons[1])
        else:
            self.draw_button(False, self.buttons[2])

        pygame.display.update()

    def update_screen(self, text, option):
        self.main.draw_box(LIGHT_PINK, 270, 250, 220, 50)

        if option == 2 or option == 0:
            if len(text) >= 20:
                text = "*" * 20
            else:
                text = "*" * len(text)
            self.main.draw_text(DARK_VIOLET, 290, 265, 32, text)
        else:
            if len(text) >= 12:
                text = text[0:12]
            self.main.draw_text(DARK_VIOLET, 290, 265, 32, text)
        pygame.display.update()

    def password_display(self, option):
        if option == 1:
            color = DARK_VIOLET
        else:
            color = SOFT_BLACK
        self.main.draw_box(color, 75, 200, 450, 250)
        self.main.draw_box(LIGHT_PINK, 270, 250, 220, 50)
        self.main.draw_text(LIGHT_PINK, 110, 265, 32, "PASSWORD:")
        pygame.display.update()

    def draw_button(self, hovered, button):
        self.main.draw_button(hovered, button)
        pygame.display.update()
