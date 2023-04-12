import random
from registeration.player_database import Database

class Pattern:
    def __init__(self, player):
        self.pattern_list = []
        self.level = 0
        self.player = player
        self.database = Database()
        self.high_score = self.database.get_hs(player)
    
    def add_random_press(self):
        random_press = random.randint(1, 9)
        self.pattern_list.append(random_press)
    
    def level_up(self):
        self.level += 1

    def change_high_score(self):
        if self.level > self.high_score:
            self.high_score = self.level
    
    def update_hs_in_db(self):
        self.database.change_hs(self.player, self.high_score)

    def default(self):
        self.level = 0
        self.pattern_list = []

