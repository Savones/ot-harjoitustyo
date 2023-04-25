import random


class Variables:
    def __init__(self, player, database):
        self.pattern_list = []
        self.level = 0
        self.player = player
        self.database = database
        self.high_score = self.database.get_high_score(player)

    def add_random_press(self):
        random_press = random.randint(0, 8)
        self.pattern_list.append(random_press)

    def level_up(self):
        self.level += 1

    def change_high_score(self):
        if self.level > self.high_score:
            self.high_score = self.level

    def update_hs_in_db(self):
        self.database.change_high_score(self.player, self.high_score)

    def default(self):
        self.level = 0
        self.pattern_list = []
