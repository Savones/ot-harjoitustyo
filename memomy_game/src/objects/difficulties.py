
class Difficulties:
    def __init__(self, difficulty):
        self.name = difficulty
        if difficulty == "EASY":
            speed = self.easy()[0]
            addition = self.easy()[1]
            column = 1
        elif difficulty == "MEDIUM":
            speed = self.medium()[0]
            addition = self.medium()[1]
            column = 2
        else:
            speed = self.hard()[0]
            addition = self.hard()[1]
            column = 3
        self.speed = speed
        self.addition = addition
        self.column = column

    def easy(self):
        return (200, 1)

    def medium(self):
        return (175, 2)

    def hard(self):
        return (150, 3)
