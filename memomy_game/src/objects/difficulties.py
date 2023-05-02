
class Difficulties:
    def __init__(self, difficulty):
        self.name = difficulty
        if difficulty == "EASY":
            speed = self.easy()
        elif difficulty == "MEDIUM":
            speed = self.medium()
        else:
            speed = self.hard()
        self.speed = speed

    def easy(self):
        return 300

    def medium(self):
        return 175

    def hard(self):
        return 100
