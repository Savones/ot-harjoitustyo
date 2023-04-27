from objects.buttons import Button

class Makebuttons():
    def __init__(self):
        self.buttons = self.make_buttons()
    
    def make_buttons(self):
        try_again = Button("TRY AGAIN", 75, 405, 200, 60)
        scoreboard = Button("SCOREBOARD", 325, 405, 200, 60)
        log_out = Button("LOG OUT", 450, 25, 120, 45)
        return [try_again, scoreboard, log_out]