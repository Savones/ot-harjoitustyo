
class Difficulties:
    def __init__(self, difficulty):
        self.name = difficulty
        self.speed = 0
        self. addition = 0
        self.column = 0
        if difficulty == "EASY":
            self.easy()
        elif difficulty == "MEDIUM":
            self.medium()
        else:
            self.hard()

    def easy(self):
        self.speed = 200
        self.addition = 1
        self.column = 1

    def medium(self):
        self.speed = 175
        self.addition = 2
        self.column = 2

    def hard(self):
        self.speed = 150
        self.addition = 3
        self.column = 3