from ui.main_ui import MainUi

DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)


class GameOverDisplay:
    def __init__(self, screen, buttons):
        self.display = screen
        self.buttons = buttons
        self.main = MainUi(self.display)

    def draw_screen(self):
        self.display.fill((BABY_PINK))

        self.main.draw_text(SALMON, 130, 210, 82, "GAME OVER")

        for button in self.buttons:
            self.draw_button(False, button)

    def draw_button(self, hovered: bool, button):
        self.main.draw_button(hovered, button)
