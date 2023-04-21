import pygame
from ui.main_ui import MainUi

WHITE = (255, 255, 255)
YELLOW = (255, 255, 153)
DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)
GREEN = (88, 179, 104)


class RegisDisplay:
    def __init__(self, screen):
        self.display = screen
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
        self.main.draw_box(color3, 65, 190, 470, 270)
        self.main.draw_box(color2, 75, 200, 450, 250)
        self.main.draw_box(color3, 270, 250, 220, 50)

        self.main.draw_text(color4, x, y, font, text)
        self.main.draw_text(color3, 110, 265, 32, "USERNAME:")

        self.enter_button(False)

        if option == 1:
            self.create_account_button(False)
        else:
            self.return_button(False)

        pygame.display.update()

    def update_screen(self, text):
        self.main.draw_box(LIGHT_PINK, 270, 250, 220, 50)
        self.main.draw_text(DARK_VIOLET, 290, 265, 32, text)
        pygame.display.update()
    
    def password_display(self, option):
        if option == 1:
            color = DARK_VIOLET
        else:
            color = VIOLET
        self.main.draw_box(color, 75, 200, 450, 250)
        self.main.draw_box(LIGHT_PINK, 270, 250, 220, 50)
        self.main.draw_text(LIGHT_PINK, 110, 265, 32, "PASSWORD:")
        pygame.display.update()

    def enter_button(self, hovered):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = SALMON
        else:
            text_color = SALMON
            box_color = LIGHT_PINK

        self.main.draw_box(box_color, 340, 340, 150, 60)
        self.main.draw_text(text_color, 365, 357, 42, "ENTER")
        pygame.display.update()

    def create_account_button(self, hovered):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = SALMON
        else:
            text_color = SALMON
            box_color = LIGHT_PINK

        self.main.draw_box(box_color, 170, 490, 260, 55)
        self.main.draw_text(text_color, 195, 508, 32, "CREATE ACCOUNT")
        pygame.display.update()

    def return_button(self, hovered: bool):
        if not hovered:
            text_color = LIGHT_PINK
            box_color = SALMON
        else:
            text_color = SALMON
            box_color = LIGHT_PINK

        self.main.draw_box(box_color, 450, 25, 120, 45)
        self.main.draw_text(text_color, 468, 39, 28, "RETURN")
        pygame.display.update()
