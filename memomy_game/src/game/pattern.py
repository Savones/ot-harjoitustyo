import random

class Pattern:
    def __init__(self):
        self.pattern_list = []
        self.level = 0
        self.high_score = 0
    
    def add_random_press(self):
        random_press = random.randint(1, 9)
        self.pattern_list.append(random_press)
    
    def level_up(self):
        self.level += 1

    def change_high_score(self):
        if self.level > self.high_score:
            self.high_score = self.level

    def default(self):
        self.level = 0
        self.pattern_list = []
