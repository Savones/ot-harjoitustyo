
class Buttons:
    def __init__(self):
        self.gameover = self.set_gameover_buttons()

    def set_gameover_buttons(self):
        buttons = [["TRY AGAIN", 75, 405, 200, 60], ["SCOREBOARD", 325, 405, 200, 60]
                   ["LOG OUT", 450, 25, 120, 45]]
        return buttons
