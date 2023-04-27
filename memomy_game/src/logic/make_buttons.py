from objects.buttons import Button

DARK_VIOLET = (54, 29, 50)
VIOLET = (84, 60, 82)
SALMON = (245, 89, 81)
BABY_PINK = (237, 210, 203)
LIGHT_PINK = (241, 232, 230)

class Makebuttons():
    def __init__(self, display):
        if display == 0:
            self.buttons = []
        elif display == 1:
            self.buttons = self.game_over_buttons()
        else:
            self.buttons = self.scoreboard_buttons()
    
    def game_over_buttons(self):
        try_again = Button("TRY AGAIN", 75, 405, 200, 60, 105, 423, 36, (LIGHT_PINK, VIOLET))
        scoreboard = Button("SCOREBOARD", 325, 405, 200, 60, 340, 423, 36, (LIGHT_PINK, VIOLET))
        log_out = Button("LOG OUT", 450, 25, 120, 45, 465, 39, 28, (LIGHT_PINK, DARK_VIOLET))
        return [try_again, scoreboard, log_out]
    
    def scoreboard_buttons(self):
        go_back = Button("RETURN", 450, 25, 120, 45, 468, 39, 28, (LIGHT_PINK, SALMON))
        return [go_back]