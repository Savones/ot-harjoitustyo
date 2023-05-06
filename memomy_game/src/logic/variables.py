import random


class Variables:
    """A class that handles variables relevant after logging in

    Attributes:
        player: the logged in players username
        database: an object of Database class
    """

    def __init__(self, player, database):
        """The classes construct which initializes the variables after logging in

        Attributes:
            Listed above
        """

        self.pattern_list = []
        self.level = 0
        self.player = player
        self.database = database
        # self.high_score = self.database.get_high_score(player)

    def add_random_press(self):
        """Adds a new random square hit to the pattern after a round
        """

        random_press = random.randint(0, 8)
        self.pattern_list.append(random_press)
    
    def high_score(self, difficulty):
        return self.database.get_high_score(self.player, difficulty)

    def level_up(self):
        """Increases level by one after a round
        """

        self.level += 1

    def change_high_score(self, difficulty):
        """If level is higher than high score, changes high score to the level
        """

        if self.level > self.high_score(difficulty):
            self.database.change_high_score(self.player, self.level, difficulty)

    def default(self):
        """Sets level to zero and empties the pattern list when new game starts 
        """

        self.level = 0
        self.pattern_list = []
