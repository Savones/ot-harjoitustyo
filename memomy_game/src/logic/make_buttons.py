from objects.buttons import Button

DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)


class Makebuttons():
    """A class that creates a list of buttons for a display

    Attributes:
        display: for which ui view the buttons are for
    """

    def __init__(self, display):
        match display:
            case 0:
                self.buttons = []
            case 1:
                self.buttons = self.game_over_buttons()
            case 2:
                self.buttons = self.scoreboard_buttons()
            case 3:
                self.buttons = self.login_buttons()
            case 4:
                self.buttons = self.settings_buttons()

    def game_over_buttons(self):
        try_again = Button("TRY AGAIN", 75, 405, 200, 60,
                           105, 423, 36, (LIGHT_PINK, VIOLET))
        scoreboard = Button("SCOREBOARD", 325, 405, 200, 60,
                            340, 423, 36, (LIGHT_PINK, VIOLET))
        log_out = Button("LOG OUT", 450, 25, 120, 45, 465,
                         39, 28, (LIGHT_PINK, DARK_VIOLET))
        return [try_again, scoreboard, log_out]

    def scoreboard_buttons(self):
        go_back = Button("RETURN", 450, 25, 120, 45, 468,
                         39, 28, (LIGHT_PINK, SALMON))
        return [go_back]

    def login_buttons(self):
        enter = Button("ENTER", 340, 340, 150, 60, 365,
                       357, 42, (LIGHT_PINK, SALMON))
        create = Button("CREATE ACCOUNT", 170, 490, 260, 55,
                        195, 508, 32, (LIGHT_PINK, SALMON))
        go_back = self.scoreboard_buttons()[0]
        return [enter, create, go_back]

    def settings_buttons(self):
        easy = Button("EASY", 200, 215, 200, 60, 258,
                      233, 40, (LIGHT_PINK, VIOLET))
        medium = Button("MEDIUM", 200, 295, 200, 60, 245,
                        313, 40, (LIGHT_PINK, VIOLET))
        hard = Button("HARD", 200, 375, 200, 60, 258,
                      393, 40, (LIGHT_PINK, VIOLET))

        enter = Button("START GAME", 175, 475, 250, 80,
                       198, 500, 46, (LIGHT_PINK, SALMON))
        log_out = Button("LOG OUT", 450, 25, 120, 45, 465,
                         39, 28, (LIGHT_PINK, DARK_VIOLET))
        return [easy, medium, hard, enter, log_out]
