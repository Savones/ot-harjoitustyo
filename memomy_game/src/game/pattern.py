import random

class Pattern:
    def __init__(self):
        self.pattern_list = []
    
    def add_random_press(self):
        random_press = random.randint(1, 9)
        self.pattern_list.append(random_press)
